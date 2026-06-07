import os
import re

html_files = [
    'activities.html',
    'packs.html',
    'about.html',
    'reviews.html',
    'contact.html',
    'blog.html',
    'blog-single.html',
    'checkout.html'
]

for file in html_files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Purge problematic classes from <nav>
    def nav_replacer(match):
        nav_tag = match.group(0)
        # Remove any potential transparent classes
        nav_tag = re.sub(r'\b(ftco_navbar|ftco-navbar-light|navbar-light|navbar-dark|bg-transparent|bg-dark|text-white|text-gray-100)\b', '', nav_tag)
        
        # Ensure we have bg-[#F6F7EA] and text-[#10100E]
        if 'bg-[#F6F7EA]' not in nav_tag:
            nav_tag = re.sub(r'class="', 'class="bg-[#F6F7EA] ', nav_tag)
        if 'text-[#10100E]' not in nav_tag:
            nav_tag = re.sub(r'class="', 'class="text-[#10100E] ', nav_tag)
            
        # Clean up multiple spaces
        nav_tag = re.sub(r'\s+', ' ', nav_tag).replace('class=" ', 'class="')
        
        return nav_tag

    content = re.sub(r'<nav\b[^>]*>', nav_replacer, content)
    
    # 2. Search for any script tag blocks that might add scroll logic for navbar
    # We already removed the inline // Header shrink-on-scroll logic in the previous step,
    # but let's check for any remaining.
    content = re.sub(
        r'<script[^>]*>\s*(?://.*?)*\s*document\.addEventListener\([\'"]DOMContentLoaded[\'"], function \(\) \{\s*const navbar = document\.querySelector\([\'"]#ftco-navbar[\'"]\).*?\}\);\s*\}\);\s*</script>',
        '', content, flags=re.MULTILINE | re.DOTALL)
        
    # Remove any stray JS scroll event listeners modifying the navbar
    content = re.sub(
        r'window\.addEventListener\([\'"]scroll[\'"], function \(\) \{\s*if \(window\.scrollY > \d+\) \{\s*navbar\.classList\.add\([\'"]scrolled[\'"]\);\s*\} else \{\s*navbar\.classList\.remove\([\'"]scrolled[\'"]\);\s*\}\s*\}\);',
        '', content, flags=re.MULTILINE | re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

