import glob

files = glob.glob("en/blog/*.html")

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Clean up any preload navbar-stayhere.css
    content = content.replace('<link rel="preload" href="/css/navbar-stayhere.css" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n  <noscript><link rel="stylesheet" href="/css/navbar-stayhere.css"></noscript>', '')
    content = content.replace('<link rel="preload" href="/css/navbar-stayhere.css" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">', '')
    content = content.replace('<noscript><link rel="stylesheet" href="/css/navbar-stayhere.css"></noscript>', '')

    # 2. Ensure standard clean CSS block in <head>
    standard_css_block = """  <!-- CSS -->
  <link rel="stylesheet" href="/css/vendor-bundle.css">
  <link rel="stylesheet" href="/css/custom-bundle.css">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/navbar-stayhere.css">
  <link rel="stylesheet" href="/css/tailwind-built.css">"""

    # Replace existing CSS block if present
    old_css_blocks = [
        """  <!-- CSS -->
  <link rel="stylesheet" href="/css/vendor-bundle.css">
  <link rel="stylesheet" href="/css/custom-bundle.css">
  <link rel="stylesheet" href="/css/style.css">""",
        """  <!-- ═══════════════════════════════════════════════
       CSS BUNDLE
  ═══════════════════════════════════════════════ -->
  <link rel="stylesheet" href="/css/vendor-bundle.css">
  <link rel="stylesheet" href="/css/custom-bundle.css">
  <link rel="stylesheet" href="/css/style.css">"""
    ]

    for old_block in old_css_blocks:
        if old_block in content:
            content = content.replace(old_block, standard_css_block)

    # If navbar-stayhere.css is not yet present, add it after style.css
    if '/css/navbar-stayhere.css' not in content:
        content = content.replace('<link rel="stylesheet" href="/css/style.css">', '<link rel="stylesheet" href="/css/style.css">\n  <link rel="stylesheet" href="/css/navbar-stayhere.css">')

    # If tailwind-built.css is not in head before </head>, ensure it is
    if '/css/tailwind-built.css' not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="/css/tailwind-built.css">\n</head>')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed navbar CSS in: {filepath}")

print("All article files updated with navbar-stayhere.css and tailwind-built.css.")
