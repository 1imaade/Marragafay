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

    # The current structure:
    # <span class="absolute top-2 -left-[5px] w-2.5 h-2.5 rounded-full bg-[#523225]"></span>
    
    old_span = '<span class="absolute top-2 -left-[5px] w-2.5 h-2.5 rounded-full bg-[#523225]">'
    new_span = '<span class="absolute top-2 -left-[5px] w-2.5 h-2.5 rounded-full bg-[#523225] transform translate-y-[2px] md:translate-y-[3px]">'
    
    if old_span in content:
        new_content = content.replace(old_span, new_span)
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed dots in {filepath}")

for f in html_files:
    process_file(f)

