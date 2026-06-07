import os
import glob

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Reduce the global text-heavy padding from px-5 to px-4 on mobile
    content = content.replace('px-5 md:px-10 lg:px-16', 'px-4 md:px-10 lg:px-16')

    # 2. Reduce the excessive timeline left padding
    # From `<div class="relative pl-8">` to `<div class="relative pl-5 md:pl-8">`
    content = content.replace('<div class="relative pl-8">', '<div class="relative pl-5 md:pl-8">')

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
