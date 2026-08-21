import os
import glob

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    old_div = '<div class="w-full flex justify-end">'
    new_div = '<div class="w-full flex justify-start">'
    
    old_p = '<p class="text-[12px] text-[#10100E]/50 font-medium text-right pr-2 tracking-tight mt-2 mb-0">No upfront payment required'
    new_p = '<p class="text-[12px] text-[#10100E]/50 font-medium text-left tracking-tight mt-2 mb-0">No upfront payment required'
    
    content = content.replace(old_div, new_div)
    content = content.replace(old_p, new_p)

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
