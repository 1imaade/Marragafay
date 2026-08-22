import os
import glob
import re

# 1. Update en/blog/index.html
with open("en/blog/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace rootless or extensionless links with direct .html references
replacements = {
    'href="/en/blog/agafay-desert-guide"': 'href="/en/blog/agafay-desert-guide.html"',
    'href="/en/blog/agafay-camel-ride"': 'href="/en/blog/agafay-camel-ride.html"',
    'href="/en/blog/berber-culture-agafay"': 'href="/en/blog/berber-culture-agafay.html"',
    'href="/en/blog/marrakech-to-agafay"': 'href="/en/blog/marrakech-to-agafay.html"',
    'href="/en/blog/agafay-dinner-experience"': 'href="/en/blog/agafay-dinner-experience.html"',
    'href="/en/blog/agafay-quad-biking-guide"': 'href="/en/blog/agafay-quad-biking-guide.html"',
    'href="/en/blog/agafay-desert-vs-sahara"': 'href="/en/blog/agafay-desert-vs-sahara.html"',
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open("en/blog/index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated en/blog/index.html links.")

# 2. Update all articles in en/blog/*.html
article_files = glob.glob("en/blog/*.html")

for filepath in article_files:
    if filepath.endswith("index.html"):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        art_content = f.read()
    
    # Update breadcrumb / related links
    for old, new in replacements.items():
        art_content = art_content.replace(old, new)
    
    # Ensure "All Articles" links to /en/blog/index.html or /en/blog/
    art_content = art_content.replace('href="/en/blog"', 'href="/en/blog/index.html"')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(art_content)
    print(f"Updated links in: {filepath}")

# 3. Update multilingual index pages
for lang in ['fr', 'es', 'ar']:
    idx_path = f"{lang}/blog/index.html"
    if os.path.exists(idx_path):
        with open(idx_path, "r", encoding="utf-8") as f:
            l_content = f.read()
        for old, new in replacements.items():
            l_content = l_content.replace(old, new)
        with open(idx_path, "w", encoding="utf-8") as f:
            f.write(l_content)
        print(f"Updated links in: {idx_path}")

print("All blog article links updated to point to valid .html files.")
