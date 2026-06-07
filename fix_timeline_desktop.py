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

    # The current structure has a flex wrapper:
    # <div class="flex flex-row items-baseline gap-2 md:flex-col md:items-start md:gap-0">
    #   <div class="... mb-0 md:mb-1">STEP X</div>
    #   <h3 class="mt-0 md:mt-1 ...">...</h3>
    # </div>
    
    # We will replace it with:
    # <div class="flex flex-row items-baseline gap-2 md:block">
    #   <div class="... mb-0 md:mb-1">STEP X</div>
    #   <h3 class="...">...</h3>
    # </div>
    
    pattern = r'<div class="flex flex-row items-baseline gap-2 md:flex-col md:items-start md:gap-0">\s*(<div class="text-\[12px\][^>]*>STEP \d+</div>)\s*<h3 class="mt-0 md:mt-1 ([^"]*)">([^<]*)</h3>\s*</div>'
    
    def replacer(m):
        step_div = m.group(1)
        h3_classes = m.group(2)
        h3_text = m.group(3)
        
        wrapper = f'<div class="flex flex-row items-baseline gap-2 md:block">\n              {step_div}\n              <h3 class="{h3_classes}">{h3_text}</h3>\n            </div>'
        return wrapper
        
    new_content = re.sub(pattern, replacer, content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

for f in html_files:
    process_file(f)

