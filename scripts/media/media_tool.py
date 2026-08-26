#!/usr/bin/env python3
"""Read-only media inventory and canonical manifest checks for Marragafay.

This tool never moves, renames, deletes, rewrites, compresses, or generates
image files. It is intentionally dependency-free so it can be used before a
future media migration batch is accepted.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Iterator, Sequence
from urllib.parse import unquote, urlparse


IMAGE_TYPES = {
    ".avif": "avif",
    ".gif": "gif",
    ".jpeg": "jpeg",
    ".jpg": "jpeg",
    ".png": "png",
    ".svg": "svg",
    ".webp": "webp",
}
SOURCE_EXTENSIONS = {".css", ".htm", ".html", ".js", ".jsx", ".mjs", ".ts", ".tsx"}
IGNORED_DIRS = {".git", ".next", "node_modules", "__pycache__"}
REFERENCE_IGNORED_DIRS = IGNORED_DIRS | {".agents", ".claude", ".gemini", ".vscode", "docs", "scripts"}
OWNER_RE = re.compile(
    r"^(?:activities|packs|shared|brand|blog|seo)"
    r"(?:/[a-z0-9]+(?:-[a-z0-9]+)*)*$"
)
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_ROLES = {
    "hero",
    "gallery",
    "thumb",
    "content",
    "background",
    "logo",
    "icon",
    "og",
    "avatar",
    "candidate",
}
ALLOWED_FORMATS = {"avif", "gif", "jpeg", "jpg", "png", "svg", "webp"}
IMAGE_SUFFIXES = tuple(IMAGE_TYPES)
ACTIVITY_NAMES = ("quad", "buggy", "camel", "paragliding", "hot-air-balloon", "dinner-show")
PACK_NAMES = ("basic", "comfort", "luxe")
SHARED_NAMES = ("camp", "pool", "transport", "dining", "show")
REQUIRED_MEDIA_DIRS = [
    *(f"activities/{activity}/{role}" for activity in ACTIVITY_NAMES for role in ("hero", "gallery", "thumbs")),
    *(f"packs/{pack}/{role}" for pack in PACK_NAMES for role in ("hero", "gallery", "thumbs")),
    *(f"shared/{name}" for name in SHARED_NAMES),
    "brand",
    "blog",
    "seo",
]
CANONICAL_PATH_RE = re.compile(
    r"^/media/[a-z0-9][a-z0-9/-]*\.(?:avif|gif|jpeg|jpg|png|svg|webp)$"
)


def project_root_from_args(args: argparse.Namespace) -> Path:
    if args.project_root:
        return Path(args.project_root).expanduser().resolve()
    return Path(__file__).resolve().parents[2]


def scan_roots(project_root: Path, args: argparse.Namespace) -> list[Path]:
    roots = args.scan_root or [str(project_root)]
    return [Path(root).expanduser().resolve() for root in roots]


def iter_files(root: Path, ignored_dirs: set[str] | None = None) -> Iterator[Path]:
    ignored = IGNORED_DIRS if ignored_dirs is None else ignored_dirs
    if root.is_file():
        yield root
        return
    if not root.exists():
        return
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        try:
            relative_parts = path.relative_to(root).parts
        except ValueError:
            relative_parts = path.parts
        if any(part in ignored for part in relative_parts):
            continue
        yield path


def image_files(roots: Sequence[Path]) -> list[Path]:
    seen: set[Path] = set()
    results: list[Path] = []
    for root in roots:
        for path in iter_files(root):
            if path.suffix.lower() not in IMAGE_TYPES or path in seen:
                continue
            seen.add(path)
            results.append(path)
    return sorted(results, key=lambda item: item.as_posix().lower())


def display_path(path: Path, project_root: Path) -> str:
    try:
        return path.relative_to(project_root).as_posix()
    except ValueError:
        return path.as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def jpeg_dimensions(path: Path) -> tuple[int, int] | None:
    sof_markers = {
        0xC0,
        0xC1,
        0xC2,
        0xC3,
        0xC5,
        0xC6,
        0xC7,
        0xC9,
        0xCA,
        0xCB,
        0xCD,
        0xCE,
        0xCF,
    }
    try:
        with path.open("rb") as handle:
            if handle.read(2) != b"\xff\xd8":
                return None
            while True:
                byte = handle.read(1)
                if not byte:
                    return None
                if byte != b"\xff":
                    continue
                marker_byte = handle.read(1)
                while marker_byte == b"\xff":
                    marker_byte = handle.read(1)
                if not marker_byte:
                    return None
                marker = marker_byte[0]
                if marker in {0xD8, 0xD9}:
                    continue
                length_bytes = handle.read(2)
                if len(length_bytes) != 2:
                    return None
                length = struct.unpack(">H", length_bytes)[0]
                if length < 2:
                    return None
                if marker in sof_markers:
                    dimensions = handle.read(5)
                    if len(dimensions) != 5:
                        return None
                    height, width = struct.unpack(">HH", dimensions[1:5])
                    return width, height
                handle.seek(length - 2, 1)
    except (OSError, struct.error):
        return None


def svg_dimensions(path: Path) -> tuple[int, int] | None:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")[:65536]
    except OSError:
        return None
    root_match = re.search(r"<svg\b([^>]*)>", text, re.IGNORECASE)
    if not root_match:
        return None
    attributes = root_match.group(1)
    view_box = re.search(
        r"\bviewBox\s*=\s*[\"']\s*[-+0-9.eE]+\s+[-+0-9.eE]+\s+"
        r"([-+0-9.eE]+)\s+([-+0-9.eE]+)\s*[\"']",
        attributes,
        re.IGNORECASE,
    )
    width = re.search(r"\bwidth\s*=\s*[\"']\s*([0-9.]+)\s*(?:px)?\s*[\"']", attributes, re.IGNORECASE)
    height = re.search(r"\bheight\s*=\s*[\"']\s*([0-9.]+)\s*(?:px)?\s*[\"']", attributes, re.IGNORECASE)
    try:
        if width and height:
            return round(float(width.group(1))), round(float(height.group(1)))
        if view_box:
            return round(float(view_box.group(1))), round(float(view_box.group(2)))
    except ValueError:
        return None
    return None


def webp_dimensions(path: Path) -> tuple[int, int] | None:
    try:
        with path.open("rb") as handle:
            header = handle.read(34)
    except OSError:
        return None
    if len(header) < 16 or header[:4] != b"RIFF" or header[8:12] != b"WEBP":
        return None
    chunk = header[12:16]
    if chunk == b"VP8X" and len(header) >= 34:
        width = 1 + int.from_bytes(header[28:31], "little")
        height = 1 + int.from_bytes(header[31:34], "little")
        return width, height
    return None


def detect_type_and_dimensions(path: Path) -> tuple[str, tuple[int, int] | None]:
    try:
        with path.open("rb") as handle:
            header = handle.read(64)
    except OSError:
        return "unreadable", None
    if not header:
        return "empty", None
    if header.startswith(b"\xff\xd8\xff"):
        return "jpeg", jpeg_dimensions(path)
    if header.startswith(b"\x89PNG\r\n\x1a\n"):
        dimensions = None
        if len(header) >= 24:
            dimensions = struct.unpack(">II", header[16:24])
        return "png", dimensions
    if header.startswith((b"GIF87a", b"GIF89a")):
        dimensions = None
        if len(header) >= 10:
            dimensions = struct.unpack("<HH", header[6:10])
        return "gif", dimensions
    if header.startswith(b"RIFF") and header[8:12] == b"WEBP":
        return "webp", webp_dimensions(path)
    if header.lstrip().startswith(b"<") and b"<svg" in header.lower():
        return "svg", svg_dimensions(path)
    if len(header) >= 12 and header[4:8] == b"ftyp" and header[8:12] in {b"avif", b"avis"}:
        return "avif", None
    return "unknown", None


def image_record(path: Path, project_root: Path) -> dict[str, object]:
    actual_type, dimensions = detect_type_and_dimensions(path)
    width, height = dimensions if dimensions else (None, None)
    return {
        "path": display_path(path, project_root),
        "bytes": path.stat().st_size,
        "extension": path.suffix.lower().lstrip("."),
        "actualType": actual_type,
        "width": width,
        "height": height,
        "sha256": sha256(path),
    }


def print_json_or_text(payload: object, as_json: bool, text_output: str) -> None:
    if as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(text_output)


def run_inventory(args: argparse.Namespace) -> int:
    project_root = project_root_from_args(args)
    records = [image_record(path, project_root) for path in image_files(scan_roots(project_root, args))]
    total_bytes = sum(int(record["bytes"]) for record in records)
    lines = [
        f"Media inventory: {len(records)} image file(s), {total_bytes:,} byte(s)",
        "path | bytes | extension | actual type | dimensions | sha256",
    ]
    for record in records:
        dimensions = (
            f"{record['width']}x{record['height']}"
            if record["width"] and record["height"]
            else "unknown"
        )
        lines.append(
            f"{record['path']} | {record['bytes']} | .{record['extension']} | "
            f"{record['actualType']} | {dimensions} | {record['sha256']}"
        )
    print_json_or_text(records, args.json, "\n".join(lines))
    return 0


def run_duplicates(args: argparse.Namespace) -> int:
    project_root = project_root_from_args(args)
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in image_files(scan_roots(project_root, args)):
        groups[sha256(path)].append(path)
    duplicates = [
        {
            "sha256": digest,
            "bytes": paths[0].stat().st_size,
            "paths": [display_path(path, project_root) for path in paths],
        }
        for digest, paths in sorted(groups.items())
        if len(paths) > 1
    ]
    duplicate_bytes = sum(int(group["bytes"]) * (len(group["paths"]) - 1) for group in duplicates)
    lines = [f"Exact duplicate groups: {len(duplicates)}; duplicate overhead: {duplicate_bytes:,} byte(s)"]
    for group in duplicates:
        lines.append(f"\n{group['sha256']} ({group['bytes']} byte(s))")
        lines.extend(f"  - {path}" for path in group["paths"])
    if not duplicates:
        lines.append("No exact byte-for-byte duplicate image files found.")
    print_json_or_text(duplicates, args.json, "\n".join(lines))
    return 0


def run_verify_types(args: argparse.Namespace) -> int:
    project_root = project_root_from_args(args)
    issues: list[dict[str, object]] = []
    for path in image_files(scan_roots(project_root, args)):
        expected = IMAGE_TYPES[path.suffix.lower()]
        actual, dimensions = detect_type_and_dimensions(path)
        if actual != expected:
            issues.append(
                {
                    "path": display_path(path, project_root),
                    "extension": path.suffix.lower(),
                    "expected": expected,
                    "actual": actual,
                    "dimensions": dimensions,
                }
            )
    if issues:
        lines = [f"Extension/type issues: {len(issues)}"]
        lines.extend(
            f"- {item['path']}: extension {item['extension']} expects {item['expected']}, "
            f"detected {item['actual']}"
            for item in issues
        )
    else:
        lines = ["All image extensions match their detected file types."]
    print_json_or_text(issues, args.json, "\n".join(lines))
    return 0


def source_files(project_root: Path) -> Iterator[Path]:
    for path in iter_files(project_root, REFERENCE_IGNORED_DIRS):
        if path.suffix.lower() in SOURCE_EXTENSIONS:
            yield path


QUOTED_REFERENCE_RE = re.compile(
    r"(?P<quote>[\"'])(?P<value>(?:https?:)?//[^\"'\s]+|/[^\"'\s]+|"
    r"(?:\.\.?/)?[^\"'\s]+)(?P=quote)",
    re.IGNORECASE,
)
CSS_REFERENCE_RE = re.compile(
    r"url\(\s*[\"']?(?P<value>[^\"')\s]+)[\"']?\s*\)",
    re.IGNORECASE,
)


def image_reference_values(text: str) -> Iterator[str]:
    seen: set[str] = set()
    for match in list(QUOTED_REFERENCE_RE.finditer(text)) + list(CSS_REFERENCE_RE.finditer(text)):
        value = unquote(match.group("value")).strip()
        if value in seen:
            continue
        seen.add(value)
        if any(character in value for character in "<>"):
            continue
        parsed = urlparse(value)
        if parsed.scheme in {"http", "https", "data"} or parsed.netloc:
            continue
        path = parsed.path
        if Path(path).suffix.lower() not in IMAGE_TYPES:
            continue
        yield path


def reference_candidates(project_root: Path, source: Path, reference: str) -> list[Path]:
    if reference.startswith("/"):
        route_path = reference.lstrip("/")
        return [project_root / route_path, project_root / "public" / route_path]
    relative_path = (source.parent / reference).resolve()
    candidates = [relative_path, project_root / reference, project_root / "public" / reference]
    if relative_path.is_relative_to(project_root):
        candidates.append(project_root / "public" / relative_path.relative_to(project_root))
    return candidates


def run_missing_references(args: argparse.Namespace) -> int:
    project_root = project_root_from_args(args)
    reference_sources: dict[str, set[str]] = defaultdict(set)
    for source in source_files(project_root):
        try:
            text = source.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for reference in image_reference_values(text):
            reference_sources[reference].add(display_path(source, project_root))

    missing: list[dict[str, object]] = []
    suspicious_public_prefix: list[dict[str, object]] = []
    for reference, sources in sorted(reference_sources.items()):
        source_path = project_root / next(iter(sorted(sources)))
        candidates = reference_candidates(project_root, source_path, reference)
        if not any(candidate.is_file() for candidate in candidates):
            missing.append({"reference": reference, "sources": sorted(sources)})
        elif reference.startswith("/public/"):
            suspicious_public_prefix.append({"reference": reference, "sources": sorted(sources)})

    payload = {"missing": missing, "suspiciousPublicPrefix": suspicious_public_prefix}
    lines = [
        f"Unique local image references: {len(reference_sources)}",
        f"Missing references: {len(missing)}",
        f"Suspicious /public/ URL prefixes: {len(suspicious_public_prefix)}",
    ]
    for item in missing:
        lines.append(f"\nMISSING {item['reference']}")
        lines.extend(f"  - {source}" for source in item["sources"])
    for item in suspicious_public_prefix:
        lines.append(f"\nCHECK URL PREFIX {item['reference']}")
        lines.extend(f"  - {source}" for source in item["sources"])
    print_json_or_text(payload, args.json, "\n".join(lines))
    return 0


def media_path_from_url(project_root: Path, url_path: str) -> Path | None:
    if not url_path.startswith("/media/"):
        return None
    relative = url_path.removeprefix("/media/")
    if not relative or Path(relative).is_absolute() or ".." in Path(relative).parts:
        return None
    return project_root / "public" / "media" / relative


def validate_manifest_shape(manifest: object, project_root: Path) -> list[str]:
    errors: list[str] = []
    if not isinstance(manifest, dict):
        return ["manifest root must be an object"]
    if manifest.get("schemaVersion") != 1:
        errors.append("schemaVersion must be 1")
    if manifest.get("canonicalRoot") != "/media/":
        errors.append("canonicalRoot must be /media/")
    assets = manifest.get("assets")
    if not isinstance(assets, list):
        return errors + ["assets must be an array"]
    ids: set[str] = set()
    paths: set[str] = set()
    for index, asset in enumerate(assets):
        label = f"assets[{index}]"
        if not isinstance(asset, dict):
            errors.append(f"{label} must be an object")
            continue
        required = {"id", "canonicalPath", "owner", "roles", "shared", "dimensions", "alt", "variants"}
        missing = sorted(required - set(asset))
        if missing:
            errors.append(f"{label} missing: {', '.join(missing)}")
            continue
        asset_id = asset["id"]
        if not isinstance(asset_id, str) or not SLUG_RE.fullmatch(asset_id):
            errors.append(f"{label}.id must be lowercase kebab-case")
        elif asset_id in ids:
            errors.append(f"{label}.id is duplicated: {asset_id}")
        else:
            ids.add(asset_id)

        canonical_path = asset["canonicalPath"]
        if not isinstance(canonical_path, str) or not CANONICAL_PATH_RE.fullmatch(canonical_path):
            errors.append(f"{label}.canonicalPath must be a lowercase /media/ file path")
        else:
            if canonical_path in paths:
                errors.append(f"{label}.canonicalPath is duplicated: {canonical_path}")
            paths.add(canonical_path)
            resolved = media_path_from_url(project_root, canonical_path)
            if resolved is None or not resolved.is_file():
                errors.append(f"{label}.canonicalPath does not point to a file: {canonical_path}")

        owner = asset["owner"]
        if not isinstance(owner, str) or not OWNER_RE.fullmatch(owner):
            errors.append(f"{label}.owner must be a lowercase canonical owner path")
        shared = asset["shared"]
        if not isinstance(shared, bool):
            errors.append(f"{label}.shared must be boolean")
        elif isinstance(owner, str) and ((owner.startswith("shared/") and not shared) or (shared and not owner.startswith("shared/"))):
            errors.append(f"{label}.shared must match the shared/ owner namespace")

        roles = asset["roles"]
        if not isinstance(roles, list) or not roles or any(role not in ALLOWED_ROLES for role in roles):
            errors.append(f"{label}.roles must contain at least one allowed role")

        dimensions = asset["dimensions"]
        if not isinstance(dimensions, dict) or not all(isinstance(dimensions.get(key), int) and dimensions.get(key) > 0 for key in ("width", "height")):
            errors.append(f"{label}.dimensions must contain positive integer width and height")

        if not isinstance(asset["alt"], str) or not asset["alt"].strip():
            errors.append(f"{label}.alt must be non-empty accessible text")

        variants = asset["variants"]
        if not isinstance(variants, list):
            errors.append(f"{label}.variants must be an array")
        else:
            for variant_index, variant in enumerate(variants):
                variant_label = f"{label}.variants[{variant_index}]"
                if not isinstance(variant, dict):
                    errors.append(f"{variant_label} must be an object")
                    continue
                for key in ("path", "kind", "format", "dimensions"):
                    if key not in variant:
                        errors.append(f"{variant_label} missing: {key}")
                variant_path = variant.get("path")
                if isinstance(variant_path, str):
                    if not CANONICAL_PATH_RE.fullmatch(variant_path):
                        errors.append(f"{variant_label}.path must be a lowercase /media/ file path")
                    resolved_variant = media_path_from_url(project_root, variant_path)
                    if resolved_variant is None or not resolved_variant.is_file():
                        errors.append(f"{variant_label}.path does not point to a file: {variant_path}")
                if variant.get("kind") not in {"responsive", "format", "thumbnail"}:
                    errors.append(f"{variant_label}.kind is invalid")
                if variant.get("format") not in ALLOWED_FORMATS:
                    errors.append(f"{variant_label}.format is invalid")
                elif isinstance(variant_path, str):
                    suffix_format = Path(variant_path).suffix.lower().lstrip(".")
                    if suffix_format == "jpg":
                        suffix_format = "jpeg"
                    if suffix_format != variant.get("format"):
                        errors.append(f"{variant_label}.format does not match its path extension")
                variant_dimensions = variant.get("dimensions")
                if not isinstance(variant_dimensions, dict) or not all(isinstance(variant_dimensions.get(key), int) and variant_dimensions.get(key) > 0 for key in ("width", "height")):
                    errors.append(f"{variant_label}.dimensions must contain positive integer width and height")
    return errors


def run_validate_manifest(args: argparse.Namespace) -> int:
    project_root = project_root_from_args(args)
    manifest_path = Path(args.manifest).expanduser() if args.manifest else project_root / "public" / "media" / "manifest.json"
    if not manifest_path.is_absolute():
        manifest_path = (project_root / manifest_path).resolve()
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors = [f"manifest not found: {manifest_path}"]
    except json.JSONDecodeError as error:
        errors = [f"invalid JSON in {manifest_path}: {error}"]
    except OSError as error:
        errors = [f"could not read {manifest_path}: {error}"]
    else:
        errors = validate_manifest_shape(manifest, project_root)
        media_root = project_root / "public" / "media"
        errors.extend(
            f"missing canonical directory: public/media/{relative_dir}"
            for relative_dir in REQUIRED_MEDIA_DIRS
            if not (media_root / relative_dir).is_dir()
        )

    if errors:
        print_json_or_text(errors, args.json, "Manifest validation failed:\n" + "\n".join(f"- {error}" for error in errors))
        return 1
    print_json_or_text({"valid": True, "manifest": display_path(manifest_path, project_root)}, args.json, f"Manifest valid: {display_path(manifest_path, project_root)}")
    return 0


def add_project_and_json_arguments(parser: argparse.ArgumentParser, scan: bool = False) -> None:
    parser.add_argument("--project-root", help="Project root; defaults to the Marragafay project root")
    if scan:
        parser.add_argument("--scan-root", action="append", help="Image root to scan; repeat for multiple roots")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    inventory = commands.add_parser("inventory", help="List image files, types, dimensions, and hashes")
    add_project_and_json_arguments(inventory, scan=True)
    duplicates = commands.add_parser("duplicates", help="Group exact byte-for-byte image duplicates")
    add_project_and_json_arguments(duplicates, scan=True)
    verify_types = commands.add_parser("verify-types", help="Compare image extensions with detected file types")
    add_project_and_json_arguments(verify_types, scan=True)
    missing = commands.add_parser("missing-references", help="Find local image references with no matching file")
    add_project_and_json_arguments(missing)
    validate = commands.add_parser("validate-manifest", help="Validate manifest shape and canonical file paths")
    add_project_and_json_arguments(validate)
    validate.add_argument("--manifest", help="Manifest path relative to project root or absolute")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    commands = {
        "inventory": run_inventory,
        "duplicates": run_duplicates,
        "verify-types": run_verify_types,
        "missing-references": run_missing_references,
        "validate-manifest": run_validate_manifest,
    }
    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
