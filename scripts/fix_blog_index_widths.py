import re

index_files = [
    "en/blog/index.html",
    "fr/blog/index.html",
    "es/blog/index.html",
    "ar/blog/index.html"
]

for filepath in index_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Hero Inner max-width from 1200px to 1440px
    content = re.sub(r'\.journal-hero__inner\s*\{[^}]*\}',
        """.journal-hero__inner { max-width: 1440px; margin: 0 auto; padding: 0 32px; box-sizing: border-box; }""",
        content
    )

    # 2. Update Journal Section max-width from 1200px to 1440px
    content = re.sub(r'\.journal-section\s*\{[^}]*\}',
        """.journal-section { max-width: 1440px; margin: 0 auto; padding: 0 32px; box-sizing: border-box; }""",
        content
    )

    # 3. Enhance Featured Article typography and padding
    content = re.sub(r'\.featured-article__content\s*\{[^}]*\}',
        """.featured-article__content { padding: 60px 60px 60px 64px; display: flex; flex-direction: column; justify-content: center; background: #EEF0E2; box-sizing: border-box; }""",
        content
    )

    content = re.sub(r'\.featured-article__title\s*\{[^}]*\}',
        """.featured-article__title { font-size: clamp(1.8rem, 3.2vw, 2.75rem); font-weight: 700; line-height: 1.1; letter-spacing: -0.02em; color: #272724; margin: 0 0 20px; }""",
        content
    )

    content = re.sub(r'\.featured-article__excerpt\s*\{[^}]*\}',
        """.featured-article__excerpt { font-size: 1.05rem; line-height: 1.75; color: #5a5a54; margin: 0 0 32px; max-width: 540px; }""",
        content
    )

    # 4. Enhance Card body & typography
    content = re.sub(r'\.article-card__body\s*\{[^}]*\}',
        """.article-card__body { padding: 30px 28px 26px; display: flex; flex-direction: column; flex: 1; box-sizing: border-box; }""",
        content
    )

    content = re.sub(r'\.article-card__title\s*\{[^}]*\}',
        """.article-card__title { font-size: 1.15rem; font-weight: 700; line-height: 1.3; letter-spacing: -0.01em; color: #272724; margin: 0 0 12px; }""",
        content
    )

    content = re.sub(r'\.article-card__excerpt\s*\{[^}]*\}',
        """.article-card__excerpt { font-size: 0.925rem; line-height: 1.7; color: #5a5a54; margin: 0 0 20px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }""",
        content
    )

    # In Arabic, ensure text alignment remains right
    if "ar/blog" in filepath:
        content = content.replace("text-align: right;", "text-align: right;")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated container width to 1440px in: {filepath}")

print("All blog index pages updated successfully.")
