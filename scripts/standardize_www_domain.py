import re
import glob

# 1. Update sitemap.xml
with open("sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()

sitemap = sitemap.replace("https://marragafay.com", "https://www.marragafay.com")

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)
print("Updated sitemap.xml to https://www.marragafay.com")

# 2. Update robots.txt
with open("robots.txt", "r", encoding="utf-8") as f:
    robots = f.read()

robots = robots.replace("https://marragafay.com", "https://www.marragafay.com")

with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots)
print("Updated robots.txt to https://www.marragafay.com/sitemap.xml")

# 3. Update canonical and hreflang across all HTML files
html_files = glob.glob("**/*.html", recursive=True)
count = 0
for fpath in html_files:
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    orig = html
    # Update canonical and hreflang links to www
    html = re.sub(r'href=["\']https://marragafay\.com(/[^"\']*)?["\']', r'href="https://www.marragafay.com\1"', html)
    html = re.sub(r'content=["\']https://marragafay\.com(/[^"\']*)?["\']', r'content="https://www.marragafay.com\1"', html)
    html = re.sub(r'"url":\s*"https://marragafay\.com(/[^"]*)?"', r'"url": "https://www.marragafay.com\1"', html)

    if html != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        count += 1

print(f"Updated canonical and schema URLs to www. in {count} HTML files")
