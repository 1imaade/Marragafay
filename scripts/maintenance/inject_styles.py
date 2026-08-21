import os
import re

css_block = """
  <style>
    .brutal-cta-bg { background-color: #F6F7EA !important; border-top-color: #d1cfc0 !important; }
    .brutal-cta-title { font-size: 64px !important; color: #10100E !important; }
    @media (min-width: 768px) { .brutal-cta-title { font-size: 9vw !important; } }
    .brutal-cta-btn { background-color: #FF5A36 !important; color: #10100E !important; font-size: 13px !important; letter-spacing: 0.2em !important; }
    @media (min-width: 768px) { .brutal-cta-btn { font-size: 14px !important; } }
    .brutal-cta-btn:hover { background-color: #10100E !important; color: #F6F7EA !important; }
  </style>
  <section class="w-full brutal-cta-bg py-24 md:py-32 border-t overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center flex flex-col items-center justify-center">
      <h2 class="brutal-cta-title font-bold tracking-tighter uppercase mb-12 flex flex-col" style="line-height: 0.85;">
        <span>Experience</span>
        <span>The Extreme.</span>
      </h2>
      <a href="#booking" class="inline-flex items-center justify-center px-12 py-5 brutal-cta-btn font-bold uppercase transition-colors duration-300 w-full sm:w-auto">
        Secure Your Expedition
      </a>
    </div>
  </section>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the current section we inserted
    # Look for the section with "Secure Your Expedition"
    section_pattern = re.compile(r'<section class="w-full bg-\[#F6F7EA\].*?Secure Your Expedition\s*</a>\s*</div>\s*</section>', re.DOTALL)
    
    if section_pattern.search(content):
        new_content = section_pattern.sub(css_block, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected styles in {filepath}")
    else:
        # Maybe we already injected it? Let's check for brutal-cta-bg
        if "brutal-cta-bg" not in content:
            # Let's search for the old pro-slogan-section just in case
            old_pattern = re.compile(r'<section\s+class="pro-slogan-section"[^>]*>.*?</section>', re.DOTALL)
            if old_pattern.search(content):
                new_content = old_pattern.sub(css_block, content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Injected styles in {filepath} (from old pattern)")

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
        new_content = section_pattern.sub(css_block, content)
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected styles in {template_path}")
