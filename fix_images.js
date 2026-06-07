const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const filesToProcess = [
  'packages/comfort.html',
  'packages/luxe.html',
  'activities/buggy.html',
  'activities/camel-ride.html',
  'activities/dinner-show.html',
  'activities/hot-air-balloon.html',
  'activities/paragliding.html',
  'activities/quad-biking.html'
];

const imagesDir = 'images/activites';
const imageFiles = fs.readdirSync(imagesDir)
  .filter(f => f.endsWith('.webp') || f.endsWith('.jpg') || f.endsWith('.jpeg'))
  .map(f => `../images/activites/${f}`);

function getRandomImage() {
  const randIndex = Math.floor(Math.random() * imageFiles.length);
  return imageFiles[randIndex];
}

filesToProcess.forEach(filePath => {
  console.log(`Fixing images in ${filePath}...`);
  const html = fs.readFileSync(filePath, 'utf8');
  const dom = new JSDOM(html);
  const doc = dom.window.document;

  // 1. Hero Section Images
  const heroSection = doc.querySelector('section.w-full.h-\\[80vh\\]');
  if (heroSection) {
    const heroImages = heroSection.querySelectorAll('img');
    heroImages.forEach(img => {
      img.src = getRandomImage();
      img.alt = "Marragafay Experience";
    });
    
    // Also update preload link for the hero image if there is one
    const preloadLink = doc.querySelector('link[rel="preload"][as="image"]');
    if (preloadLink && heroImages.length > 0) {
      preloadLink.href = heroImages[0].src;
    }
  }

  // 2. Gallery Section Images
  const gallerySection = doc.querySelector('#experience-gallery');
  if (gallerySection) {
    const galleryImages = gallerySection.querySelectorAll('img');
    galleryImages.forEach(img => {
      img.src = getRandomImage();
      img.alt = "Marragafay Experience";
    });
  }

  const finalHtml = dom.serialize();
  fs.writeFileSync(filePath, finalHtml);
});

console.log('Image placeholder injection complete.');
