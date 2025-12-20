/* =========================================== */
/* TESTIMONIALS SLIDER JAVASCRIPT */
/* SwiperJS implementation matching agafaymarrakech.com */
/* =========================================== */

// ========================================= //
// TESTIMONIALS DATA STRUCTURE
// ========================================= //
const testimonialsData = [
  {
    id: 1,
    name: "Sylvie Bontijnck",
    location: "Belgium",
    review: "Unique and magnificent place that you absolutely must discover. A more than perfect dinner and warm welcome...",
    rating: 5,
    photo: "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face",
    verifiedSource: "TripAdvisor",
    verifiedBooking: "Luxe Pack",
    date: "Dec 2024"
  },
  {
    id: 2,
    name: "Gab de Solages",
    location: "France",
    review: "What an experience! Breathtaking food and quality service. The sunset camel ride was magical.",
    rating: 5,
    photo: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face",
    verifiedSource: "Google",
    verifiedBooking: "Comfort Pack",
    date: "Nov 2024"
  },
  {
    id: 3,
    name: "Hadia Tagaoui",
    location: "Morocco",
    review: "Great service and I really loved it. The quad biking was thrilling and the dinner was delicious!",
    rating: 5,
    photo: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face",
    verifiedSource: "TripAdvisor",
    verifiedBooking: "Basic Pack",
    date: "Dec 2024"
  },
  {
    id: 4,
    name: "Asma El Kebriti",
    location: "Morocco",
    review: "My friends, my daughter and I shared an excellent moment at Agafay. The activities (quad, camel) were perfect and the dinner show was unforgettable!",
    rating: 5,
    photo: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&h=150&fit=crop&crop=face",
    verifiedSource: "Google",
    verifiedBooking: "Comfort Pack",
    date: "Nov 2024"
  },
  {
    id: 5,
    name: "Ahmed Hassan",
    location: "UAE",
    review: "An unforgettable experience in the heart of the Agafay desert. The hospitality was exceptional and the activities were perfectly organized.",
    rating: 5,
    photo: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face",
    verifiedSource: "TripAdvisor",
    verifiedBooking: "Luxe Pack",
    date: "Oct 2024"
  },
  {
    id: 6,
    name: "Maria Rodriguez",
    location: "Spain",
    review: "Magical evening under the stars with authentic Moroccan cuisine. The team made our anniversary celebration truly special.",
    rating: 5,
    photo: "https://images.unsplash.com/photo-1489424731084-a5d8b219a5bb?w=150&h=150&fit=crop&crop=face",
    verifiedSource: "Google",
    verifiedBooking: "Private Dinner",
    date: "Dec 2024"
  }
];

// ========================================= //
// STAR RATING SVG GENERATOR
// ========================================= //
function generateStarRating(rating) {
  const starSVG = `
    <svg class="star-icon" viewBox="0 0 24 24" aria-label="Star rating">
      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
    </svg>
  `;

  let starsHTML = '';
  for (let i = 0; i < 5; i++) {
    starsHTML += starSVG;
  }
  return starsHTML;
}

// ========================================= //
// TESTIMONIAL CARD COMPONENT
// ========================================= //
function createTestimonialCard(testimonial) {
  // Source icon based on platform
  const sourceIcon = testimonial.verifiedSource === 'TripAdvisor'
    ? `<svg viewBox="0 0 24 24" class="source-icon"><circle cx="6.5" cy="12" r="2.5" fill="currentColor"/><circle cx="17.5" cy="12" r="2.5" fill="currentColor"/><path d="M12 4c-4.4 0-8 3.6-8 8h-4l5 5 5-5h-3c0-2.8 2.2-5 5-5s5 2.2 5 5h-3l5 5 5-5h-4c0-4.4-3.6-8-8-8z" fill="currentColor"/></svg>`
    : `<svg viewBox="0 0 24 24" class="source-icon"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg>`;

  return `
    <div class="swiper-slide">
      <div class="testimonial-card" 
           role="article" 
           aria-label="Testimonial from ${testimonial.name}"
           tabindex="0">
        
        <!-- Background Quote Icon -->
        <div class="testimonial-quote-bg" aria-hidden="true">❝</div>
        
        <!-- Quote Icon Badge -->
        <div class="testimonial-quote" aria-hidden="true">"</div>
        
        <!-- Client Avatar -->
        <img src="${testimonial.photo}" 
             alt="${testimonial.name}" 
             class="testimonial-avatar"
             loading="lazy"
             onerror="this.src='https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150&h=150&fit=crop&crop=face'">
        
        <!-- Review Text -->
        <div class="testimonial-review">
          "${testimonial.review}"
        </div>
        
        <!-- Star Rating with Verified Source -->
        <div class="testimonial-rating-row">
          <div class="testimonial-rating" 
               role="img" 
               aria-label="${testimonial.rating} out of 5 stars">
            ${generateStarRating(testimonial.rating)}
          </div>
          <div class="testimonial-source">
            ${sourceIcon}
            <span>via ${testimonial.verifiedSource}</span>
          </div>
        </div>
        
        <!-- Client Information -->
        <div class="testimonial-client">
          <div class="testimonial-name">${testimonial.name}</div>
          <div class="testimonial-location">${testimonial.location}</div>
          <!-- Verified Booking Badge -->
          <div class="testimonial-verified">
            <svg viewBox="0 0 24 24" class="verified-icon"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" fill="currentColor"/></svg>
            Verified Booking: ${testimonial.verifiedBooking}
          </div>
        </div>
        
        <!-- Date -->
        <div class="testimonial-date">${testimonial.date}</div>
      </div>
    </div>
  `;
}

// ========================================= //
// SWIPER INITIALIZATION
// ========================================= //
function initTestimonialsSwiper() {
  console.log('Initializing testimonials swiper...');

  // Check if Swiper is loaded
  if (typeof Swiper === 'undefined') {
    console.error('Swiper library not loaded. Please include Swiper CSS and JS files.');
    return;
  }
  console.log('Swiper library loaded successfully');

  // Generate testimonial cards
  const swiperWrapper = document.querySelector('.testimonials-swiper .swiper-wrapper');
  if (!swiperWrapper) {
    console.error('Testimonials swiper wrapper not found');
    return;
  }
  console.log('Swiper wrapper found');

  // Clear existing content and add testimonials
  swiperWrapper.innerHTML = '';
  testimonialsData.forEach(testimonial => {
    swiperWrapper.innerHTML += createTestimonialCard(testimonial);
  });
  console.log(`Added ${testimonialsData.length} testimonials to slider`);

  // Initialize Swiper with simplified configuration
  const testimonialsSwiper = new Swiper('.testimonials-swiper', {
    // Basic Configuration
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    speed: 400,

    // Responsive Breakpoints
    slidesPerView: 1,
    spaceBetween: 30,
    breakpoints: {
      1024: {
        slidesPerView: 2,
        spaceBetween: 40
      }
    },

    // Navigation
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    // Pagination
    pagination: {
      el: '.swiper-pagination',
      clickable: true
    },

    // Touch/Swipe Settings
    grabCursor: true,

    // Events
    on: {
      init: function () {
        console.log('Testimonials slider initialized');
        // Add ARIA labels to navigation
        this.navigation.nextEl.setAttribute('aria-label', 'Next testimonial');
        this.navigation.prevEl.setAttribute('aria-label', 'Previous testimonial');
      },

      slideChange: function () {
        // Update active slide accessibility
        const activeSlide = this.slides[this.activeIndex];
        if (activeSlide) {
          activeSlide.setAttribute('aria-current', 'true');
        }

        // Remove aria-current from other slides
        this.slides.forEach((slide, index) => {
          if (index !== this.activeIndex) {
            slide.removeAttribute('aria-current');
          }
        });
      },

      reachEnd: function () {
        console.log('Reached last testimonial');
      },

      reachBeginning: function () {
        console.log('Reached first testimonial');
      }
    }
  });

  // ========================================= //
  // KEYBOARD NAVIGATION ENHANCEMENT
  // ========================================= //
  document.addEventListener('keydown', function (e) {
    if (!testimonialsSwiper) return;

    // Only handle keyboard events when testimonials section is in focus
    const testimonialsSection = document.querySelector('.testimonials-section');
    if (!testimonialsSection.contains(document.activeElement)) return;

    switch (e.key) {
      case 'ArrowLeft':
        e.preventDefault();
        testimonialsSwiper.slidePrev();
        break;
      case 'ArrowRight':
        e.preventDefault();
        testimonialsSwiper.slideNext();
        break;
      case 'Home':
        e.preventDefault();
        testimonialsSwiper.slideTo(0);
        break;
      case 'End':
        e.preventDefault();
        testimonialsSwiper.slideTo(testimonialsSwiper.slides.length - 1);
        break;
    }
  });

  // ========================================= //
  // TOUCH/SWIPE ENHANCEMENTS FOR MOBILE
  // ========================================= //
  let touchStartX = 0;
  let touchEndX = 0;

  const handleTouchStart = (e) => {
    touchStartX = e.changedTouches[0].screenX;
  };

  const handleTouchEnd = (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  };

  const handleSwipe = () => {
    const swipeThreshold = 50;
    const diff = touchStartX - touchEndX;

    if (Math.abs(diff) > swipeThreshold) {
      if (diff > 0) {
        // Swipe left - next slide
        testimonialsSwiper.slideNext();
      } else {
        // Swipe right - previous slide
        testimonialsSwiper.slidePrev();
      }
    }
  };

  // Add touch listeners to testimonials section
  const testimonialsSection = document.querySelector('.testimonials-section');
  if (testimonialsSection) {
    testimonialsSection.addEventListener('touchstart', handleTouchStart, { passive: true });
    testimonialsSection.addEventListener('touchend', handleTouchEnd, { passive: true });
  }

  return testimonialsSwiper;
}

// ========================================= //
// INITIALIZATION
// ========================================= //
document.addEventListener('DOMContentLoaded', function () {
  console.log('DOM loaded, initializing testimonials...');

  // Wait a bit for all resources to load
  setTimeout(() => {
    window.testimonialsSwiper = initTestimonialsSwiper();
  }, 500);
});

// Also try to initialize when window loads (fallback)
window.addEventListener('load', function () {
  if (!window.testimonialsSwiper) {
    console.log('Window loaded, trying to initialize testimonials...');
    setTimeout(() => {
      window.testimonialsSwiper = initTestimonialsSwiper();
    }, 100);
  }
});

// ========================================= //
// UTILITY FUNCTIONS
// ========================================= //

// Refresh testimonials (useful for dynamic content updates)
function refreshTestimonials() {
  if (window.testimonialsSwiper) {
    window.testimonialsSwiper.destroy(true, true);
    window.testimonialsSwiper = initTestimonialsSwiper();
  }
}

// Add new testimonial dynamically
function addTestimonial(testimonial) {
  testimonialsData.push(testimonial);
  refreshTestimonials();
}

// Update testimonial data
function updateTestimonialsData(newData) {
  testimonialsData.length = 0;
  testimonialsData.push(...newData);
  refreshTestimonials();
}

// Manual initialization function for debugging
window.initTestimonials = function () {
  console.log('Manual initialization called...');
  if (window.testimonialsSwiper) {
    window.testimonialsSwiper.destroy(true, true);
  }
  window.testimonialsSwiper = initTestimonialsSwiper();
  return window.testimonialsSwiper;
};

// Export functions for external use
window.TestimonialsSlider = {
  refresh: refreshTestimonials,
  addTestimonial: addTestimonial,
  updateData: updateTestimonialsData,
  getData: () => [...testimonialsData],
  init: window.initTestimonials
};
