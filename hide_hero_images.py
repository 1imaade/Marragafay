import os
import glob

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    old_class = 'class="col-span-1 lg:col-span-1 grid grid-rows-2 gap-[2px] h-full w-full"'
    new_class = 'class="col-span-1 lg:col-span-1 hidden lg:grid grid-rows-2 gap-[2px] h-full w-full"'
    
    content = content.replace(old_class, new_class)

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
