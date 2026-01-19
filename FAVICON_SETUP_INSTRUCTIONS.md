# Favicon Setup Instructions for Google Search

## 📋 Overview
To fix the Google Search "Globe" icon issue, we need to provide high-resolution favicon files that Google can use in search results.

## 🎯 Required Files

You need to create the following favicon files from your logo at `images/logo/logo-high-res.png`:

### 1. **favicon-192.png** (CRITICAL for Google Search)
- **Size**: 192x192 pixels
- **Format**: PNG
- **Location**: `e:\Marragafay\images\favicon-192.png`
- **Purpose**: This is the minimum size Google requires to display your logo in search results

### 2. **apple-touch-icon.png**
- **Size**: 180x180 pixels
- **Format**: PNG
- **Location**: `e:\Marragafay\images\apple-touch-icon.png`
- **Purpose**: For Apple devices (iPhone, iPad) when users save your site to home screen

### 3. **favicon-32.png**
- **Size**: 32x32 pixels
- **Format**: PNG
- **Location**: `e:\Marragafay\images\favicon-32.png`
- **Purpose**: Standard browser tab favicon

### 4. **favicon.ico**
- **Size**: 48x48 pixels (or multi-size: 16, 32, 48)
- **Format**: ICO
- **Location**: `e:\Marragafay\images\favicon.ico`
- **Purpose**: Legacy browser support

## 🛠️ How to Create These Files

### Option 1: Online Tool (Easiest)
1. Go to https://realfavicongenerator.net/
2. Upload `images/logo/logo-high-res.png`
3. Download the favicon package
4. Extract and place files in `e:\Marragafay\images\` folder

### Option 2: Using Photoshop/GIMP
1. Open `images/logo/logo-high-res.png`
2. Resize to each required size
3. Export as PNG (or ICO for favicon.ico)
4. Save to `e:\Marragafay\images\` with the correct filename

### Option 3: Using ImageMagick (Command Line)
```powershell
# Install ImageMagick first from: https://imagemagick.org/script/download.php#windows

# Then run these commands:
cd e:\Marragafay
magick images/logo/logo-high-res.png -resize 192x192 images/favicon-192.png
magick images/logo/logo-high-res.png -resize 180x180 images/apple-touch-icon.png
magick images/logo/logo-high-res.png -resize 32x32 images/favicon-32.png
magick images/logo/logo-high-res.png -resize 48x48 images/favicon.ico
```

## ✅ After Creating Files

After creating all favicon files, the HTML files have been updated with the correct `<link>` tags to reference these favicons.

## 🔍 Verification

1. **Test locally**: Open your site and check if favicon appears in browser tab
2. **Check file paths**: Ensure all favicon files exist in `e:\Marragafay\images\`
3. **Google Search Console**: Use "URL Inspection" tool to check if Google can see your favicon
4. **Wait**: It may take 1-2 weeks for Google to re-crawl and update search results

## 📝 Next Steps After File Creation

1. Deploy updated HTML files to your live server
2. Submit sitemap to Google Search Console
3. Request re-indexing of your homepage
4. Wait for Google to crawl and update (this can take days to weeks)
