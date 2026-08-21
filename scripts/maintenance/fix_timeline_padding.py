import os

html_files = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html') and ('packages' in root or 'activities' in root):
            html_files.append(os.path.join(root, file))

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Change pb-6 to pb-8
    content = content.replace('<div class="relative flex flex-row items-stretch pb-6 md:pb-10 group">', '<div class="relative flex flex-row items-stretch pb-8 md:pb-10 group">')

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Patched {filepath}")

for f in html_files:
    process_file(f)
