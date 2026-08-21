import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the <style> block and the accompanying <section> block
    pattern = re.compile(r'<style>\s*\.bento-cta-bg.*?</style>\s*<section class="w-full bento-cta-bg.*?</section>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub('', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed PreFooterCTA section from {filepath}")
    else:
        # Check if the section exists without the style block
        pattern2 = re.compile(r'<section class="w-full bento-cta-bg.*?</section>', re.DOTALL)
        if pattern2.search(content):
            new_content = pattern2.sub('', content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed PreFooterCTA section from {filepath} (without style block)")

for file in os.listdir('.'):
    if file.endswith('.html') and file != 'index_backup_20260127_205923.html':
        process_file(file)

template_path = 'js/TourPageTemplate.js'
if os.path.exists(template_path):
    process_file(template_path)
