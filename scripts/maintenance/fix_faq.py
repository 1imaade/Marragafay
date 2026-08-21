with open("packages/basic.html", "r") as f:
    html = f.read()

old_header_block = """      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16">

        <div class="lg:col-span-4">
          <div class="lg:sticky lg:top-32">
            <span class="text-[#FF5A36] text-[11px] font-semibold uppercase tracking-widest block"
              style="margin-bottom: 1rem; color: #FF5A36; font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase;">
              Inquiries
            </span>
            <h2 class="font-bold text-[#10100E] lowercase"
              style="'Clash Grotesk', sans-serif; font-weight: 700; color: #10100E; letter-spacing: -0.025em; line-height: 1; font-size: clamp(32px, 5vw, 48px); margin: 0;">
              frequently asked questions
            </h2>
          </div>
        </div>

        <div class="lg:col-span-8 pt-4 lg:pt-0">
          <div style="border-top: 1px solid rgba(16, 16, 14, 0.1);">"""

new_header_block = """      <div class="w-full">

        <div class="w-full mb-12">
            <h2 class="font-bold text-[#10100E] lowercase"
              style="font-family: 'Clash Grotesk', sans-serif; font-weight: 700; color: #10100E; letter-spacing: -0.025em; line-height: 1; font-size: 24px; margin: 0;">
              frequently asked questions
            </h2>
        </div>

        <div class="w-full">
          <div style="border-top: 1px solid rgba(16, 16, 14, 0.1);">"""

html = html.replace(old_header_block, new_header_block)

# change icon color to orange
html = html.replace('text-[#10100E] transition-transform duration-300 faq-icon"', 'text-[#FF5A26] transition-transform duration-300 faq-icon"')
html = html.replace('color: #10100E; margin-left: 1.5rem; flex-shrink: 0; text-align: right; width: 24px;"', 'color: #FF5A26; margin-left: 1.5rem; flex-shrink: 0; text-align: right; width: 24px;"')

with open("packages/basic.html", "w") as f:
    f.write(html)
