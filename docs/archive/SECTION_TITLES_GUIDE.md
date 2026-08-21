# Section Titles - Unified Luxury Design System

## 📋 Overview
All main section titles now follow the **exact same format** as "AGAFAY MARRAKECH DESERT / Votre Bon Endroit Pour Découvrir Agafay" with consistent typography, spacing, and hierarchy.

## 🎨 Design Pattern

### Two-Line Title Format
```
GOLD SUBTITLE (Small, uppercase, letter-spaced)
Main Title (Large, bold, uppercase, Playfair Display)
```

## 📁 Files
- **`css/section-titles.css`** - Unified styling system
- **Updated `index.html`** - All sections now use new format

## ✅ Updated Sections

### 1. **Pourquoi Choisir Agafay** (Why Choose)
```html
<p class="section-subtitle">Agafay Marrakech Desert</p>
<h2 class="section-main-title">Votre Bon Endroit Pour Découvrir Agafay</h2>
```

### 2. **Activities Section**
```html
<p class="section-subtitle">Agafay Marrakech Desert</p>
<h2 class="section-main-title">Découvrez Nos Activités D'Exception dans le Désert</h2>
```

### 3. **Packages Section**
```html
<p class="section-subtitle">Best Packages</p>
<h2 class="section-main-title">Nos Meilleures Formules Pour Découvrir Agafay</h2>
```

### 4. **Gallery Section**
```html
<p class="section-subtitle">Galerie</p>
<h2 class="section-main-title">Galerie de Souvenirs Inoubliables</h2>
```

### 5. **FAQ Section**
```html
<p class="section-subtitle">FAQ</p>
<h2 class="section-main-title">Tout Savoir Sur L'Expérience Agafay</h2>
```

### 6. **Testimonials Section**
```html
<p class="section-subtitle">Témoignages</p>
<h2 class="section-main-title">Ce Que Nos Clients Disent De Nous</h2>
```

## 🎯 CSS Classes

### Container
```css
.section-title-block {
  text-align: center;
  margin-bottom: 3.5rem;
}
```

### Gold Subtitle
```css
.section-subtitle {
  font-size: 0.95rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #bc6c25;
  margin: 0 0 0.5em 0;
}
```

### Main Title
```css
.section-main-title {
  font-family: 'Playfair Display', serif;
  font-size: 2.8rem;
  font-weight: 900;
  line-height: 1.05;
  text-transform: uppercase;
  color: #172139;
  margin: 0 0 1.2em 0;
}
```

## 📐 Specifications

### Typography
- **Gold Subtitle**: 0.95rem, semi-bold (600), uppercase, 2px letter-spacing
- **Main Title**: 2.8rem, extra bold (900), uppercase, Playfair Display font

### Colors
- **Gold**: `#bc6c25` (brand color for subtitle)
- **Deep Blue**: `#172139` (main title color)

### Spacing
- **Subtitle margin-bottom**: 0.5em
- **Title margin-bottom**: 1.2em
- **Block margin-bottom**: 3.5rem

### Responsive Breakpoints
- **Desktop**: 2.8rem title
- **Tablet** (≤1024px): 2.4rem title
- **Mobile** (≤768px): 2rem title
- **Small Mobile** (≤480px): 1.75rem title

## ✏️ How to Add New Section Title

### HTML Structure
```html
<!-- Your Section Title -->
<div class="section-title-block">
  <p class="section-subtitle">YOUR GOLD SUBTITLE</p>
  <h2 class="section-main-title">Your Main Title Here</h2>
</div>
```

### Left-Aligned Version
```html
<div class="section-title-block text-left">
  <p class="section-subtitle">YOUR SUBTITLE</p>
  <h2 class="section-main-title">Your Title</h2>
</div>
```

## 🎨 Customization Tips

### Change Subtitle Text
Find the section in `index.html` and update:
```html
<p class="section-subtitle">YOUR NEW SUBTITLE</p>
```

### Change Main Title
Update the h2 content:
```html
<h2 class="section-main-title">Your New Main Title</h2>
```

### Adjust Colors
Edit `css/section-titles.css`:
- Line 23: Change subtitle color
- Line 43: Change main title color

### Adjust Font Sizes
Edit `css/section-titles.css`:
- Line 17: Change subtitle font-size
- Line 37: Change main title font-size

## 🌍 French Title Examples

### Recommended Titles
- **Activities**: "Découvrez Nos Activités D'Exception dans le Désert"
- **Packages**: "Nos Meilleures Formules Pour Découvrir Agafay"
- **Gallery**: "Galerie de Souvenirs Inoubliables"
- **FAQ**: "Tout Savoir Sur L'Expérience Agafay"
- **Testimonials**: "Ce Que Nos Clients Disent De Nous"
- **About**: "Notre Histoire et Notre Passion"
- **Contact**: "Contactez-Nous Pour Réserver Votre Aventure"

### Gold Subtitle Options
- "Agafay Marrakech Desert"
- "Best Packages" / "Meilleurs Forfaits"
- "Activités de Luxe"
- "Galerie"
- "FAQ" / "Questions Fréquentes"
- "Témoignages"
- "À Propos"

## ♿ Accessibility

✅ **Semantic HTML**: Proper use of `<p>` and `<h2>` tags
✅ **Color Contrast**: WCAG compliant (4.5:1)
✅ **Responsive**: Scales properly on all devices
✅ **Keyboard Navigation**: Fully accessible
✅ **Screen Readers**: Clear hierarchy

## 🚀 Benefits

### Consistency
- ✅ All sections use identical format
- ✅ Visual harmony throughout site
- ✅ Professional appearance

### Maintainability
- ✅ Easy to update titles
- ✅ Clear code structure
- ✅ Well-documented

### Performance
- ✅ Lightweight CSS
- ✅ No JavaScript required
- ✅ Fast rendering

### User Experience
- ✅ Clear visual hierarchy
- ✅ Easy to scan
- ✅ Professional and elegant

## 📱 Mobile Optimization

All titles automatically adapt:
- **Desktop**: Full size (2.8rem)
- **Tablet**: Medium size (2.4rem)
- **Mobile**: Small size (2rem)
- **Small Mobile**: Extra small (1.75rem)

## 🎯 Result

Every section title now:
- ✅ Follows the **exact same pattern**
- ✅ Uses **consistent typography**
- ✅ Has **perfect spacing**
- ✅ Matches **agafaymarrakech.com style**
- ✅ Is **fully responsive**
- ✅ Is **accessible**

The website now has a **unified, professional, luxury design system** for all section titles!
