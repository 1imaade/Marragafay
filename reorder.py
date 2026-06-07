import re

file_path = "packages/basic.html"
with open(file_path, "r") as f:
    content = f.read()

# Define patterns to identify boundaries
faq_start_pattern = r'<section class="w-full py-24 bg-\[\#F6F7EA\] border-t border-\[\#e2e0d3\] px-5 xl:px-20 flex flex-col items-center" id="marragafay-faq"'
faq_end_pattern = r'  </script>\n'
reviews_start_pattern = r'<!-- Reviews Section -->\n<section class="w-full py-24 px-5 xl:px-20" style="background-color: #F6F7EA !important;">'
reviews_end_pattern = r'      \}\);\n    </script>\n    \n  </div>\n</section>\n'

# Find indices
faq_start_match = re.search(faq_start_pattern, content)
faq_end_match = re.search(faq_end_pattern, content)
reviews_start_match = re.search(reviews_start_pattern, content)
reviews_end_match = re.search(reviews_end_pattern, content)

if not (faq_start_match and faq_end_match and reviews_start_match and reviews_end_match):
    print("Could not find all boundaries.")
    print("FAQ start:", bool(faq_start_match))
    print("FAQ end:", bool(faq_end_match))
    print("Reviews start:", bool(reviews_start_match))
    print("Reviews end:", bool(reviews_end_match))
    import sys
    sys.exit(1)

faq_start_idx = faq_start_match.start()
faq_end_idx = faq_end_match.end()
reviews_start_idx = reviews_start_match.start()
reviews_end_idx = reviews_end_match.end()

print(f"FAQ: {faq_start_idx} to {faq_end_idx}")
print(f"Reviews: {reviews_start_idx} to {reviews_end_idx}")

# The file structure is:
# [Part 1: Start to FAQ start]
# [Part 2: FAQ]
# [Part 3: Between FAQ and Reviews]
# [Part 4: Reviews]
# [Part 5: Reviews end to End of file]

part1 = content[:faq_start_idx]
part2 = content[faq_start_idx:faq_end_idx]
part3 = content[faq_end_idx:reviews_start_idx]
part4 = content[reviews_start_idx:reviews_end_idx]
part5 = content[reviews_end_idx:]

# New order: Part 1 + Part 3 + Part 4 + Part 2 + Part 5
# Note: Part 3 is likely just whitespace/newlines
new_content = part1 + part3 + part4 + "\n\n" + part2 + "\n" + part5

with open(file_path, "w") as f:
    f.write(new_content)

print("Sections swapped successfully.")
