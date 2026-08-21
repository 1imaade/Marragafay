import os
import glob
import re

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Modify the bottom disclaimer to hide on xl:
    old_bottom = '<div class="w-full flex justify-start">\n            <p class="text-[12px] text-[#10100E]/50 font-medium text-left tracking-tight mt-2 mb-0">No upfront payment required. You will pay at the end of the experience.</p>\n          </div>'
    new_bottom = '<div class="w-full flex justify-start xl:hidden">\n            <p class="text-[12px] text-[#10100E]/50 font-medium text-left tracking-tight mt-2 mb-0">No upfront payment required. You will pay at the end of the experience.</p>\n          </div>'
    content = content.replace(old_bottom, new_bottom)

    # 2. Add the disclaimer above the form pill.
    # The form pill starts with: <!-- RIGHT: The Expanded Input Pill (4 Fields) -->
    # We will replace that comment and the following div start with a wrapper.
    # We need to find the exact line. It's safe to just replace the comment.
    
    old_right = '<!-- RIGHT: The Expanded Input Pill (4 Fields) -->\n          <div class="flex flex-col xl:flex-row items-stretch'
    new_right = '<!-- RIGHT: Form Wrapper -->\n          <div class="flex flex-col w-full 2xl:w-auto">\n            <div class="hidden xl:block text-left mb-2 pl-2">\n              <p class="text-[12px] text-[#10100E]/50 font-medium tracking-tight mb-0">No upfront payment required. You will pay at the end of the experience.</p>\n            </div>\n            <!-- RIGHT: The Expanded Input Pill (4 Fields) -->\n            <div class="flex flex-col xl:flex-row items-stretch'
    
    # We also need to close the wrapper div after the form pill closes.
    # The form pill closes right before the bottom disclaimer.
    # Let's find the closing tag of the pill.
    # The pill closes exactly 2 lines above the bottom disclaimer.
    
    # Let's do it with a regex or simple string replacement.
    # Actually, we can just replace `</button>\n\n          </div>\n\n          </div>\n          \n          <div class="w-full flex justify-start xl:hidden">`
    # Wait, in the HTML, there are two closing divs before the bottom disclaimer.
    # Lines:
    # 928:             </button>
    # 929: 
    # 930:           </div>
    # 931: 
    # 932:           </div>
    # 933:           
    # 934:           <div class="w-full flex justify-start xl:hidden">
    # The first `</div>` closes the flex row of inputs.
    # The second `</div>` closes the `w-full flex flex-col 2xl:flex-row ...` wrapper!
    # Wait, if we added a wrapper `<div class="flex flex-col w-full 2xl:w-auto">`, we must close it BEFORE the `flex flex-col 2xl:flex-row` closes!
    # So we should insert `</div>` between line 930 and 932.
    
    # Let's do this:
    old_close = '            </button>\n\n          </div>\n\n          </div>'
    new_close = '            </button>\n\n          </div>\n          </div><!-- Close Form Wrapper -->\n\n          </div>'
    
    content = content.replace(old_right, new_right)
    content = content.replace(old_close, new_close)

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
