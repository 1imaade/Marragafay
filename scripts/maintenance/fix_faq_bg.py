import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the FAQ section and append style="background-color: #F6F7EA !important;"
    pattern = re.compile(r'(<section[^>]*id="marragafay-faq"[^>]*)>', re.IGNORECASE)
    
    def replacer(match):
        tag = match.group(1)
        # remove old injected style if exists
        tag = tag.replace('style="background-color: #F6F7EA;"', '')
        
        if 'style="' in tag:
            if 'background-color' not in tag:
                return tag.replace('style="', 'style="background-color: #F6F7EA !important; ') + '>'
            return match.group(0) # already has it
        else:
            return tag + ' style="background-color: #F6F7EA !important;">'

    if pattern.search(content):
        new_content = pattern.sub(replacer, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated FAQ background in {filepath}")

for file in os.listdir('.'):
    if file.endswith('.html') and file != 'index_backup_20260127_205923.html':
        process_file(file)

template_path = 'js/TourPageTemplate.js'
if os.path.exists(template_path):
    process_file(template_path)
