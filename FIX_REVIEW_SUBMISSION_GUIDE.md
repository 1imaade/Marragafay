# Fix Public Review Submission - Complete Guide 🔐

## Problem
Users cannot submit reviews on `reviews.html` due to blocked RLS policy in Supabase.

## Solution Overview
Since this is a **static HTML website** (not Next.js), we need to:
1. Fix the Supabase RLS policy to allow public INSERTs
2. Ensure the JavaScript submission code is correct
3. Test the submission flow

---

## Step 1: Fix Supabase RLS Policy (CRITICAL) 🔐

### Open Supabase SQL Editor
1. Go to your Supabase Dashboard → **SQL Editor**
2. Create a new query
3. Run the following SQL:

```sql
-- ============================================
-- ENABLE PUBLIC REVIEW SUBMISSIONS
-- (With automatic 'pending' status enforcement)
-- ============================================

-- 1. DROP existing policies (if any)
DROP POLICY IF EXISTS "Allow public SELECT for approved reviews" ON reviews;
DROP POLICY IF EXISTS "Allow public INSERT for pending reviews" ON reviews;
DROP POLICY IF EXISTS "Allow public inserts" ON reviews;

-- 2. CREATE SELECT policy (public can read ONLY approved reviews)
CREATE POLICY "Allow public SELECT for approved reviews"
ON reviews
FOR SELECT
TO anon, authenticated
USING (status = 'approved');

-- 3. CREATE INSERT policy (public can submit with 'pending' status ONLY)
CREATE POLICY "Allow public INSERT for pending reviews"
ON reviews
FOR INSERT
TO anon, authenticated
WITH CHECK (status = 'pending');

-- 4. Verify RLS is ENABLED
ALTER TABLE reviews ENABLE ROW LEVEL SECURITY;

-- 5. Grant INSERT permission to anon role
GRANT INSERT ON reviews TO anon;
GRANT SELECT ON reviews TO anon;
```

### Explanation:
-  **WITH CHECK (status = 'pending')** - Users can ONLY insert reviews with `status = 'pending'`
- ✅ **USING (status = 'approved')** - Users can ONLY read reviews with `status = 'approved'`
- ✅ **TO anon, authenticated** - Works for both anonymous and logged-in users

---

## Step 2: Verify JavaScript Code ✅

The existing `js/reviews-manager.js` already has the correct submission logic (lines 605-710). Here's what it does:

### Current Submission Flow:
```javascript
// 1. Collect form data
const name = document.querySelector('#reviewer-name').value.trim();
const comment = document.querySelector('#reviewer-comment').value.trim();
const rating = selectedRating; // From star selector

// 2. Upload photos to Supabase Storage (if provided)
const photoUrls = []; // Uploads to 'review-images' bucket

// 3. Insert review with 'pending' status
const reviewData = {
    name: name,
    rating: selectedRating,
    comment: comment,          // ✅ Matches Supabase schema
    status: 'pending',         // ✅ CRITICAL - users cannot publish directly
    image_url: photoUrls[0],   // ✅ Matches Supabase schema
    created_at: new Date().toISOString()
};

// 4. Submit to Supabase
const { data, error } = await supabaseClient
    .from('reviews')
    .insert([reviewData]);

// 5. Show success message
showMessage('Thank you! Your review has been submitted for approval.', 'success');
```

### ✅ **This code is already correct!**

---

## Step 3: Ensure Supabase Client is Initialized

Make sure `js/supabase-client.js` exists and initializes the client properly:

### Check `js/supabase-client.js`:
```javascript
// Initialize Supabase client
const SUPABASE_URL = 'YOUR_SUPABASE_URL';  // e.g., https://xxxxx.supabase.co
const SUPABASE_ANON_KEY = 'YOUR_ANON_KEY'; // Your public anon key

const supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

console.log('Supabase client initialized');
```

### Verify in `reviews.html`:
Make sure these scripts are loaded in the correct order:

```html
<!-- Supabase Client (for review submissions) -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="js/supabase-client.js"></script>

<!-- Reviews Manager -->
<script src="js/reviews-manager.js"></script>
```

**Order matters!** Supabase must load before `reviews-manager.js`.

---

## Step 4: Create Supabase Storage Bucket (For Photos)

If users upload photos, you need a storage bucket:

### Run in Supabase SQL Editor:
```sql
-- Create storage bucket for review images
INSERT INTO storage.buckets (id, name, public)
VALUES ('review-images', 'review-images', true)
ON CONFLICT (id) DO NOTHING;

-- Allow public uploads to review-images bucket
CREATE POLICY "Allow public uploads to review-images"
ON storage.objects
FOR INSERT
TO anon, authenticated
WITH CHECK (bucket_id = 'review-images');

-- Allow public reads from review-images bucket
CREATE POLICY "Allow public reads from review-images"
ON storage.objects
FOR SELECT
TO anon, authenticated
USING (bucket_id = 'review-images');
```

---

## Step 5: Test the Submission 🧪

### Manual Test Steps:
1. Open `reviews.html` in a browser
2. Click "Write a Review" button
3. Fill in:
   - Name: "Test User"
   - Rating: 5 stars
   - Comment: "This is a test review"
   - (Optional) Upload a photo
4. Click "SUBMIT REVIEW"
5. You should see: **"Thank you! Your review has been submitted for approval."**

### Verify in Supabase:
1. Go to Supabase Dashboard → **Table Editor** → `reviews`
2. You should see a new row with:
   - `name`: "Test User"
   - `rating`: 5
   - `comment`: "This is a test review"
   - `status`: **'pending'** ← IMPORTANT!
   - `image_url`: (URL if photo was uploaded)

### Check Browser Console:
Open Developer Tools (F12) → Console. You should see:
```
Supabase client initialized
Review submitted successfully: {...}
```

If you see an error, check:
- ❌ **"INSERT policy violation"** → RLS policy not configured correctly
- ❌ **"supabaseClient is not defined"** → Supabase client not initialized
- ❌ **"Network error"** → Check Supabase URL and API key

---

## Step 6: Approve Reviews in Dashboard

New reviews have `status = 'pending'`. To make them visible:

### Option 1: Approve via Supabase Dashboard
1. Go to Supabase → **Table Editor** → `reviews`
2. Find the pending review
3. Edit the `status` column → Change from `'pending'` to `'approved'`
4. Save

### Option 2: Approve via Admin Dashboard (Recommended)
If you have an admin dashboard (Next.js app), use the Review Manager component to approve/reject reviews.

---

## Troubleshooting 🔧

### Error: "new row violates row-level security policy"
**Solution:** Run Step 1 SQL to fix RLS policy

### Error: "supabaseClient is not defined"
**Solution:** 
1. Check `js/supabase-client.js` exists
2. Verify script loading order in `reviews.html`
3. Check browser console for initialization errors

### Error: "Failed to upload photo"
**Solution:** Run Step 4 SQL to create storage bucket and policies

### Success message shows but review doesn't appear
**Expected behavior!** Reviews start as `'pending'` and need admin approval before appearing on the page.

---

## Summary of Changes

### ✅ What You Need to Do:

1. **Run SQL in Supabase** (Step 1) - Fix RLS policy
2. **Verify Supabase client** (Step 3) - Check initialization
3. **Create storage bucket** (Step 4) - If using photos
4. **Test submission** (Step 5) - Verify it works
5. **Approve reviews** (Step 6) - Make them visible

### ✅ What's Already Done:

- `js/reviews-manager.js` has correct submission logic
- Form validation is implemented
- Success/error messaging works
- Photo upload to Supabase Storage is coded

---

## Expected User Flow

1. **User visits** `reviews.html`
2. **Clicks** "Write a Review" button
3. **Fills form**:
   - Name
   - Star rating (1-5)
   - Review text
   - Optional photo
4. **Clicks** "SUBMIT REVIEW"
5. **Sees message**: "Thank you! Your review has been submitted for approval."
6. **Modal closes** automatically after 2.5 seconds
7. **Review is saved** to Supabase with `status = 'pending'`
8. **Admin approves** review in dashboard
9. **Review appears** on `reviews.html` for all users

---

## Security Features ✅

- ✅ **Users cannot publish directly** - All reviews start as 'pending'
- ✅ **Users cannot read pending reviews** - Only 'approved' reviews are visible
- ✅ **RLS enforces the rules** - Even if JS is bypassed, database blocks it
- ✅ **Anon users can submit** - No login required for review submission

---

**Status:** Ready to fix! Run the SQL in Step 1 and test.
