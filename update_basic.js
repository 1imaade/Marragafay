const fs = require('fs');
const { JSDOM } = require('jsdom');

const basicHtmlPath = 'packages/basic.html';
const html = fs.readFileSync(basicHtmlPath, 'utf8');

const dom = new JSDOM(html);
const doc = dom.window.document;

const newTimeline = [
  { title: "Transport Arrival", text: "Meeting point pickup from central Marrakech for a hassle-free start to your desert evening." },
  { title: "Quad Session", text: "Discover wild and arid expanses, guided by experts for a safe experience. Enjoy the feeling of freedom while exploring this unique setting, in an exciting and memorable atmosphere." },
  { title: "Camel Ride", text: "Experience a unique journey through the golden dunes of the Agafay desert, discovering and admiration. Admire the natural beauty of this magical place, away from the bustle, in a peaceful and serene atmosphere." },
  { title: "Pool & Tea", text: "Relax by the pool and enjoy a refreshing cup of traditional Moroccan mint tea, the perfect complement to your desert adventure." },
  { title: "Dinner", text: "Savor an authentic Moroccan dinner surrounded by desert landscapes. Discover the rich flavors of traditional cuisine, with expertly prepared dishes, from fragrant tagines to delicate pastries." },
  { title: "Live Show", text: "Let yourself be carried away by the beauty and energy of this unique show, for an unforgettable memory. Immerse yourself in an enchanting cultural show under the stars, combining live music, traditional dance and artistic ambiance." },
  { title: "Transport Return", text: "Drop-off at the central meeting point in Marrakech after an unforgettable evening under the desert stars." }
];

const newIncluded = [
  "Quad Adventure: 1 hour of pure desert freedom on quad bike.",
  "Camel Ride: 20-minute journey as the desert turns golden at sunset.",
  "Moroccan Dinner: Traditional dishes served under an open sky.",
  "Live Show: Hypnotic fire and music performance under the stars.",
  "Pool Access: Refreshing dip and traditional mint tea on arrival.",
  "Transport: Shared pickup from central Marrakech meeting point.",
  "Guide: Bilingual professional throughout your experience."
];

const newNotIncluded = [
  "Additional Drinks"
];

// Update Timeline
const timelineTrack = doc.querySelector('div.relative.border-l.border-\\[\\#e2e0d3\\].ml-2');
if (timelineTrack) {
  const stepTemplate = timelineTrack.firstElementChild.cloneNode(true);
  timelineTrack.innerHTML = '';
  
  newTimeline.forEach((step, idx) => {
    const stepEl = stepTemplate.cloneNode(true);
    
    // Time/Step label
    const timeEl = stepEl.querySelector('div.text-\\[12px\\]');
    if (timeEl) timeEl.textContent = `STEP ${idx + 1}`;
    
    // Title
    const titleEl = stepEl.querySelector('h3.text-\\[18px\\]');
    if (titleEl) titleEl.textContent = step.title;
    
    // Text
    const descEl = stepEl.querySelector('p.text-\\[15px\\]');
    if (descEl) descEl.textContent = step.text;
    
    // Fix styling for the last element (removing mb-8 if it was there)
    if (idx === newTimeline.length - 1) {
      stepEl.classList.remove('mb-8');
    } else {
      if (!stepEl.classList.contains('mb-8')) {
        stepEl.classList.add('mb-8');
      }
    }
    
    timelineTrack.appendChild(stepEl);
  });
}

// Update Specs
const ulLists = doc.querySelectorAll('ul.space-y-3');
if (ulLists.length >= 2) {
  const includedList = ulLists[0];
  if (includedList) {
    const liTemplate = includedList.firstElementChild.cloneNode(true);
    includedList.innerHTML = '';
    newIncluded.forEach(item => {
      const li = liTemplate.cloneNode(true);
      li.querySelector('span.text-\\[14px\\]').textContent = item;
      includedList.appendChild(li);
    });
  }
  
  const notIncludedList = ulLists[1];
  if (notIncludedList) {
    const liTemplate = notIncludedList.firstElementChild.cloneNode(true);
    notIncludedList.innerHTML = '';
    newNotIncluded.forEach(item => {
      const li = liTemplate.cloneNode(true);
      li.querySelector('span.text-\\[14px\\]').textContent = item;
      notIncludedList.appendChild(li);
    });
  }
}

const finalHtml = dom.serialize();
fs.writeFileSync(basicHtmlPath, finalHtml);
console.log('Successfully updated basic.html');
