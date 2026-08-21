import os
import re

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

    # The current overlay: <div class="absolute inset-x-0 bottom-0 h-[40%] bg-gradient-to-t from-[#10100E]/90 via-[#10100E]/30 to-transparent z-10 pointer-events-none"></div>
    # We want to change to: <div class="absolute inset-0 bg-gradient-to-t from-[#10100E] via-[#10100E]/70 via-60% md:via-50% to-[#10100E]/30 z-10 pointer-events-none"></div>
    
    old_overlay = '<div class="absolute inset-x-0 bottom-0 h-[40%] bg-gradient-to-t from-[#10100E]/90 via-[#10100E]/30 to-transparent z-10 pointer-events-none"></div>'
    new_overlay = '<div class="absolute inset-0 bg-gradient-to-t from-[#10100E] via-[#10100E]/70 via-60% md:via-50% to-[#10100E]/30 z-10 pointer-events-none"></div>'
    
    if old_overlay in content:
        content = content.replace(old_overlay, new_overlay)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Patched gradient in {filepath}")

for f in html_files:
    process_file(f)

