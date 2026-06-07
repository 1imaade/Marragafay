import re

with open('packages/basic.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_hero = """      <!-- HERO: StayHere-Style Asymmetric Bento Grid -->
      <section class="w-full h-[70vh] min-h-[500px] relative mt-0">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-1 h-full w-full bg-white">
          
          <!-- LEFT COLUMN: 1 Large Image (66%) -->
          <div class="col-span-1 lg:col-span-2 relative h-full w-full overflow-hidden">
            <img src="https://images.unsplash.com/photo-1542401886-65d6c61de007?q=80&w=2000" alt="Main" class="absolute inset-0 w-full h-full object-cover">
            <!-- Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-[#10100E] via-[#10100E]/20 to-transparent z-10 pointer-events-none"></div>
            <!-- Text Wrapper -->
            <div class="absolute inset-0 flex flex-col justify-end p-8 md:p-12 z-20 pointer-events-none">
              <div class="pointer-events-auto">
                <h1 class="text-[40px] md:text-[60px] leading-[1.1] font-semibold text-[#F6F7EA] tracking-tight uppercase mb-4" style="font-family: 'Clash Grotesk', sans-serif;">DISCOVERY PACK.</h1>
                <p class="text-[16px] text-[#F6F7EA]/90 leading-[24px] font-normal mb-6 max-w-2xl" style="font-family: 'Clash Grotesk', sans-serif;">Your first night under the desert stars. Ride camels at golden hour and dine under the sky.</p>
              </div>
            </div>
          </div>

          <!-- RIGHT COLUMN: 2 Stacked Images (33%) -->
          <div class="col-span-1 lg:col-span-1 grid grid-rows-2 gap-1 h-full w-full">
            <!-- Top Right Image -->
            <div class="relative h-full w-full overflow-hidden">
              <img src="https://images.unsplash.com/photo-1682687982501-1e58f8101458?q=80&w=1000" alt="Detail 1" class="absolute inset-0 w-full h-full object-cover">
            </div>
            <!-- Bottom Right Image -->
            <div class="relative h-full w-full overflow-hidden">
              <img src="https://images.unsplash.com/photo-1528605248644-14dd04022da1?q=80&w=1000" alt="Detail 2" class="absolute inset-0 w-full h-full object-cover">
            </div>
          </div>

        </div>
      </section>"""

# Replace the specific hero section
pattern = re.compile(r'      <!-- HERO SECTION -->\s*<section class="relative w-full h-\[75vh\] min-h-\[550px\] flex flex-col justify-end pb-\[100px\]">[\s\S]*?      </section>', re.MULTILINE)
content, count = pattern.subn(new_hero, content)

print(f"Replaced {count} occurrences in basic.html")

with open('packages/basic.html', 'w', encoding='utf-8') as f:
    f.write(content)

