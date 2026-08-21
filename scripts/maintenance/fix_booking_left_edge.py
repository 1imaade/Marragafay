import os
import glob

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # The main container was previously updated to have `rounded-xl xl:rounded-full`
    old_classes = 'rounded-xl xl:rounded-full'
    new_classes = 'rounded-l-none rounded-r-3xl xl:rounded-full'
    
    # We only want to replace it on the booking form container, which has this specific string:
    target = 'class="flex flex-col xl:flex-row items-stretch bg-white border border-[#10100E]/10 rounded-xl xl:rounded-full shadow-sm w-full 2xl:w-auto"'
    replacement = 'class="flex flex-col xl:flex-row items-stretch bg-white border border-[#10100E]/10 rounded-l-none rounded-r-3xl xl:rounded-full shadow-sm w-full 2xl:w-auto"'
    
    content = content.replace(target, replacement)

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
