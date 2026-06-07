file_path = "packages/basic.html"
with open(file_path, "r") as f:
    lines = f.readlines()

# FAQ: lines 1128 to 1294 (0-indexed: 1128 to 1294, Wait: line 1129 is index 1128)
faq_start = 1128
faq_end = 1294

# Reviews: lines 1295 to 1449 (0-indexed: 1295 to 1449)
reviews_start = 1295
reviews_end = 1449

part1 = lines[:faq_start]
faq_section = lines[faq_start:faq_end]
middle = lines[faq_end:reviews_start] # Should be an empty line at 1294
reviews_section = lines[reviews_start:reviews_end]
part5 = lines[reviews_end:]

new_lines = part1 + reviews_section + middle + faq_section + part5

with open(file_path, "w") as f:
    f.writelines(new_lines)

print("Swapped by lines!")
