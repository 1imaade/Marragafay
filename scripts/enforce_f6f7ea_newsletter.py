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

    # Enforce inline style on the section tag
    content = content.replace(
        '<section class="band-newsletter">',
        '<section class="band-newsletter" style="background-color: #F6F7EA !important;">'
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Enforced #F6F7EA on: {filepath}")

print("All index files have #F6F7EA explicitly enforced.")
