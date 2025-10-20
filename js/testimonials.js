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
    photo: "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face"
  },
  {
    id: 2,
    name: "Gab de Solages",
    location: "France", 
    review: "What an experience! Breathtaking food and quality service...",
    rating: 5,
    photo: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face"
  },
  {
    id: 3,
    name: "Hadia Tagaoui",
    location: "Morocco",
    review: "Great service and I really loved it. I recommend it, lots of...",
    rating: 5,
    photo: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face"
  },
  {
    id: 4,
    name: "Asma El Kebriti",
    location: "Morocco",
    review: "Hello, My friends, my daughter and I shared an excellent moment at Agafay from pickup at our residence, for the activities done on site (quad, camel) everything was perfect and the dinner show in the...",
    rating: 5,
    photo: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&h=150&fit=crop&crop=face"
  },
  {
    id: 5,
    name: "Ahmed Hassan",
    location: "UAE",
    review: "An unforgettable experience in the heart of the Agafay desert. The hospitality was exceptional and the activities were perfectly organized.",
    rating: 5,
    photo: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face"
  },
  {
    id: 6,
    name: "Maria Rodriguez",
    location: "Spain",
    review: "Magical evening under the stars with authentic Moroccan cuisine. The team made our anniversary celebration truly special.",
    rating: 5,
    photo: "https://images.unsplash.com/photo-1489424731084-a5d8b219a5bb?w=150&h=150&fit=crop&crop=face"
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
  return `
    <div class="swiper-slide">
      <div class="testimonial-card" 
           role="article" 
           aria-label="Testimonial from ${testimonial.name}"
           tabindex="0">
        
        <!-- Quote Icon -->
        <div class="testimonial-quote" aria-hidden="true">"</div>
        
        <!-- Client Avatar -->
        <img src="${testimonial.photo}" 
             alt="${testimonial.name}" 
             class="testimonial-avatar"
             loading="lazy"
             onerror="this.src='images/testimonials/default-avatar.jpg'">
        
        <!-- Review Text -->
        <div class="testimonial-review">
          "${testimonial.review}"
        </div>
        
        <!-- Star Rating -->
        <div class="testimonial-rating" 
             role="img" 
             aria-label="${testimonial.rating} out of 5 stars">
          ${generateStarRating(testimonial.rating)}
        </div>
        
        <!-- Client Information -->
        <div class="testimonial-client">
          <div class="testimonial-name">${testimonial.name}</div>
          <div class="testimonial-location">${testimonial.location}</div>
        </div>
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
      init: function() {
        console.log('Testimonials slider initialized');
        // Add ARIA labels to navigation
        this.navigation.nextEl.setAttribute('aria-label', 'Next testimonial');
        this.navigation.prevEl.setAttribute('aria-label', 'Previous testimonial');
      },
      
      slideChange: function() {
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
      
      reachEnd: function() {
        console.log('Reached last testimonial');
      },
      
      reachBeginning: function() {
        console.log('Reached first testimonial');
      }
    }
  });

  // ========================================= //
  // KEYBOARD NAVIGATION ENHANCEMENT
  // ========================================= //
  document.addEventListener('keydown', function(e) {
    if (!testimonialsSwiper) return;
    
    // Only handle keyboard events when testimonials section is in focus
    const testimonialsSection = document.querySelector('.testimonials-section');
    if (!testimonialsSection.contains(document.activeElement)) return;
    
    switch(e.key) {
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
document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM loaded, initializing testimonials...');
  
  // Wait a bit for all resources to load
  setTimeout(() => {
    window.testimonialsSwiper = initTestimonialsSwiper();
  }, 500);
});

// Also try to initialize when window loads (fallback)
window.addEventListener('load', function() {
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
window.initTestimonials = function() {
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
