import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace UL classes
content = content.replace('ul class="space-y-4"', 'ul class="space-y-4 list-none p-0 m-0"')

# Replace link/li classes to add block
# Inquiries
content = content.replace('class="text-[#a3a39a] hover:text-[#FF5A36] text-[14px] transition-colors"', 'class="text-[#a3a39a] hover:text-[#FF5A36] text-[14px] transition-colors block"')
content = content.replace('class="text-[#a3a39a] text-[14px] mt-4 leading-[22px]"', 'class="text-[#a3a39a] text-[14px] mt-4 leading-[22px] block"')

# Experience / Legal
content = content.replace('class="text-[#a3a39a] hover:text-[#F6F7EA] text-[14px] transition-colors"', 'class="text-[#a3a39a] hover:text-[#F6F7EA] text-[14px] transition-colors block"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html footer css resets applied.")
