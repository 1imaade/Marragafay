import glob
import os
import re

# Find all article html files in en/blog, fr/blog, es/blog, ar/blog
article_files = glob.glob("*/blog/*.html")

# Remove index.html
article_files = [f for f in article_files if not f.endswith("index.html")]

for filepath in article_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Make related cards frameless
    content = content.replace(
        "    .related-card {\n      display: flex;\n      flex-direction: column;\n      text-decoration: none;\n      color: inherit;\n      border-radius: 4px;\n      overflow: hidden;\n      background: #EEF0E2;\n      transition: transform 0.25s cubic-bezier(0.4,0,0.2,1);\n    }",
        "    .related-card {\n      display: flex;\n      flex-direction: column;\n      text-decoration: none;\n      color: inherit;\n      border-radius: 4px;\n      overflow: hidden;\n      background: transparent;\n      transition: transform 0.25s cubic-bezier(0.4,0,0.2,1);\n    }"
    )
    # Just in case the format is different
    content = re.sub(
        r'\.related-card\s*\{[^}]*background:\s*#EEF0E2;[^}]*\}',
        ".related-card { display: flex; flex-direction: column; text-decoration: none; color: inherit; background: transparent; transition: transform 0.25s ease; }",
        content
    )
    content = re.sub(
        r'\.related-card:hover\s*\{[^}]*box-shadow:[^}]*\}',
        ".related-card:hover { text-decoration: none; color: inherit; }",
        content
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated {len(article_files)} article pages to have frameless related cards.")
