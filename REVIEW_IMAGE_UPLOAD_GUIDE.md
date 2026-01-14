# Review Image Upload - Server Action Complete ✅

## Summary
Created a **Next.js Server Action** (`app/actions/submit-review.ts`) with full image upload support to Supabase Storage.

---

## ✨ Features Implemented

### 1. **Image Upload to Supabase Storage**
- ✅ Uploads to `review-images` bucket
- ✅ Generates unique filenames: `{timestamp}-{random}.{ext}`
- ✅ Returns public URL
- ✅ Automatic cleanup if database insert fails

### 2. **Validation**
- ✅ **Required Fields:** name, rating (1-5), comment
- ✅ **Image Type:** JPG, PNG, WebP only
- ✅ **Image Size:** Max 5MB
- ✅ **Error Messages:** User-friendly validation errors

### 3. **Error Handling**
- ✅ Image upload failures
- ✅ Database insert failures
- ✅ Cleanup uploaded images on DB failure
- ✅ Comprehensive console logging for debugging

### 4. **Security**
- ✅ Uses Service Role Key (server-side only)
- ✅ Reviews set to `status: 'pending'` (require approval)
- ✅ File type validation
- ✅ File size limits

---

## 📋 Prerequisites

### 1. Environment Variables

Add these to your `.env.local` file:

```env
# Supabase Configuration
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key-here
```

⚠️ **Important:** 
- Use `SUPABASE_SERVICE_ROLE_KEY` (not the anon key) for Server Actions
- Never expose the service role key to the client

### 2. Supabase Storage Bucket

Run this SQL in **Supabase SQL Editor** to create the bucket and policies:

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

## 🔧 Server Action Usage

### Basic Usage (Form Component)

```tsx
'use client';

import { submitReview } from '@/app/actions/submit-review';
import { useState } from 'react';

export function ReviewForm() {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [message, setMessage] = useState('');

  async function handleSubmit(formData: FormData) {
    setIsSubmitting(true);
    setMessage('');

    const result = await submitReview(formData);

    if (result.success) {
      setMessage(result.message || 'Review submitted!');
      // Reset form or show success
    } else {
      setMessage(result.error || 'Failed to submit');
    }

    setIsSubmitting(false);
  }

  return (
    <form action={handleSubmit}>
      <input
        type="text"
        name="name"
        placeholder="Your Name"
        required
      />

      <select name="rating" required>
        <option value="">Select Rating</option>
        <option value="5">5 Stars</option>
        <option value="4">4 Stars</option>
        <option value="3">3 Stars</option>
        <option value="2">2 Stars</option>
        <option value="1">1 Star</option>
      </select>

      <textarea
        name="comment"
        placeholder="Your Review"
        required
      />

      <input
        type="file"
        name="image"
        accept="image/jpeg,image/jpg,image/png,image/webp"
      />

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Submitting...' : 'Submit Review'}
      </button>

      {message && <p>{message}</p>}
    </form>
  );
}
```

### Using with `useFormStatus` (Recommended)

```tsx
'use client';

import { submitReview } from '@/app/actions/submit-review';
import { useFormStatus } from 'react-dom';
import { useFormState } from 'react-dom';

function SubmitButton() {
  const { pending } = useFormStatus();
  
  return (
    <button type="submit" disabled={pending}>
      {pending ? 'Submitting...' : 'Submit Review'}
    </button>
  );
}

export function ReviewForm() {
  const [state, formAction] = useFormState(submitReview, {});

  return (
    <form action={formAction}>
      {/* form fields */}
      <SubmitButton />
      {state.error && <p className="error">{state.error}</p>}
      {state.success && <p className="success">{state.message}</p>}
    </form>
  );
}
```

---

## 🔍 Server Action Flow

```
1. Client submits form with formData
   ↓
2. Extract: name, rating, comment, image
   ↓
3. Validate all fields
   ↓
4. IF image exists:
   ├─ Validate type (JPG/PNG/WebP)
   ├─ Validate size (< 5MB)
   ├─ Generate unique filename
   ├─ Upload to Supabase Storage
   └─ Get public URL
   ↓
5. Insert review into database
   ├─ name, rating, comment
   ├─ image_url (if uploaded)
   └─ status: 'pending'
   ↓
6. Return success or error
```

---

## 🐛 Debugging

### Console Logs
The Server Action includes comprehensive logging:

```typescript
🔵 [Server Action] submitReview called
📝 Form Data Received: { name, rating, comment, hasImage, ... }
✅ Image validation passed
📤 Uploading image to Supabase Storage...
✅ Upload successful
🔗 Public URL: https://...
💾 Inserting review into database...
✅ Review inserted successfully
```

### Check Logs in Development:
```bash
npm run dev
```

Then submit a review - you'll see detailed logs in your terminal.

### Common Issues:

**❌ "Failed to upload image"**
- Check bucket `review-images` exists in Supabase
- Verify storage policies are set correctly
- Check `SUPABASE_SERVICE_ROLE_KEY` in `.env.local`

**❌ "Invalid image type"**
- Only JPG, PNG, WebP allowed
- Make sure `accept` attribute matches in the input

**❌ "Database Error"**
- Check `reviews` table has `image_url` column (TEXT type)
- Verify RLS policies allow inserts with `status = 'pending'`

---

## 📊 Database Schema

The Server Action expects this table structure:

```sql
CREATE TABLE reviews (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
  comment TEXT NOT NULL,
  image_url TEXT,          -- Public URL from Supabase Storage
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected')),
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## 🔐 Security Features

### ✅ **Server-Side Only**
- Uses `'use server'` directive
- Runs in Node.js environment
- Service role key never exposed to client

### ✅ **Validation**
- File type checking
- File size limits
- Required field validation

### ✅ **Pending Reviews**
- All reviews start as `status: 'pending'`
- Admin approval required before public display
- Prevents spam and inappropriate content

### ✅ **Error Handling**
- Try-catch blocks
- Cleanup on failures
- User-friendly error messages

---

## 🚀 Testing

### 1. **Test with Image**
```bash
# Submit a review with a JPG image (< 5MB)
# Expected:
# ✅ Image uploads to Supabase Storage
# ✅ Review inserted with image_url
# ✅ Status = 'pending'
```

### 2. **Test without Image**
```bash
# Submit a review without selecting an image
# Expected:
# ✅ Review inserted
# ✅ image_url = null
# ✅ Status = 'pending'
```

### 3. **Test Invalid Image**
```bash
# Try uploading a PDF or file > 5MB
# Expected:
# ❌ Validation error message
# ❌ No upload happens
```

### 4. **Test in Supabase Dashboard**
1. Go to **Storage** → `review-images`
2. Verify uploaded images appear
3. Check **Table Editor** → `reviews`
4. Verify `image_url` contains full public URL

---

## 📈 Next Steps

### Optional Enhancements:

1. **Image Optimization**
   ```typescript
   // Add image resizing before upload
   import sharp from 'sharp';
   
   const optimized = await sharp(buffer)
     .resize(800, 800, { fit: 'inside' })
     .jpeg({ quality: 80 })
     .toBuffer();
   ```

2. **Multiple Images**
   ```typescript
   // Allow up to 3 images per review
   const images = formData.getAll('images') as File[];
   const imageUrls = await Promise.all(
     images.map(file => uploadImage(file))
   );
   ```

3. **Progress Indicator**
   ```typescript
   // Show upload progress
   const { data, error } = await supabase.storage
     .from('review-images')
     .upload(filePath, buffer, {
       onUploadProgress: (progress) => {
         console.log(`${progress.loaded}/${progress.total}`);
       }
     });
   ```

4. **Image Moderation**
   ```typescript
   // Integrate with AWS Rekognition or similar
   const isAppropriate = await moderateImage(imageUrl);
   if (!isAppropriate) {
     // Delete image and reject review
   }
   ```

---

## 📄 Files Created

| File | Purpose |
|------|---------|
| `app/actions/submit-review.ts` | Server Action with image upload |

---

## Summary

✅ **Server Action Created:** Full image upload support  
✅ **Validation:** File type, size, required fields  
✅ **Error Handling:** Comprehensive with cleanup  
✅ **Logging:** Debug-friendly console logs  
✅ **Security:** Server-side only, pending reviews  
✅ **Documentation:** SQL snippets, usage examples  

**Status:** Ready to use! Just add environment variables and create the storage bucket.

---

**Created:** January 12, 2026  
**File:** `app/actions/submit-review.ts`  
**Storage Bucket:** `review-images`
