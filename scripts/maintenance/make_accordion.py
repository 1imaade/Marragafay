import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html') and ('packages' in root or 'activities' in root):
            html_files.append(os.path.join(root, file))

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    pattern = r'(<div class="flex flex-row items-baseline gap-2 md:block">)\s*(<div class="text-\[18px\] font-semibold text-\[#523225\] tracking-tight capitalize mb-0 md:mb-1">STEP \d+</div>)\s*<h3 class="([^"]*)">([^<]*)</h3>\s*</div>\s*<p class="([^"]*)">'

    def replacer(m):
        wrapper_open = m.group(1).replace('md:block', 'md:block w-full itinerary-header cursor-pointer md:cursor-auto')
        step_div = m.group(2)
        h3_classes = m.group(3)
        h3_text = m.group(4)
        p_classes = m.group(5)
        
        if 'flex-1' not in h3_classes:
            h3_classes = h3_classes.replace('mb-1 md:mb-2', 'mb-1 md:mb-2 flex-1 flex justify-between items-center md:block')
            
        chevron = '<svg class="w-4 h-4 text-[#523225] inline-block md:hidden ml-auto transition-transform duration-300 chevron-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>'
        
        if 'itinerary-content' not in p_classes:
            new_p_classes = p_classes + ' hidden md:block itinerary-content'
        else:
            new_p_classes = p_classes
            
        return f'{wrapper_open}\n              {step_div}\n              <h3 class="{h3_classes}">{h3_text}{chevron}</h3>\n            </div>\n            <p class="{new_p_classes}">'
        
    script = """
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const headers = document.querySelectorAll('.itinerary-header');
    headers.forEach((header) => {
      header.addEventListener('click', function() {
        if (window.innerWidth >= 768) return;
        const content = this.nextElementSibling;
        const chevron = this.querySelector('.chevron-icon');
        if (content && content.classList.contains('itinerary-content')) {
          content.classList.toggle('hidden');
          if (chevron) {
            chevron.classList.toggle('rotate-180');
          }
        }
      });
    });
    const firstStep = document.querySelector('.itinerary-header');
    if (firstStep) {
      const firstContent = firstStep.nextElementSibling;
      const firstChevron = firstStep.querySelector('.chevron-icon');
      if (firstContent && firstContent.classList.contains('itinerary-content')) {
        firstContent.classList.remove('hidden');
        if (firstChevron) {
          firstChevron.classList.add('rotate-180');
        }
      }
    }
  });
</script>
"""

    if 'itinerary-header' not in content:
        content = re.sub(pattern, replacer, content)
        if '<script src="../js/dynamic-pricing.js"></script>' in content:
            content = content.replace('<script src="../js/dynamic-pricing.js"></script>', script + '\n  <script src="../js/dynamic-pricing.js"></script>')
        else:
            content = content.replace('</body>', script + '\n</body>')
        
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Patched {filepath}")

for f in html_files:
    process_file(f)
