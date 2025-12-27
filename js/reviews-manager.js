/**
 * Reviews Page Manager
 * Handles filtering, loading, and submission of reviews
 * Integrates with Supabase for data persistence
 */

(function () {
    'use strict';

    // =========================================
    // SUPABASE REVIEWS DATA
    // Fetches approved reviews dynamically from Supabase
    // =========================================
    let allReviews = []; // Will be populated from Supabase

    // Sample reviews as fallback if Supabase is unavailable
    const sampleReviews = [
        {
            id: 1,
            name: 'Sarah Jenkins',
            location: 'London, UK',
            rating: 5,
            text: 'A truly magical experience! The camel ride at sunset was breathtaking, and the dinner show was the perfect end to the day. The staff went above and beyond to make our visit unforgettable. Highly recommended for anyone visiting Marrakech!',
            date: '2025-12-19',
            verified: true,
            photo: null,
            status: 'approved'
        },
        {
            id: 2,
            name: 'Marc Dubois',
            location: 'Paris, France',
            rating: 5,
            text: 'Professional guides and top-notch equipment. The quad biking was thrilling but felt very safe. Will definitely come back!',
            date: '2025-12-18',
            verified: true,
            photo: null,
            status: 'approved'
        },
        {
            id: 3,
            name: 'Emma Wilson',
            location: 'New York, USA',
            rating: 5,
            text: 'Best desert experience ever! The sunset was incredible and the traditional dinner exceeded all expectations. The entire team was so welcoming and professional.',
            date: '2025-12-17',
            verified: true,
            photo: 'images/activites/camel.jpg',
            status: 'approved'
        },
        {
            id: 4,
            name: 'Hassan Ahmed',
            location: 'Dubai, UAE',
            rating: 4,
            text: 'Great value for money. The buggy tour was fantastic and our guide Mohammed was very knowledgeable about the area.',
            date: '2025-12-16',
            verified: true,
            photo: null,
            status: 'approved'
        },
        {
            id: 5,
            name: 'Sylvie Bontijnck',
            location: 'Belgium',
            rating: 5,
            text: 'Unique and magnificent place that you absolutely must discover. A more than perfect dinner and warm welcome! The atmosphere under the stars was pure magic.',
            date: '2025-12-14',
            verified: true,
            photo: null,
            status: 'approved'
        },
        {
            id: 6,
            name: 'Gab de Solages',
            location: 'France',
            rating: 5,
            text: 'What an experience! Breathtaking food and quality service. The staff made us feel like royalty.',
            date: '2025-12-12',
            verified: true,
            photo: 'images/activites/quad.jpeg',
            status: 'approved'
        },
        {
            id: 7,
            name: 'Lisa Müller',
            location: 'Berlin, Germany',
            rating: 5,
            text: 'Perfect romantic getaway! The hot air balloon at sunrise followed by a champagne breakfast was unforgettable. We celebrated our anniversary here and it was the best decision ever!',
            date: '2025-12-10',
            verified: true,
            photo: 'images/activites/hote-aire.jpeg',
            status: 'approved'
        },
        {
            id: 8,
            name: 'Carlos Rivera',
            location: 'Madrid, Spain',
            rating: 4,
            text: 'Amazing desert adventure. The quad biking was exhilarating and the staff were incredibly friendly.',
            date: '2025-12-08',
            verified: true,
            photo: null,
            status: 'approved'
        },
        {
            id: 9,
            name: 'Yuki Tanaka',
            location: 'Tokyo, Japan',
            rating: 5,
            text: 'A once-in-a-lifetime experience. The camel trek through the desert at sunset was absolutely magical. Everything was perfectly organized from pickup to drop-off.',
            date: '2025-12-06',
            verified: true,
            photo: null,
            status: 'approved'
        },
        {
            id: 10,
            name: 'Anna Kowalski',
            location: 'Warsaw, Poland',
            rating: 5,
            text: 'Exceeded all expectations! The dinner show was entertaining and the food was authentic Moroccan cuisine.',
            date: '2025-12-04',
            verified: true,
            photo: 'images/activites/show.jpeg',
            status: 'approved'
        }
    ];

    /**
     * Fetch approved reviews from Supabase
     */
    async function fetchApprovedReviews() {
        try {
            console.log('Fetching approved reviews from Supabase...');

            const { data, error } = await supabaseClient
                .from('reviews')
                .select('*')
                .eq('status', 'approved') // ONLY fetch approved reviews
                .order('created_at', { ascending: false }); // Newest first

            if (error) throw error;

            console.log(`Fetched ${data.length} approved reviews from Supabase`);
            return data;

        } catch (error) {
            console.error('Error fetching reviews from Supabase:', error);
            console.log('Falling back to sample reviews');
            return sampleReviews;
        }
    }

    // =========================================
    // DOM ELEMENTS
    // =========================================
    let reviewsContainer,
        filterButtons,
        loadMoreBtn,
        writeReviewBtn,
        modalOverlay,
        modalCloseBtn,
        reviewForm,
        starRatingSelector;

    // =========================================
    // STATE
    // =========================================
    let currentFilter = 'all';
    let displayedReviews = 0;
    const reviewsPerLoad = 10;
    let selectedRating = 0;

    // =========================================
    // INITIALIZATION
    // =========================================
    function init() {
        // Cache DOM elements
        reviewsContainer = document.getElementById('reviews-grid');
        filterButtons = document.querySelectorAll('.filter-btn');
        loadMoreBtn = document.getElementById('load-more-btn');
        writeReviewBtn = document.getElementById('write-review-btn');
        modalOverlay = document.getElementById('review-modal-overlay');
        modalCloseBtn = document.getElementById('review-modal-close');
        reviewForm = document.getElementById('review-submission-form');
        starRatingSelector = document.getElementById('star-rating-selector');

        if (!reviewsContainer) {
            console.warn('Reviews container not found');
            return;
        }

        // Initialize event listeners
        initFilterListeners();
        initModalListeners();
        initStarRatingSelector();
        initFormSubmission();
        initPhotoUpload();

        // Load initial reviews
        loadReviews();

        console.log('Reviews Manager initialized');
    }

    // =========================================
    // PHOTO UPLOAD FUNCTIONALITY
    // =========================================
    function initPhotoUpload() {
        const uploadContainer = document.getElementById('photo-upload-container');
        const photoInput = document.getElementById('reviewer-photos');
        const previewContainer = document.getElementById('photo-preview-container');

        if (!uploadContainer || !photoInput) return;

        // Drag and drop handlers
        uploadContainer.addEventListener('dragover', function (e) {
            e.preventDefault();
            uploadContainer.classList.add('drag-over');
        });

        uploadContainer.addEventListener('dragleave', function (e) {
            e.preventDefault();
            uploadContainer.classList.remove('drag-over');
        });

        uploadContainer.addEventListener('drop', function (e) {
            e.preventDefault();
            uploadContainer.classList.remove('drag-over');

            if (e.dataTransfer.files.length > 0) {
                photoInput.files = e.dataTransfer.files;
                updatePhotoPreview(e.dataTransfer.files, previewContainer);
            }
        });

        // File input change handler
        photoInput.addEventListener('change', function () {
            updatePhotoPreview(this.files, previewContainer);
        });
    }

    function updatePhotoPreview(files, previewContainer) {
        if (!previewContainer) return;
        previewContainer.innerHTML = '';

        Array.from(files).forEach((file, index) => {
            if (!file.type.startsWith('image/')) return;

            const reader = new FileReader();
            reader.onload = function (e) {
                const previewItem = document.createElement('div');
                previewItem.className = 'photo-preview-item';
                previewItem.innerHTML = `
                    <img src="${e.target.result}" alt="Preview ${index + 1}">
                    <button type="button" class="photo-preview-remove" data-index="${index}">&times;</button>
                `;
                previewContainer.appendChild(previewItem);
            };
            reader.readAsDataURL(file);
        });
    }

    // =========================================
    // FILTER FUNCTIONALITY
    // =========================================
    function initFilterListeners() {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', function () {
                const filter = this.dataset.filter;
                setActiveFilter(filter);
                filterReviews(filter);
            });
        });
    }

    function setActiveFilter(filter) {
        filterButtons.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.filter === filter);
        });
        currentFilter = filter;
    }

    function filterReviews(filter) {
        const cards = reviewsContainer.querySelectorAll('.review-card');

        cards.forEach(card => {
            const rating = parseInt(card.dataset.rating);
            const hasPhoto = card.dataset.hasPhoto === 'true';
            let show = false;

            switch (filter) {
                case 'all':
                    show = true;
                    break;
                case '5':
                    show = rating === 5;
                    break;
                case '4':
                    show = rating === 4;
                    break;
                case '3':
                    show = rating <= 3;
                    break;
                case 'photos':
                    show = hasPhoto;
                    break;
                default:
                    show = true;
            }

            card.style.display = show ? '' : 'none';
        });
    }

    // =========================================
    // LOAD REVIEWS
    // =========================================
    async function loadReviews() {
        // Show loading state
        showLoadingState();

        // Fetch approved reviews from Supabase
        allReviews = await fetchApprovedReviews();

        reviewsContainer.innerHTML = '';

        if (allReviews.length === 0) {
            showEmptyState();
        } else {
            allReviews.forEach((review, index) => {
                const card = createReviewCard(review);
                card.style.animationDelay = `${index * 0.1}s`;
                reviewsContainer.appendChild(card);
            });
        }

        displayedReviews = allReviews.length;
        updateLoadMoreButton();

        // Update star distribution based on real data
        updateStarDistribution(allReviews);

        // Update the rating header with real stats
        updateRatingHeader(allReviews);
    }

    function showLoadingState() {
        reviewsContainer.innerHTML = `
            <div style="text-align: center; padding: 60px 20px;">
                <div class="spinner-border" role="status" style="color: #b18c58; width: 3rem; height: 3rem; border-width: 3px;">
                    <span class="sr-only">Loading...</span>
                </div>
                <p style="margin-top: 20px; color: #666; font-size: 16px;">Loading reviews...</p>
            </div>
        `;
    }

    function showEmptyState() {
        reviewsContainer.innerHTML = `
            <div style="text-align: center; padding: 80px 20px;">
                <svg viewBox="0 0 24 24" width="64" height="64" fill="none" stroke="#b18c58" stroke-width="1.5" style="margin: 0 auto 20px;">
                    <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path>
                </svg>
                <h4 style="color: #333; margin-bottom: 12px; font-weight: 600;">No Reviews Yet</h4>
                <p style="color: #666; margin-bottom: 24px;">Be the first to share your experience with Marragafay!</p>
                <button class="btn-write-review" onclick="document.getElementById('write-review-btn').click()">
                    Write First Review
                </button>
            </div>
        `;
    }

    function createReviewCard(review) {
        const card = document.createElement('div');
        card.className = 'review-card fade-in';
        card.dataset.rating = review.rating;
        card.dataset.hasPhoto = (review.photo || review.image_url) ? 'true' : 'false';

        // Use consistent field names - support both 'photo' and 'image_url'
        const photoUrl = review.photo || review.image_url || null;

        // Use correct field name - 'comment' from Supabase
        const reviewText = review.comment || review.text || '';

        // Location with fallback
        const location = review.location || 'Guest';

        // Generate avatar HTML - Always use initials with brand identity gold
        const initials = review.name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase();
        const bgColor = getAvatarColor();
        const avatarHTML = `<div class="review-avatar-placeholder" style="background: ${bgColor};">${initials}</div>`;

        // Generate stars HTML
        const starsHTML = generateStarsHTML(review.rating);

        // Generate photo HTML with 16:9 aspect ratio container
        const photoHTML = photoUrl
            ? `<div class="review-photo-container"><img src="${photoUrl}" alt="Review photo" class="review-photo" loading="lazy"></div>`
            : '';

        // Format date (relative time) - support both 'date' and 'created_at'
        const dateValue = review.created_at || review.date;
        const formattedDate = formatRelativeDate(dateValue);

        // Check if review text is long (needs Read More)
        const maxLength = 120;
        const isLongReview = reviewText.length > maxLength;
        const displayText = isLongReview ? reviewText.substring(0, maxLength) + '...' : reviewText;
        const readMoreHTML = isLongReview ? `<a href="javascript:void(0)" class="read-more-link" data-full-text="${reviewText.replace(/"/g, '&quot;')}">Read More</a>` : '';

        card.innerHTML = `
      <div class="review-card-header">
        ${avatarHTML}
        <div class="review-author-info">
          <h4 class="review-author-name">${review.name}</h4>
          <div class="review-author-meta">
            <span class="review-author-location">${location}</span>
          </div>
        </div>
      </div>
      <div class="review-stars">
        ${starsHTML}
      </div>
      ${photoHTML}
      <div class="review-content-wrapper">
        <p class="review-content">${displayText}</p>
        ${readMoreHTML}
      </div>
      <div class="review-footer">
        <span class="review-date">${formattedDate}</span>
        <span class="review-verified">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
          </svg>
          Verified
        </span>
      </div>
    `;

        // Add Read More click handler
        const readMoreLink = card.querySelector('.read-more-link');
        if (readMoreLink) {
            readMoreLink.addEventListener('click', function (e) {
                e.preventDefault();
                const fullText = this.getAttribute('data-full-text');
                const contentP = this.previousElementSibling;
                if (contentP) {
                    contentP.textContent = fullText;
                }
                this.style.display = 'none';
            });
        }

        return card;
    }

    function generateStarsHTML(rating) {
        let html = '';
        for (let i = 1; i <= 5; i++) {
            const filled = i <= rating;
            html += `
        <svg class="star-icon ${filled ? '' : 'empty'}" viewBox="0 0 24 24">
          <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
        </svg>
      `;
        }
        return html;
    }

    // Avatar background color - Brand Identity Gold
    const AVATAR_COLOR = '#b18c58';

    function getAvatarColor() {
        return AVATAR_COLOR;
    }

    function formatDate(dateString) {
        const date = new Date(dateString);
        const options = { month: 'short', year: 'numeric' };
        return date.toLocaleDateString('en-US', options);
    }

    function formatRelativeDate(dateString) {
        const date = new Date(dateString);
        const now = new Date();
        const diffTime = Math.abs(now - date);
        const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));

        if (diffDays === 0) {
            return 'Today';
        } else if (diffDays === 1) {
            return 'Yesterday';
        } else if (diffDays < 7) {
            return `${diffDays} days ago`;
        } else if (diffDays < 14) {
            return '1 week ago';
        } else if (diffDays < 30) {
            const weeks = Math.floor(diffDays / 7);
            return `${weeks} weeks ago`;
        } else if (diffDays < 60) {
            return '1 month ago';
        } else {
            const options = { month: 'short', year: 'numeric' };
            return date.toLocaleDateString('en-US', options);
        }
    }

    function updateLoadMoreButton() {
        if (loadMoreBtn) {
            loadMoreBtn.style.display = displayedReviews >= sampleReviews.length ? 'none' : 'inline-flex';
        }
    }

    // =========================================
    // MODAL FUNCTIONALITY
    // =========================================
    function initModalListeners() {
        if (writeReviewBtn) {
            writeReviewBtn.addEventListener('click', openModal);
        }

        if (modalCloseBtn) {
            modalCloseBtn.addEventListener('click', closeModal);
        }

        if (modalOverlay) {
            modalOverlay.addEventListener('click', function (e) {
                if (e.target === modalOverlay) {
                    closeModal();
                }
            });
        }

        // Close on ESC key
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && modalOverlay && modalOverlay.classList.contains('active')) {
                closeModal();
            }
        });
    }

    function openModal() {
        if (modalOverlay) {
            modalOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeModal() {
        if (modalOverlay) {
            modalOverlay.classList.remove('active');
            document.body.style.overflow = '';
            resetForm();
        }
    }

    // =========================================
    // STAR RATING SELECTOR
    // =========================================
    function initStarRatingSelector() {
        if (!starRatingSelector) return;

        const starButtons = starRatingSelector.querySelectorAll('.star-btn');

        starButtons.forEach((btn, index) => {
            btn.addEventListener('click', function () {
                selectedRating = index + 1;
                updateStarSelection(selectedRating);
            });

            btn.addEventListener('mouseenter', function () {
                updateStarHover(index + 1);
            });

            btn.addEventListener('mouseleave', function () {
                updateStarHover(0);
                updateStarSelection(selectedRating);
            });
        });
    }

    function updateStarSelection(rating) {
        const starButtons = starRatingSelector.querySelectorAll('.star-btn');
        starButtons.forEach((btn, index) => {
            btn.classList.toggle('selected', index < rating);
        });
    }

    function updateStarHover(rating) {
        const starButtons = starRatingSelector.querySelectorAll('.star-btn');
        starButtons.forEach((btn, index) => {
            btn.classList.toggle('hovered', index < rating);
        });
    }

    // =========================================
    // FORM SUBMISSION
    // =========================================
    function initFormSubmission() {
        if (!reviewForm) return;

        reviewForm.addEventListener('submit', async function (e) {
            e.preventDefault();

            const submitBtn = reviewForm.querySelector('.btn-submit-review');
            const messageEl = reviewForm.querySelector('.review-form-message');

            // Validate
            const name = reviewForm.querySelector('#reviewer-name').value.trim();
            const comment = reviewForm.querySelector('#reviewer-comment').value.trim();
            const photoInput = reviewForm.querySelector('#reviewer-photos');
            const photos = photoInput ? photoInput.files : null;

            if (!name || !comment || selectedRating === 0) {
                showMessage(messageEl, 'Please fill in all fields and select a rating.', 'error');
                return;
            }

            // Disable button
            submitBtn.disabled = true;
            submitBtn.textContent = 'Submitting...';

            try {
                // Upload photos to Supabase Storage if they exist
                let photoUrls = [];
                if (photos && photos.length > 0 && typeof supabaseClient !== 'undefined') {
                    console.log('Uploading photos to Supabase Storage...');

                    for (let i = 0; i < photos.length; i++) {
                        const file = photos[i];
                        const fileExt = file.name.split('.').pop();
                        const fileName = `${Date.now()}_${i}.${fileExt}`;
                        const filePath = `${fileName}`;

                        // Upload to Supabase Storage
                        const { data: uploadData, error: uploadError } = await supabaseClient
                            .storage
                            .from('review-images')
                            .upload(filePath, file, {
                                cacheControl: '3600',
                                upsert: false
                            });

                        if (uploadError) {
                            console.error('Upload error:', uploadError);
                            throw uploadError;
                        }

                        // Get public URL
                        const { data: { publicUrl } } = supabaseClient
                            .storage
                            .from('review-images')
                            .getPublicUrl(filePath);

                        photoUrls.push(publicUrl);
                        console.log(`Uploaded: ${publicUrl}`);
                    }
                } else if (photos && photos.length > 0) {
                    // Fallback if Supabase not available
                    for (let i = 0; i < photos.length; i++) {
                        photoUrls.push(photos[i].name);
                    }
                    console.log('Photos prepared (demo mode):', photoUrls);
                }

                // Submit to Supabase with pending status
                const reviewData = {
                    name: name,
                    rating: selectedRating,
                    comment: comment, // Using 'comment' field from Supabase schema
                    status: 'pending', // Awaiting dashboard approval
                    image_url: photoUrls.length > 0 ? photoUrls[0] : null, // Using 'image_url' field
                    created_at: new Date().toISOString()
                };

                // Check if Supabase client exists
                if (typeof supabaseClient !== 'undefined') {
                    const { data, error } = await supabaseClient
                        .from('reviews')
                        .insert([reviewData]);

                    if (error) {
                        throw error;
                    }

                    console.log('Review submitted successfully:', data);
                } else {
                    // Simulate submission for demo
                    console.log('Review submitted (demo mode):', reviewData);
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }

                showMessage(messageEl, 'Thank you! Your review has been submitted for approval.', 'success');

                // Reset form after success
                setTimeout(() => {
                    closeModal();
                }, 2500);

            } catch (error) {
                console.error('Error submitting review:', error);
                showMessage(messageEl, 'Failed to submit review. Please try again.', 'error');
            } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = 'SUBMIT REVIEW';
            }
        });
    }

    function showMessage(el, message, type) {
        if (!el) return;
        el.textContent = message;
        el.className = 'review-form-message ' + type;
    }

    function resetForm() {
        if (reviewForm) {
            reviewForm.reset();
            selectedRating = 0;
            updateStarSelection(0);
            const messageEl = reviewForm.querySelector('.review-form-message');
            if (messageEl) {
                messageEl.className = 'review-form-message';
                messageEl.textContent = '';
            }
        }
    }

    // =========================================
    // UPDATE STAR DISTRIBUTION ON PAGE
    // =========================================
    function updateStarDistribution(reviews) {
        if (!reviews || reviews.length === 0) return;

        const stats = calculateStats(reviews);

        // Update average rating display
        const avgRatingEl = document.querySelector('.aggregate-rating-value');
        if (avgRatingEl) {
            avgRatingEl.textContent = stats.average;
        }

        // Update total reviews count
        const totalReviewsEl = document.querySelector('.total-reviews-count');
        if (totalReviewsEl) {
            totalReviewsEl.textContent = `${stats.total} reviews`;
        }

        // Update star breakdown bars
        for (let i = 1; i <= 5; i++) {
            const barEl = document.querySelector(`[data-star="${i}"] .star-bar-fill`);
            const percentEl = document.querySelector(`[data-star="${i}"] .star-percent`);

            if (barEl) {
                barEl.style.width = `${stats.percentages[i]}%`;
            }

            if (percentEl) {
                percentEl.textContent = `${stats.percentages[i]}%`;
            }
        }

        console.log('Star distribution updated:', stats);
    }

    // =========================================
    // UPDATE RATING HEADER ON PAGE
    // =========================================
    function updateRatingHeader(reviews) {
        if (!reviews || reviews.length === 0) {
            // Set default values when no reviews
            const avgRatingEl = document.querySelector('.rating-big-number');
            if (avgRatingEl) {
                avgRatingEl.textContent = '0.0';
            }

            const countEl = document.querySelector('.rating-count');
            if (countEl) {
                countEl.textContent = 'No reviews yet';
            }

            // Update all breakdown bars to 0%
            const breakdownRows = document.querySelectorAll('.breakdown-row');
            breakdownRows.forEach(row => {
                const fillEl = row.querySelector('.breakdown-fill');
                const percentEl = row.querySelector('.breakdown-percent');
                if (fillEl) fillEl.style.width = '0%';
                if (percentEl) percentEl.textContent = '0%';
            });

            return;
        }

        const stats = calculateStats(reviews);

        // Update the big average rating number
        const avgRatingEl = document.querySelector('.rating-big-number');
        if (avgRatingEl) {
            avgRatingEl.textContent = stats.average;
        }

        // Update the review count text
        const countEl = document.querySelector('.rating-count');
        if (countEl) {
            const reviewText = stats.total === 1 ? 'Review' : 'Reviews';
            countEl.textContent = `Based on ${stats.total}+ Verified ${reviewText}`;
        }

        // Update the star breakdown bars with animation
        const breakdownRows = document.querySelectorAll('.breakdown-row');
        breakdownRows.forEach((row, index) => {
            const starLevel = 5 - index; // 5, 4, 3, 2, 1
            const fillEl = row.querySelector('.breakdown-fill');
            const percentEl = row.querySelector('.breakdown-percent');

            if (fillEl && percentEl) {
                const percentage = stats.percentages[starLevel] || 0;

                // Animate the width
                setTimeout(() => {
                    fillEl.style.width = `${percentage}%`;
                    percentEl.textContent = `${percentage}%`;
                }, index * 100);
            }
        });

        console.log('Rating header updated with real stats:', stats);
    }

    // =========================================
    // CALCULATE AGGREGATE STATS
    // =========================================
    function calculateStats(reviews) {
        const total = reviews.length;
        const sum = reviews.reduce((acc, r) => acc + r.rating, 0);
        const average = (sum / total).toFixed(1);

        const breakdown = {
            5: 0,
            4: 0,
            3: 0,
            2: 0,
            1: 0
        };

        reviews.forEach(r => {
            breakdown[r.rating]++;
        });

        const percentages = {};
        for (let i = 1; i <= 5; i++) {
            percentages[i] = Math.round((breakdown[i] / total) * 100);
        }

        return { average, total, breakdown, percentages };
    }

    // =========================================
    // INITIALIZE ON DOM READY
    // =========================================
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
