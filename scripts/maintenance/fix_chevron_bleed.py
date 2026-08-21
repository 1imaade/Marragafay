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

    # Update style block
    old_style = '.is-active .itinerary-header { transform: scale(1.03) !important; }'
    new_style = '.is-active .itinerary-text-group { transform: scale(1.03) !important; }'
    if old_style in content:
        content = content.replace(old_style, new_style)

    # Restructure DOM
    pattern = (
        r'<div class="flex flex-row items-baseline gap-2 md:block w-full itinerary-header cursor-pointer md:cursor-auto transition-transform duration-300 ease-in-out origin-left">\s*'
        r'(<div class="itinerary-step[^>]*>STEP \d+</div>)\s*'
        r'<h3 class="itinerary-title text-\[12px\] font-semibold text-\[#10100E\] tracking-widest uppercase mb-1 md:mb-2 flex-1 flex justify-between items-center md:block">([^<]*)'
        r'<svg class="([^"]*)"([^>]*)>(.*?)</svg></h3>\s*'
        r'</div>'
    )

    def replacer(m):
        step_html = m.group(1)
        title_text = m.group(2)
        chevron_classes = m.group(3).replace('ml-auto ', '')
        chevron_rest = m.group(4)
        chevron_inner = m.group(5)
        
        header_parent = '<div class="flex flex-row justify-between items-center md:block w-full itinerary-header cursor-pointer md:cursor-auto">'
        inner_wrapper = '<div class="flex flex-row items-baseline gap-2 md:block itinerary-text-group transition-transform duration-300 ease-in-out origin-left">'
        new_h3 = f'<h3 class="itinerary-title text-[12px] font-semibold text-[#10100E] tracking-widest uppercase mb-1 md:mb-2">{title_text}</h3>'
        chevron = f'<svg class="{chevron_classes}"{chevron_rest}>{chevron_inner}</svg>'
        
        return f'{header_parent}\n              {inner_wrapper}\n                {step_html}\n                {new_h3}\n              </div>\n              {chevron}\n            </div>'

    content = re.sub(pattern, replacer, content)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Patched bleed in {filepath}")

for f in html_files:
    process_file(f)

