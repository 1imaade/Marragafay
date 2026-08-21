# Review Submission Fix - Database Schema Update ✅

## Problem
Getting **400 Bad Request** when submitting reviews from `reviews.html` because:
- Database schema was updated from `image_url` (TEXT) to `images` (TEXT[])
- JavaScript code `reviews-manager.js` was still sending `image_url` field

## Solution
Updated `js/reviews-manager.js` to match the new Supabase schema.

---

## Changes Made

### 1. **Submission Logic** (Line 675)

**Before:**
```javascript
const reviewData = {
    name: name,
    rating: selectedRating,
    comment: comment,
    status: 'pending',
    image_url: photoUrls.length > 0 ? photoUrls[0] : null, // ❌ Wrong field
    created_at: new Date().toISOString()
};
```

**After:**
```javascript
const reviewData = {
    name: name,
    rating: selectedRating,
    comment: comment,
    status: 'pending',
    images: photoUrls.length > 0 ? [photoUrls[0]] : null, // ✅ Array format
    created_at: new Date().toISOString()
};
```

**Key Changes:**
- ✅ Changed field name: `image_url` → `images`
- ✅ Changed value format: `photoUrls[0]` → `[photoUrls[0]]` (wrapped in array)
- ✅ Maintains `null` for reviews without images

---

### 2. **Display Logic** (Lines 375-387)

**Before:**
```javascript
function createReviewCard(review) {
    const card = document.createElement('div');
    card.className = 'review-card fade-in';
    card.dataset.rating = review.rating;
    card.dataset.hasPhoto = (review.photo || review.image_url) ? 'true' : 'false';

    // Use consistent field names - support both 'photo' and 'image_url'
    const photoUrl = review.photo || review.image_url || null;
```

**After:**
```javascript
function createReviewCard(review) {
    const card = document.createElement('div');
    card.className = 'review-card fade-in';
    card.dataset.rating = review.rating;
    
    // Support new 'images' (TEXT[]) and legacy 'image_url' (TEXT) fields
    const photoUrl = review.images && review.images.length > 0 
        ? review.images[0]      // New: images array - take first image
        : review.image_url      // Legacy: single image_url
        ? review.image_url 
        : null;
    
    card.dataset.hasPhoto = photoUrl ? 'true' : 'false';
```

**Key Changes:**
- ✅ **Backward compatible**: Checks for both `review.images` (new) and `review.image_url` (old)
- ✅ **Array handling**: Uses `review.images[0]` to get the first image from the array
- ✅ **Fallback logic**: Falls back to old `image_url` field if `images` doesn't exist
- ✅ **UI unchanged**: Still displays one image, so existing layout doesn't break

---

## Database Schema

### Current Schema
```sql
CREATE TABLE reviews (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
  comment TEXT NOT NULL,
  images TEXT[],              -- NEW: Array of image URLs
  image_url TEXT,             -- LEGACY: Keep for old reviews
  status TEXT NOT NULL DEFAULT 'pending',
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Data Format

**New Review (with image):**
```json
{
  "name": "John Doe",
  "rating": 5,
  "comment": "Great experience!",
  "images": ["https://...supabase.co/.../photo.jpg"],
  "status": "pending"
}
```

**New Review (without image):**
```json
{
  "name": "Jane Smith",
  "rating": 4,
  "comment": "Very good!",
  "images": null,
  "status": "pending"
}
```

---

## How It Works

### Submission Flow
```
User fills form → Select image (optional)
    ↓
Upload to Supabase Storage
    ↓
Get public URL: "https://...image.jpg"
    ↓
Create reviewData:
  images: ["https://...image.jpg"]  ← Wrapped in array
    ↓
Insert to database (reviews table)
    ↓
Success! ✅
```

### Display Flow
```
Fetch review from database
    ↓
Check if review.images exists
    ↓
YES → Take first image: review.images[0]
NO  → Check review.image_url (legacy)
    ↓
Display image (or show no image)
```

---

## Backward Compatibility

The display logic supports **both formats**, so:

**Old Reviews (before schema update):**
```json
{
  "image_url": "https://...old-image.jpg",
  "images": null
}
```
→ Will display `image_url` ✅

**New Reviews (after schema update):**
```json
{
  "images": ["https://...new-image.jpg"],
  "image_url": null
}
```
→ Will display `images[0]` ✅

---

## Testing

### Test Case 1: Submit Review with Image
1. Go to `reviews.html`
2. Click "Write a Review"
3. Fill form + Upload an image
4. Click "Submit Review"
5. **Expected:** Success message, no 400 error

### Test Case 2: Submit Review without Image
1. Fill form without selecting an image
2. Submit
3. **Expected:** Success, `images: null` in database

### Test Case 3: Display Old Reviews
1. Create a review with old `image_url` field
2. View on `reviews.html`
3. **Expected:** Image displays correctly

---

## Files Modified

| File | Lines Changed | Purpose |
|------|---------------|---------|
| `js/reviews-manager.js` | 675-676 | Fixed submission payload |
| `js/reviews-manager.js` | 375-387 | Fixed display logic with backward compatibility |

---

## Key Points

✅ **Database field changed:** `image_url` → `images` (TEXT[])  
✅ **JavaScript updated:** Sends array format `[url]`  
✅ **Display logic:** Checks `images[0]` first, then falls back to `image_url`  
✅ **Backward compatible:** Old reviews still display correctly  
✅ **No UI changes:** Still shows one image, design unchanged  

---

## Status

✅ **FIXED** - Reviews can now be submitted successfully without 400 errors!

**Updated:** January 12, 2026  
**File:** `js/reviews-manager.js`  
**Issue:** 400 Bad Request (schema mismatch)  
**Resolution:** Updated to use `images` (TEXT[]) column
