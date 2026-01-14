'use server';

import { createClient } from '@supabase/supabase-js';

/**
 * Initialize Supabase Client for Server Actions
 * Make sure SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY are in your .env.local
 */
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!;
const supabaseServiceKey = process.env.SUPABASE_SERVICE_ROLE_KEY!;

const supabase = createClient(supabaseUrl, supabaseServiceKey);

/**
 * SQL Snippet to create the review-images bucket (run this in Supabase SQL Editor if bucket doesn't exist):
 * 
 * -- Create storage bucket for review images
 * INSERT INTO storage.buckets (id, name, public)
 * VALUES ('review-images', 'review-images', true)
 * ON CONFLICT (id) DO NOTHING;
 * 
 * -- Allow public uploads to review-images bucket
 * CREATE POLICY "Allow public uploads to review-images"
 * ON storage.objects
 * FOR INSERT
 * TO anon, authenticated
 * WITH CHECK (bucket_id = 'review-images');
 * 
 * -- Allow public reads from review-images bucket
 * CREATE POLICY "Allow public reads from review-images"
 * ON storage.objects
 * FOR SELECT
 * TO anon, authenticated
 * USING (bucket_id = 'review-images');
 */

interface SubmitReviewResult {
    success?: boolean;
    message?: string;
    error?: string;
}

/**
 * Server Action: Submit Review with Image Upload
 * @param formData - Form data containing: name, rating, comment, image
 * @returns Success or error message
 */
export async function submitReview(formData: FormData): Promise<SubmitReviewResult> {
    try {
        console.log('🔵 [Server Action] submitReview called');

        // ============================================
        // 1. EXTRACT FORM DATA
        // ============================================
        const name = formData.get('name') as string;
        const rating = parseInt(formData.get('rating') as string);
        const comment = formData.get('comment') as string;
        const imageFile = formData.get('image') as File | null;

        console.log('📝 Form Data Received:', {
            name,
            rating,
            comment,
            hasImage: !!imageFile,
            imageSize: imageFile?.size,
            imageType: imageFile?.type,
        });

        // ============================================
        // 2. VALIDATION
        // ============================================

        // Validate required fields
        if (!name?.trim()) {
            console.log('❌ Validation Error: Name is required');
            return { error: 'Name is required' };
        }

        if (!rating || rating < 1 || rating > 5) {
            console.log('❌ Validation Error: Invalid rating');
            return { error: 'Rating must be between 1 and 5' };
        }

        if (!comment?.trim()) {
            console.log('❌ Validation Error: Comment is required');
            return { error: 'Review comment is required' };
        }

        // Validate image if provided
        let imageUrl: string | null = null;

        if (imageFile && imageFile.size > 0) {
            console.log('🖼️ Image file detected, validating...');

            // Check file type
            const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];
            if (!allowedTypes.includes(imageFile.type)) {
                console.log('❌ Validation Error: Invalid image type:', imageFile.type);
                return {
                    error: 'Invalid image type. Please upload a JPG, PNG, or WebP image.',
                };
            }

            // Check file size (5MB max)
            const maxSize = 5 * 1024 * 1024; // 5MB in bytes
            if (imageFile.size > maxSize) {
                console.log('❌ Validation Error: Image too large:', imageFile.size);
                return {
                    error: 'Image is too large. Maximum size is 5MB.',
                };
            }

            console.log('✅ Image validation passed');

            // ============================================
            // 3. UPLOAD IMAGE TO SUPABASE STORAGE
            // ============================================

            try {
                // Generate unique filename
                const fileExt = imageFile.name.split('.').pop();
                const fileName = `${Date.now()}-${Math.random().toString(36).substring(7)}.${fileExt}`;
                const filePath = fileName;

                console.log('📤 Uploading image to Supabase Storage...');
                console.log('   - Bucket: review-images');
                console.log('   - Path:', filePath);
                console.log('   - Size:', imageFile.size, 'bytes');

                // Convert File to ArrayBuffer for upload
                const arrayBuffer = await imageFile.arrayBuffer();
                const buffer = Buffer.from(arrayBuffer);

                // Upload to Supabase Storage
                const { data: uploadData, error: uploadError } = await supabase.storage
                    .from('review-images')
                    .upload(filePath, buffer, {
                        contentType: imageFile.type,
                        cacheControl: '3600',
                        upsert: false,
                    });

                if (uploadError) {
                    console.log('❌ Upload Error:', uploadError);
                    throw uploadError;
                }

                console.log('✅ Upload successful:', uploadData);

                // Get public URL
                const { data: urlData } = supabase.storage
                    .from('review-images')
                    .getPublicUrl(filePath);

                imageUrl = urlData.publicUrl;
                console.log('🔗 Public URL:', imageUrl);

            } catch (uploadError: any) {
                console.error('❌ Image upload failed:', uploadError);
                return {
                    error: `Failed to upload image: ${uploadError.message || 'Unknown error'}`,
                };
            }
        } else {
            console.log('ℹ️ No image provided with review');
        }

        // ============================================
        // 4. INSERT REVIEW INTO DATABASE
        // ============================================

        console.log('💾 Inserting review into database...');

        const reviewData = {
            name: name.trim(),
            rating,
            comment: comment.trim(),
            image_url: imageUrl,
            status: 'pending', // Reviews start as pending and need admin approval
            created_at: new Date().toISOString(),
        };

        console.log('📊 Review Data:', reviewData);

        const { data, error: dbError } = await supabase
            .from('reviews')
            .insert([reviewData])
            .select();

        if (dbError) {
            console.error('❌ Database Error:', dbError);

            // If DB insert fails but image was uploaded, try to delete the image
            if (imageUrl) {
                try {
                    const filePath = imageUrl.split('/').pop();
                    if (filePath) {
                        await supabase.storage.from('review-images').remove([filePath]);
                        console.log('🗑️ Cleaned up uploaded image after DB failure');
                    }
                } catch (cleanupError) {
                    console.error('⚠️ Failed to cleanup image:', cleanupError);
                }
            }

            throw dbError;
        }

        console.log('✅ Review inserted successfully:', data);

        return {
            success: true,
            message: 'Thank you! Your review has been submitted and is pending approval.',
        };

    } catch (error: any) {
        console.error('❌ [Server Action] Error:', error);
        return {
            error: error.message || 'Failed to submit review. Please try again.',
        };
    }
}
