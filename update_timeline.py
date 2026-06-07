import re

with open('packages/basic.html', 'r') as f:
    content = f.read()

# 1. Update the parent container
# From: <div class="relative border-l border-[#e2e0d3] ml-2 flex flex-col gap-6 md:gap-10">
# To: <div class="w-full flex flex-col">
content = content.replace('<div class="relative border-l border-[#e2e0d3] ml-2 flex flex-col gap-6 md:gap-10">', '<div class="w-full flex flex-col">')

# 2. Update each step
# Old child: <div class="relative pl-3 md:pl-6">\n            <span class="absolute top-2 -left-[5px] w-2.5 h-2.5 rounded-full bg-[#523225] transform translate-y-[2px] md:translate-y-[3px]"></span>
#            (everything else until the next step or end)
# We can use regex to wrap the content

pattern = r'<div class="relative pl-3 md:pl-6">\s*<span class="absolute top-2 -left-\[5px\] w-2\.5 h-2\.5 rounded-full bg-\[#523225\] transform translate-y-\[2px\] md:translate-y-\[3px\]"></span>'

def replacer(m):
    # Instead of just replacing, we need to inject the flex row and left/right columns
    # We will close the right content and the row wrapper at the end of the step. 
    # But regex won't easily find the end of the step.
    
    return '''<div class="relative flex flex-row items-stretch pb-6 md:pb-10 group">
            <!-- left axis -->
            <div class="relative w-4 md:w-6 flex flex-col items-center flex-shrink-0">
               <span class="relative z-10 w-2.5 h-2.5 rounded-full bg-[#523225] flex-shrink-0 mt-[10px] md:mt-[11px]"></span>
               <div class="absolute top-[20px] md:top-[21px] bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-[#523225] group-last:hidden timeline-line"></div>
            </div>
            <!-- right content -->
            <div class="flex-1 pl-3 md:pl-4">'''

content = re.sub(pattern, replacer, content)

# 3. Now we need to close the two extra divs we opened. The old step only had one </div>.
# We replaced `<div class="relative pl-3 md:pl-6">` (1 opening) with `<div class="relative flex..."> ... <div class="flex-1...">` (2 openings, not counting the closed left axis).
# So we need to find the closing `</div>` of each step and replace it with `</div>\n          </div>`.
# Wait, finding the exact closing div is tricky. The next step starts with `<div class="relative flex flex-row`.
# We can just split the content by `<div class="relative flex flex-row items-stretch` and add an extra `</div>` to the end of each block (except the first one, which is the stuff before the first step).

blocks = content.split('<div class="relative flex flex-row items-stretch pb-6 md:pb-10 group">')
for i in range(1, len(blocks)):
    # The last </div> before the next block or the end of the timeline
    # We can look for the closing div that corresponds to the old `<div class="relative pl-3 md:pl-6">`
    # The old structure:
    # </div>
    # </div> (closing of parent) or <div class="relative pl-3...">
    # Actually, the old string `</div><div class="relative pl-3 md:pl-6">` would now look like `</div>` and then immediately the next block!
    pass
