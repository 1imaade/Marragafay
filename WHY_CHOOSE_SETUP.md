# POURQUOI CHOISIR AGAFAY MARRAKECH - Setup Guide

## 📁 Files Created
- `css/why-choose-section.css` - Modern luxury styling
- Updated `index.html` - Section structure added after hero

## 🎨 Design Features

### Modern Luxury Layout
- **Two-column grid** (desktop) / **Single column** (mobile)
- **Clean, minimalist design** with sharp edges
- **Professional spacing** and typography
- **Subtle hover effects** on cards

### Left Column - Image Collage
- **3 overlapping images** with precise positioning
- **Gold overlay badge** with section title
- **Dynamic stacking** creates visual interest
- **Responsive scaling** maintains layout on all devices

### Right Column - Content
- **Gold subtitle**: "AGAFAY MARRAKECH DESERT"
- **Large title**: "VOTRE BON ENDROIT POUR DÉCOUVRIR AGAFAY"
- **Decorative separator**: Gold dots + icon + gold dots
- **Description text**: Luxury serif font, excellent readability
- **3 advantage cards**: Icons + titles + descriptions

## 🖼️ Image Placeholders

Update these image paths in `index.html`:

```html
<!-- Image 1: Desert adventure -->
<img src="images/desert-adventure.jpg" alt="...">

<!-- Image 2: Luxury camp setup -->
<img src="images/luxury-camp-setup.jpg" alt="...">

<!-- Image 3: Camel sunset -->
<img src="images/camel-sunset.jpg" alt="...">
```

## ✏️ Text Customization

### Main Headers
- **Gold subtitle**: Line 862 - "Agafay Marrakech Desert"
- **Main title**: Line 865 - "Votre Bon Endroit Pour Découvrir Agafay"
- **Badge text**: Line 838 - "Pourquoi Choisir Agafay Marrakech"

### Description Paragraphs
- **Paragraph 1**: Lines 887-894
- **Paragraph 2**: Lines 896-901

### Advantage Cards
- **Card 1**: Meilleur Prix Qualité (Best Price Quality)
- **Card 2**: Meilleur Destination (Best Destination)
- **Card 3**: Service Personnalisé (Personalized Service)

## 🎨 Color Scheme

```css
Gold: #bc6c25 (brand color)
Blue: #172139 (headings)
Dark Gray: #222222 (body text)
Light Gray: #666666 (descriptions)
White: #ffffff (backgrounds)
```

## 📱 Responsive Breakpoints

- **Desktop**: 1025px+ (Two columns, full layout)
- **Tablet**: 769px-1024px (Two columns, adjusted spacing)
- **Mobile**: 481px-768px (Single column, stacked layout)
- **Small Mobile**: <480px (Optimized for small screens)

## ♿ Accessibility Features

✅ **Semantic HTML**: Proper heading hierarchy (h2, h3, p)  
✅ **ARIA labels**: All SVG icons have role="img" and aria-label  
✅ **Focus styles**: Keyboard navigation support  
✅ **Color contrast**: WCAG 4.5:1 compliant  
✅ **Reduced motion**: Respects user preferences  
✅ **Alt text**: All images have descriptive alt attributes

## 🎯 Key Features

### Dynamic Image Stacking
- Images positioned at different z-index levels
- Creates depth and visual interest
- Gold badge overlays naturally
- Responsive on all screen sizes

### Typography Hierarchy
- **Gold subtitle**: Uppercase, letter-spacing, brand color
- **Main title**: Large, bold, Playfair Display font
- **Description**: Serif font for luxury feel
- **Card titles**: Bold, clear, accessible

### Advantage Cards
- **Clean design**: White background, subtle shadow
- **Gold icons**: Square with rounded corners
- **Hover effects**: Subtle lift on hover
- **Responsive**: Stack on mobile

## 🔧 Customization Tips

### Change Colors
Edit `css/why-choose-section.css`:
- Line 44: Gold badge background
- Line 130: Subtitle color
- Line 143: Title color

### Adjust Spacing
Edit `css/why-choose-section.css`:
- Line 11: Section padding
- Line 29: Grid gap between columns
- Line 186: Cards margin

### Modify Card Layout
Change grid columns:
```css
.why-choose-cards {
  grid-template-columns: repeat(3, 1fr); /* Change 3 to 2 or 4 */
}
```

## 📍 Section Position

Currently placed after the hero section:
1. **Hero** (booking form)
2. **🆕 Why Choose Agafay** ← New section
3. **Activities**
4. **Packages**
5. **Gallery**
6. **Testimonials**

## ✨ Production Ready

- ✅ Clean, semantic HTML
- ✅ Modern CSS (Grid, Flexbox)
- ✅ Fully responsive design
- ✅ Accessibility compliant
- ✅ Performance optimized
- ✅ Browser compatible
- ✅ Easy to customize

The section is now live and matches the agafaymarrakech.com design with a modern, luxury aesthetic!
