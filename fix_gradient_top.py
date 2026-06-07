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

    # The current overlay:
    old_overlay = 'bg-gradient-to-t from-[#10100E]/95 via-transparent via-40% md:via-50% to-[#10100E]/40'
    new_overlay = 'bg-gradient-to-t from-[#10100E]/95 via-transparent via-40% md:via-50% to-transparent'
    
    if old_overlay in content:
        content = content.replace(old_overlay, new_overlay)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Patched top gradient to transparent in {filepath}")

for f in html_files:
    process_file(f)

