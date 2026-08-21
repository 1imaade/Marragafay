import os
import glob

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Reduce the space between the brown dot and the step text
    old_pl = '<div class="relative pl-5 md:pl-8">'
    new_pl = '<div class="relative pl-3 md:pl-6">'
    content = content.replace(old_pl, new_pl)

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
