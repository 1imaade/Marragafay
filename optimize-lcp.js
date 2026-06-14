const sharp = require('sharp');
const fs = require('fs');

async function optimizeImages() {
  const images = [
    {
      path: './images/logo-no-text.png',
      type: 'png',
      width: 400, // resize to be smaller
      quality: 80
    },
    {
      path: './images/Slider-images/slider-4.webp',
      type: 'webp',
      width: 1920,
      quality: 60
    },
    {
      path: './images/why-choose/why3.webp',
      type: 'webp',
      width: 800,
      quality: 60
    }
  ];

  for (const img of images) {
    if (!fs.existsSync(img.path)) {
      console.log(`File not found: ${img.path}`);
      continue;
    }
    
    const originalSize = fs.statSync(img.path).size;
    const backupPath = img.path + '.bak';
    
    // Backup original
    fs.copyFileSync(img.path, backupPath);
    
    try {
      let pipeline = sharp(backupPath).resize(img.width, null, { withoutEnlargement: true });
      
      if (img.type === 'png') {
        pipeline = pipeline.png({ quality: img.quality, compressionLevel: 9, adaptiveFiltering: true });
      } else if (img.type === 'webp') {
        pipeline = pipeline.webp({ quality: img.quality, effort: 6 });
      }
      
      await pipeline.toFile(img.path);
      
      const newSize = fs.statSync(img.path).size;
      console.log(`Optimized ${img.path}: ${(originalSize/1024).toFixed(1)}KB -> ${(newSize/1024).toFixed(1)}KB`);
      
      // Remove backup if successful
      fs.unlinkSync(backupPath);
    } catch (err) {
      console.error(`Error optimizing ${img.path}:`, err);
      // Restore backup
      fs.copyFileSync(backupPath, img.path);
      fs.unlinkSync(backupPath);
    }
  }
}

optimizeImages();
