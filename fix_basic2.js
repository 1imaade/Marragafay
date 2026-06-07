const fs = require('fs');
let html = fs.readFileSync('packages/basic.html', 'utf8');

// Replace the badge wrapper with the exact requested micro tag
const badBadgeHTML = `<div class="flex items-center gap-2 mb-6">
            <span class="bg-[#523225] text-[#f6f7ea] px-3 py-1 rounded-full text-[10px] font-semibold tracking-wide" style="font-family: 'Lay Grotesk', sans-serif;">ENTRY EXPERIENCE</span>
            
          </div>`;
          
const goodBadgeHTML = `<span class="text-xs font-bold uppercase tracking-widest text-white/80 mb-4 block">ENTRY EXPERIENCE</span>`;

html = html.replace(badBadgeHTML, goodBadgeHTML);

fs.writeFileSync('packages/basic.html', html, 'utf8');
