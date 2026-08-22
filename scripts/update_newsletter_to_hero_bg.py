import glob

index_files = [
    "en/blog/index.html",
    "fr/blog/index.html",
    "es/blog/index.html",
    "ar/blog/index.html"
]

for filepath in index_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Update .band-newsletter background to #F6F7EA (hero background color)
    content = content.replace(
        "background-color: #E8E2D5 !important;\n      padding: 96px 0 106px;\n      width: 100%;\n      box-sizing: border-box;\n      border-top: 1px solid rgba(39, 39, 36, 0.08);",
        "background-color: #F6F7EA !important;\n      padding: 96px 0 106px;\n      width: 100%;\n      box-sizing: border-box;\n      border-top: 1px solid rgba(39, 39, 36, 0.08);"
    )
    # Also handle single line
    content = content.replace(
        ".band-newsletter {\n      background-color: #E8E2D5 !important;",
        ".band-newsletter {\n      background-color: #F6F7EA !important;"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated newsletter background to #F6F7EA in: {filepath}")

print("All language files updated!")
