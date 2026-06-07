import os
import re

html_to_insert = """  <section class="w-full bg-[#F6F7EA] py-24 md:py-32 border-t border-[#d1cfc0] overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center flex flex-col items-center justify-center">
      <h2 class="text-[64px] md:text-[9vw] font-bold text-[#10100E] tracking-tighter uppercase mb-12 flex flex-col" style="line-height: 0.85;">
        <span>Experience</span>
        <span>The Extreme.</span>
      </h2>
      <a href="#booking" class="inline-flex items-center justify-center px-12 py-5 bg-[#FF5A36] text-[#10100E] text-[13px] md:text-[14px] font-bold uppercase tracking-[0.2em] hover:bg-[#10100E] hover:text-[#F6F7EA] transition-colors duration-300 w-full sm:w-auto">
        Secure Your Expedition
      </a>
    </div>
  </section>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the previously inserted section
    # We look for <section class="w-full bg-[#F6F7EA] ... Secure Your Expedition ... </section>
    section_pattern = re.compile(r'<section class="w-full bg-\[#F6F7EA\].*?Secure Your Expedition\s*</a>\s*</div>\s*</section>', re.DOTALL)
    
    if section_pattern.search(content):
        # Replace the section
        new_content = section_pattern.sub(html_to_insert, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        pass

for file in os.listdir('.'):
    if file.endswith('.html') and file != 'index_backup_20260127_205923.html':
        process_file(file)

# Also update the TourPageTemplate.js
template_path = 'js/TourPageTemplate.js'
if os.path.exists(template_path):
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    section_pattern = re.compile(r'<section class="w-full bg-\[#F6F7EA\].*?Secure Your Expedition\s*</a>\s*</div>\s*</section>', re.DOTALL)
    if section_pattern.search(content):
        new_content = section_pattern.sub(html_to_insert, content)
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {template_path}")
