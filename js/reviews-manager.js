/**
 * Reviews Page Manager
 * Handles filtering, loading, and submission of reviews
 * Integrates with Supabase for data persistence
 */

(function () {
    'use strict';

    // =========================================
    // SAMPLE REVIEWS DATA
    // In production, this would be fetched from Supabase
    // =========================================
    const sampleReviews = [
        {
            id: 1,
            name: 'Sarah Jenkins',
            location: 'London, UK',
            rating: 5,
            text: 'A truly magical experience! The camel ride at sunset was breathtaking, and the dinner show was the perfect end to the day. The staff went above and beyond to make our visit unforgettable. Highly recommended for anyone visiting Marrakech!',
            date: '2025-12-19',
            verified: true,
            photo: null
        },
        {
            id: 2,
            name: 'Marc Dubois',
            location: 'Paris, France',
            rating: 5,
            text: 'Professional guides and top-notch equipment. The quad biking was thrilling but felt very safe. Will definitely come back!',
            date: '2025-12-18',
            verified: true,
            photo: null
        },
        {
            id: 3,
            name: 'Emma Wilson',
            location: 'New York, USA',
            rating: 5,
            text: 'Best desert experience ever! The sunset was incredible and the traditional dinner exceeded all expectations. The entire team was so welcoming and professional.',
            date: '2025-12-17',
            verified: true,
            photo: 'images/activites/camel.jpg'
        },
        {
            id: 4,
            name: 'Hassan Ahmed',
            location: 'Dubai, UAE',
            rating: 4,
            text: 'Great value for money. The buggy tour was fantastic and our guide Mohammed was very knowledgeable about the area.',
            date: '2025-12-16',
            verified: true,
            photo: null
        },
        {
            id: 5,
            name: 'Sylvie Bontijnck',
            location: 'Belgium',
            rating: 5,
            text: 'Unique and magnificent place that you absolutely must discover. A more than perfect dinner and warm welcome! The atmosphere under the stars was pure magic.',
            date: '2025-12-14',
            verified: true,
            photo: null
        },
        {
            id: 6,
            name: 'Gab de Solages',
            location: 'France',
            rating: 5,
            text: 'What an experience! Breathtaking food and quality service. The staff made us feel like royalty.',
            date: '2025-12-12',
            verified: true,
            photo: 'images/activites/quad.jpeg'
        },
        {
            id: 7,
            name: 'Lisa Müller',
            location: 'Berlin, Germany',
            rating: 5,
            text: 'Perfect romantic getaway! The hot air balloon at sunrise followed by a champagne breakfast was unforgettable. We celebrated our anniversary here and it was the best decision ever!',
            date: '2025-12-10',
            verified: true,
            photo: 'images/activites/hote-aire.jpeg'
        },
        {
            id: 8,
            name: 'Carlos Rivera',
            location: 'Madrid, Spain',
            rating: 4,
            text: 'Amazing desert adventure. The quad biking was exhilarating and the staff were incredibly friendly.',
            date: '2025-12-08',
            verified: true,
            photo: null
        },
        {
            id: 9,
            name: 'Yuki Tanaka',
            location: 'Tokyo, Japan',
            rating: 5,
            text: 'A once-in-a-lifetime experience. The camel trek through the desert at sunset was absolutely magical. Everything was perfectly organized from pickup to drop-off.',
            date: '2025-12-06',
            verified: true,
            photo: null
        },
        {
            id: 10,
            name: 'Anna Kowalski',
            location: 'Warsaw, Poland',
            rating: 5,
            text: 'Exceeded all expectations! The dinner show was entertaining and the food was authentic Moroccan cuisine.',
            date: '2025-12-04',
            verified: true,
            photo: 'images/activites/show.jpeg'
        }
    ];

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
    function loadReviews() {
        const reviews = sampleReviews;
        reviewsContainer.innerHTML = '';

        reviews.forEach((review, index) => {
            const card = createReviewCard(review);
            card.style.animationDelay = `${index * 0.1}s`;
            reviewsContainer.appendChild(card);
        });

        displayedReviews = reviews.length;
        updateLoadMoreButton();
    }

    function createReviewCard(review) {
        const card = document.createElement('div');
        card.className = 'review-card fade-in';
        card.dataset.rating = review.rating;
        card.dataset.hasPhoto = review.photo ? 'true' : 'false';

        // Generate avatar HTML - Always use initials with brand identity gold
        const initials = review.name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase();
        const bgColor = getAvatarColor();
        const avatarHTML = `<div class="review-avatar-placeholder" style="background: ${bgColor};">${initials}</div>`;

        // Generate stars HTML
        const starsHTML = generateStarsHTML(review.rating);

        // Generate photo HTML with 16:9 aspect ratio container
        const photoHTML = review.photo
            ? `<div class="review-photo-container"><img src="${review.photo}" alt="Review photo" class="review-photo" loading="lazy"></div>`
            : '';

        // Format date (relative time)
        const formattedDate = formatRelativeDate(review.date);

        // Check if review text is long (needs Read More)
        const maxLength = 120;
        const isLongReview = review.text.length > maxLength;
        const displayText = isLongReview ? review.text.substring(0, maxLength) + '...' : review.text;
        const readMoreHTML = isLongReview ? `<a href="javascript:void(0)" class="read-more-link" data-full-text="${review.text.replace(/"/g, '&quot;')}">Read More</a>` : '';

        card.innerHTML = `
      <div class="review-card-header">
        ${avatarHTML}
        <div class="review-author-info">
          <h4 class="review-author-name">${review.name}</h4>
          <div class="review-author-meta">
            <span class="review-author-location">${review.location}</span>
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
                // Prepare photo URLs array (in production, these would be uploaded to storage first)
                let photoUrls = [];
                if (photos && photos.length > 0) {
                    // In production: Upload to Supabase Storage and get URLs
                    // For now, we'll prepare the file names for submission
                    for (let i = 0; i < photos.length; i++) {
                        photoUrls.push(photos[i].name);
                    }
                    console.log('Photos to upload:', photoUrls);
                }

                // Submit to Supabase with pending status
                const reviewData = {
                    name: name,
                    rating: selectedRating,
                    text: comment,
                    status: 'pending', // Awaiting dashboard approval
                    date: new Date().toISOString().split('T')[0],
                    verified: false,
                    photo: photoUrls.length > 0 ? photoUrls[0] : null, // First photo as primary
                    photos: photoUrls, // All photos array
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
