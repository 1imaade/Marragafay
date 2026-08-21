import re

with open('activities.html', 'r') as f:
    content = f.read()

# Extract everything before <main
head_match = re.search(r'(.*?)(<main)', content, re.DOTALL)
head = head_match.group(1)

# Extract everything after </main>
tail_match = re.search(r'(</main>)(.*)', content, re.DOTALL)
tail = tail_match.group(2)

new_main = '''<main class="bg-[#F6F7EA] min-h-screen flex items-center justify-center py-32" style="background-color: #F6F7EA !important;">
  <div class="max-w-xl w-full mx-auto px-6 flex flex-col items-center">
    
    <!-- Ultra-thin SVG Checkmark -->
    <svg class="w-14 h-14 text-[#523225] mb-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
      <polyline points="22 4 12 14.01 9 11.01"></polyline>
    </svg>
    
    <!-- Header -->
    <h1 class="text-[32px] md:text-[44px] font-bold text-[#10100E] text-center mb-6 tracking-tight leading-tight lowercase" style="font-family: 'Clash Grotesk', sans-serif;">
      booking request received.
    </h1>
    
    <!-- Expectation-setting Copy -->
    <p class="text-[#10100E]/70 text-center text-[16px] max-w-md mb-12 leading-relaxed" style="font-family: 'Lay Grotesk', sans-serif;">
      Thank you for choosing Marragafay. Our concierge team is currently reviewing your itinerary and will contact you directly via WhatsApp shortly to finalize your logistics.
    </p>
    
    <!-- The Receipt Card -->
    <div class="w-full bg-white border border-[#10100E]/10 rounded-3xl rounded-bl-none xl:rounded-l-none xl:rounded-r-3xl p-6 md:p-8 mb-12 shadow-sm flex flex-col gap-6">
      
      <div class="flex flex-col gap-1.5 border-b border-[#10100E]/10 pb-4">
        <span class="text-[11px] font-semibold text-[#10100E]/40 uppercase tracking-widest">Experience</span>
        <span class="text-[16px] font-medium text-[#10100E]">The Signature Expedition</span>
      </div>
      
      <div class="flex flex-col gap-1.5 border-b border-[#10100E]/10 pb-4">
        <span class="text-[11px] font-semibold text-[#10100E]/40 uppercase tracking-widest">Date & Time</span>
        <span class="text-[16px] font-medium text-[#10100E]">October 14th, 2026 — 16:30</span>
      </div>
      
      <div class="flex flex-col gap-1.5 border-b border-[#10100E]/10 pb-4">
        <span class="text-[11px] font-semibold text-[#10100E]/40 uppercase tracking-widest">Guests</span>
        <span class="text-[16px] font-medium text-[#10100E]">2 Adults</span>
      </div>
      
      <div class="flex flex-col gap-1.5">
        <span class="text-[11px] font-semibold text-[#10100E]/40 uppercase tracking-widest">Client</span>
        <span class="text-[16px] font-medium text-[#10100E]">John Doe <span class="text-[#10100E]/20 mx-2">|</span> +212 600 000 000</span>
      </div>
      
    </div>
    
    <!-- Exit Navigation -->
    <a href="index.html" class="inline-flex items-center gap-2 text-[14px] font-semibold text-[#10100E]/60 hover:text-[#523225] transition-colors group tracking-wide">
      Return to Homepage 
      <span class="transition-transform group-hover:translate-x-1">&rarr;</span>
    </a>
    
  </div>
</main>'''

# Need to update title in head
head = head.replace('<title>Marragafay | Agafay Desert Luxury Tours &amp; Camps</title>', '<title>Booking Success | Marragafay</title>')

with open('success.html', 'w') as f:
    f.write(head + new_main + tail)

print("Created success.html successfully.")
