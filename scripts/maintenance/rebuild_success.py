import re

with open('success.html', 'r') as f:
    content = f.read()

# 1. Update Navbar CSS
# We will remove the enforcing solid background block and replace it with transparent enforcing
old_nav_style = '''    /* Enforce solid background color for the navbar */
    #ftco-navbar, 
    #ftco-navbar.scrolled, 
    #ftco-navbar.awake, 
    #ftco-navbar.sleep {
      background-color: #F6F7EA !important;
      background: #F6F7EA !important;
      --nav-text: #272724 !important;
      --nav-text-muted: #272724 !important;
    }
    
    /* Enforce dark text color for all navbar elements (except booking button) */
    #ftco-navbar .nav-link:not(.booking-btn),
    #ftco-navbar .navbar-brand,
    #ftco-navbar .language-toggle,
    #ftco-navbar .language-toggle span,
    #ftco-navbar .language-toggle i,
    #ftco-navbar .language-toggle::after,
    #ftco-navbar .dropdown-item,
    #ftco-navbar .navbar-toggler,
    #ftco-navbar .icon-menu,
    #ftco-navbar .icon-menu::before,
    #ftco-navbar.scrolled .nav-link:not(.booking-btn),
    #ftco-navbar.scrolled .navbar-brand {
      color: #272724 !important;
      border-color: #272724 !important;
    }'''

new_nav_style = '''    /* Enforce transparent background for hero */
    #ftco-navbar {
      background-color: transparent !important;
      background: transparent !important;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    #ftco-navbar.scrolled, 
    #ftco-navbar.awake, 
    #ftco-navbar.sleep {
      background-color: #10100E !important;
      background: #10100E !important;
    }
    
    /* Enforce light text color for all navbar elements */
    #ftco-navbar .nav-link:not(.booking-btn),
    #ftco-navbar .navbar-brand,
    #ftco-navbar .language-toggle,
    #ftco-navbar .language-toggle span,
    #ftco-navbar .language-toggle i,
    #ftco-navbar .language-toggle::after,
    #ftco-navbar .navbar-toggler,
    #ftco-navbar .icon-menu,
    #ftco-navbar .icon-menu::before,
    #ftco-navbar.scrolled .nav-link:not(.booking-btn),
    #ftco-navbar.scrolled .navbar-brand {
      color: #ffffff !important;
      border-color: #ffffff !important;
    }'''

content = content.replace(old_nav_style, new_nav_style)

# 2. Update Navbar HTML
old_nav_html = '''<nav class="navbar navbar-expand-lg bg-[#F6F7EA] text-[#272724] fixed top-0 z-[1000] w-full" style="position: fixed !important; top: 0 !important; background: #F6F7EA !important;" id="ftco-navbar">'''
new_nav_html = '''<nav class="navbar navbar-expand-lg bg-transparent text-white fixed top-0 z-[1000] w-full transition-colors duration-300" style="position: fixed !important; top: 0 !important;" id="ftco-navbar">'''

content = content.replace(old_nav_html, new_nav_html)

# 3. Rebuild Main Block
main_match = re.search(r'(<main class="bg-\[\#F6F7EA\].*?</main>)', content, re.DOTALL)
if main_match:
    old_main = main_match.group(1)
    new_main = '''<main class="relative min-h-screen flex items-center justify-center overflow-hidden pt-20">
  
  <!-- Desert Background & Overlay -->
  <div class="absolute inset-0 w-full h-full z-0">
    <img src="images/Slider-images/slider-1.webp" alt="Agafay Desert" class="absolute inset-0 w-full h-full object-cover scale-105" />
    <div class="absolute inset-0 bg-gradient-to-t from-[#10100E]/95 via-[#10100E]/70 to-black/40"></div>
  </div>

  <div class="max-w-2xl w-full mx-auto px-6 flex flex-col items-center relative z-10 py-12">
    
    <!-- Visual Authority Icon (Inverted) -->
    <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center mx-auto mb-6 shadow-[0_4px_20px_rgba(0,0,0,0.3)]">
      <svg class="w-5 h-5 text-[#10100E]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="20 6 9 17 4 12"></polyline>
      </svg>
    </div>
    
    <!-- Header -->
    <h1 class="text-[32px] md:text-[44px] font-bold text-white text-center mb-3 tracking-tight leading-tight lowercase" style="font-family: 'Clash Grotesk', sans-serif; text-shadow: 0 4px 10px rgba(0,0,0,0.5);">
      booking request received.
    </h1>
    
    <!-- Expectation-setting Copy -->
    <p class="text-white/80 text-center text-[16px] max-w-md mb-10 leading-relaxed font-light" style="font-family: 'Lay Grotesk', sans-serif;">
      Thank you for choosing Marragafay. Our concierge team is currently reviewing your itinerary and will contact you directly via WhatsApp shortly to finalize your logistics.
    </p>
    
    <!-- The Receipt Card -->
    <div class="max-w-xl mx-auto w-full bg-white border border-[#10100E]/10 rounded-xl p-8 md:p-10 mb-12 flex flex-col shadow-[0_20px_50px_rgba(0,0,0,0.5)]">
      
      <div class="flex flex-col md:flex-row md:items-center justify-between py-5 border-b border-gray-200 first:pt-0">
        <span class="text-[11px] md:text-xs font-bold tracking-[0.15em] uppercase text-gray-500">Experience</span>
        <span class="text-sm md:text-base font-semibold text-[#10100E] mt-1 md:mt-0 text-left md:text-right">The Signature Expedition</span>
      </div>
      
      <div class="flex flex-col md:flex-row md:items-center justify-between py-5 border-b border-gray-200">
        <span class="text-[11px] md:text-xs font-bold tracking-[0.15em] uppercase text-gray-500">Date & Time</span>
        <span class="text-sm md:text-base font-semibold text-[#10100E] mt-1 md:mt-0 text-left md:text-right">October 14th, 2026 — 16:30</span>
      </div>
      
      <div class="flex flex-col md:flex-row md:items-center justify-between py-5 border-b border-gray-200">
        <span class="text-[11px] md:text-xs font-bold tracking-[0.15em] uppercase text-gray-500">Guests</span>
        <span class="text-sm md:text-base font-semibold text-[#10100E] mt-1 md:mt-0 text-left md:text-right">2 Adults</span>
      </div>
      
      <div class="flex flex-col md:flex-row md:items-center justify-between py-5 border-b border-gray-200 last:border-0 last:pb-0">
        <span class="text-[11px] md:text-xs font-bold tracking-[0.15em] uppercase text-gray-500">Client</span>
        <span class="text-sm md:text-base font-semibold text-[#10100E] mt-1 md:mt-0 text-left md:text-right">John Doe <span class="text-[#10100E]/20 mx-2">|</span> +212 600 000 000</span>
      </div>
      
    </div>
    
    <!-- Exit Navigation -->
    <a href="index.html" class="inline-flex items-center gap-2 text-[14px] font-semibold text-white/80 hover:text-white transition-colors group tracking-wide">
      Return to Homepage 
      <span class="transition-transform group-hover:translate-x-1">&rarr;</span>
    </a>
    
  </div>
</main>'''
    content = content.replace(old_main, new_main)

with open('success.html', 'w') as f:
    f.write(content)

print("Rebuilt success.html successfully.")
