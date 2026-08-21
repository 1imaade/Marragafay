import re
import os

files_to_update = {
    'packages/basic.html': [
        {
            'name': 'ELENA M.',
            'initials': 'EM',
            'meta': 'Italy · March 2026 · Discovery Pack',
            'text': '"Incredible value for the experience. The shared transport was right on time, and the quad biking at golden hour was pure adrenaline."'
        },
        {
            'name': 'LUCAS D.',
            'initials': 'LD',
            'meta': 'France · April 2026 · Discovery Pack',
            'text': '"A must-do from Marrakech. The logistics were smooth, the camp was beautiful, and the traditional tea by the pool was incredibly refreshing."'
        },
        {
            'name': 'CHLOE S.',
            'initials': 'CS',
            'meta': 'UK · May 2026 · Discovery Pack',
            'text': '"Exactly what we wanted for a half-day excursion. The camel ride was so peaceful, and watching the sunset over the dunes was unforgettable."'
        }
    ],
    'packages/comfort.html': [
        {
            'name': 'SOFIA R.',
            'initials': 'SR',
            'meta': 'Spain · May 2026 · Signature Pack',
            'text': '"The shared transport was surprisingly comfortable and punctual. The camel ride at sunset was the highlight of our Marrakech trip."'
        },
        {
            'name': 'JAMESON L.',
            'initials': 'JL',
            'meta': 'Canada · Sept 2026 · Signature Pack',
            'text': '"Great balance of adventure and relaxation. The quad session was exhilarating, and the traditional Moroccan dinner exceeded all expectations."'
        },
        {
            'name': 'THOMAS & LISA',
            'initials': 'T&L',
            'meta': 'UK · Oct 2026 · Signature Pack',
            'text': '"Perfect organization from start to finish. The live show during dinner added such a magical atmosphere to our desert evening."'
        }
    ],
    'packages/luxe.html': [
        {
            'name': 'LAETITIA R.',
            'initials': 'LR',
            'meta': 'France · March 2026 · Luxury Private',
            'text': '"Private SUV transfer was seamless. The exclusive dinner setting overlooking the Atlas mountains was breathtaking. True luxury in the desert."'
        },
        {
            'name': 'MATTHEW B.',
            'initials': 'MB',
            'meta': 'UK · April 2026 · Luxury Private',
            'text': '"The level of privacy and service was exceptional. Our guide was incredibly knowledgeable and the private quad session felt totally exclusive."'
        },
        {
            'name': 'INA B.',
            'initials': 'IB',
            'meta': 'Germany · May 2026 · Luxury Private',
            'text': '"From the chilled champagne on arrival to the meticulously arranged private tent, every detail of this luxury package was flawlessly executed."'
        }
    ]
}

def create_review_html(review, index):
    classes = "md:pr-8 lg:pr-12" if index == 0 else ("md:px-8 lg:px-12 editorial-divider" if index == 1 else "md:pl-8 lg:pl-12 editorial-divider")
    
    stars = '''<svg width="14" height="14" viewBox="0 0 24 24" fill="#523225" stroke="#523225" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>''' * 5
    
    return f'''      <!-- Review {index+1} -->
      <div class="{classes} flex flex-col">
        <div class="flex gap-1 mb-5">
          {stars}
        </div>
        <p class="text-[#10100E] text-[16px] md:text-[17px] leading-[26px] md:leading-[28px] font-normal italic tracking-tight mb-6">{review['text']}</p>
        <div class="mt-auto pt-2 flex items-center gap-3">
          <div class="w-10 h-10 rounded-full bg-[#10100E] flex items-center justify-center flex-shrink-0">
            <span class="text-white text-[13px] font-semibold tracking-wider">{review['initials']}</span>
          </div>
          <div>
            <p class="text-[#523225] text-[14px] font-semibold uppercase tracking-wide leading-tight">{review['name']}</p>
            <p class="text-[#5c5c56] text-[12px] leading-tight">{review['meta']}</p>
          </div>
        </div>
      </div>'''

for filepath, reviews in files_to_update.items():
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the entire block from the grid open to the end of the script
    pattern = r'(<div class="grid grid-cols-1 md:grid-cols-3 gap-y-12">).*?(<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s*const loadMoreBtn.*?</script>)'
    
    grid_html = '<div class="grid grid-cols-1 md:grid-cols-3 gap-y-12">\n'
    for i, review in enumerate(reviews):
        grid_html += create_review_html(review, i) + '\n'
    grid_html += '    </div>'

    # Use re.sub to replace the block
    new_content = re.sub(pattern, grid_html, content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Patched reviews in {filepath}")

