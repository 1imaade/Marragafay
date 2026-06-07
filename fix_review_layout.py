import re
import os

files_to_update = ['packages/basic.html', 'packages/comfort.html', 'packages/luxe.html']

for filepath in files_to_update:
    with open(filepath, 'r') as f:
        content = f.read()

    # The current wrong layout block:
    pattern = (
        r'<div class="mt-auto pt-2 flex items-center gap-3">\s*'
        r'<div class="w-10 h-10 rounded-full bg-\[#10100E\] flex items-center justify-center flex-shrink-0">\s*'
        r'<span class="text-white text-\[13px\] font-semibold tracking-wider">([^<]+)</span>\s*'
        r'</div>\s*'
        r'<div>\s*'
        r'<p class="text-\[#523225\] text-\[14px\] font-semibold uppercase tracking-wide leading-tight">([^<]+)</p>\s*'
        r'<p class="text-\[#5c5c56\] text-\[12px\] leading-tight">([^<]+)</p>\s*'
        r'</div>\s*'
        r'</div>'
    )

    def replacer(m):
        initials = m.group(1)
        name = m.group(2)
        meta = m.group(3)
        return f'''<div class="mt-auto">
          <div class="w-10 h-10 rounded-full bg-[#10100E] flex items-center justify-center mb-3">
            <span class="text-white text-[13px] font-semibold tracking-wider">{initials}</span>
          </div>
          <p class="text-[#523225] text-[14px] font-semibold uppercase tracking-wide">{name}</p>
          <p class="text-[#5c5c56] text-[12px] mt-1">{meta}</p>
        </div>'''

    new_content = re.sub(pattern, replacer, content)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Fixed review layout in {filepath}")

