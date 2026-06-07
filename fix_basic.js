const fs = require('fs');

let html = fs.readFileSync('activities.html', 'utf8');

// 1. Fix relative paths for the subfolder
html = html.replace(/(href|src)="(?!\/|http|mailto|tel|#)([^"]+)"/g, '$1="../$2"');

// Fix specific links that are already pointing correctly or need adjustment
html = html.replace(/href="\.\.\/\.\.\/css/g, 'href="../css'); // cleanup just in case
html = html.replace(/src="\.\.\/\.\.\/images/g, 'src="../images'); 

// 2. Extract Header (up to end of Hero)
const heroEndMarker = '</section>';
let heroEndIdx = html.indexOf(heroEndMarker, html.indexOf('<!-- HERO SECTION -->'));
if (heroEndIdx !== -1) {
    heroEndIdx += heroEndMarker.length;
}

// 3. Extract Footer (from <footer to end)
const footerStartIdx = html.indexOf('<footer');

let topPart = html.substring(0, heroEndIdx);
let bottomPart = html.substring(footerStartIdx);

// 4. Update the Hero content in topPart
topPart = topPart.replace('the soul of agafay', 'DISCOVERY PACK.');
topPart = topPart.replace('An unfiltered connection to the stone desert. High-adrenaline expeditions and absolute luxury under the Moroccan sun.', 'Your first night under the desert stars. Feel the raw freedom of the open desert on quad bike, ride camels at golden hour, and dine under the stars.');
topPart = topPart.replace('6 activités', 'ENTRY EXPERIENCE');
topPart = topPart.replace('<span class="bg-[#f6f7ea] text-[#272724] px-3 py-1 rounded-full text-[10px] font-semibold tracking-wide" style="font-family: \'Lay Grotesk\', sans-serif;">10 packs</span>', '');

// Ensure uppercase on H1
topPart = topPart.replace('lowercase', 'uppercase');

// Ensure correct image in Hero
topPart = topPart.replace('images/Slider-images/slider-1.webp', 'images/packs/pack-basic.webp');

// 5. The injected Grid Architecture
const gridInjection = `
      <section class="py-24">
        <div class="max-w-[1400px] mx-auto px-6 w-full">
          <div class="grid grid-cols-1 lg:grid-cols-[2fr_1fr] gap-16 lg:gap-24 relative">
            <!-- Left Column: Content & Timeline -->
            <div id="pack-content-column" class="flex flex-col gap-16"></div>
            <!-- Right Column: Booking Widget -->
            <div id="pack-booking-column" class="relative"></div>
          </div>
        </div>
      </section>
    </main>
`;

const finalHtml = topPart + "\n" + gridInjection + "\n" + bottomPart;

fs.writeFileSync('packages/basic.html', finalHtml, 'utf8');
console.log("Successfully created pristine shell in packages/basic.html");
