import os
import re

html_files = [
    'activities.html',
    'packs.html',
    'about.html',
    'reviews.html',
    'contact.html',
    'blog.html',
    'blog-single.html',
    'checkout.html'
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the <nav> block
nav_match = re.search(r'(<nav\b[^>]*>.*?</nav>)', content, flags=re.DOTALL | re.IGNORECASE)
if not nav_match:
    print("Could not find <nav> in index.html")
    exit(1)
nav_block = nav_match.group(1)

modified_files = []

for file in html_files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Check if file has a nav block
    if re.search(r'<nav\b[^>]*>.*?</nav>', file_content, flags=re.DOTALL | re.IGNORECASE):
        new_content = re.sub(r'<nav\b[^>]*>.*?</nav>', nav_block.replace('\\', '\\\\'), file_content, count=1, flags=re.DOTALL | re.IGNORECASE)
        if new_content != file_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified_files.append(file)

print("Modified files:")
for f in modified_files:
    print("- " + f)
