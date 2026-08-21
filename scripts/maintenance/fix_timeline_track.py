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

    # Change parent container
    content = content.replace('<div class="relative border-l border-[#e2e0d3] ml-2 flex flex-col gap-6 md:gap-10">', '<div class="w-full flex flex-col">')

    # Replace end of steps (between steps)
    # Old:
    #               </div>
    #             </div>
    #           </div><div class="relative pl-3 md:pl-6">
    old_between = '              </div>\n            </div>\n          </div><div class="relative pl-3 md:pl-6">'
    new_between = '              </div>\n            </div>\n            </div>\n          </div><div class="relative pl-3 md:pl-6">'
    content = content.replace(old_between, new_between)

    # Replace end of very last step
    # Old:
    #               </div>
    #             </div>
    #           </div></div>
    old_end = '              </div>\n            </div>\n          </div></div>'
    new_end = '              </div>\n            </div>\n            </div>\n          </div></div>'
    content = content.replace(old_end, new_end)

    # Now replace the openings
    pattern_open = r'<div class="relative pl-3 md:pl-6">\s*<span class="absolute top-2 -left-\[5px\] w-2\.5 h-2\.5 rounded-full bg-\[#523225\] transform translate-y-\[2px\] md:translate-y-\[3px\]"></span>'
    
    replacer_open = '''<div class="relative flex flex-row items-stretch pb-6 md:pb-10 group">
            <div class="relative w-4 md:w-6 flex flex-col items-center flex-shrink-0 pt-[6px]">
               <span class="relative z-10 w-2.5 h-2.5 rounded-full bg-[#523225] flex-shrink-0"></span>
               <div class="absolute top-[16px] bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-[#523225] group-last:hidden timeline-line"></div>
            </div>
            <div class="flex-1 pl-3 md:pl-4">'''
            
    content = re.sub(pattern_open, replacer_open, content)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Patched {filepath}")

for f in html_files:
    process_file(f)
