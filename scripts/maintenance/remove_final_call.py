import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the span containing "Final Call" within the bento-cta-cell
    # We match from <span class="bento-cta-tag ... to </span>
    pattern = re.compile(r'<span class="bento-cta-tag font-semibold uppercase block mb-6" style="letter-spacing: 0\.1em;">\s*Final Call\s*</span>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub('', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed 'Final Call' from {filepath}")

for file in os.listdir('.'):
    if file.endswith('.html') and file != 'index_backup_20260127_205923.html':
        process_file(file)

template_path = 'js/TourPageTemplate.js'
if os.path.exists(template_path):
    process_file(template_path)
