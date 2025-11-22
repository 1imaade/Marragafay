# Tour Page Template - Data Structure Reference

## Complete Data Object Schema

```javascript
const tourPageData = {
  // ============================================
  // METADATA
  // ============================================
  formId: 'uniqueFormId',              // Unique ID for the booking form
  navActive: 'packs',                  // 'packs' or 'activities' - sets active nav item

  // ============================================
  // HERO SECTION
  // ============================================
  heroImages: [                         // Array of background slider images
    '../images/hotel-2.jpg',
    '../images/slide2.jpg',
    '../images/slide3.jpg',
    '../images/slide4.jpg'
  ],
  heroTitle: 'Agafay',                 // First part of hero title
  heroHighlight: 'Basic Pack',         // Highlighted part (gold color)
  breadcrumbParent: 'Packs',           // Breadcrumb parent text
  breadcrumbParentLink: '../packs.html', // Breadcrumb parent link
  breadcrumbCurrent: 'Basic Pack',     // Current page breadcrumb

  // ============================================
  // HEADER INFO
  // ============================================
  rating: '5.0',                       // Star rating (e.g., '5.0', '4.9')
  reviewCount: '120',                  // Number of reviews (without '+')
  title: 'Agafay Desert Basic Pack',   // Main page title
  description: 'Experience the magic...', // Introductory paragraph

  // ============================================
  // HIGHLIGHTS (Quick Info Pills)
  // ============================================
  highlights: [
    {
      icon: '<svg>...</svg>',          // SVG icon (inline)
      text: 'Duration: 4 Hours'        // Highlight text
    },
    {
      icon: '<svg>...</svg>',
      text: 'Location: Agafay Desert'
    },
    {
      icon: '<svg>...</svg>',
      text: 'Guide: Included'
    },
    {
      icon: '<svg>...</svg>',
      text: 'Transport: Optional'
    }
  ],

  // ============================================
  // TIMELINE (The Experience)
  // ============================================
  timeline: [
    {
      icon: '<svg>...</svg>',          // Timeline item icon
      title: 'Pickup & Welcome',       // Timeline step title
      description: 'Your journey begins...' // Timeline step description
    },
    {
      icon: '<svg>...</svg>',
      title: 'Quad Biking Adventure',
      description: 'Feel the adrenaline...'
    }
    // Add more timeline items as needed
  ],

  // ============================================
  // INCLUSIONS (What's Included)
  // ============================================
  inclusions: [                        // Array of included items
    '1 Hour Quad Biking',
    '20 Min Camel Ride',
    'Traditional Dinner',
    'Live Cultural Show',
    'Safety Equipment',
    'Mineral Water'
  ],

  notIncluded: 'Hotel Transfer (Extra), Alcoholic Beverages.', // Not included text

  // ============================================
  // GALLERY
  // ============================================
  galleryImages: [                     // Array of gallery images
    '../images/hotel-2.jpg',
    '../images/destination-2.jpg',
    '../images/destination-3.jpg'
  ],

  // ============================================
  // PRICING
  // ============================================
  price: '400 DH'                      // Price with currency
};
```

---

## Common SVG Icons

### Duration (Clock)
```svg
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <circle cx="12" cy="12" r="10"/>
  <polyline points="12 6 12 12 16 14"/>
</svg>
```

### Location (Map Pin)
```svg
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
  <circle cx="12" cy="10" r="3"/>
</svg>
```

### Guide (People)
```svg
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
  <circle cx="9" cy="7" r="4"/>
  <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
  <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
</svg>
```

### Transport (Car)
```svg
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <rect x="1" y="3" width="15" height="13"/>
  <polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/>
  <circle cx="5.5" cy="18.5" r="2.5"/>
  <circle cx="18.5" cy="18.5" r="2.5"/>
</svg>
```

### Welcome (Hand)
```svg
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/>
</svg>
```

### Activity (Target)
```svg
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>
```

### Safety (Shield)
```svg
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
</svg>
```

### Dining (Coffee Cup)
```svg
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M18 8h1a4 4 0 0 1 0 8h-1"/>
  <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/>
  <line x1="6" y1="1" x2="6" y2="4"/>
  <line x1="10" y1="1" x2="10" y2="4"/>
  <line x1="14" y1="1" x2="14" y2="4"/>
</svg>
```

### Star/Stargazing
```svg
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
</svg>
```

### Camera
```svg
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/>
  <circle cx="12" cy="13" r="4"/>
</svg>
```

---

## Field Guidelines

### Required Fields
All fields are required unless specifically noted as optional in your use case.

### Text Content
- **Title**: Keep under 60 characters for good display
- **Description**: 1-2 sentences, 100-200 characters ideal
- **Timeline titles**: Short, descriptive (3-6 words)
- **Timeline descriptions**: 1-2 sentences explaining the step

### Images
- **Hero Images**: Use high-quality landscape images (1920x1080 recommended)
- **Gallery Images**: Mix of landscape and portrait orientations
- Paths are relative to the HTML file location

### Pricing
- Include currency symbol (DH, €, $, etc.)
- Use comma for thousands (e.g., '1,500 DH')

### Ratings
- Use decimal format: '5.0', '4.9', '4.8', etc.
- Review count: Just the number, no '+' symbol needed (added automatically)

---

## Example: Minimal Data Object

```javascript
const minimalTourData = {
  formId: 'myTourForm',
  navActive: 'packs',
  heroImages: ['../images/hero.jpg'],
  heroTitle: 'Agafay',
  heroHighlight: 'My Tour',
  breadcrumbParent: 'Packs',
  breadcrumbParentLink: '../packs.html',
  breadcrumbCurrent: 'My Tour',
  rating: '5.0',
  reviewCount: '50',
  title: 'My Amazing Tour',
  description: 'A brief description of the tour.',
  highlights: [
    {icon: '<svg>...</svg>', text: 'Duration: 2 Hours'}
  ],
  timeline: [
    {icon: '<svg>...</svg>', title: 'Start', description: 'We begin here.'}
  ],
  inclusions: ['Item 1', 'Item 2'],
  notIncluded: 'Nothing excluded.',
  galleryImages: ['../images/1.jpg'],
  price: '200 DH'
};
```

---

## Tips

1. **Copy from existing data files** - Use `basic-pack-data.js` as a template
2. **Test SVG icons** - Preview them in browser before using
3. **Keep data clean** - Use consistent formatting
4. **Image paths** - Always use relative paths from the HTML file
5. **Timeline length** - 3-6 steps is ideal for readability
6. **Inclusions** - Split evenly between columns (the template handles this automatically)
