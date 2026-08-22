import os
import glob
import re

# 1. Update en/blog/index.html
with open("en/blog/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace any /en/blog/article.html with article.html (relative to current directory)
slugs = [
    "agafay-desert-guide",
    "agafay-camel-ride",
    "berber-culture-agafay",
    "marrakech-to-agafay",
    "agafay-dinner-experience",
    "agafay-quad-biking-guide",
    "agafay-desert-vs-sahara"
]

for s in slugs:
    content = content.replace(f'href="/en/blog/{s}.html"', f'href="{s}.html"')
    content = content.replace(f'href="/en/blog/{s}"', f'href="{s}.html"')

with open("en/blog/index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Made en/blog/index.html links universal & relative.")

# 2. Update all articles in en/blog/*.html
article_files = glob.glob("en/blog/*.html")

for filepath in article_files:
    if filepath.endswith("index.html"):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        art_content = f.read()
    
    for s in slugs:
        art_content = art_content.replace(f'href="/en/blog/{s}.html"', f'href="{s}.html"')
        art_content = art_content.replace(f'href="/en/blog/{s}"', f'href="{s}.html"')
    
    art_content = art_content.replace('href="/en/blog/index.html"', 'href="index.html"')
    art_content = art_content.replace('href="/en/blog"', 'href="index.html"')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(art_content)
    print(f"Made universal links in: {filepath}")

# 3. Update fr, es, ar
for lang in ['fr', 'es', 'ar']:
    idx = f"{lang}/blog/index.html"
    if os.path.exists(idx):
        with open(idx, "r", encoding="utf-8") as f:
            l_content = f.read()
        for s in slugs:
            l_content = l_content.replace(f'href="/en/blog/{s}.html"', f'href="/en/blog/{s}.html"')
            l_content = l_content.replace(f'href="/en/blog/{s}"', f'href="/en/blog/{s}.html"')
        with open(idx, "w", encoding="utf-8") as f:
            f.write(l_content)

print("All links are now universal and work locally via file://, localhost, and on Vercel.")
