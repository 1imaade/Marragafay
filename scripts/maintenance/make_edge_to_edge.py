import os
import glob

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Update Reviews Section
    old_reviews_sec = '<section class="w-full py-24 px-5 md:px-10 lg:px-16"'
    new_reviews_sec = '<section class="w-full py-24 px-0 md:px-10 lg:px-16"'
    content = content.replace(old_reviews_sec, new_reviews_sec)

    old_reviews_head = '<div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-4 md:gap-0">'
    new_reviews_head = '<div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-4 md:gap-0 px-5 md:px-0">'
    content = content.replace(old_reviews_head, new_reviews_head)

    old_reviews_grid = '<div class="grid grid-cols-1 md:grid-cols-3 gap-y-12">'
    new_reviews_grid = '<div class="grid grid-cols-1 md:grid-cols-3 gap-y-12 px-5 md:px-0">'
    content = content.replace(old_reviews_grid, new_reviews_grid)

    # 2. Update FAQ Section
    old_faq_sec = 'class="w-full py-24 bg-[#F6F7EA] border-t border-[#e2e0d3] px-5 md:px-10 lg:px-16 flex flex-col items-center"'
    new_faq_sec = 'class="w-full py-24 bg-[#F6F7EA] border-t border-[#e2e0d3] px-0 md:px-10 lg:px-16 flex flex-col items-center"'
    content = content.replace(old_faq_sec, new_faq_sec)

    old_faq_head = '<div class="w-full mb-12">'
    new_faq_head = '<div class="w-full mb-12 px-5 md:px-0">'
    content = content.replace(old_faq_head, new_faq_head)

    old_faq_item = 'class="cursor-pointer group faq-item"'
    new_faq_item = 'class="cursor-pointer group faq-item px-5 md:px-0"'
    content = content.replace(old_faq_item, new_faq_item)

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
