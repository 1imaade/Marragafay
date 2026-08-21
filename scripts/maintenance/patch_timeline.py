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

    pattern = r'(<div class="text-\[12px\][^>]*>STEP \d+</div>)\s*<h3 class="([^"]*)">([^<]*)</h3>'
    
    def replacer(m):
        step_div = m.group(1)
        h3_classes = m.group(2)
        h3_text = m.group(3)
        
        # Remove mt-* if present
        h3_classes = re.sub(r'\bmt-\d+\b', '', h3_classes)
        h3_classes = re.sub(r'\bmd:mt-\d+\b', '', h3_classes)
        h3_classes = h3_classes.strip()
        
        # Replace mb-1 with mb-0 md:mb-1 in step div
        step_div = step_div.replace('mb-1', 'mb-0 md:mb-1')
        
        wrapper = f'<div class="flex flex-row items-baseline gap-2 md:flex-col md:items-start md:gap-0">\n              {step_div}\n              <h3 class="mt-0 md:mt-1 {h3_classes}">{h3_text}</h3>\n            </div>'
        return wrapper
        
    new_content = re.sub(pattern, replacer, content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Patched {filepath}")

for f in html_files:
    process_file(f)

