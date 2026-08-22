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

    # Make absolutely sure all sections have inline #F6F7EA
    content = content.replace(
        '<section class="editorial-band">',
        '<section class="editorial-band" style="background-color: #F6F7EA !important;">'
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Enforced #F6F7EA inline across all index files.")
