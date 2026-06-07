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

    # The line is currently:
    # <div class="absolute top-[16px] bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-[#523225] group-last:hidden timeline-line"></div>
    # We will replace `bottom-0` with `-bottom-[38px] md:-bottom-[46px]`
    
    old_line = '<div class="absolute top-[16px] bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-[#523225] group-last:hidden timeline-line"></div>'
    new_line = '<div class="absolute top-[16px] -bottom-[38px] md:-bottom-[46px] left-1/2 -translate-x-1/2 w-[1.5px] bg-[#523225] group-last:hidden timeline-line"></div>'
    
    if old_line in content:
        content = content.replace(old_line, new_line)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Patched math in {filepath}")

for f in html_files:
    process_file(f)
