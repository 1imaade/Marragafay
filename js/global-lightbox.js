/**
 * Global Lightbox System
 * Reusable full-screen image viewer with navigation
 * Works for both dynamic (Reviews) and static (Home/Details/Packs) galleries
 */

// =========================================
// GLOBAL LIGHTBOX STATE
// =========================================

let currentLightboxImages = [];
let currentLightboxIndex = 0;

// =========================================
// CORE LIGHTBOX FUNCTIONS
// =========================================

/**
 * Opens the lightbox with the given image(s)
 * @param {string|array} imagesOrSrc - Either a single image URL or an array of URLs
 * @param {number} index - The starting index (default 0)
 */
function openLightbox(imagesOrSrc, index = 0) {
    const lightbox = document.getElementById('image-lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const prevBtn = document.getElementById('lightbox-prev');
    const nextBtn = document.getElementById('lightbox-next');

    if (!lightbox || !lightboxImg) return;

    // Convert single image to array format
    if (typeof imagesOrSrc === 'string') {
        currentLightboxImages = [imagesOrSrc];
        currentLightboxIndex = 0;
    } else {
        currentLightboxImages = Array.isArray(imagesOrSrc) ? imagesOrSrc : [imagesOrSrc];
        currentLightboxIndex = (index >= 0 && index < currentLightboxImages.length) ? index : 0;
    }

    // Set the current image
    lightboxImg.src = currentLightboxImages[currentLightboxIndex];
    lightbox.style.display = 'flex';
    lightbox.classList.add('active');

    // Show/hide navigation arrows based on image count
    if (prevBtn && nextBtn) {
        if (currentLightboxImages.length <= 1) {
            prevBtn.classList.add('hidden');
            nextBtn.classList.add('hidden');
        } else {
            prevBtn.classList.remove('hidden');
            nextBtn.classList.remove('hidden');
        }
    }

    // Prevent body scroll when lightbox is open
    document.body.style.overflow = 'hidden';
}

/**
 * Changes the current lightbox image
 * @param {number} step - Direction to move (-1 for previous, 1 for next)
 */
function changeLightboxImage(step) {
    if (!currentLightboxImages || currentLightboxImages.length === 0) return;

    // Calculate new index with looping
    currentLightboxIndex += step;

    // Loop around if out of bounds
    if (currentLightboxIndex < 0) {
        currentLightboxIndex = currentLightboxImages.length - 1;
    } else if (currentLightboxIndex >= currentLightboxImages.length) {
        currentLightboxIndex = 0;
    }

    // Update the image
    const lightboxImg = document.getElementById('lightbox-img');
    if (lightboxImg) {
        lightboxImg.src = currentLightboxImages[currentLightboxIndex];
    }

    // Stop event propagation to prevent closing
    if (typeof event !== 'undefined' && event && event.stopPropagation) {
        event.stopPropagation();
    }
}

/**
 * Closes the lightbox
 */
function closeLightbox() {
    const lightbox = document.getElementById('image-lightbox');

    if (lightbox) {
        lightbox.classList.remove('active');
        lightbox.style.display = 'none';
        // Restore body scroll
        document.body.style.overflow = '';
        // Clear state
        currentLightboxImages = [];
        currentLightboxIndex = 0;
    }
}

// =========================================
// STATIC GALLERY AUTO-INITIALIZATION
// =========================================

/**
 * Initializes lightbox for static HTML galleries
 * Automatically attaches click handlers to all images in a container
 * @param {string} containerSelector - CSS selector for the gallery container
 */
function initStaticGallery(containerSelector) {
    const containers = document.querySelectorAll(containerSelector);

    containers.forEach(container => {
        // Prevent duplicate initialization
        if (container.dataset.lightboxInitialized === 'true') return;

        // Find all images in this container
        const images = container.querySelectorAll('img');

        if (images.length === 0) return;

        container.dataset.lightboxInitialized = 'true';

        // Build array of image URLs
        const imageUrls = Array.from(images).map(img => img.src || img.getAttribute('src'));

        // Attach click handler to each image
        images.forEach((img, index) => {
            img.style.cursor = 'pointer';
            img.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();
                openLightbox(imageUrls, index);
            });
        });
    });
}

/**
 * Initializes lightbox for Owl Carousel galleries
 * Special handling for carousel items
 * @param {string} carouselSelector - CSS selector for the carousel
 */
function initCarouselGallery(carouselSelector) {
    const carousel = document.querySelector(carouselSelector);
    if (!carousel) return;

    if (carousel.dataset.lightboxInitialized === 'true') return;

    // Find all images in carousel items
    const items = carousel.querySelectorAll('.owl-item:not(.cloned) img');

    if (items.length === 0) return;

    carousel.dataset.lightboxInitialized = 'true';

    // Build array of image URLs
    const imageUrls = Array.from(items).map(img => img.src || img.getAttribute('src'));

    // Attach click handler to ALL images (including clones)
    const allImages = carousel.querySelectorAll('img');
    allImages.forEach((img) => {
        img.style.cursor = 'pointer';
        img.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            // Find original index (in case of cloned items)
            const clickedSrc = img.src || img.getAttribute('src');
            const originalIndex = imageUrls.indexOf(clickedSrc);
            if (originalIndex !== -1) {
                openLightbox(imageUrls, originalIndex);
            } else {
                openLightbox(imageUrls, 0);
            }
        });
    });
}

// =========================================
// PAGE-READY INITIALIZATION
// =========================================

document.addEventListener('DOMContentLoaded', function () {
    const lightbox = document.getElementById('image-lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const prevBtn = document.getElementById('lightbox-prev');
    const nextBtn = document.getElementById('lightbox-next');

    // Prevent image and arrow clicks from closing lightbox
    if (lightboxImg) {
        lightboxImg.addEventListener('click', function (e) {
            e.stopPropagation();
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', function (e) {
            e.stopPropagation();
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function (e) {
            e.stopPropagation();
        });
    }

    // Touch / Swipe support for mobile lightbox navigation
    if (lightbox) {
        let touchStartX = 0;
        let touchStartY = 0;
        let touchMoved = false;

        lightbox.addEventListener('touchstart', function (e) {
            if (e.touches && e.touches.length > 0) {
                touchStartX = e.touches[0].clientX;
                touchStartY = e.touches[0].clientY;
                touchMoved = false;
            }
        }, { passive: true });

        lightbox.addEventListener('touchmove', function (e) {
            if (!touchStartX || !touchStartY || !e.touches || e.touches.length === 0) return;
            const diffX = Math.abs(e.touches[0].clientX - touchStartX);
            const diffY = Math.abs(e.touches[0].clientY - touchStartY);
            if (diffX > diffY && diffX > 10) {
                touchMoved = true;
            }
        }, { passive: true });

        lightbox.addEventListener('touchend', function (e) {
            if (!touchMoved || !e.changedTouches || e.changedTouches.length === 0) {
                touchStartX = 0;
                touchStartY = 0;
                touchMoved = false;
                return;
            }
            const touchEndX = e.changedTouches[0].clientX;
            const touchEndY = e.changedTouches[0].clientY;
            const diffX = touchStartX - touchEndX;
            const diffY = touchStartY - touchEndY;

            if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 40) {
                if (diffX > 0) {
                    changeLightboxImage(1);  // Swipe left -> next image
                } else {
                    changeLightboxImage(-1); // Swipe right -> prev image
                }
            }
            touchStartX = 0;
            touchStartY = 0;
            touchMoved = false;
        }, { passive: true });
    }

    // Keyboard navigation
    document.addEventListener('keydown', function (e) {
        if (currentLightboxImages.length === 0) return;

        if (e.key === 'ArrowLeft') {
            changeLightboxImage(-1);  // Previous
        } else if (e.key === 'ArrowRight') {
            changeLightboxImage(1);   // Next
        } else if (e.key === 'Escape') {
            closeLightbox();
        }
    });

    // Auto-init static galleries if present on the page
    setTimeout(function () {
        initStaticGallery('.gallery-section');
        initStaticGallery('#experience-gallery');
    }, 100);
});
