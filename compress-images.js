// compress-images.js
// Run: node compress-images.js
// Requires: npm install sharp glob

const sharp = require('sharp');
const { glob } = require('glob');
const path = require('path');
const fs = require('fs');

const INPUT_DIR = './images';
const OUTPUT_DIR = './images/compressed';
const QUALITY = 72; // Targets ~60%+ size reduction while preserving visual quality

async function compressImages() {
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  const files = await glob(`${INPUT_DIR}/**/*.webp`, { ignore: [`${INPUT_DIR}/compressed/**`] });

  if (files.length === 0) {
    console.log('No .webp files found in', INPUT_DIR);
    return;
  }

  console.log(`Found ${files.length} WebP image(s). Compressing...\n`);

  let totalOriginal = 0;
  let totalCompressed = 0;

  for (const file of files) {
    const relativePath = path.relative(INPUT_DIR, file);
    const outputPath = path.join(OUTPUT_DIR, relativePath);
    const outputFolder = path.dirname(outputPath);

    if (!fs.existsSync(outputFolder)) {
      fs.mkdirSync(outputFolder, { recursive: true });
    }

    const originalSize = fs.statSync(file).size;

    await sharp(file)
      .webp({ quality: QUALITY, effort: 6 })
      .toFile(outputPath);

    const compressedSize = fs.statSync(outputPath).size;
    const saving = (((originalSize - compressedSize) / originalSize) * 100).toFixed(1);

    totalOriginal += originalSize;
    totalCompressed += compressedSize;

    console.log(`✓ ${relativePath}`);
    console.log(`  ${(originalSize / 1024).toFixed(1)} KB → ${(compressedSize / 1024).toFixed(1)} KB  (saved ${saving}%)\n`);
  }

  const totalSaving = (((totalOriginal - totalCompressed) / totalOriginal) * 100).toFixed(1);
  console.log('─────────────────────────────────────');
  console.log(`Total: ${(totalOriginal / 1024).toFixed(1)} KB → ${(totalCompressed / 1024).toFixed(1)} KB`);
  console.log(`Overall size reduction: ${totalSaving}%`);
  console.log('\n✅ Done! Now replace originals:');
  console.log('   1. Copy files from images/compressed/ back to images/ (overwrite originals)');
  console.log('   2. Delete the images/compressed/ folder');
}

compressImages().catch(console.error);
