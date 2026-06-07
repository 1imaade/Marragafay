import os
import re

# Get all .html files in current directory except index.html
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Delete <nav>...</nav>
    content = re.sub(r'<nav\b[^>]*>.*?</nav>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Delete <header>...</header> just in case
    content = re.sub(r'<header\b[^>]*>.*?</header>', '', content, flags=re.DOTALL | re.IGNORECASE)

    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Purged {file}")

