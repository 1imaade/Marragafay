import re
import glob

article_slugs = [
    "agafay-desert-guide",
    "agafay-camel-ride",
    "agafay-desert-vs-sahara",
    "agafay-dinner-experience",
    "agafay-quad-biking-guide",
    "berber-culture-agafay",
    "marrakech-to-agafay"
]

files = glob.glob("**/*.html", recursive=True)
print(f"Scanning {len(files)} files for relative blog links...")

count = 0
for fpath in files:
    lang = "en"
    for l in ["fr", "es", "ar"]:
        if fpath.startswith(l + "/") or fpath.startswith(l + "\\"):
            lang = l
            break

    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    orig = html

    for slug in article_slugs:
        # Match relative links like href="slug.html" or href="slug" (without /lang/blog/ in front)
        html = re.sub(
            r'href=["\'](?:(?:(?:\.\./)*blog/)?|/)?(?:' + slug + r')(?:\.html)?["\']',
            f'href="/{lang}/blog/{slug}"',
            html
        )

    # Clean any accidental double prefix if created
    html = html.replace(f'/{lang}/blog/{lang}/blog/', f'/{lang}/blog/')

    if html != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        count += 1
        print(f"Fixed article links to absolute in {fpath}")

print(f"\nFixed article links in {count} files!")
