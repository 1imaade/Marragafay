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

    # 1. Add classes to Dot
    content = content.replace(
        '<span class="relative z-10 w-2.5 h-2.5 rounded-full bg-[#523225] flex-shrink-0"></span>',
        '<span class="itinerary-dot relative z-10 w-2.5 h-2.5 rounded-full bg-[#523225] flex-shrink-0 transition-all duration-300 ease-in-out origin-center"></span>'
    )

    # 2. Add classes to Step Label
    pattern_step = r'(<div class=")(text-\[18px\] font-semibold text-\[#523225\] tracking-tight capitalize mb-0 md:mb-1)(">STEP \d+</div>)'
    content = re.sub(pattern_step, r'\g<1>itinerary-step transition-all duration-300 ease-in-out origin-left \g<2>\g<3>', content)

    # 3. Add classes to Activity Title
    pattern_title = r'(<h3 class=")(text-\[12px\] font-semibold text-\[#10100E\] tracking-widest uppercase mb-1 md:mb-2 flex-1 flex justify-between items-center md:block)(">)'
    content = re.sub(pattern_title, r'\g<1>itinerary-title transition-all duration-300 ease-in-out origin-left \g<2>\g<3>', content)

    # 4. Inject CSS Style Block before </head>
    style_block = """
  <style>
    @media (max-width: 767px) {
      .is-active .itinerary-dot { transform: scale(1.35) !important; }
      .is-active .itinerary-step { font-size: 20px !important; }
      .is-active .itinerary-title { font-size: 13px !important; }
    }
  </style>
</head>"""
    if '.is-active .itinerary-dot' not in content:
        content = content.replace('</head>', style_block)

    # 5. Update the Vanilla JS
    old_script_pattern = r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) {\s*const headers = document\.querySelectorAll\(\'\.itinerary-header\'\);.*?\}\s*\);\s*</script>'

    new_script = """<script>
  document.addEventListener('DOMContentLoaded', function() {
    const headers = document.querySelectorAll('.itinerary-header');
    
    headers.forEach((header) => {
      header.addEventListener('click', function() {
        if (window.innerWidth >= 768) return;
        
        const clickedContent = this.nextElementSibling;
        const clickedChevron = this.querySelector('.chevron-icon');
        const stepWrapper = this.closest('.group');
        
        const isCurrentlyOpen = clickedContent.classList.contains('grid-rows-[1fr]');
        
        // Force close all
        headers.forEach((otherHeader) => {
          const otherContent = otherHeader.nextElementSibling;
          const otherChevron = otherHeader.querySelector('.chevron-icon');
          const otherWrapper = otherHeader.closest('.group');
          
          if (otherContent && otherContent.classList.contains('itinerary-content')) {
            otherContent.classList.remove('grid-rows-[1fr]', 'opacity-100');
            otherContent.classList.add('grid-rows-[0fr]', 'opacity-0');
          }
          if (otherChevron) {
            otherChevron.classList.remove('rotate-180');
          }
          if (otherWrapper) {
            otherWrapper.classList.remove('is-active');
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
          if (stepWrapper) {
            stepWrapper.classList.add('is-active');
          }
        }
      });
    });

    // Programmatically open STEP 1
    const firstStep = document.querySelector('.itinerary-header');
    if (firstStep) {
      const firstContent = firstStep.nextElementSibling;
      const firstChevron = firstStep.querySelector('.chevron-icon');
      const firstWrapper = firstStep.closest('.group');
      if (firstContent && firstContent.classList.contains('itinerary-content')) {
        firstContent.classList.remove('grid-rows-[0fr]', 'opacity-0');
        firstContent.classList.add('grid-rows-[1fr]', 'opacity-100');
      }
      if (firstChevron) {
        firstChevron.classList.add('rotate-180');
      }
      if (firstWrapper) {
        firstWrapper.classList.add('is-active');
      }
    }
  });
</script>"""

    content = re.sub(old_script_pattern, new_script.replace('\\', '\\\\'), content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Patched Active State in {filepath}")

for f in html_files:
    process_file(f)
