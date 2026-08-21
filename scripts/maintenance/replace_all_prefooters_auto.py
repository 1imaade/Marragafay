import os
import re

html_to_insert = """  <section class="w-full bg-[#F6F7EA] py-32 border-t border-[#d1cfc0] overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center flex flex-col items-center justify-center">
      <h2 class="text-[56px] md:text-[10vw] font-bold text-[#10100E] leading-[0.9] tracking-tighter uppercase mb-10">
        Experience<br/>The Extreme.
      </h2>
      <a href="#booking" class="inline-block px-10 py-5 bg-[#FF5A36] text-[#10100E] text-[13px] md:text-[15px] font-bold uppercase tracking-widest hover:bg-[#10100E] hover:text-[#F6F7EA] transition-colors duration-300">
        Secure Your Expedition
      </a>
    </div>
  </section>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the entire pro-slogan-section section
    section_pattern = re.compile(r'<section\s+class="pro-slogan-section"[^>]*>.*?</section>', re.DOTALL)
    
    if section_pattern.search(content):
        # Replace the section
        new_content = section_pattern.sub(html_to_insert, content)
        
        # Remove typed.js script tag
        new_content = re.sub(r'<script src="https://unpkg.com/typed\.js[^>]*></script>\s*', '', new_content)
        
        # Remove the DOMContentLoaded typed initialization block
        typed_init_pattern = re.compile(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\',\s*function\s*\(\)\s*\{\s*//\s*Target the new ID\s*var sloganElement = document\.getElementById\(\'typed-slogan-v2\'\);.*?</script>\s*', re.DOTALL)
        new_content = typed_init_pattern.sub('', new_content)
        
        # Just in case the format is slightly different
        typed_init_pattern_2 = re.compile(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\',\s*function\s*\(\)\s*\{[^}]*typed-slogan-v2.*?</script>\s*', re.DOTALL)
        new_content = typed_init_pattern_2.sub('', new_content)

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
    section_pattern = re.compile(r'<section\s+class="pro-slogan-section"[^>]*>.*?</section>', re.DOTALL)
    if section_pattern.search(content):
        # in JS, we need to handle formatting if it's a template literal
        js_insert = "`\n" + html_to_insert + "\n`" 
        # wait, if it's already inside a template literal, we just insert the HTML
        new_content = section_pattern.sub(html_to_insert, content)
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {template_path}")
