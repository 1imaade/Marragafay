import re

indexes = {
    "en": {"path": "en/blog/index.html", "arrow": "Read &rarr;"},
    "fr": {"path": "fr/blog/index.html", "arrow": "Lire &rarr;"},
    "es": {"path": "es/blog/index.html", "arrow": "Leer &rarr;"},
    "ar": {"path": "ar/blog/index.html", "arrow": "&larr; اقرأ"}
}

for lang, data in indexes.items():
    filepath = data["path"]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace standard article card meta with enhanced left + right arrow meta
    old_meta_pattern = re.compile(
        r'<div class="article-card__meta">\s*<span>([^<]+)</span>\s*<span class="article-card__meta-sep"[^>]*></span>\s*<span>([^<]+)</span>\s*</div>'
    )

    def replace_meta(match):
        date = match.group(1).strip()
        read_time = match.group(2).strip()
        arrow_text = data["arrow"]
        return f"""<div class="article-card__meta">
                <div class="article-card__meta-left">
                  <span>{date}</span>
                  <span class="article-card__meta-sep" aria-hidden="true"></span>
                  <span>{read_time}</span>
                </div>
                <span class="article-card__meta-arrow" aria-hidden="true">{arrow_text}</span>
              </div>"""

    content = old_meta_pattern.sub(replace_meta, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Enhanced card meta rows in: {filepath}")

print("All language index pages updated with interactive card meta.")
