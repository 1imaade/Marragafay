import re

with open("packages/basic.html", "r") as f:
    html = f.read()

# We need to find all occurrences of https://images.unsplash.com/... within the gallery grid
# To do this safely, we will specifically target the src="..." attributes containing unsplash URLs

# Define the 9 local images
local_images = [
    "../images/gallery/gal1.webp",
    "../images/gallery/gal2.webp",
    "../images/gallery/gal3.webp",
    "../images/gallery/gal4.webp",
    "../images/gallery/gal5.webp",
    "../images/gallery/gal6.webp",
    "../images/gallery/gal7.webp",
    "../images/gallery/gal8.webp",
    "../images/gallery/gal9.webp",
]

# Use a replacement function that increments through our list
replacement_index = 0

def replacer(match):
    global replacement_index
    if replacement_index < len(local_images):
        new_src = f'src="{local_images[replacement_index]}"'
        replacement_index += 1
        return new_src
    return match.group(0)

# The pattern looks for src="https://images.unsplash.com/..."
pattern = re.compile(r'src="https://images\.unsplash\.com/[^"]+"')

new_html = pattern.sub(replacer, html)

with open("packages/basic.html", "w") as f:
    f.write(new_html)

print(f"Replaced {replacement_index} images.")
