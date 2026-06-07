import os
import glob
import re

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Remove the disclaimer from above the form
    # The block is exactly:
    above_block = '''<div class="hidden xl:block text-left mb-2 pl-2">
              <p class="text-[12px] text-[#10100E]/50 font-medium tracking-tight mb-0">No upfront payment required. You will pay at the end of the experience.</p>
            </div>
            <!-- RIGHT: The Expanded Input Pill (4 Fields) -->'''
    
    if above_block in content:
        content = content.replace(above_block, '<!-- RIGHT: The Expanded Input Pill (4 Fields) -->')
        
        # 2. Add the disclaimer below the form pill
        # The form pill closes right before `</div><!-- Close Form Wrapper -->`
        # We'll replace `</div><!-- Close Form Wrapper -->` with the disclaimer + closing div.
        
        old_close = '</div><!-- Close Form Wrapper -->'
        new_close = '''<div class="hidden xl:block text-left mt-2 pl-4">
              <p class="text-[12px] text-[#10100E]/50 font-medium tracking-tight mb-0">No upfront payment required. You will pay at the end of the experience.</p>
            </div>
          </div><!-- Close Form Wrapper -->'''
        
        content = content.replace(old_close, new_close)

        with open(filepath, 'w') as f:
            f.write(content)

print(f"Processed {len(files)} files.")
