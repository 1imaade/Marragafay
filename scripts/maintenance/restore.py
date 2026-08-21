file_path = "packages/basic.html"
with open(file_path, "r") as f:
    new_content = f.read()

# We know:
# orig[:45567] is new_content[:45567]
# orig[352:68600] starts at index 45567 in new_content
# orig[68600:] is at the end of new_content, after 3 newlines inserted between 68600 and the rest.

len_part_middle = 68600 - 352
part1 = new_content[:45567]
part2 = new_content[45567 : 45567 + len_part_middle]

# Let's verify part2 matches the overlapping part of part1
if part1[352:45567] == part2[:45567 - 352]:
    print("Overlap verified! We can reconstruct.")
else:
    print("Overlap does NOT match. Something is wrong.")

rest = new_content[45567 + len_part_middle:]
# rest should start with \n\n\n
if rest.startswith("\n\n\n"):
    part3 = rest[3:]
else:
    print("Rest does not start with newlines as expected. Trying to find part3.")
    # actually my script did: new_content = part1 + part3 + part4 + "\n\n" + part2 + "\n" + part5
    # Wait:
    # part1 = orig[:faq_start_idx]
    # part3 = orig[faq_end_idx:reviews_start_idx]
    # part4 = orig[reviews_start_idx:reviews_end_idx]
    # part2 = ""
    # part5 = orig[reviews_end_idx:]
    # new_content = orig[:45567] + orig[352:54872] + orig[54872:68600] + "\n\n" + "" + "\n" + orig[68600:]
    # new_content = orig[:45567] + orig[352:68600] + "\n\n\n" + orig[68600:]
    part3 = rest.lstrip('\n') # just strip the newlines

orig_reconstructed = part1[:352] + part2 + part3

with open("packages/basic_restored.html", "w") as f:
    f.write(orig_reconstructed)

print("Restored file written to basic_restored.html")
