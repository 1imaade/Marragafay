import os
import re

css_block = """
  <style>
    .bento-cta-bg { background-color: #10100E !important; }
    .bento-cta-cell { background-color: #10100E !important; border-color: #2a2a26 !important; }
    .bento-cta-cell-dark { background-color: #151513 !important; border-color: #2a2a26 !important; }
    .bento-cta-grid { border-color: #2a2a26 !important; }
    .bento-cta-title { font-size: 56px !important; color: #F6F7EA !important; }
    @media (min-width: 768px) { .bento-cta-title { font-size: 8vw !important; } }
    .bento-cta-tag { color: #FF5A36 !important; font-size: 11px !important; letter-spacing: 0.1em !important; }
    .bento-cta-desc { color: #a3a39a !important; font-size: 14px !important; line-height: 24px !important; }
    .bento-cta-btn { background-color: #FF5A36 !important; color: #10100E !important; font-size: 13px !important; letter-spacing: 0.15em !important; }
    .bento-cta-btn:hover { background-color: #F6F7EA !important; color: #10100E !important; }
  </style>
  <section class="w-full bento-cta-bg pt-24 pb-0 overflow-hidden">
    <div class="max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-12 border-t-[1px] border-l-[1px] border-solid bento-cta-grid w-full">
        
        <div class="md:col-span-8 border-b-[1px] border-r-[1px] border-solid bento-cta-cell p-8 md:p-16 flex flex-col justify-center">
          <span class="bento-cta-tag font-semibold uppercase block mb-6" style="letter-spacing: 0.1em;">
            Final Call
          </span>
          <h2 class="bento-cta-title font-bold tracking-tighter uppercase flex flex-col" style="line-height: 0.85;">
            <span>Experience</span>
            <span>The Extreme.</span>
          </h2>
        </div>

        <div class="md:col-span-4 border-b-[1px] border-r-[1px] border-solid bento-cta-cell-dark p-8 md:p-12 flex flex-col justify-between">
          <p class="bento-cta-desc mb-12">
            Expeditions are strictly limited to ensure uncompromising quality and exclusivity. Secure your fleet today.
          </p>
          <a href="#booking" class="w-full flex items-center justify-between px-6 py-5 bento-cta-btn font-bold uppercase transition-colors duration-300">
            <span>Secure Expedition</span>
            <span class="text-[18px] leading-none">&#8594;</span>
          </a>
        </div>

      </div>
    </div>
  </section>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Search for the previously injected style + section
    # <style>...</style>\s*<section class="w-full brutal-cta-bg ... </section>
    pattern = re.compile(r'<style>\s*\.brutal-cta-bg.*?</section>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(css_block, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Replaced with Bento CTA in {filepath}")
    else:
        # Just in case, try searching for the brutal-cta-bg section alone without the style tag
        pattern2 = re.compile(r'<section class="w-full brutal-cta-bg.*?</section>', re.DOTALL)
        if pattern2.search(content):
            new_content = pattern2.sub(css_block, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Replaced with Bento CTA in {filepath} (section only)")


for file in os.listdir('.'):
    if file.endswith('.html') and file != 'index_backup_20260127_205923.html':
        process_file(file)

template_path = 'js/TourPageTemplate.js'
if os.path.exists(template_path):
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'<style>\s*\.brutal-cta-bg.*?</section>', re.DOTALL)
    if pattern.search(content):
        new_content = pattern.sub(css_block, content)
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Replaced with Bento CTA in {template_path}")
