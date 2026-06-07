import re
import os

files_to_update = ['packages/basic.html', 'packages/comfort.html', 'packages/luxe.html']

for filepath in files_to_update:
    with open(filepath, 'r') as f:
        content = f.read()

    # The current profile circle block:
    pattern = r'\s*<div class="w-10 h-10 rounded-full bg-\[#10100E\] flex items-center justify-center mb-3">\s*<span class="text-white text-\[13px\] font-semibold tracking-wider">[^<]+</span>\s*</div>'

    new_content = re.sub(pattern, '', content)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Removed avatar circles in {filepath}")

