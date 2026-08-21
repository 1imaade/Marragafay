with open("packages/basic.html", "r") as f:
    html = f.read()

old_grid = """      <!-- Strict 3-Column Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-3 md:gap-4 auto-rows-[250px] md:auto-rows-[280px]">
        
        <!-- Main Anchor Image (Spans 2x2) -->
        <div class="md:col-span-2 md:row-span-2 relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1540202403-b712f0e0864c?q=80&w=1200&auto=format&fit=crop" alt="Desert Vibe" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        
        <!-- Right Stack 1 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1518509562904-e7ef99cdcc86?q=80&w=600&auto=format&fit=crop" alt="Details" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        
        <!-- Right Stack 2 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=600&auto=format&fit=crop" alt="Quad" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>

        <!-- Bottom Row 1 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1545832063-74f2d924b61a?q=80&w=600&auto=format&fit=crop" alt="Camp" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        
        <!-- Bottom Row 2 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1528277342758-f1d7613953a2?q=80&w=600&auto=format&fit=crop" alt="Food" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        
        <!-- Bottom Row 3 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1473163928189-364b2c4e1135?q=80&w=600&auto=format&fit=crop" alt="Stargazing" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>

        <!-- Extra Row for exact match (3 images) -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1502920514313-52581002a659?q=80&w=600&auto=format&fit=crop" alt="Fire" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1516483638261-f40889228a55?q=80&w=600&auto=format&fit=crop" alt="Tent" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1483729558449-99ef09a8c325?q=80&w=600&auto=format&fit=crop" alt="Sunset" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>

      </div>"""

new_grid = """      <!-- Strict 3-Column Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-2 auto-rows-[250px] md:auto-rows-[280px]">
        
        <!-- Main Anchor Image (Spans 2x2) -->
        <div class="md:col-span-2 md:row-span-2 relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1489599874182-36340656a59b?q=80&w=1200&auto=format&fit=crop" alt="Desert Vibe" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        
        <!-- Right Stack 1 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1518509562904-e7ef99cdcc86?q=80&w=600&auto=format&fit=crop" alt="Details" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        
        <!-- Right Stack 2 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=600&auto=format&fit=crop" alt="Quad" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>

        <!-- Bottom Row 1 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1545832063-74f2d924b61a?q=80&w=600&auto=format&fit=crop" alt="Camp" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        
        <!-- Bottom Row 2 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1528277342758-f1d7613953a2?q=80&w=600&auto=format&fit=crop" alt="Food" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        
        <!-- Bottom Row 3 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1473163928189-364b2c4e1135?q=80&w=600&auto=format&fit=crop" alt="Stargazing" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>

        <!-- Bottom Row 4 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1502920514313-52581002a659?q=80&w=600&auto=format&fit=crop" alt="Fire" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        
        <!-- Bottom Row 5 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1504280741503-f32fc2ab4400?q=80&w=600&auto=format&fit=crop" alt="Tent" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>
        
        <!-- Bottom Row 6 -->
        <div class="relative rounded-xl overflow-hidden group bg-white/5 cursor-pointer">
          <img src="https://images.unsplash.com/photo-1483729558449-99ef09a8c325?q=80&w=600&auto=format&fit=crop" alt="Sunset" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
        </div>

      </div>"""

if old_grid in html:
    html = html.replace(old_grid, new_grid)
    with open("packages/basic.html", "w") as f:
        f.write(html)
    print("Successfully replaced grid")
else:
    print("Error: Old grid not found in basic.html")
