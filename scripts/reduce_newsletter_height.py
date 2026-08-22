import glob
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

    # Reduce .band-newsletter padding
    content = re.sub(
        r'\.band-newsletter\s*\{[^}]*\}',
        """.band-newsletter {
      background-color: #F6F7EA !important;
      padding: 64px 0 72px;
      width: 100%;
      box-sizing: border-box;
      border-top: 1px solid rgba(39, 39, 36, 0.08);
    }""",
        content
    )

    # Adjust inner subtext margin from 40px to 28px
    content = content.replace("margin: 0 auto 40px;", "margin: 0 auto 28px;")
    content = content.replace("margin: 0 0 18px;\n    }", "margin: 0 0 14px;\n    }")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Reduced height in: {filepath}")

print("All index files updated with sleeker newsletter height.")
