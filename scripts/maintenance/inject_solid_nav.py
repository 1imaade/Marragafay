import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

# 1. Extract <nav> from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

nav_match = re.search(r'(<nav\b[^>]*>.*?</nav>)', index_content, flags=re.DOTALL | re.IGNORECASE)
if not nav_match:
    print("Could not find <nav> in index.html")
    exit(1)

nav_block = nav_match.group(1)

# 2. Mutate the extracted nav block
# Remove transparent/dark classes
nav_block = re.sub(r'\b(ftco_navbar|ftco-navbar-light|navbar-light|navbar-dark|bg-transparent|bg-dark|text-white|text-gray-100|text-\[\#F6F7EA\])\b', '', nav_block)

# Remove id="ftco-navbar"
nav_block = re.sub(r'\bid="[^"]*"\b', '', nav_block)

# Add strict solid classes: bg-[#F6F7EA] text-[#10100E] fixed w-full top-0 z-50
nav_class_match = re.search(r'<nav\b[^>]*class="([^"]*)"', nav_block)
if nav_class_match:
    classes = nav_class_match.group(1).split()
    classes = [c for c in classes if c.strip()]
    classes.extend(['bg-[#F6F7EA]', 'text-[#10100E]', 'fixed', 'w-full', 'top-0', 'z-50', 'shadow-sm'])
    classes = list(dict.fromkeys(classes))
    new_class_str = 'class="' + ' '.join(classes) + '"'
    nav_block = re.sub(r'class="[^"]*"', new_class_str, nav_block, count=1)
else:
    nav_block = re.sub(r'<nav\b', '<nav class="navbar navbar-expand-lg bg-[#F6F7EA] text-[#10100E] fixed w-full top-0 z-50 shadow-sm"', nav_block, count=1)

# Clean up multiple spaces
nav_block = re.sub(r'\s+', ' ', nav_block).replace('> <', '><').replace('class=" ', 'class="')

# Format properly with newlines for aesthetics
nav_block = nav_block.replace('</nav>', '\n</nav>')
nav_block = nav_block.replace('<nav', '\n<nav')

injected_files = []

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    # 3. Inject at the top of <body> (after noscript if it exists)
    # We will search for <!-- END nav --> and inject before it, or if missing, just after <body>
    if '<!-- END nav -->' in content:
        content = content.replace('<!-- END nav -->', f"{nav_block}\n  <!-- END nav -->")
    elif '</noscript>' in content:
        content = content.replace('</noscript>', f"</noscript>\n{nav_block}\n")
    else:
        content = re.sub(r'(<body[^>]*>)', f"\\1\n{nav_block}\n", content, count=1, flags=re.IGNORECASE)
        
    # 4. Padding Adjustment
    # Find the first major section. Typically <div class="hero-wrap...
    # We'll just add inline style padding-top: 100px to it or pt-24 if using tailwind.
    # Let's add pt-[100px] to the hero-wrap or whatever is the first element.
    # We can inject a <style> block right after the nav to force padding on the next element.
    # Better: dynamically add pt-24 to hero-wrap or ftco-section.
    hero_match = re.search(r'<div\b[^>]*class="[^"]*hero-wrap[^"]*"[^>]*>', content)
    if hero_match:
        hero_tag = hero_match.group(0)
        # add padding-top: 100px to style, or create style if doesn't exist
        if 'style="' in hero_tag:
            new_hero_tag = re.sub(r'style="', 'style="padding-top: 100px; ', hero_tag)
        else:
            new_hero_tag = hero_tag.replace('class="', 'style="padding-top: 100px;" class="')
        content = content.replace(hero_tag, new_hero_tag, 1)
    else:
        # Check for ftco-section
        section_match = re.search(r'<section\b[^>]*class="[^"]*ftco-section[^"]*"[^>]*>', content)
        if section_match:
            sec_tag = section_match.group(0)
            if 'style="' in sec_tag:
                new_sec_tag = re.sub(r'style="', 'style="padding-top: 100px; ', sec_tag)
            else:
                new_sec_tag = sec_tag.replace('class="', 'style="padding-top: 100px;" class="')
            content = content.replace(sec_tag, new_sec_tag, 1)

    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        injected_files.append(file)

print("Injected files:")
for f in injected_files:
    print("- " + f)

