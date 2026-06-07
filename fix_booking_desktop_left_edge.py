import os
import glob

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # The container currently has `rounded-l-none rounded-r-3xl xl:rounded-full`
    # We will change `xl:rounded-full` to `xl:rounded-r-full xl:rounded-l-none`
    # to ensure the left edge is completely square across ALL breakpoints.
    old_classes = 'rounded-l-none rounded-r-3xl xl:rounded-full'
    new_classes = 'rounded-l-none rounded-r-3xl xl:rounded-l-none xl:rounded-r-full'
    
    content = content.replace(old_classes, new_classes)

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
