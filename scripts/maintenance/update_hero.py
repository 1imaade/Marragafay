import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The new hero HTML to insert
new_hero = """  <!-- Hero Section Redesign: Agdal Collection -->
  <section id="home" class="hero-section relative w-full h-auto lg:h-[100vh] min-h-[600px] overflow-hidden">
    <div class="grid grid-cols-1 lg:grid-cols-12 h-full">
      
      <!-- Left Column: Background Image (60% -> 7 columns out of 12 approx) -->
      <div class="relative lg:col-span-7 h-[50vh] lg:h-full flex flex-col justify-end p-8 lg:p-16">
        <!-- Background Image -->
        <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('images/hero-agdal/luxury_terrace_hero_1780518413098.png');"></div>
        <!-- Dark Overlay -->
        <div class="absolute inset-0 bg-black/40"></div>
        
        <!-- Content -->
        <div class="relative z-10 max-w-2xl">
          <h1 class="text-4xl lg:text-6xl text-white font-medium mb-3" style="font-family: 'Clash Grotesk', sans-serif;">
            StayHere Rabat - Agdal Collection
          </h1>
          <p class="text-lg lg:text-xl text-white/90">
            Rabat - Résidence Comfort
          </p>
        </div>
      </div>
      
      <!-- Right Column: Booking Section (40% -> 5 columns) -->
      <div class="lg:col-span-5 bg-white h-auto lg:h-full flex flex-col justify-center p-6 lg:p-12 border-l border-gray-100 shadow-xl z-20">
        
        <div class="max-w-md mx-auto w-full">
          <!-- Image Grid (2x2) -->
          <div class="grid grid-cols-2 gap-2 mb-6">
            <img src="images/hero-agdal/modern_kitchen_1780518431349.png" alt="Kitchen" class="w-full h-24 lg:h-32 object-cover rounded-tl-lg" />
            <img src="images/hero-agdal/luxury_living_room_1780518446951.png" alt="Living Room" class="w-full h-24 lg:h-32 object-cover rounded-tr-lg" />
            <img src="images/hero-agdal/luxury_bedroom_1780518476199.png" alt="Bedroom" class="w-full h-24 lg:h-32 object-cover rounded-bl-lg" />
            <div class="relative w-full h-24 lg:h-32">
              <img src="images/hero-agdal/luxury_bathroom_1780518493480.png" alt="Bathroom" class="w-full h-full object-cover rounded-br-lg" />
              <div class="absolute inset-0 bg-black/40 rounded-br-lg flex items-center justify-center">
                <span class="text-white font-semibold text-sm">4 photos</span>
              </div>
            </div>
          </div>
          
          <!-- Rating and Reviews -->
          <div class="flex items-center justify-between mb-6 pb-6 border-b border-gray-100">
            <div class="flex items-center gap-3">
              <div class="w-11 h-11 rounded-full bg-[#FF5722] flex items-center justify-center text-white font-bold text-sm shadow-md">
                9.4
              </div>
              <div>
                <div class="text-gray-900 font-semibold leading-tight">Exceptionnel</div>
                <div class="text-gray-500 text-sm">729 avis</div>
              </div>
            </div>
            <div class="text-right">
              <div class="text-2xl font-bold text-gray-900 leading-none">799 MAD</div>
              <div class="text-gray-500 text-sm mt-1">/ nuit</div>
            </div>
          </div>

          <div class="text-sm text-[#FF5722] bg-[#FF5722]/10 p-2 rounded-md font-medium text-center mb-6">
            Meilleur tarif en réservation directe
          </div>
          
          <!-- Booking Form -->
          <form class="space-y-4">
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-gray-600 uppercase tracking-wide mb-1">Arrivée</label>
                <div class="relative">
                  <input type="text" class="datepicker form-control w-full border border-gray-200 rounded-md py-2.5 px-3 text-sm text-gray-700 focus:ring-[#FF5722] focus:border-[#FF5722] transition-colors" placeholder="mm/dd/yyyy">
                </div>
              </div>
              <div>
                <label class="block text-xs font-bold text-gray-600 uppercase tracking-wide mb-1">Départ</label>
                <div class="relative">
                  <input type="text" class="datepicker form-control w-full border border-gray-200 rounded-md py-2.5 px-3 text-sm text-gray-700 focus:ring-[#FF5722] focus:border-[#FF5722] transition-colors" placeholder="mm/dd/yyyy">
                </div>
              </div>
            </div>
            
            <button type="button" class="w-full bg-[#FF5722] hover:bg-[#e64a19] text-white font-bold py-3.5 px-4 rounded-md transition-all duration-200 mt-4 shadow-[0_4px_14px_0_rgba(255,87,34,0.39)] transform hover:-translate-y-0.5">
              Vérifier les disponibilités
            </button>
          </form>
          
        </div>
      </div>
      
    </div>
  </section>"""

# 1. Replace the HTML hero block
# Regex to find the <div class="hero-wrap ...>...</div> chunk.
pattern_html = re.compile(r'<div class="hero-wrap hero-section js-fullheight" id="home"[\s\S]*?<div class="hero-dots-container"[\s\S]*?</div>\n  </div>', re.MULTILINE)

content, count = pattern_html.subn(new_hero, content)
print(f"Replaced hero HTML: {count} times")

# 2. Remove the JavaScript hero slider logic
# Look for <script>\n      // ========================================\n      // HERO SLIDESHOW - AUTO-CYCLING ... to })();\n  </script>
pattern_js = re.compile(r'  <script>\n\s*// ========================================\n\s*// HERO SLIDESHOW[\s\S]*?\}\)\(\);\n  </script>\n', re.MULTILINE)
content, count_js = pattern_js.subn('', content)
print(f"Removed JS slideshow logic: {count_js} times")

# 3. Remove the CSS associated with hero luxury navigation
pattern_css = re.compile(r'  <style>\n\s*/\* ========================================= \*/\n\s*/\* HERO SLIDESHOW - LUXURY NAVIGATION STYLES \*/[\s\S]*?</style>\n', re.MULTILINE)
content, count_css = pattern_css.subn('', content)
print(f"Removed CSS slideshow logic: {count_css} times")


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

