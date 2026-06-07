import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace wrapper border classes
content = content.replace('class="border-t-[1px] border-solid border-[#d1cfc0]"', 'class="border-t border-[#d1cfc0] border-x-0 border-b-0"')

# Replace item border classes
content = content.replace('class="border-b-[1px] border-solid border-[#d1cfc0] py-4 cursor-pointer group faq-item"', 'class="border-b border-[#d1cfc0] border-x-0 border-t-0 py-4 cursor-pointer group faq-item"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html borders replaced.")
