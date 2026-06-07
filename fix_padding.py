import os
import glob

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Target the Gallery section (edge-to-edge on mobile)
    old_gallery = 'class="w-full py-24 bg-[#10100E] px-5 xl:px-20 flex flex-col items-center scroll-mt-32"'
    new_gallery = 'class="w-full py-24 bg-[#10100E] px-0 md:px-10 lg:px-16 flex flex-col items-center scroll-mt-32"'
    content = content.replace(old_gallery, new_gallery)

    # 2. Target Text-Heavy Sections (Itinerary, Reviews, FAQ)
    # They currently all use `px-5 xl:px-20`
    content = content.replace('px-5 xl:px-20', 'px-5 md:px-10 lg:px-16')

    # 3. Align inner content (remove rogue paddings if they exist)
    # e.g., the FAQ items might have p-8 or p-6? Let's check common tailwind classes
    # We will just write the content back.
    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
