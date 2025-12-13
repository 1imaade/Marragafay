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
      body { font-family: "Poppins", Arial, sans-serif; font-size: 16px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); }
      
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
      .highlight-item { display: flex; align-items: center; gap: 8px; font-size: 0.95rem; color: var(--color-text); background: white; padding: 8px 16px; border: 1px solid #eee; border-radius: 8px; }

      /* Timeline */
      .section-title { font-family: "EB Garamond", serif; font-size: 2rem; color: var(--color-dark); margin-bottom: 25px; margin-top: 50px; }
      .timeline-container { position: relative; padding-left: 30px; margin: 40px 0; }
      .timeline-line { position: absolute; left: 15px; top: 10px; bottom: 10px; width: 2px; background: #e2e8f0; }
      .timeline-item { position: relative; margin-bottom: 40px; }
      .timeline-icon { position: absolute; left: -45px; top: 0; width: 32px; height: 32px; background: var(--color-gold); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; z-index: 2; box-shadow: 0 0 0 5px #fff; }
      .timeline-content h4 { font-family: "EB Garamond", serif; font-size: 1.4rem; color: var(--color-dark); margin-bottom: 5px; }

      /* Inclusions */
      .inclusions-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; background: #f8fafc; padding: 30px; border-radius: var(--radius-lg); border: 1px solid #edf2f7; }
      .check-list li { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; font-size: 1rem; }
      
      /* Gallery */
      .masonry-grid { display: grid; grid-template-columns: repeat(2, 1fr); grid-template-rows: repeat(2, 200px); gap: 15px; }
      .masonry-item { width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-lg); transition: transform 0.3s ease; }
      .masonry-item:first-child { grid-row: span 2; height: 100%; }

      /* Booking Card */
      .booking-card { position: sticky; top: 120px; background: white; padding: 30px; border-radius: var(--radius-xl); box-shadow: var(--shadow-soft); border: 1px solid rgba(0,0,0,0.04); transition: box-shadow 0.3s ease; }
      .booking-card:hover { box-shadow: var(--shadow-hover); }
      .price-tag { font-family: "EB Garamond", serif; font-size: 2.5rem; color: var(--color-gold); font-weight: 700; line-height: 1; }
      .booking-input { width: 100%; padding: 12px 15px; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 15px; font-family: "Open Sans", sans-serif; transition: all 0.2s; }
      .btn-reserve { width: 100%; background: var(--color-dark); color: white; padding: 16px; border-radius: 8px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; border: none; cursor: pointer; transition: all 0.3s; margin-top: 10px; }
      .btn-reserve:hover { background: var(--color-gold); transform: translateY(-2px); }
      .trust-badges { display: flex; justify-content: center; gap: 15px; margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee; }
      .trust-item { display: flex; flex-direction: column; align-items: center; font-size: 0.75rem; color: #718096; gap: 5px; }

      /* Mobile */
      @media (max-width: 768px) {
        .pack-detail-container { display: flex; flex-direction: column; padding: 0 15px; margin-top: 20px; margin-bottom: 100px; }
        .pack-sidebar { order: 1; width: 100%; }
        .booking-card { position: relative; top: 0; box-shadow: none; border: 1px solid #eee; padding: 20px; margin-top: 30px; }
        .pack-title { font-size: 2rem; margin-bottom: 15px; }
        .section-title { font-size: 1.75rem; margin-top: 40px; margin-bottom: 20px; }
        .timeline-container { padding-left: 20px; margin: 30px 0; }
        .timeline-line { left: 10px; }
        .timeline-icon { width: 28px; height: 28px; left: -34px; }
        .masonry-grid { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 15px; padding-bottom: 15px; -ms-overflow-style: none; scrollbar-width: none; }
        .masonry-grid::-webkit-scrollbar { display: none; }
        .masonry-item { flex: 0 0 85%; height: 250px; scroll-snap-align: center; }
        .mobile-bottom-bar { display: flex !important; position: fixed; bottom: 0; left: 0; width: 100%; background: white; z-index: 1000; padding: 15px 20px; box-shadow: 0 -5px 20px rgba(0,0,0,0.1); align-items: center; justify-content: space-between; border-top: 1px solid #eee; }
        .mobile-price { font-family: "EB Garamond", serif; font-size: 1.8rem; color: var(--color-gold); font-weight: 700; line-height: 1; }
        .mobile-price span { font-size: 0.8rem; color: #718096; font-family: "Open Sans", sans-serif; font-weight: 400; display: block; }
        .btn-mobile-book { background: var(--color-dark); color: white; padding: 12px 25px; border-radius: 50px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; border: none; font-size: 0.9rem; }
      }
      .mobile-bottom-bar { display: none; }
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

  // Helper to render gallery
  function renderGallery(images) {
    return images.map(img => `
      <img src="${img}" class="masonry-item" alt="Gallery Image">
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
              style="width: 80px; height: auto;"></a>

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

          <button class="navbar-toggler" type="button" aria-label="Toggle navigation">
            <span class="icon-menu"></span>
          </button>

          <div class="collapse navbar-collapse">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item"><a href="../index.html" class="nav-link">Home</a></li>
              <li class="nav-item ${subTitle === 'Activity' ? 'active' : ''}"><a href="../activities.html" class="nav-link">Activities</a></li>
              <li class="nav-item ${subTitle !== 'Activity' ? 'active' : ''}"><a href="../packs.html" class="nav-link">Packs</a></li>
              <li class="nav-item"><a href="../about.html" class="nav-link">About</a></li>
              <li class="nav-item"><a href="../reviews.html" class="nav-link">Reviews</a></li>
              <li class="nav-item"><a href="../blog.html" class="nav-link">Blog</a></li>
              <li class="nav-item"><a href="../contact.html" class="nav-link">Contact</a></li>
              <li class="nav-item"><a href="#" class="nav-link booking-btn">Booking</a></li>
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

              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <div class="form-group">
                  <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Date</label>
                  <input type="date" name="date" class="booking-input" required>
                </div>
                <div class="form-group">
                  <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Guests</label>
                  <select name="guests" class="booking-input" required>
                    <option value="1">1 Person</option>
                    <option value="2" selected>2 People</option>
                    <option value="3">3 People</option>
                    <option value="4">4 People</option>
                    <option value="5+">5+ Group</option>
                  </select>
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
                <p>Experience the magic of Agafay Desert.</p>
              </div>
            </div>
            <div class="col-md">
              <div class="ftco-footer-widget mb-4">
                <h2 class="ftco-heading-2">Quick Links</h2>
                <ul class="list-unstyled">
                  <li><a href="../index.html">Home</a></li>
                  <li><a href="../about.html">About</a></li>
                  <li><a href="../contact.html">Contact</a></li>
                </ul>
              </div>
            </div>
            <div class="col-md">
              <div class="ftco-footer-widget mb-4">
                <h2 class="ftco-heading-2">Contact</h2>
                <ul class="list-unstyled">
                  <li><a href="tel:+212612345678">+212 612 345 678</a></li>
                  <li><a href="mailto:info@marragafay.com">info@marragafay.com</a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="row"><div class="col-md-12 text-center"><p>Copyright &copy; 2024 Marragafay</p></div></div>
        </div>
      </footer>
    `;

    // Inject HTML
    target.innerHTML = html;

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
  }

  return { render };

})();

if (typeof module !== 'undefined') module.exports = TourPageTemplate;
