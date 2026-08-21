import re

# 1. Update success.html
with open('success.html', 'r') as f:
    html = f.read()

# Moving the header inside the card
# The header block is:
header_block = '''    <!-- Editorial Header -->
    <div class="text-center mb-10">
      <div class="inline-flex items-center justify-center w-16 h-16 rounded-full border border-[#C4622D]/30 bg-[#1A1208]/40 backdrop-blur-sm mb-6 animate-fade-up delay-100">
        <svg class="w-8 h-8 text-[#C4622D]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path class="success-icon-path" d="M20 6L9 17l-5-5"/>
        </svg>
      </div>
      <h1 class="font-editorial italic font-semibold text-5xl md:text-6xl lg:text-7xl text-[#FAF5EB] tracking-tight animate-fade-up delay-200">
        booking request received.
      </h1>
      <p class="mt-6 text-[#E3D9C8] text-lg font-light tracking-wide uppercase text-sm animate-fade-up delay-300">
        Marragafay Expeditions
      </p>
    </div>'''

# We need to extract the header, change text colors, and place it inside the card.
# First, remove it from the main flow
if header_block in html:
    html = html.replace(header_block, '')

# New Header block for inside the card
new_header_block = '''    <!-- Editorial Header (Encapsulated) -->
      <div class="text-center mb-10">
        <div class="inline-flex items-center justify-center w-16 h-16 rounded-full border border-[#C4622D]/30 bg-[#1A1208]/5 backdrop-blur-sm mb-6 animate-fade-up delay-100">
          <svg class="w-8 h-8 text-[#C4622D]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path class="success-icon-path" d="M20 6L9 17l-5-5"/>
          </svg>
        </div>
        <h1 class="font-editorial italic font-semibold text-4xl md:text-5xl lg:text-6xl text-[#10100E] tracking-tight animate-fade-up delay-200 mb-2">
          booking request received.
        </h1>
        <p class="text-[#9C8B72] text-[13px] font-bold uppercase tracking-[0.15em] animate-fade-up delay-300 mb-6">
          Marragafay Expeditions
        </p>
      </div>'''

# Inject inside the card
# Find: <div class="bg-[#FAF5EB] rounded-[20px] shadow-warm p-8 md:p-12 animate-fade-up delay-400">
card_start = '<div class="bg-[#FAF5EB] rounded-[20px] shadow-warm p-8 md:p-12 animate-fade-up delay-400">'
if card_start in html:
    html = html.replace(card_start, card_start + '\n\n  ' + new_header_block)

# 2. Fix the CTA Copy
html = html.replace('Contact VIP Support', 'WhatsApp Concierge')

# 3. Dynamic Data Injection script
old_script_start = '''<script>
    // Retrieve booking data from URL parameters'''
old_script_end = '''  </script>
</body>'''

new_script = '''<script>
    document.addEventListener('DOMContentLoaded', () => {
      const storedBooking = localStorage.getItem('recentBooking');
      if (!storedBooking) {
        // No data found, fallback
        document.getElementById('display-pack').textContent = 'Custom Expedition';
        document.getElementById('display-date').textContent = 'To be confirmed';
        document.getElementById('display-guests').textContent = '1 Guest';
        document.getElementById('display-name').textContent = 'Valued Guest';
        return;
      }

      try {
        const data = JSON.parse(storedBooking);
        
        const packName = data.package_name || 'Custom Expedition';
        const date = data.date || 'To be confirmed';
        const guests = data.guests_total || '1';
        const name = data.name || 'Valued Guest';

        let displayPack = packName;
        if(packName.toLowerCase().includes('luxe')) displayPack = 'The Luxury Private Experience';
        if(packName.toLowerCase().includes('basic')) displayPack = 'The Discovery Experience';
        if(packName.toLowerCase().includes('comfort')) displayPack = 'The Signature Experience';

        document.getElementById('display-pack').textContent = displayPack;
        document.getElementById('display-date').textContent = date;
        document.getElementById('display-guests').textContent = guests + (guests == 1 ? ' Guest' : ' Guests');
        document.getElementById('display-name').textContent = name;
        
      } catch (e) {
        console.error('Failed to parse recent booking', e);
      }
    });
  </script>
</body>'''

html = re.sub(r'<script>\s*// Retrieve booking data from URL parameters.*?</script>\s*</body>', new_script, html, flags=re.DOTALL)

with open('success.html', 'w') as f:
    f.write(html)

# 4. Update booking-manager.js
with open('js/booking-manager.js', 'r') as f:
    js_content = f.read()

injection_line = "            localStorage.setItem('recentBooking', JSON.stringify({ name: bookingData.name, date: bookingData.date, package_name: bookingData.package_title, guests_total: bookingData.guests }));\n            // Forcibly trigger a JavaScript redirect to the new dedicated success page\n            window.location.href = '../success.html';"

js_content = js_content.replace(
    "            // Forcibly trigger a JavaScript redirect to the new dedicated success page\n            window.location.href = '../success.html';", 
    injection_line
)

with open('js/booking-manager.js', 'w') as f:
    f.write(js_content)

print("Execution Plan completed successfully!")

