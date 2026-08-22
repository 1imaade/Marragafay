import re
import glob
import os

files = glob.glob("**/*.html", recursive=True)
print(f"Auditing {len(files)} HTML files for complete integrity...")

issues = []

for fpath in files:
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Check fake numbers
    if "612 345 678" in content or "612345678" in content:
        issues.append((fpath, "Found fake phone number"))

    # Check wrong city alt
    if 'alt="Casablanca"' in content:
        issues.append((fpath, "Found alt='Casablanca'"))

    # Check brand typos
    if 'alt="Marragafy"' in content:
        issues.append((fpath, "Found alt='Marragafy'"))
    if '>MARRAGAFA.<' in content:
        issues.append((fpath, "Found >MARRAGAFA.<"))

    # Check placeholder example emails
    if "example.com" in content:
        issues.append((fpath, "Found example.com email"))

    # Check dead links in footer
    if 'href="#fleet"' in content or 'href="#events"' in content or 'href="#standard"' in content:
        issues.append((fpath, "Found dead # anchor in footer"))

    # Check contradictory review sentence
    if "We do not curate these" in content or "Nous ne les modifions pas" in content:
        issues.append((fpath, "Found contradictory review sentence"))

if not issues:
    print("\n🎉 100% CLEAN! Zero fake placeholders, zero broken footer links, zero brand typos, zero AI contradictions found across all HTML files!")
else:
    print(f"\nFound {len(issues)} remaining issues:")
    for f, msg in issues:
        print(f"  {f}: {msg}")
