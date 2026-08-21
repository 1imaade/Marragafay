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

    # 1. Update the style block
    old_style = """  <style>
    @media (max-width: 767px) {
      .is-active .itinerary-dot { transform: scale(1.35) !important; }
      .is-active .itinerary-step { font-size: 20px !important; }
      .is-active .itinerary-title { font-size: 13px !important; }
    }
  </style>"""
    new_style = """  <style>
    @media (max-width: 767px) {
      .is-active .itinerary-dot { transform: scale(1.25) !important; }
      .is-active .itinerary-header { transform: scale(1.03) !important; }
    }
  </style>"""
    if old_style in content:
        content = content.replace(old_style, new_style)
    else:
        # Fallback if whitespace differs
        content = re.sub(r'<style>\s*@media \(max-width: 767px\) \{\s*\.is-active \.itinerary-dot \{ transform: scale\(1\.35\) !important; \}\s*\.is-active \.itinerary-step \{ font-size: 20px !important; \}\s*\.is-active \.itinerary-title \{ font-size: 13px !important; \}\s*\}\s*</style>', new_style, content)

    # 2. Add transition physics to the itinerary-header wrapper
    # `<div class="flex flex-row items-baseline gap-2 md:block w-full itinerary-header cursor-pointer md:cursor-auto">`
    content = content.replace(
        'w-full itinerary-header cursor-pointer md:cursor-auto">',
        'w-full itinerary-header cursor-pointer md:cursor-auto transition-transform duration-300 ease-in-out origin-left">'
    )

    # 3. Strip the individual transitions from the step and title elements
    content = content.replace('itinerary-step transition-all duration-300 ease-in-out origin-left ', 'itinerary-step ')
    content = content.replace('itinerary-title transition-all duration-300 ease-in-out origin-left ', 'itinerary-title ')

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Patched thrashing in {filepath}")

for f in html_files:
    process_file(f)
