const fs = require('fs');
const { JSDOM } = require('jsdom');

const basicHtml = fs.readFileSync('packages/basic.html', 'utf8');

const migrations = [
  { path: 'packages/comfort.html', type: 'package', name: 'Marragafay Signature', shortName: 'Signature' },
  { path: 'packages/luxe.html', type: 'package', name: 'The Marragafay Luxury', shortName: 'Luxury' },
  { path: 'activities/buggy.html', type: 'activity', name: 'Dune Buggy Adventure', shortName: 'Buggy' },
  { path: 'activities/camel-ride.html', type: 'activity', name: 'Sunset Camel Trek', shortName: 'Camel Trek' },
  { path: 'activities/dinner-show.html', type: 'activity', name: 'Agafay Dinner Show', shortName: 'Dinner Show' },
  { path: 'activities/hot-air-balloon.html', type: 'activity', name: 'Hot Air Balloon', shortName: 'Balloon' },
  { path: 'activities/paragliding.html', type: 'activity', name: 'Paragliding', shortName: 'Paragliding' },
  { path: 'activities/quad-biking.html', type: 'activity', name: 'Extreme Quad Biking', shortName: 'Quad Biking' }
];

function processMigration(migration) {
  console.log(`Processing ${migration.path}...`);
  const targetHtml = fs.readFileSync(migration.path, 'utf8');
  
  // Extract config
  const configMatch = targetHtml.match(/TourPageTemplate\.render\(([\s\S]*?),\s*'page-root'\);/);
  if (!configMatch) {
    console.error(`No config found in ${migration.path}`);
    return;
  }
  
  let configString = configMatch[1].trim();
  let config;
  try {
    eval('config = ' + configString);
  } catch (e) {
    console.error(`Failed to parse config for ${migration.path}:`, e);
    return;
  }

  const dom = new JSDOM(basicHtml);
  const doc = dom.window.document;

  // 1. Title Tag
  const titleTag = doc.querySelector('title');
  if (titleTag) titleTag.textContent = `${migration.name} - Agafay Desert | Marragafay`;

  // 2. Breadcrumbs
  const breadcrumbContainer = doc.querySelector('nav[aria-label="Breadcrumb"]');
  if (breadcrumbContainer) {
    const spans = breadcrumbContainer.querySelectorAll('span.text-\\[\\#EAE8E3\\]\\/90');
    if (spans.length > 0) {
      spans[spans.length - 1].textContent = migration.name;
    }
    if (migration.type === 'activity') {
      const aTags = breadcrumbContainer.querySelectorAll('a');
      if (aTags.length > 1) {
        aTags[1].textContent = 'Activities';
        aTags[1].href = '../activities.html';
      }
    }
  }

  // 3. Hero Section
  // H1 Title
  const h1Elements = doc.querySelectorAll('h1');
  h1Elements.forEach(h1 => {
    if (h1.textContent.includes('tonight, the desert is yours.')) {
      h1.textContent = config.title;
    }
  });

  // Hero Subtitle / Description (below H1)
  const heroDesc = doc.querySelector('p.text-\\[14px\\].text-white\\/75');
  if (heroDesc) {
    heroDesc.textContent = config.description || config.subTitle;
  }

  // Rating & Reviews in Hero
  const ratingDiv = doc.querySelector('.flex.items-center.gap-3.mt-0.text-sm');
  if (ratingDiv) {
    const ratingSpan = ratingDiv.querySelector('.text-orange-500');
    if (ratingSpan && config.rating) ratingSpan.textContent = config.rating + '/5';
    
    const reviewSpan = Array.from(ratingDiv.querySelectorAll('span')).find(s => s.textContent.includes('reviews'));
    if (reviewSpan && config.reviews) reviewSpan.textContent = `${config.reviews} reviews`;
  }

  // Hero Image
  const heroImg = doc.querySelector('img[src="../images/packs/pack-basic.webp"]');
  if (heroImg && config.heroImage) {
    heroImg.src = config.heroImage;
  }
  // Also preloaded image
  const preloadImg = doc.querySelector('link[rel="preload"][as="image"]');
  if (preloadImg && config.heroImage) {
    preloadImg.href = config.heroImage;
  }

  // 4. Booking Bar
  const bookingTitles = doc.querySelectorAll('span.font-semibold.text-\\[\\#10100E\\]');
  bookingTitles.forEach(span => {
    if (span.textContent.trim() === 'Discovery Pack') {
      span.textContent = migration.name;
    }
  });
  
  // Replace all occurrences of 39 € with actual price
  const spans = doc.querySelectorAll('span');
  spans.forEach(span => {
    if (span.textContent.trim() === '39 €' || span.textContent.trim() === '39€') {
      span.textContent = config.price;
    }
  });

  // 5. WhatsApp Links
  const waLinks = doc.querySelectorAll('a[href^="https://wa.me/"]');
  waLinks.forEach(link => {
    link.href = `https://wa.me/212672531624?text=Hello%20Marragafay!%20I%20want%20to%20book%20the%20${encodeURIComponent(migration.name)}.%20My%20details:`;
  });

  // 6. Highlights / Details Grid
  const highlightsContainer = doc.querySelector('div.w-full.max-w-\\[1300px\\].mx-auto.grid.grid-cols-2.md\\:grid-cols-4.gap-10');
  if (highlightsContainer && config.highlights) {
    const items = highlightsContainer.querySelectorAll('div.flex.flex-col.items-center');
    config.highlights.forEach((highlight, idx) => {
      if (items[idx]) {
        const textEl = items[idx].querySelector('span.text-\\[14px\\]');
        if (textEl) textEl.textContent = highlight.text;
        
        const svgPath = items[idx].querySelector('path');
        // We will keep the SVGs as they are for aesthetics, just update the text.
      }
    });
  }

  // 7. Itinerary (Timeline)
  const timelineTrack = doc.querySelector('div.relative.border-l.border-\\[\\#e2e0d3\\].ml-2');
  if (timelineTrack && config.timeline) {
    const stepTemplate = timelineTrack.firstElementChild.cloneNode(true);
    timelineTrack.innerHTML = ''; 
    
    config.timeline.forEach((step, idx) => {
      const stepEl = stepTemplate.cloneNode(true);
      
      const timeEl = stepEl.querySelector('div.text-\\[12px\\]');
      if (timeEl) timeEl.textContent = `STEP ${idx + 1}`; 
      
      const titleEl = stepEl.querySelector('h3.text-\\[18px\\]');
      if (titleEl) titleEl.textContent = step.title;
      
      const descEl = stepEl.querySelector('p.text-\\[15px\\]');
      if (descEl) descEl.textContent = step.text;
      
      timelineTrack.appendChild(stepEl);
    });
  }
  
  // 8. Specifications (What's included / Not included)
  const ulLists = doc.querySelectorAll('ul.space-y-3');
  if (ulLists.length >= 2) {
    const includedList = ulLists[0];
    if (includedList && config.included) {
      const liTemplate = includedList.firstElementChild.cloneNode(true);
      includedList.innerHTML = '';
      config.included.forEach(item => {
        const li = liTemplate.cloneNode(true);
        li.querySelector('span.text-\\[14px\\]').textContent = item;
        includedList.appendChild(li);
      });
    }
    
    const notIncludedList = ulLists[1];
    if (notIncludedList && config.notIncluded) {
      const liTemplate = notIncludedList.firstElementChild.cloneNode(true);
      notIncludedList.innerHTML = '';
      const notIncArray = Array.isArray(config.notIncluded) ? config.notIncluded : [config.notIncluded];
      notIncArray.forEach(item => {
        const li = liTemplate.cloneNode(true);
        li.querySelector('span.text-\\[14px\\]').textContent = item;
        notIncludedList.appendChild(li);
      });
    }
  }

  // 9. Gallery
  const galleryGrid = doc.querySelector('#experience-gallery div.grid');
  if (galleryGrid && config.gallery) {
    const images = galleryGrid.querySelectorAll('img');
    const badgeNumber = doc.querySelector('#experience-gallery span.text-white\\/40');
    if (badgeNumber) badgeNumber.textContent = config.gallery.length; 
    
    images.forEach((img, idx) => {
      const src = config.gallery[idx % config.gallery.length];
      // Note: original gallery paths might be `/public/...`. The basic.html uses `../images/...`
      // So if it starts with `/public/`, we can leave it, it might work, or replace `/public` with `..`
      img.src = src.replace('/public/', '../');
    });
    
    // Also update the two mini gallery images in the hero section right column
    const heroGridImgs = doc.querySelectorAll('div.col-span-1.lg\\:col-span-1.grid img');
    if (heroGridImgs.length >= 2 && config.gallery.length >= 2) {
      heroGridImgs[0].src = config.gallery[0].replace('/public/', '../');
      heroGridImgs[1].src = config.gallery[1].replace('/public/', '../');
    }
  }
  
  // 10. Update 8 photos button text in Hero
  const photosBtn = doc.querySelector('a[href="#experience-gallery"]');
  if (photosBtn && config.gallery) {
    photosBtn.innerHTML = photosBtn.innerHTML.replace(/\\d+ photos/, `${config.gallery.length} photos`);
  }

  const finalHtml = dom.serialize();
  fs.writeFileSync(migration.path, finalHtml);
  console.log(`Successfully migrated ${migration.path}`);
}

migrations.forEach(processMigration);
