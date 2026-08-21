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

    # Original STEP: text-[12px] font-semibold text-[#523225] tracking-widest uppercase mb-0 md:mb-1
    # Original Title: text-[18px] font-semibold text-[#10100E] tracking-tight capitalize mb-1 md:mb-2
    
    # regex matches:
    pattern = r'(<div class=")(text-\[12px\] font-semibold) (text-\[#523225\]) (tracking-widest uppercase)( mb-0 md:mb-1">STEP \d+</div>)\s*(<h3 class=")(text-\[18px\] font-semibold) (text-\[#10100E\]) (tracking-tight capitalize)( mb-1 md:mb-2">)([^<]*</h3>)'
    
    def replacer(m):
        step_open = m.group(1)
        step_micro = m.group(2)
        step_color = m.group(3)
        step_micro_track = m.group(4)
        step_close = m.group(5)
        
        h3_open = m.group(6)
        h3_macro = m.group(7)
        h3_color = m.group(8)
        h3_macro_track = m.group(9)
        h3_close = m.group(10)
        h3_text = m.group(11)
        
        # New STEP classes: Macro size/weight/tracking, original color
        new_step_classes = f"{h3_macro} {step_color} {h3_macro_track}"
        
        # New TITLE classes: Micro size/weight/tracking, original color
        new_h3_classes = f"{step_micro} {h3_color} {step_micro_track}"
        
        wrapper = f'{step_open}{new_step_classes}{step_close}\n              {h3_open}{new_h3_classes}{h3_close}{h3_text}'
        return wrapper
        
    new_content = re.sub(pattern, replacer, content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

for f in html_files:
    process_file(f)

