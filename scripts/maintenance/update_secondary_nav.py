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
    
    original_content = content
    
    # 1. Modify the <nav> element's classes
    # Look for <nav class="... ftco_navbar ..." ...>
    # We'll just replace 'navbar-dark', 'bg-dark', 'ftco-navbar-light', 'bg-transparent', 'text-white', 'text-[#F6F7EA]'
    def nav_replacer(match):
        nav_tag = match.group(0)
        nav_tag = nav_tag.replace('navbar-dark', '')
        nav_tag = nav_tag.replace('bg-dark', '')
        nav_tag = nav_tag.replace('ftco-navbar-light', '')
        nav_tag = nav_tag.replace('bg-transparent', '')
        nav_tag = nav_tag.replace('text-white', '')
        nav_tag = nav_tag.replace('text-[#F6F7EA]', '')
        
        # Add the new classes
        # Find class="..." and inject new classes
        class_match = re.search(r'class="([^"]*)"', nav_tag)
        if class_match:
            classes = class_match.group(1).split()
            # Clean up empty strings
            classes = [c for c in classes if c.strip()]
            classes.extend(['bg-[#F6F7EA]', 'text-[#10100E]', 'navbar-light']) # added navbar-light just in case bootstrap needs it
            # Remove duplicates just in case
            classes = list(dict.fromkeys(classes))
            new_class_str = 'class="' + ' '.join(classes) + '"'
            nav_tag = re.sub(r'class="[^"]*"', new_class_str, nav_tag)
        
        return nav_tag

    content = re.sub(r'<nav\b[^>]*>', nav_replacer, content)
    
    # 2. Remove the JavaScript snippet for navbar shrink
    # It looks like:
    # // Header shrink-on-scroll
    # const navbar = document.querySelector('#ftco-navbar');
    # window.addEventListener('scroll', function () {
    #   if (window.scrollY > 50) {
    #     navbar.classList.add('scrolled');
    #   } else {
    #     navbar.classList.remove('scrolled');
    #   }
    # });
    
    script_pattern = re.compile(
        r'// Header shrink-on-scroll\s+const navbar = document\.querySelector\([\'"]#ftco-navbar[\'"]\);\s+window\.addEventListener\([\'"]scroll[\'"], function \(\) \{\s+if \(window\.scrollY > 50\) \{\s+navbar\.classList\.add\([\'"]scrolled[\'"]\);\s+\} else \{\s+navbar\.classList\.remove\([\'"]scrolled[\'"]\);\s+\}\s+\}\);',
        re.MULTILINE | re.DOTALL
    )
    
    content = script_pattern.sub('', content)
    
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"No changes made to {file}")
