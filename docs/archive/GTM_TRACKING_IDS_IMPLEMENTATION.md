# Google Tag Manager Tracking IDs Implementation

## Overview
This document tracks the implementation of GTM tracking IDs across all 21 HTML files in the Marragafay website for comprehensive event tracking.

## Tracking ID Schema

### 1. Booking Forms
- **Package Modals (index.html)**: `id="booking-form"`
- **Activity Modals (index.html)**: `id="booking-form-activity"`
- **Checkout Form (checkout.html)**: `id="booking-form"` to be added to `#checkoutForm`
- **Other pages**: `id="booking-form"` (if applicable)

### 2. Submit Buttons
- **Package Modal Submit**: `id="booking-submit-btn"`
- **Activity Modal Submit**: `id="booking-submit-btn-activity"`
- **Checkout Submit**: `id="booking-submit-btn"` to be added

### 3. WhatsApp Buttons
- **Package Modal**: `id="whatsapp-btn"` ✅ DONE
- **Activity Modal**: `id="whatsapp-btn-activity"` ✅ DONE
- **All other WhatsApp links**: `id="whatsapp-btn"` or unique IDs if multiple on same page

### 4. Messenger Buttons
- No messenger buttons found in initial scan

### 5. CTA "Book Now" Buttons
- **Hero Section**: `id="cta-book-now-hero"`
- **Activity Grid Cards**: `id="cta-book-now-{activity-name}"` (e.g., `cta-book-now-camel`)
- **Package Cards**: `id="cta-book-now-{package-name}"` (e.g., `cta-book-now-luxury`)
- **Other Book Now buttons**: Unique IDs based on context

### 6. Success Messages
- **SweetAlert Success Popups**: Add `id="booking-success-msg"` to success containers
- **Form Success States**: Add tracking to success message divs

## Implementation Status

### Files Completed
1. ✅ **index.html** - PARTIALLY COMPLETED
   - ✅ Package modal booking form: `id="booking-form"`
   - ✅ Activity modal booking form: `id="booking-form-activity"`  
   - ✅ Package modal submit button: `id="booking-submit-btn"`
   - ✅ Package modal WhatsApp button: `id="whatsapp-btn"`
   - ✅ Activity modal WhatsApp button: `id="whatsapp-btn-activity"`
   - ✅ First activity grid CTA: `id="cta-book-now"` (Camel Ride)
   - ⏳ Remaining activity grid buttons (5 more) need unique IDs
   - ⏳ Hero "Book Now" button needs ID
   - ⏳ Package card "Book Now" buttons (3) need IDs

2. ✅ **checkout.html** - COMPLETED
   - ✅ Main form: `id="booking-form"`  
   - ✅ Submit button: `id="booking-submit-btn"`
   - ✅ Updated JavaScript selector from `#checkoutForm` to `#booking-form`

3. ✅ **packs.html** - COMPLETED
   - ✅ Basic Pack CTA: `id="cta-book-now-basic"`
   - ✅ Comfort Pack CTA: `id="cta-book-now-comfort"`
   - ✅ Luxury Pack CTA: `id="cta-book-now-luxury"`

4. ✅ **activities.html** - COMPLETED
   - ✅ Camel Ride CTA: `id="cta-book-now-camel"`
   - ✅ Quad Biking CTA: `id="cta-book-now-quad"`
   - ✅ Buggy CTA: `id="cta-book-now-buggy"`
   - ✅ Hot Air Balloon CTA: `id="cta-book-now-balloon"`
   - ✅ Paragliding CTA: `id="cta-book-now-paragliding"`
   - ✅ Dinner Show CTA: `id="cta-book-now-dinner"`

### Files Pending (Lower Priority)
5. ⏳ about.html - May have "Book Now" button
6. ⏳ contact.html - Contact form (NOT a booking form)
7. ⏳ reviews.html - No booking elements expected
8. ⏳ blog.html / blog-single.html - No booking elements expected
9. ⏳ activities/camel-ride.html - Detail page (may have booking elements)
10. ⏳ activities/quad-biking.html - Detail page
11. ⏳ activities/buggy.html - Detail page
12. ⏳ activities/dinner-show.html - Detail page
13. ⏳ activities/hot-air-balloon.html - Detail page
14. ⏳ activities/paragliding.html - Detail page
15. ⏳ packages/basic.html  - Detail page
16. ⏳ packages/comfort.html - Detail page
17. ⏳ packages/luxe.html - Detail page

## Summary

### Key Conversions Tracking Implemented:
- ✅ **Main Booking Forms**: checkout.html, index.html modals
- ✅ **Submit Buttons**: All booking forms have `id="booking-submit-btn"` or variant
- ✅ **WhatsApp CTAs**: Package and activity modals have WhatsApp tracking
- ✅ **CTA "Book Now" Buttons**: All listing pages (packs.html, activities.html) have tracking
- ⏳ **Success Messages**: Requires JavaScript modification (currently using alert/SweetAlert)

### Notes on Remaining Work:
- Individual activity/package detail pages likely have their own booking widgets
- These detail pages should be checked for consistency
- Success message tracking may require modifying the SweetAlert configuration or adding IDs to success container elements


