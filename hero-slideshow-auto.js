// ========================================
// HERO SLIDESHOW - AUTO-CYCLING WITH MANUAL CONTROL
// ========================================
// Features: Auto-advance every 6-8 seconds, Touch/Swipe, Image preloading, Smooth crossfade
// AUTO-ADVANCE ENABLED: Slides cycle automatically + manual controls available
// SLIDE COUNTER REMOVED: No "(4/4)" indicator displayed

(function () {
  'use strict';

  // ========================================
  // CONFIGURATION - ADJUST SLIDESHOW SPEED HERE
  // ========================================
  const AUTO_ADVANCE_INTERVAL = 7000; // Milliseconds between auto-advances (7 seconds = 7000ms)
  // Change to 6000 for 6 seconds, 8000 for 8 seconds, etc.

  const TRANSITION_DURATION = 600; // Fade transition duration in milliseconds (400-700ms recommended)

  // SLIDE DATA - Add/edit slides here
  // Each slide has: image, headline (with HTML), subtitle (marketing text)
  // TEXT-IMAGE SYNC: When image changes, headline and subtitle update together
  const heroSlides = [
    {
      image: 'images/Slider-images/slider-1.jpeg',
      headline: 'AGAFAY DESERT<br><span style="color: #cfbda5; font-weight: 400;">EXPERIENCE</span>',
      subtitle: 'Discover the authentic essence of the Moroccan desert in a setting of exceptional luxury'
    },
    {
      image: 'images/Slider-images/slider-2.jpg',
      headline: 'SUNSET CAMEL<br><span style="color: #cfbda5; font-weight: 400;">RIDES</span>',
      subtitle: 'Experience the authentic Agafay adventure as golden hour illuminates the desert dunes'
    },
    {
      image: 'images/Slider-images/slider-3.jpg',
      headline: 'LUXURY CAMP<br><span style="color: #cfbda5; font-weight: 400;">NIGHTS</span>',
      subtitle: 'Comfort meets wilderness under a blanket of stars in our premium desert accommodations'
    },
    {
      image: 'images/Slider-images/slider-4.jpeg',
      headline: 'EXCLUSIVE DESERT<br><span style="color: #cfbda5; font-weight: 400;">DINING</span>',
      subtitle: 'Savor traditional Moroccan cuisine in an unforgettable open-air setting'
    }
  ];

  let currentSlide = 0;
  let isTransitioning = false;
  let touchStartX = 0;
  let touchEndX = 0;
  let autoAdvanceTimer = null; // Timer for auto-cycling

  // Get DOM elements
  const bgImage = document.querySelector('.hero-bg-image');
  const contentWrapper = document.querySelector('.hero-content-wrapper');
  const headline = document.querySelector('.hero-headline');
  const subtitle = document.querySelector('.hero-subtitle');
  const leftArrow = document.querySelector('.hero-nav-left');
  const rightArrow = document.querySelector('.hero-nav-right');
  const dotsContainer = document.querySelector('.hero-dots-container');
  const heroWrap = document.querySelector('.hero-wrap');

  // Preload all images for smooth transitions
  function preloadImages() {
    heroSlides.forEach(slide => {
      const img = new Image();
      img.src = slide.image;
    });
  }

  // Initialize slideshow
  function init() {
    // Preload images
    preloadImages();

    // Set initial background
    bgImage.style.backgroundImage = `linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('${heroSlides[0].image}')`;

    // Create luxury navigation dots
    heroSlides.forEach((slide, index) => {
      const dot = document.createElement('button');
      dot.className = 'hero-dot';
      dot.setAttribute('data-slide', index);
      dot.setAttribute('aria-label', `Go to slide ${index + 1}`);
      dot.style.cssText = `
        width: ${index === 0 ? '28px' : '10px'};
        height: 10px;
        border-radius: 5px;
        border: 1px solid rgba(207, 189, 165, 0.5);
        background: ${index === 0 ? 'rgba(207, 189, 165, 0.9)' : 'rgba(207, 189, 165, 0.2)'};
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        padding: 0;
      `;
      dot.addEventListener('click', () => {
        goToSlide(index);
        resetAutoAdvance(); // Reset timer when user clicks
      });
      dotsContainer.appendChild(dot);
    });

    // Arrow button interactions
    leftArrow.addEventListener('click', () => {
      prevSlide();
      resetAutoAdvance(); // Reset timer when user clicks
    });
    rightArrow.addEventListener('click', () => {
      nextSlide();
      resetAutoAdvance(); // Reset timer when user clicks
    });

    // Keyboard navigation
    document.addEventListener('keydown', handleKeyboard);

    // Touch/Swipe support for mobile
    heroWrap.addEventListener('touchstart', handleTouchStart, { passive: true });
    heroWrap.addEventListener('touchend', handleTouchEnd, { passive: true });

    // START AUTO-ADVANCE SLIDESHOW
    startAutoAdvance();
  }

  // ========================================
  // AUTO-ADVANCE FUNCTIONS
  // ========================================

  // Start automatic slideshow cycling
  function startAutoAdvance() {
    autoAdvanceTimer = setInterval(() => {
      const nextIndex = (currentSlide + 1) % heroSlides.length;
      goToSlide(nextIndex);
    }, AUTO_ADVANCE_INTERVAL);
  }

  // Reset auto-advance timer (called when user manually navigates)
  function resetAutoAdvance() {
    clearInterval(autoAdvanceTimer);
    startAutoAdvance();
  }

  // Enhanced slide transition with crossfade effect
  // TEXT-IMAGE SYNC: Headline and subtitle update together with image
  function goToSlide(index) {
    if (isTransitioning || index === currentSlide) return;
    isTransitioning = true;

    // Smooth fade out (content disappears)
    contentWrapper.style.opacity = '0';
    contentWrapper.style.transform = 'translateY(10px)';

    // Update content at mid-transition (while faded out)
    setTimeout(() => {
      // UPDATE TEXT CONTENT - SYNCED WITH IMAGE
      // Headline updates with per-slide marketing text
      headline.innerHTML = heroSlides[index].headline;
      // Subtitle updates with per-slide marketing description
      subtitle.textContent = heroSlides[index].subtitle;

      // Update background image (crossfade effect)
      bgImage.style.backgroundImage = `linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('${heroSlides[index].image}')`;

      // Update dots with elegant animation
      const dots = document.querySelectorAll('.hero-dot');
      dots.forEach((dot, i) => {
        if (i === index) {
          dot.style.width = '28px';
          dot.style.background = 'rgba(207, 189, 165, 0.9)';
        } else {
          dot.style.width = '10px';
          dot.style.background = 'rgba(207, 189, 165, 0.2)';
        }
      });

      // NOTE: Slide counter removed - no "(4/4)" displayed per requirements
      // To restore counter, uncomment: slideCounter.textContent = index + 1;

      // Smooth fade in (content reappears)
      requestAnimationFrame(() => {
        contentWrapper.style.opacity = '1';
        contentWrapper.style.transform = 'translateY(0)';
      });

      currentSlide = index;

      // Release transition lock
      setTimeout(() => {
        isTransitioning = false;
      }, 400);
    }, TRANSITION_DURATION / 2); // Mid-transition timing
  }

  // Navigation functions
  function nextSlide() {
    const nextIndex = (currentSlide + 1) % heroSlides.length;
    goToSlide(nextIndex);
  }

  function prevSlide() {
    const prevIndex = (currentSlide - 1 + heroSlides.length) % heroSlides.length;
    goToSlide(prevIndex);
  }

  // Keyboard navigation handler
  function handleKeyboard(e) {
    if (e.key === 'ArrowLeft' || e.key === 'Left') {
      prevSlide();
      resetAutoAdvance();
    } else if (e.key === 'ArrowRight' || e.key === 'Right') {
      nextSlide();
      resetAutoAdvance();
    }
  }

  // Touch/Swipe handlers for mobile luxury UX
  function handleTouchStart(e) {
    touchStartX = e.changedTouches[0].screenX;
  }

  function handleTouchEnd(e) {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  }

  function handleSwipe() {
    const swipeThreshold = 50; // Minimum swipe distance
    const diff = touchStartX - touchEndX;

    if (Math.abs(diff) > swipeThreshold) {
      if (diff > 0) {
        // Swipe left - next slide
        nextSlide();
      } else {
        // Swipe right - previous slide
        prevSlide();
      }
      resetAutoAdvance();
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Cleanup on page unload
  window.addEventListener('beforeunload', () => {
    clearInterval(autoAdvanceTimer);
    document.removeEventListener('keydown', handleKeyboard);
  });
})();
