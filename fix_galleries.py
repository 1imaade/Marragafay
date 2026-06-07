import os
import glob

# Find all html files in packages/ and activities/
files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Update the grid container
    old_grid = 'class="grid grid-cols-1 md:grid-cols-3 gap-2 auto-rows-[250px] md:auto-rows-[280px]"'
    new_grid = 'class="grid grid-cols-2 md:grid-cols-3 gap-3 md:gap-4 auto-rows-[180px] sm:auto-rows-[220px] md:auto-rows-[280px]"'
    content = content.replace(old_grid, new_grid)

    # 2. Update the first image (Main Anchor Image)
    old_main = 'class="md:col-span-2 md:row-span-2 relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer"'
    new_main = 'class="col-span-2 row-span-2 md:col-span-2 md:row-span-2 relative rounded-2xl overflow-hidden group bg-white/5 cursor-pointer"'
    content = content.replace(old_main, new_main)

    # 3. Update the other images (Right Stack and Bottom Rows)
    old_other = 'class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer"'
    new_other = 'class="col-span-1 relative rounded-2xl overflow-hidden group bg-white/5 cursor-pointer"'
    content = content.replace(old_other, new_other)

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Updated {len(files)} files.")
