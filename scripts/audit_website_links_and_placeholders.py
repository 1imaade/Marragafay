import os
import glob
import re
from urllib.parse import urlparse

files = sorted(glob.glob("**/*.html", recursive=True))

dead_links = []
hash_links = []
typos = []
english_in_foreign = []

for fpath in files:
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 1. Search for dead placeholder links: href="#"
    matches = re.findall(r'href=["\'](#[^"\']*)["\']', content)
    for m in matches:
        # Ignore dropdown toggles if handled by JS, but flag empty href="#"
        if m == "#" or m.startswith("#"):
            hash_links.append((fpath, m))

    # 2. Search for broken relative link targets
    hrefs = re.findall(r'href=["\']([^"\':#]+)["\']', content)
    for h in hrefs:
        if h.startswith("mailto:") or h.startswith("tel:") or h.startswith("javascript:") or h.startswith("http"):
            continue
        # Clean query or hash
        clean_h = h.split("?")[0].split("#")[0]
        if not clean_h:
            continue
        
        # Check if file exists relative to fpath or relative to root
        base_dir = os.path.dirname(fpath)
        rel_target = os.path.normpath(os.path.join(base_dir, clean_h))
        root_target = os.path.normpath(os.path.join(".", clean_h.lstrip("/")))
        
        # Also check with .html if extension omitted
        target_found = False
        for cand in [rel_target, root_target, rel_target + ".html", root_target + ".html", os.path.join(rel_target, "index.html"), os.path.join(root_target, "index.html")]:
            if os.path.exists(cand):
                target_found = True
                break
        
        if not target_found:
            dead_links.append((fpath, h))

    # 3. Check for obvious typos / placeholders
    typo_patterns = [
        (r'MARRAGAFA\.', 'MARRAGAFA. (missing Y in brand)'),
        (r'Marragafy', 'Marragafy (typo in brand name)'),
        (r'Casablanca', 'Casablanca (wrong city alt tag in Agafay site)'),
        (r'lorem ipsum', 'Lorem Ipsum placeholder text'),
        (r'example\.com', 'example.com placeholder URL'),
        (r'TODO', 'TODO marker'),
        (r'undefined', 'undefined string'),
        (r'null', 'null string in UI')
    ]
    for pat, desc in typo_patterns:
        if re.search(pat, content, re.IGNORECASE):
            # check where
            matches = re.findall(rf'.{{0,40}}{pat}.{{0,40}}', content, re.IGNORECASE)
            for snippet in matches[:3]:
                typos.append((fpath, desc, snippet.strip()))

print(f"Total HTML files analyzed: {len(files)}")
print(f"\n--- 1. DEAD / UNRESOLVED INTERNAL LINKS ({len(dead_links)} found) ---")
for f, l in dead_links[:30]:
    print(f"  {f} -> {l}")

print(f"\n--- 2. PLACEHOLDER HREF='#' LINKS ({len(hash_links)} found) ---")
for f, l in hash_links[:20]:
    print(f"  {f} -> {l}")

print(f"\n--- 3. BRAND TYPOS & PLACEHOLDER WORDS ({len(typos)} found) ---")
for f, desc, snip in typos:
    print(f"  {f} [{desc}]: ...{snip}...")
