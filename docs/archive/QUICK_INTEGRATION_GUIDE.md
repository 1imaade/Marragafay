# Quick Script Integration Guide

## Files That Need Supabase Scripts

### ✅ Already Complete:
- `reviews.html` - ✅ Has all scripts
- `packages/basic.html` - ✅ Has all scripts

---

### 📝 To Update:

#### 1. `index.html`
**Add before closing `</body>` tag:**
```html
<!-- Supabase Integration -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="js/supabase-client.js"></script>
<script src="js/dynamic-pricing.js"></script>
<script src="js/booking-manager.js"></script>
```

#### 2. `packs.html`
**Add before closing `</body>` tag:**
```html
<!-- Supabase Integration -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="js/supabase-client.js"></script>
<script src="js/dynamic-pricing.js"></script>
<script src="js/booking-manager.js"></script>
```

#### 3. `activities.html`
**Add before closing `</body>` tag:**
```html
<!-- Supabase Integration -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="js/supabase-client.js"></script>
<script src="js/dynamic-pricing.js"></script>
<script src="js/booking-manager.js"></script>
```

#### 4. Package Detail Pages:
- `packages/comfort.html`
- `packages/luxe.html`

**Add before closing `</body>` tag:**
```html
<!-- Supabase Integration -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="../js/supabase-client.js"></script>
<script src="../js/dynamic-pricing.js"></script>
<script src="../js/booking-manager.js"></script>
```

#### 5. Activity Detail Pages:
- `activities/buggy.html`
- `activities/camel-ride.html`
- `activities/dinner-show.html`
- `activities/hot-air-balloon.html`
- `activities/paragliding.html`
- `activities/quad-biking.html`

**Add before closing `</body>` tag:**
```html
<!-- Supabase Integration -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="../js/supabase-client.js"></script>
<script src="../js/dynamic-pricing.js"></script>
<script src="../js/booking-manager.js"></script>
```

---

## HTML Price Update Examples

### For Package Cards (packs.html, index.html):

**FIND THIS:**
```html
<span style="font-size: 2rem; font-weight: 700; color: #d4af37;">400 <small style="font-size: 1.2rem;">MAD</small></span>
```

**REPLACE WITH:**
```html
<div data-price-type="package" data-price-name="Basic">
  <span style="font-size: 2rem; font-weight: 700; color: #d4af37;">
    <span class="price-value">400</span> 
    <small style="font-size: 1.2rem;" class="price-currency">MAD</small>
  </span>
</div>
```

### For Activity Cards:

**FIND THIS:**
```html
<span>350 MAD/person</span>
```

**REPLACE WITH:**
```html
<div data-price-type="activity" data-price-name="Quad Biking">
  <span><span class="price-value">350</span> <span class="price-currency">MAD</span>/person</span>
</div>
```

---

## Testing After Integration

### 1. Open Browser Console (F12)
### 2. Navigate to each page
### 3. Check for these messages:

**Expected Console Output:**
```
Supabase client initialized successfully
Dynamic Pricing Manager Loaded
Fetching pricing from Supabase...
Pricing data fetched: [...]
Dynamic pricing initialized successfully
Booking Manager Loaded
```

### 4. Submit Test Booking
- Fill form
- Click submit
- Should see SweetAlert success message
- Check Supabase Dashboard → Table Editor → bookings

### 5. Test Reviews (reviews.html)
- Navigate to reviews page
- Should see: "Fetched X approved reviews from Supabase"
- Click "Write a Review"
- Upload image
- Submit
- Check Supabase Dashboard → Storage → review-images
- Check Table Editor → reviews (status should be 'pending')

---

## Priority Order for Implementation:

1. ✅ `reviews.html` - Already done
2. ⚡ `index.html` - Homepage (most traffic)
3. ⚡ `packs.html` - Package listing
4. ⚡ `activities.html` - Activity listing
 5. 📦 `packages/comfort.html`
6. 📦 `packages/luxe.html`
7. 🎯 All activity detail pages

---

## Common Issues & Fixes:

### Issue: "supabaseClient is not defined"
**Fix:** Ensure Supabase CDN script loads BEFORE supabase-client.js

### Issue: "Prices not updating"
**Fix:** 
1. Check console for errors
2. Verify data-price-type and data-price-name are correct
3. Ensure pricing table has matching records

### Issue: "Booking not saving"
**Fix:**
1. Check RLS policy on bookings table
2. Verify form has id="bookingForm"
3. Check field names match expected values

---

**Last Updated:** December 24, 2025  
**Status:** Integration scripts ready for deployment
