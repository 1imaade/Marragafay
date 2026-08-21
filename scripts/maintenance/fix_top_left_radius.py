import os
import glob
import re

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Fix the Main Container
    old_container = 'rounded-l-none rounded-r-3xl xl:rounded-l-none xl:rounded-r-full'
    new_container = 'rounded-3xl rounded-bl-none xl:rounded-r-full xl:rounded-l-none'
    content = content.replace(old_container, new_container)

    # 2. Fix the Date Input
    old_date = 'booking-input-cell rounded-l-none'
    new_date = 'booking-input-cell rounded-tl-3xl rounded-bl-none xl:rounded-l-none'
    content = content.replace(old_date, new_date)

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
