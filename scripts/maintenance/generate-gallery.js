const fs = require('fs');
const path = require('path');

const galleryDir = path.join(process.cwd(), 'public', 'gallery-pages');
const outputFile = path.join(process.cwd(), 'lib', 'gallery-data.ts');

try {
    const categories = fs.readdirSync(galleryDir).filter(f => fs.statSync(path.join(galleryDir, f)).isDirectory());
    const galleryData = {};

    categories.forEach(category => {
        const images = fs.readdirSync(path.join(galleryDir, category))
            .filter(f => /\.(jpg|jpeg|png|webp)$/i.test(f))
            .map(f => `/gallery-pages/${category}/${f}`);

        galleryData[category] = images;
    });

    const fileContent = `export const GALLERY_DATA: Record<string, string[]> = ${JSON.stringify(galleryData, null, 2)};\n`;

    // Ensure lib dir exists
    if (!fs.existsSync(path.join(process.cwd(), 'lib'))) {
        fs.mkdirSync(path.join(process.cwd(), 'lib'));
    }

    fs.writeFileSync(outputFile, fileContent);
    console.log('Successfully generated lib/gallery-data.ts');
    console.log('Categories found:', Object.keys(galleryData));
} catch (error) {
    console.error('Error generating gallery data:', error);
}
