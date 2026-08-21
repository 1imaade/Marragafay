import os
import glob

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Change hover color of h3
    content = content.replace('group-hover:text-[#FF5A36]', 'group-hover:text-[#523225]')
    content = content.replace('group-hover:text-[#FF5A26]', 'group-hover:text-[#523225]')

    # Change text color of span
    content = content.replace('text-[#FF5A26]', 'text-[#523225]')
    content = content.replace('text-[#FF5A36]', 'text-[#523225]')

    # Change inline style color of span
    content = content.replace('color: #FF5A26;', 'color: #523225;')
    content = content.replace('color: #FF5A36;', 'color: #523225;')

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
