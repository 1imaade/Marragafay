import os
import glob
import re

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # The user wants to add the same left/right padding to the gallery section.
    # The gallery section currently has `px-0 md:px-10 lg:px-16`
    # We will change it to `px-4 md:px-10 lg:px-16` to match the text sections.
    
    # Let's target the gallery section specifically
    old_class = '<section id="experience-gallery" class="w-full py-24 bg-[#10100E] px-0 md:px-10 lg:px-16 flex flex-col items-center scroll-mt-32" style="background-color: #10100E !important;">'
    new_class = '<section id="experience-gallery" class="w-full py-24 bg-[#10100E] px-4 md:px-10 lg:px-16 flex flex-col items-center scroll-mt-32" style="background-color: #10100E !important;">'
    
    # Also just in case the py-24 was changed or something, let's use regex
    pattern = r'(<section id="experience-gallery"[^>]*?)px-0 md:px-10 lg:px-16([^>]*?>)'
    content = re.sub(pattern, r'\1px-4 md:px-10 lg:px-16\2', content)

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
