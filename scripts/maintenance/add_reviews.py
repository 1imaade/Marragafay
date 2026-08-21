import re

html_template = """
      <!-- Review {idx} (Hidden initially) -->
      <div class="{col_class} review-item hidden opacity-0 transition-opacity duration-700 ease-in-out flex flex-col">
        <div class="flex gap-1 mb-5">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#523225" stroke="#523225" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" /></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#523225" stroke="#523225" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" /></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#523225" stroke="#523225" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" /></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#523225" stroke="#523225" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" /></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#523225" stroke="#523225" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" /></svg>
        </div>
        <p class="text-[#10100E] text-[16px] md:text-[17px] leading-[26px] md:leading-[28px] font-normal italic tracking-tight mb-6">"{text}"</p>
        <div class="mt-auto pt-2">
          <p class="text-[#523225] text-[14px] font-semibold uppercase tracking-wide">{name}</p>
          <p class="text-[#5c5c56] text-[12px] mt-1">{location}</p>
        </div>
      </div>"""

reviews = [
    ("The most majestic experience of our trip to Morocco. The quad bikes were top-notch and the sunset was unreal.", "DAVID & EMMA", "Australia · Jan 2026 · Discovery Pack"),
    ("A flawless operation. From the private transfer to the exquisite dining, Marragafay exceeded all expectations.", "JONATHAN W.", "USA · Feb 2026 · Luxury Private"),
    ("Breathtaking views and incredible hospitality. Our guide made sure we felt safe and showed us the best spots.", "MARIA S.", "Spain · Mar 2026 · Signature Pack"),
    ("Nothing compares to eating a tagine under a blanket of stars in the Agafay. Worth every penny.", "LUKE & SARAH", "UK · Apr 2026 · Discovery Pack"),
    ("We booked the private pack for our anniversary. The romantic setup and the sunset ride were perfect.", "ANNA P.", "Germany · May 2026 · Luxury Private"),
    ("Superb! The equipment is brand new and the guides are so friendly. Highly recommended for thrill seekers.", "CARLOS M.", "Mexico · Jun 2026 · Signature Pack"),
    ("I was a bit nervous as a first-time rider, but the staff was so reassuring. Had the time of my life!", "JULIA T.", "Canada · Jul 2026 · Discovery Pack"),
    ("A magical escape from the bustling city of Marrakech. The contrast of the desert is stunning.", "AHMED R.", "UAE · Aug 2026 · Signature Pack"),
    ("We’ve done desert tours before, but the level of luxury here is unmatched. It truly is 'Quiet Luxury'.", "SOPHIE & JAMES", "France · Sep 2026 · Luxury Private"),
    ("Incredible from start to finish. The dinner was one of the best meals we had during our entire trip.", "LIAM H.", "Ireland · Oct 2026 · Discovery Pack"),
    ("A must-do experience. The sunset casting shadows over the dunes is a sight I will never forget.", "CHLOE B.", "Australia · Nov 2026 · Signature Pack"),
    ("Everything was meticulously planned. We just had to show up and enjoy the ride. Five stars!", "DANIEL & CLAIRE", "USA · Dec 2026 · Luxury Private"),
    ("The quad biking was thrilling, but the serene dinner that followed was the true highlight.", "NINA K.", "Sweden · Jan 2027 · Discovery Pack"),
    ("Professional, safe, and wildly fun. Marragafay is the only company you should book with in the desert.", "OLIVER F.", "UK · Feb 2027 · Signature Pack"),
    ("A sensory delight! The roar of the engines followed by the silence of the desert night. Perfect.", "ISABELLA G.", "Italy · Mar 2027 · Luxury Private")
]

generated_html = ""
for i, (text, name, location) in enumerate(reviews):
    idx = 7 + i
    col_index = idx % 3
    if col_index == 1:
        col_class = "md:pr-8 lg:pr-12"
    elif col_index == 2:
        col_class = "md:px-8 lg:px-12 editorial-divider"
    else:
        col_class = "md:pl-8 lg:pl-12 editorial-divider"
        
    generated_html += html_template.format(idx=idx, col_class=col_class, text=text, name=name, location=location)

file_path = "packages/basic.html"
with open(file_path, "r") as f:
    content = f.read()

# Find the end of the grid (line before <!-- Load More Button -->)
# Look for:
#       </div>
# 
#     </div>
#     
#     <!-- Load More Button -->
import re
pattern = r'(      </div>\n\n    </div>\n    \n    <!-- Load More Button -->)'
new_content = re.sub(pattern, lambda m: generated_html + "\n" + m.group(1), content)

with open(file_path, "w") as f:
    f.write(new_content)

print("Added 15 reviews successfully!")
