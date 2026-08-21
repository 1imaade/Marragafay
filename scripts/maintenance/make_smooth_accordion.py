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

    # 1. Strip the static hidden classes and wrap in the physics div
    pattern_p = r'<p class="([^"]*) hidden md:block itinerary-content">(.*?)</p>'
    def p_replacer(m):
        p_classes = m.group(1)
        p_text = m.group(2)
        wrapper = f'<div class="grid transition-all duration-300 ease-in-out md:!grid-rows-[1fr] md:!opacity-100 grid-rows-[0fr] opacity-0 itinerary-content">\n              <div class="overflow-hidden">\n                <p class="{p_classes}">{p_text}</p>\n              </div>\n            </div>'
        return wrapper
        
    new_content = re.sub(pattern_p, p_replacer, content)

    # 2. Replace the old script with the new exclusive logic
    old_script_pattern = r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) {\s*const headers = document\.querySelectorAll\(\'\.itinerary-header\'\);.*?\}\s*\);\s*</script>'

    new_script = """<script>
  document.addEventListener('DOMContentLoaded', function() {
    const headers = document.querySelectorAll('.itinerary-header');
    
    headers.forEach((header) => {
      header.addEventListener('click', function() {
        if (window.innerWidth >= 768) return;
        
        const clickedContent = this.nextElementSibling;
        const clickedChevron = this.querySelector('.chevron-icon');
        
        const isCurrentlyOpen = clickedContent.classList.contains('grid-rows-[1fr]');
        
        // Force close all
        headers.forEach((otherHeader) => {
          const otherContent = otherHeader.nextElementSibling;
          const otherChevron = otherHeader.querySelector('.chevron-icon');
          
          if (otherContent && otherContent.classList.contains('itinerary-content')) {
            otherContent.classList.remove('grid-rows-[1fr]', 'opacity-100');
            otherContent.classList.add('grid-rows-[0fr]', 'opacity-0');
          }
          if (otherChevron) {
            otherChevron.classList.remove('rotate-180');
          }
        });
        
        // Toggle the clicked one
        if (!isCurrentlyOpen) {
          if (clickedContent && clickedContent.classList.contains('itinerary-content')) {
            clickedContent.classList.remove('grid-rows-[0fr]', 'opacity-0');
            clickedContent.classList.add('grid-rows-[1fr]', 'opacity-100');
          }
          if (clickedChevron) {
            clickedChevron.classList.add('rotate-180');
          }
        }
      });
    });

    // Programmatically open STEP 1
    const firstStep = document.querySelector('.itinerary-header');
    if (firstStep) {
      const firstContent = firstStep.nextElementSibling;
      const firstChevron = firstStep.querySelector('.chevron-icon');
      if (firstContent && firstContent.classList.contains('itinerary-content')) {
        firstContent.classList.remove('grid-rows-[0fr]', 'opacity-0');
        firstContent.classList.add('grid-rows-[1fr]', 'opacity-100');
      }
      if (firstChevron) {
        firstChevron.classList.add('rotate-180');
      }
    }
  });
</script>"""

    new_content = re.sub(old_script_pattern, new_script.replace('\\', '\\\\'), new_content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Patched {filepath}")

for f in html_files:
    process_file(f)
