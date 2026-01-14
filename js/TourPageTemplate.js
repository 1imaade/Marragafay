/**
 * Master Tour Page Template
 * Simulates a React Component for Static HTML Site
 * 
 * usage:
 * TourPageTemplate.render({
 *   title: "String",
 *   ...
 * }, 'page-root');
 */

const TourPageTemplate = (function () {

  const styles = `
      /* Global Typography - Matching Homepage */
      body { font-family: "Overpass", "Open Sans", sans-serif; font-size: 16px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); background-color: #fcfbf7; }
      
      :root {
        --color-gold: #bc6c25;
        --color-gold-light: #d4af37;
        --color-dark: #1a365d;
        --color-text: #4a5568;
        --color-bg-light: #f8f9fa;
        --color-white: #ffffff;
        --shadow-soft: 0 10px 40px -10px rgba(0,0,0,0.08);
        --shadow-hover: 0 20px 50px -10px rgba(0,0,0,0.12);
        --radius-xl: 16px;
        --radius-lg: 12px;
      }

      .font-serif { font-family: "EB Garamond", serif; }
      .font-sans { font-family: "Open Sans", sans-serif; }

      /* Hero Utilities (Refactor) */
      .relative { position: relative; }
      .absolute { position: absolute; }
      .inset-0 { top: 0; left: 0; right: 0; bottom: 0; }
      .h-full { height: 100%; }
      .w-full { width: 100%; }
      .object-cover { object-fit: cover; }
      .z-10 { z-index: 10; }
      .flex { display: flex; }
      .flex-col { flex-direction: column; }
      .items-center { align-items: center; }
      .justify-center { justify-content: center; }
      .text-center { text-align: center; }
      .hero-container { height: 60vh; min-height: 400px; }
      .bg-black-40 { background-color: rgba(0,0,0,0.4); }
      .hero-blur-overlay {
        background: linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.6));
        backdrop-filter: blur(3px);
        box-shadow: inset 0 0 100px rgba(0,0,0,0.5);
      }
      .text-white { color: white !important; }

      .font-serif { font-family: "EB Garamond", serif; }
      .font-sans { font-family: "Open Sans", sans-serif; }

      /* Navbar Dynamic Styles */
      .navbar-transition { transition: background-color 0.3s ease-in-out, backdrop-filter 0.3s ease-in-out; }
      .bg-transparent-custom { background-color: transparent !important; box-shadow: none !important; }
      .bg-black-custom { background-color: rgba(0, 0, 0, 0.9) !important; backdrop-filter: blur(10px); box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1); }

      /* Hero Utilities (Refactor) */
      .pack-detail-container { max-width: 1280px; margin: 40px auto 80px; padding: 0 20px; display: grid; grid-template-columns: 65% 35%; gap: 40px; align-items: start; }
      @media (max-width: 991px) { .pack-detail-container { grid-template-columns: 1fr; } .pack-sidebar { order: 1; } }

      /* Header */
      .pack-header { margin-bottom: 40px; border-bottom: 1px solid #eee; padding-bottom: 30px; }
      .rating-badge { display: inline-flex; align-items: center; background: #fff8e1; color: #b7860b; padding: 6px 12px; border-radius: 20px; font-weight: 600; font-size: 0.9rem; margin-bottom: 15px; }
      .pack-title { font-family: "EB Garamond", serif; font-size: 3.5rem; line-height: 1.1; color: var(--color-dark); margin-bottom: 20px; }
      .highlights-row { display: flex; flex-wrap: wrap; gap: 20px; margin-top: 25px; }
      .highlight-item { display: flex; align-items: center; gap: 8px; font-size: 0.95rem; color: var(--color-text); background: #ffffff; padding: 8px 16px; border: 1px solid #eee; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }

      /* Timeline */
      .section-title { font-family: "EB Garamond", serif; font-size: 2rem; color: var(--color-dark); margin-bottom: 25px; margin-top: 50px; }
      .timeline-container { position: relative; padding-left: 60px; margin: 40px 0; }
      .timeline-container::before { content: ''; position: absolute; left: 35px; top: 0; bottom: 40px; width: 2px; background: #e0e0e0; }
      .timeline-line { display: none; } /* Hide old line element, using ::before now */
      .timeline-item { position: relative; padding-bottom: 40px; }
      .timeline-item:last-child { padding-bottom: 0; }
      .timeline-item:last-child::after { content: ''; position: absolute; left: -45px; top: 40px; bottom: 0; width: 2px; background: transparent; } /* Ensures line doesn't extend past last icon */
      .timeline-icon { position: absolute; left: -45px; top: 0; width: 40px; height: 40px; background: var(--color-gold); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; z-index: 2; box-shadow: 0 0 0 4px #fcfbf7; }
      .timeline-content h4 { font-family: "EB Garamond", serif; font-size: 1.4rem; color: var(--color-dark); margin-bottom: 5px; }
      .timeline-content p { color: #444; font-weight: 450; line-height: 1.6; margin-bottom: 0; }

      /* Inclusions */
      .inclusions-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; background: #ffffff; padding: 30px; padding-left: 25px; border-radius: var(--radius-lg); border: 1px solid #edf2f7; box-shadow: 0 2px 10px rgba(0,0,0,0.02); }
      .check-list { padding-left: 0; }
      .check-list li { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; font-size: 1rem; white-space: nowrap; }
      .check-list li svg { flex-shrink: 0; color: #22c55e; }
      
      /* Gallery - Column Masonry Layout (No Cropping, Sharp Corners) */
      .masonry-grid { 
        columns: 1; 
        column-gap: 15px; 
        margin-bottom: 40px; 
      }
      @media (min-width: 640px) { .masonry-grid { columns: 2; } }
      @media (min-width: 1024px) { .masonry-grid { columns: 3; } }
      
      .masonry-item { 
        display: block;
        width: 100%; 
        height: auto; /* Natural aspect ratio - NO CROPPING */
        object-fit: contain; /* Show full image */
        margin-bottom: 15px;
        break-inside: avoid; /* Prevent column breaks */
        border-radius: 0; /* Sharp corners - NO RADIUS */
        box-shadow: 0 2px 8px rgba(0,0,0,0.08); 
        transition: box-shadow 0.3s ease, transform 0.3s ease; 
        cursor: pointer;
      }
      .masonry-item:hover { 
        box-shadow: 0 4px 16px rgba(0,0,0,0.12);
        transform: translateY(-2px);
      }

      /* Gallery Lightbox Modal - Sharp Corners */
      .gallery-lightbox {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.95);
        z-index: 10000;
        align-items: center;
        justify-content: center;
        animation: fadeIn 0.3s ease;
      }
      .gallery-lightbox.active { display: flex; }
      
      .lightbox-content {
        position: relative;
        max-width: 90%;
        max-height: 90%;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      
      .lightbox-image {
        max-width: 100%;
        max-height: 90vh;
        width: auto;
        height: auto;
        border-radius: 0; /* Sharp corners - NO RADIUS */
        box-shadow: 0 10px 50px rgba(0, 0, 0, 0.5);
      }
      
      .lightbox-close {
        position: absolute;
        top: 20px;
        right: 30px;
        font-size: 40px;
        color: white;
        cursor: pointer;
        z-index: 10001;
        background: rgba(0, 0, 0, 0.5);
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 0; /* Sharp corners */
        transition: background 0.3s ease;
      }
      .lightbox-close:hover { background: rgba(188, 108, 37, 0.8); }
      
      .lightbox-nav {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        font-size: 30px;
        color: white;
        cursor: pointer;
        background: rgba(0, 0, 0, 0.5);
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 0; /* Sharp corners */
        transition: background 0.3s ease;
        user-select: none;
      }
      .lightbox-nav:hover { background: rgba(188, 108, 37, 0.8); }
      .lightbox-prev { left: 30px; }
      .lightbox-next { right: 30px; }
      
      @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

      /* Booking Card */
      /* Booking Card */
      .booking-card { position: sticky; top: 120px; background: #fcfbf7; padding: 30px; border-radius: var(--radius-xl); box-shadow: var(--shadow-soft); border: 1px solid rgba(188, 108, 37, 0.2); transition: box-shadow 0.3s ease; }
      .booking-card:hover { box-shadow: var(--shadow-hover); }
      .price-tag { font-family: "EB Garamond", serif; font-size: 2.5rem; color: var(--color-gold); font-weight: 700; line-height: 1; }
      .booking-input { width: 100%; padding: 12px 15px; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 15px; font-family: "Open Sans", sans-serif; transition: all 0.2s; }
      .btn-reserve { width: 100%; background: #C19B76; color: white; padding: 16px; border-radius: 8px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; border: 2px solid #C19B76; cursor: pointer; transition: all 0.3s; margin-top: 10px; }
      .btn-reserve:hover { background: #b08d68; border-color: #b08d68; transform: translateY(-2px); }
      .trust-badges { display: flex; justify-content: center; gap: 15px; margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee; }
      .trust-item { display: flex; flex-direction: column; align-items: center; font-size: 0.75rem; color: #718096; gap: 5px; }
      /* Guest Selector Popover - Premium Design */
      .guest-selector-wrapper { position: relative; }
      .guest-trigger { 
        cursor: pointer; 
        background-color: #fff; 
        text-align: left; 
        display: flex;
        align-items: center;
        justify-content: space-between;
      }
      .guest-trigger::after {
        content: '';
        display: inline-block;
        width: 0; 
        height: 0; 
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-top: 5px solid #a0aec0;
        margin-left: 10px;
      }
      .guest-dropdown {
        display: none;
        position: absolute;
        top: calc(100% + 8px);
        left: 0;
        right: 0;
        background: #ffffff;
        border: 1px solid rgba(0,0,0,0.08);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.12);
        z-index: 100;
        min-width: 280px;
        animation: fadeIn 0.2s ease-out;
      }
      @keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
      .guest-dropdown.active { display: block; }
      
      .guest-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
        padding-bottom: 20px;
        border-bottom: 1px solid #f0f0f0;
      }
      .guest-row:last-child { margin-bottom: 0; padding-bottom: 0; border-bottom: none; }
      
      .guest-info { flex: 1; }
      .guest-label { font-size: 1rem; font-weight: 700; color: #1a202c; display: block; margin-bottom: 2px;}
      .guest-sub { font-size: 0.85rem; color: #718096; font-weight: 400; }
      
      .counter-control { display: flex; align-items: center; gap: 15px; }
      .counter-btn {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        border: 1px solid #cbd5e0;
        background: white;
        color: #718096;
        font-size: 1.2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.2s;
        user-select: none;
        line-height: 0;
        padding-bottom: 4px;
      }
      .counter-btn:hover { border-color: #bc6c25; color: #bc6c25; background: #fffcf5; }
      .counter-btn:active { transform: scale(0.95); }
      .counter-val { font-weight: 700; font-size: 1.1rem; min-width: 25px; text-align: center; color: #2d3748; }
      /* Mobile */
      @media (max-width: 768px) {
        .pack-detail-container { display: flex; flex-direction: column; padding: 0 20px; margin-top: 20px; margin-bottom: 100px; }
        .pack-sidebar { order: 1; width: 100%; }
        .booking-card { position: relative; top: 0; box-shadow: none; border: 1px solid #eee; padding: 20px; margin-top: 40px; }
        .pack-title { font-size: 2rem; margin-bottom: 15px; }
        .pack-title { font-size: 2rem; margin-bottom: 15px; }
        .section-title { font-size: 1.75rem; margin-top: 40px; margin-bottom: 20px; }
        
        /* Mobile Form Grid Stack */
        .booking-form-grid { grid-template-columns: 1fr !important; gap: 10px !important; }
        
        /* Mobile Guest Dropdown Fit */
        .guest-dropdown { min-width: auto; width: 100%; top: calc(100% + 5px); }
        /* ===== MOBILE TIMELINE - HARD RESET ===== */
        /* Line on EACH ITEM, Icon at left:0, Line at left:24px */
        
        /* 1. RESET CONTAINER - Remove all padding/borders */
        .timeline-container { 
          position: relative !important;
          padding-left: 0 !important;
          margin: 30px 15px !important; /* 15px from screen edges */
          border: none !important;
        }
        
        /* 2. KILL container's ::before line */
        .timeline-container::before { 
          display: none !important;
          content: none !important;
        }
        
        /* 3. KILL old .timeline-line element */
        .timeline-line { 
          display: none !important;
        }
        
        /* 4. TIMELINE ITEM - Wrapper for each step */
        .timeline-item { 
          position: relative !important;
          padding-left: 70px !important; /* 50px icon + 20px gap */
          padding-bottom: 40px !important;
          margin-bottom: 0 !important;
          margin-left: 0 !important;
          border: none !important;
        }
        
        /* 5. THE LINE - Created on EACH item's ::before */
        /* Icon is 50px at left:0, center is at 25px */
        /* Line is 2px wide at left:24px, centers at 25px */
        .timeline-item::before { 
          content: '' !important;
          position: absolute !important;
          left: 24px !important;
          top: 0 !important;
          bottom: 0 !important;
          width: 2px !important;
          background: #e6e6e6 !important;
          z-index: 1 !important;
        }
        
        /* 6. LAST ITEM - No line below */
        .timeline-item:last-child { 
          padding-bottom: 0 !important;
        }
        .timeline-item:last-child::before { 
          display: none !important;
        }
        
        /* 7. THE ICON - 50x50px at left:0 */
        .timeline-icon { 
          position: absolute !important;
          left: 0 !important;
          top: 0 !important;
          width: 50px !important;
          height: 50px !important;
          border-radius: 50% !important;
          display: flex !important;
          align-items: center !important;
          justify-content: center !important;
          z-index: 2 !important;
          background: var(--color-gold) !important;
          color: #fff !important;
          box-shadow: 0 0 0 4px #fcfbf7 !important;
        }
        
        /* 8. TEXT CONTENT - Reset */
        .timeline-content { 
          padding-left: 0 !important;
          margin-left: 0 !important;
          padding-top: 0 !important;
        }
        .timeline-content h4 { 
          font-size: 1.2rem !important;
          margin: 0 0 5px 0 !important;
          line-height: 1.3 !important;
        }
        .timeline-content p { 
          font-size: 0.95rem !important;
          line-height: 1.6 !important;
          margin: 0 !important;
        }
        
        /* Fixed: Inclusions grid for mobile */
        .inclusions-grid { grid-template-columns: 1fr; padding: 20px; padding-left: 20px; }
        .check-list li { font-size: 14px; white-space: normal; flex-wrap: nowrap; }
        .check-list li svg { min-width: 20px; }
        
        
        /* Fixed: Gallery - 2 Column Masonry on Mobile (No Cropping, Sharp Corners) */
        .masonry-grid { columns: 2 !important; column-gap: 10px !important; margin-bottom: 40px; }
        .masonry-item { 
          width: 100% !important; 
          height: auto !important; 
          object-fit: contain !important;
          margin-bottom: 10px;
          break-inside: avoid;
          border-radius: 0 !important; /* Sharp corners on mobile too */
          box-shadow: 0 2px 8px rgba(0,0,0,0.08); 
        }
        
        /* Fixed: Mobile bottom bar with brand gold button */
        .mobile-bottom-bar { display: flex !important; position: fixed; bottom: 0; left: 0; width: 100%; background: white; z-index: 1000; padding: 15px 20px; box-shadow: 0 -5px 20px rgba(0,0,0,0.1); align-items: center; justify-content: space-between; border-top: 1px solid #eee; }
        .mobile-price { font-family: "EB Garamond", serif; font-size: 1.8rem; color: #C19B76; font-weight: 700; line-height: 1; }
        .mobile-price span { font-size: 0.8rem; color: #718096; font-family: "Open Sans", sans-serif; font-weight: 400; display: block; }
        .btn-mobile-book { background: #C19B76; color: white; padding: 12px 25px; border-radius: 50px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; border: none; font-size: 0.9rem; }
        .btn-mobile-book:hover, .btn-mobile-book:active { background: #b08d68; }
      }
      .mobile-bottom-bar { display: none; }
      /* NAVBAR BOOKING BUTTON - Gold Theme (Matches Index & Packs) */
      .navbar .nav-link.booking-btn {
        background: #bc6c25 !important;
        color: #fff !important;
        border: 1.5px solid #bc6c25 !important;
        border-radius: 0 !important;
        font-weight: 600 !important;
        padding: 10px 20px !important;
        transition: all 0.2s ease !important;
        display: inline-block !important;
      }

      .navbar .nav-link.booking-btn:hover {
        background: #d4af37 !important;
        border-color: #d4af37 !important;
        color: #fff !important;
      }
      
      @media (max-width: 768px) {
        .navbar .nav-link.booking-btn {
          padding: 12px 20px !important;
          font-size: 1rem !important;
        }
      }
  `;

  // Icons (Lucide-like SVGs)
  const icons = {
    star: '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>',
    clock: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    mapPin: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    user: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    bus: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
    check: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>',
    whatsapp: '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="margin-right: 8px;"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'
  };

  // Helper to render highlights
  function renderHighlights(items) {
    return items.map(item => `
      <div class="highlight-item">
        ${icons[item.icon] || icons.star}
        ${item.text}
      </div>
    `).join('');
  }

  // Helper to render timeline
  function renderTimeline(items) {
    return items.map(item => `
      <div class="timeline-item">
        <div class="timeline-icon">
          ${icons[item.icon] || icons.star}
        </div>
        <div class="timeline-content">
          <h4>${item.title}</h4>
          <p>${item.text}</p>
        </div>
      </div>
    `).join('');
  }

  // Helper to render gallery (using global lightbox)
  function renderGallery(images) {
    return images.map((img, index) => `
      <img src="${img}" class="masonry-item" alt="Gallery Image" data-gallery-index="${index}">
    `).join('');
  }

  // Main Render Function
  function render(data, targetId = 'page-root') {
    const {
      title,
      subTitle = "Pack",
      description,
      price,
      heroImage,
      rating = "5.0",
      reviews = "120+",
      highlights = [],
      timeline = [],
      included = [],
      notIncluded = "",
      gallery = [],
      galleryPathPrefix = "../"
    } = data;

    // Get Target
    const target = document.getElementById(targetId);
    if (!target) return;

    // Inject CSS
    const styleEl = document.createElement('style');
    styleEl.innerHTML = styles;
    document.head.appendChild(styleEl);

    // Fix image paths
    // If the path is already relative (starts with ../) or absolute (http), use it as is.
    // Otherwise, assume it's from root and prepend the prefix.
    let bgImage = heroImage;
    if (!heroImage.startsWith('http') && !heroImage.startsWith('../')) {
      bgImage = galleryPathPrefix + heroImage;
    }

    const html = `
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
        <div class="container">
          <a class="navbar-brand" href="../index.html"><img src="../images/logo-trensparent.png" alt="Marragafy"
              style="width: 70px; height: 70px;"></a>

          <!-- Moved language switcher here -->
          <div class="mobile-language-switcher">
            <a href="#" class="language-toggle" id="languageDropdown" role="button" data-toggle="dropdown"
              aria-haspopup="true" aria-expanded="false">
              <i class="icon-globe"></i> <span>EN</span>
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="languageDropdown">
              <a class="dropdown-item lang-option" href="#" data-lang="en">English</a>
              <a class="dropdown-item lang-option" href="#" data-lang="fr">Français</a>
              <a class="dropdown-item lang-option" href="#" data-lang="ar" dir="rtl">العربية</a>
            </div>
          </div>

          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="icon-menu"></span>
          </button>

          <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item"><a href="../index.html" class="nav-link">Home</a></li>
              <li class="nav-item ${subTitle === 'Activity' ? 'active' : ''}"><a href="../activities.html" class="nav-link">Activities</a></li>
              <li class="nav-item ${subTitle !== 'Activity' ? 'active' : ''}"><a href="../packs.html" class="nav-link">Packs</a></li>
              <li class="nav-item"><a href="../about.html" class="nav-link">About</a></li>
              <li class="nav-item"><a href="../reviews.html" class="nav-link">Reviews</a></li>
              <!-- <li class="nav-item"><a href="../blog.html" class="nav-link">Blog</a></li> -->
              <li class="nav-item"><a href="../contact.html" class="nav-link">Contact</a></li>
              <li class="nav-item"><a href="../packs.html" class="nav-link booking-btn">Booking</a></li>
            </ul>
          </div>
        </div>
      </nav>

      <!-- Hero Section -->
      <div class="hero-container relative w-full">
        <img src="${bgImage}" class="absolute inset-0 h-full w-full object-cover" alt="${title}">
        <div class="absolute inset-0 hero-blur-overlay"></div>
        
        <div class="container relative z-10 flex h-full flex-col items-center justify-center text-center">
          <h1 class="mb-4 text-white" style="font-family: 'EB Garamond', serif; font-size: 3.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">${title}</h1>
          <p class="breadcrumbs text-white" style="font-size: 1.1rem; letter-spacing: 1px;">
            <span class="mr-2"><a href="../index.html" class="text-white">Home</a></span> 
            <span class="text-white" style="opacity: 0.8;">${subTitle}</span>
          </p>
        </div>
      </div>

      <!-- Main Content -->
      <div class="pack-detail-container">
        
        <!-- Left Column -->
        <div class="pack-main-content">
          <div class="pack-header">
            <div class="rating-badge">${icons.star} ${rating} (${reviews} Reviews)</div>
            <h1 class="pack-title">${title}</h1>
            <p class="font-sans" style="font-size: 1.1rem; color: #718096; line-height: 1.6;">${description}</p>
            <div class="highlights-row">
              ${renderHighlights(highlights)}
            </div>
          </div>

          <h3 class="section-title">The Experience</h3>
          <div class="timeline-container">
            <div class="timeline-line"></div>
            ${renderTimeline(timeline)}
          </div>

          <h3 class="section-title">What's Included</h3>
          <div class="inclusions-grid">
            <ul class="check-list list-unstyled">
              ${included.map(i => `<li>${icons.check} ${i}</li>`).join('')}
            </ul>
          </div>
          <div style="margin-top: 15px; font-size: 0.9rem; color: #718096;">
            <strong>Not Included:</strong> ${notIncluded}
          </div>

          <h3 class="section-title">Gallery</h3>
          <div class="masonry-grid">
            ${renderGallery(gallery)}
          </div>
        </div>

        <!-- Right Column (Sticky Booking) -->
        <div class="pack-sidebar" id="booking-section">
          <div class="booking-card">
            
            <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 20px;">
              <div>
                <div class="price-tag">${price}</div>
                <div class="price-sub">per person</div>
              </div>
              <div class="rating-badge" style="margin:0;">
                ★ ${rating}
              </div>
            </div>

            <form id="bookingForm">
              <div class="form-group">
                <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Full Name</label>
                <input type="text" name="name" class="booking-input" placeholder="John Doe" required>
              </div>
              
              <div class="form-group">
                <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Email Address</label>
                <input type="email" name="email" class="booking-input" placeholder="john@example.com" required>
              </div>

              <div class="form-group">
                <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Phone Number</label>
                <div style="display: grid; grid-template-columns: 120px 1fr; gap: 10px;">
                  <select name="countryCode" class="booking-input" required>
                    <option value="+212" selected>🇲🇦 +212</option>
                    <option value="+1">🇺🇸 +1</option>
                    <option value="+44">🇬🇧 +44</option>
                    <option value="+33">🇫🇷 +33</option>
                    <option value="+34">🇪🇸 +34</option>
                    <option value="+49">🇩🇪 +49</option>
                    <option value="+39">🇮🇹 +39</option>
                    <option value="+31">🇳🇱 +31</option>
                    <option value="+32">🇧🇪 +32</option>
                    <option value="+41">🇨🇭 +41</option>
                    <option value="+971">🇦🇪 +971</option>
                    <option value="+966">🇸🇦 +966</option>
                  </select>
                  <input type="tel" name="phone" class="booking-input" placeholder="612345678" required>
                </div>
              </div>

              <div class="booking-form-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <div class="form-group">
                  <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Date</label>
                  <input type="date" name="date" class="booking-input" required>
                </div>
                
                <div class="form-group guest-selector-wrapper">
                  <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Guests</label>
                  <!-- Visual Input (Read Only) -->
                  <input type="text" id="guestDisplay" class="booking-input guest-trigger" value="2 Adults, 0 Children" readonly>
                  
                  <!-- Hidden Inputs for Form Submission -->
                  <input type="hidden" name="adults" id="adultsInput" value="2">
                  <input type="hidden" name="children" id="childrenInput" value="0">

                  <!-- Popover -->
                  <div class="guest-dropdown" id="guestDropdown">
                    <!-- Adults Row -->
                    <div class="guest-row">
                      <div>
                        <div class="guest-label">Adults</div>
                        <span class="guest-sub">Age 13+</span>
                      </div>
                      <div class="counter-control">
                        <div class="counter-btn" onclick="updateGuest('adults', -1)">-</div>
                        <span class="counter-val" id="adultsVal">2</span>
                        <div class="counter-btn" onclick="updateGuest('adults', 1)">+</div>
                      </div>
                    </div>
                    <!-- Children Row -->
                    <div class="guest-row">
                      <div>
                        <div class="guest-label">Children</div>
                        <span class="guest-sub">Age 2-12</span>
                      </div>
                      <div class="counter-control">
                        <div class="counter-btn" onclick="updateGuest('children', -1)">-</div>
                        <span class="counter-val" id="childrenVal">0</span>
                        <div class="counter-btn" onclick="updateGuest('children', 1)">+</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <button type="submit" class="btn-reserve">
                Reserve Now
              </button>
            </form>

            <div class="trust-badges">
              <div class="trust-item">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                Secure Booking
              </div>
              <div class="trust-item">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                Best Price
              </div>
              <div class="trust-item">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                Local Expert
              </div>
            </div>
            
            <div style="text-align: center; margin-top: 20px;">
               <p style="font-size: 0.9rem; color: #718096; margin-bottom: 10px;">Need help?</p>
               <a href="https://wa.me/212612345678" style="display: inline-flex; align-items: center; color: #25D366; font-weight: 600; text-decoration: none;">
                 <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="margin-right: 8px;"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
                 Chat on WhatsApp
               </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Mobile Bottom Bar -->
      <div class="mobile-bottom-bar">
        <div class="mobile-price">${price} <span>per person</span></div>
        <button onclick="document.getElementById('booking-section').scrollIntoView({behavior: 'smooth'})" class="btn-mobile-book">Book Now</button>
      </div>

      <!-- Footer -->
      <footer class="ftco-footer ftco-bg-dark ftco-section" style="background-color: #132a13 !important; margin-top: 60px;">
        <div class="container">
          <div class="row mb-5">
            <div class="col-md">
              <div class="ftco-footer-widget mb-4">
                <h2 class="ftco-heading-2">Marragafay</h2>
                <p>Discover the beauty of Agafay Desert with our unique experiences and activities.</p>
                <ul class="ftco-footer-social list-unstyled float-md-left float-lft mt-3">
                  <li class="ftco-animate"><a href="#"><span class="icon-twitter"></span></a></li>
                  <li class="ftco-animate"><a href="#"><span class="icon-facebook"></span></a></li>
                  <li class="ftco-animate"><a href="#"><span class="icon-instagram"></span></a></li>
                </ul>
              </div>
            </div>
            <div class="col-md">
              <div class="ftco-footer-widget mb-4 ml-md-4">
                <h2 class="ftco-heading-2">Information</h2>
                <ul class="list-unstyled">
                  <li><a href="../about.html" class="py-2 d-block">About Us</a></li>
                  <li><a href="../contact.html" class="py-2 d-block">Contact Us</a></li>
                  <li><a href="#" class="py-2 d-block">Terms & Conditions</a></li>
                  <li><a href="#" class="py-2 d-block">Privacy Policy</a></li>
                </ul>
              </div>
            </div>
            <div class="col-md">
              <div class="ftco-footer-widget mb-4">
                <h2 class="ftco-heading-2">Quick Links</h2>
                <ul class="list-unstyled">
                  <li><a href="../activities.html" class="py-2 d-block">Activities</a></li>
                  <li><a href="../packs.html" class="py-2 d-block">Packs</a></li>
                  <li><a href="../about.html" class="py-2 d-block">About</a></li>
                  <li><a href="../reviews.html" class="py-2 d-block">Reviews</a></li>
                  <!-- <li><a href="../blog.html" class="py-2 d-block">Blog</a></li> -->
                </ul>
              </div>
            </div>
            <div class="col-md">
              <div class="ftco-footer-widget mb-4">
                <h2 class="ftco-heading-2">Have a Question?</h2>
                <div class="block-23 mb-3">
                  <ul>
                    <li><span class="icon icon-map-marker"></span><span class="text">Agafay Desert, Marrakech,
                        Morocco</span></li>
                    <li><a href="#"><span class="icon icon-phone"></span><span class="text">+212 600 000000</span></a></li>
                    <li><a href="#"><span class="icon icon-envelope"></span><span
                          class="text">info@marragafay.com</span></a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12 text-center">
              <p>&copy; <script>document.write(new Date().getFullYear());</script> Marragafay. All rights reserved.</p>
            </div>
          </div>
        </div>
      </footer>
      
      <!-- NOTE: Gallery Lightbox moved to global system (see global-lightbox.js) -->
    `;

    // Inject HTML
    target.innerHTML = html;

    // Booking Date Logic - Restrict Past & Today
    const dateInput = target.querySelector('input[name="date"]');
    if (dateInput) {
      const today = new Date();
      const tomorrow = new Date(today);
      tomorrow.setDate(tomorrow.getDate() + 1);

      const yyyy = tomorrow.getFullYear();
      let mm = tomorrow.getMonth() + 1; // Months start at 0
      let dd = tomorrow.getDate();

      if (dd < 10) dd = '0' + dd;
      if (mm < 10) mm = '0' + mm;

      const minDate = yyyy + '-' + mm + '-' + dd;
      dateInput.min = minDate;
    }

    // Guest Selector Logic
    const guestTrigger = target.querySelector('.guest-trigger');
    const guestDropdown = target.querySelector('.guest-dropdown');

    if (guestTrigger && guestDropdown) {
      // Toggle Dropdown
      guestTrigger.addEventListener('click', (e) => {
        e.stopPropagation();
        guestDropdown.classList.toggle('active');
      });

      // Close when clicking outside
      document.addEventListener('click', (e) => {
        if (!guestTrigger.contains(e.target) && !guestDropdown.contains(e.target)) {
          guestDropdown.classList.remove('active');
        }
      });
    }

    // Export update function to window so onclick works
    window.updateGuest = function (type, change) {
      const input = document.getElementById(type + 'Input');
      const valDisplay = document.getElementById(type + 'Val');
      const display = document.getElementById('guestDisplay');

      let currentVal = parseInt(input.value);
      let newVal = currentVal + change;

      // Restraints
      if (type === 'adults' && newVal < 1) newVal = 1;
      if (type === 'children' && newVal < 0) newVal = 0;

      // Update State
      input.value = newVal;
      valDisplay.textContent = newVal;

      // Update Display String
      const a = parseInt(document.getElementById('adultsInput').value);
      const c = parseInt(document.getElementById('childrenInput').value);

      let text = `${a} Adult${a !== 1 ? 's' : ''}`;
      if (c > 0) {
        text += `, ${c} Child${c !== 1 ? 'ren' : ''}`;
      }
      display.value = text;
    };

    // Navbar Scroll & Mobile Logic - EXACT MATCH TO HOME PAGE
    const navbar = document.getElementById('ftco-navbar');
    if (navbar) {
      // Use jQuery for consistency with home page
      const $navbar = $(navbar);
      const $body = $('body');

      // Scroll handler matching main.js exactly
      const handleScroll = () => {
        const scrollTop = $(window).scrollTop();

        // At 20px - add scrolled class (solid white)
        if (scrollTop > 20) {
          if (!$navbar.hasClass('scrolled')) {
            $navbar.addClass('scrolled');
          }
        } else {
          if ($navbar.hasClass('scrolled')) {
            $navbar.removeClass('scrolled');
          }
        }
      };

      // Listen for scroll
      $(window).on('scroll', handleScroll);

      // Mobile menu toggle
      const toggler = navbar.querySelector('.navbar-toggler');
      if (toggler) {
        $(toggler).on('click', function () {
          setTimeout(handleScroll, 50);
        });
      }

      // Initial check
      handleScroll();
    }

    // Initialize global lightbox for gallery images
    // Wait for DOM to be ready, then attach click handlers
    setTimeout(() => {
      const galleryImages = document.querySelectorAll('.masonry-item');
      galleryImages.forEach((img, index) => {
        img.style.cursor = 'pointer';
        img.addEventListener('click', function () {
          // Use global lightbox system
          if (typeof openLightbox === 'function') {
            openLightbox(gallery, index);
          }
        });
      });
    }, 100);
  }

  return { render };

})();

if (typeof module !== 'undefined') module.exports = TourPageTemplate;
