import os
import glob
import re

files = glob.glob('packages/*.html') + glob.glob('activities/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Compress Section Y-Padding
    # Replace `<section class="w-full py-24 bg-[#F6F7EA] px-5 md:px-10 lg:px-16 flex flex-col items-center">`
    # specifically for the itinerary (it's the first section with this exact class after the hero in most files, 
    # but to be safe we can use a regex that looks for the itinerary comment)
    
    # We'll use regex to target the section right after "Brand-Aligned Itinerary" or similar
    pattern1 = r'(<!--.*?Itinerary.*?-->\s*<section class="[^"]*?)py-24([^"]*")'
    content = re.sub(pattern1, r'\1py-10 md:py-16\2', content, flags=re.IGNORECASE)

    # 2. Compress Timeline Gaps
    # The timeline container
    old_track = '<div class="relative border-l border-[#e2e0d3] ml-2">'
    new_track = '<div class="relative border-l border-[#e2e0d3] ml-2 flex flex-col gap-6 md:gap-10">'
    content = content.replace(old_track, new_track)

    # Remove mb-8 from steps (since we now use flex gap)
    content = content.replace('<div class="mb-8 relative pl-8">', '<div class="relative pl-8">')

    # Also compress the main grid gap between left/right columns on mobile
    old_grid = '<div class="w-full max-w-[1300px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-20 relative">'
    new_grid = '<div class="w-full max-w-[1300px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-6 md:gap-10 lg:gap-20 relative">'
    content = content.replace(old_grid, new_grid)

    # 3. Compress internal text spacing (h3 mb-2 -> mb-1 md:mb-2)
    # The h3 elements
    pattern_h3 = r'(<h3 class="[^"]*?)mb-2([^"]*")'
    content = re.sub(pattern_h3, r'\1mb-1 md:mb-2\2', content)

    # Note: the h3 pattern might hit the right column h3 as well:
    # `<h3 class="... mb-6 border-b ...">pack specifications</h3>` but this has mb-6, so it's safe.

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Processed {len(files)} files.")
