/**
 * Marragafay Navbar - StayHere-Inspired Design
 * Modern, clean, minimal navigation with full-screen menu overlay
 * 
 * Features:
 * - Hamburger → X animation
 * - Full-screen menu overlay with organized columns
 * - Scroll-based shadow effect
 * - Language selector dropdown
 * - Active page indicator
 * - Keyboard navigation & accessibility
 * - Mobile-responsive behavior
 */

(function () {
  'use strict';

  // ─── Configuration ──────────────────────────────────────────────
  const CONFIG = {
    scrollThreshold: 10,
    animationDelay: 50,
    
    menuItems: (function() {
      const pathLang = window.location.pathname.split('/').find(p => ['en', 'fr', 'es', 'ar'].includes(p)) || 'en';
      const dictionaries = {
        en: {
          experiencesPacks: [
        { label: 'Marragafay Signature Agafay Escape', href: 'packages/comfort' },
        { label: 'Marragafay VIP Luxury Desert Retreat', href: 'packages/luxe' },
        { label: 'Marragafay Complete Discovery Expedition', href: 'packages/basic' },
      ],
      experiencesActivities: [
        { label: 'Marragafay Extreme Quad Biking Adventure', href: 'activities/quad-biking' },
        { label: 'Marragafay Traditional Camel Ride Trek', href: 'activities/camel-ride' },
        { label: 'Marragafay Dune Buggy Adrenaline Safari', href: 'activities/buggy' },
        { label: 'Marragafay Sunrise Hot Air Balloon Flight', href: 'activities/hot-air-balloon' },
        { label: 'Marragafay Atlas Mountains Paragliding', href: 'activities/paragliding' },
        { label: 'Marragafay Nomadic Desert Dinner & Show', href: 'activities/dinner-show' },
      ],
      brand: [
        { label: 'About Marragafay', href: 'about' },
        { label: 'Customer Reviews', href: 'reviews' },
        { label: 'Our Blog', href: 'blog' },
        { label: 'Careers', href: 'about' },
        { label: 'FAQ', href: 'about' },
      ],
      packs: [
        { label: 'Agafay Discovery Pack', href: 'packages/basic' },
        { label: 'VIP Luxury Escape', href: 'packages/luxe' },
        { label: 'Romantic Sunset Pack', href: 'packages/comfort' },
      ],
      booking: [
        { label: 'Book an Experience', href: 'packs', arrow: true },
        { label: 'Contact Concierge', href: 'contact', arrow: true },
      ],
        },
        fr: {
          experiencesPacks: [
            { label: 'Signature Marragafay Escapade Agafay', href: 'packages/comfort' },
            { label: 'Retraite VIP Luxe dans le Désert', href: 'packages/luxe' },
            { label: 'Expédition Découverte Complète', href: 'packages/basic' },
          ],
          experiencesActivities: [
            { label: 'Aventure Extrême en Quad', href: 'activities/quad-biking' },
            { label: 'Randonnée Traditionnelle à Dos de Chameau', href: 'activities/camel-ride' },
            { label: 'Safari Adrénaline en Buggy', href: 'activities/buggy' },
            { label: 'Vol en Montgolfière au Lever du Soleil', href: 'activities/hot-air-balloon' },
            { label: 'Parapente dans les Montagnes de l\'Atlas', href: 'activities/paragliding' },
            { label: 'Dîner et Spectacle Nomade dans le Désert', href: 'activities/dinner-show' },
          ],
          brand: [
            { label: 'À Propos de Marragafay', href: 'about' },
            { label: 'Avis des Clients', href: 'reviews' },
            { label: 'Notre Blog', href: 'blog' },
            { label: 'Carrières', href: 'about' },
            { label: 'FAQ', href: 'about' },
          ],
          packs: [
            { label: 'Pack Découverte Agafay', href: 'packages/basic' },
            { label: 'Escapade VIP Luxe', href: 'packages/luxe' },
            { label: 'Pack Coucher de Soleil Romantique', href: 'packages/comfort' },
          ],
          booking: [
            { label: 'Réserver une Expérience', href: 'packs', arrow: true },
            { label: 'Contacter le Concierge', href: 'contact', arrow: true },
          ],
        },
        es: {
          experiencesPacks: [
            { label: 'Marragafay Escapada Signature Agafay', href: 'packages/comfort' },
            { label: 'Retiro VIP de Lujo en el Desierto', href: 'packages/luxe' },
            { label: 'Expedición de Descubrimiento Completo', href: 'packages/basic' },
          ],
          experiencesActivities: [
            { label: 'Aventura Extrema en Quad', href: 'activities/quad-biking' },
            { label: 'Paseo Tradicional en Camello', href: 'activities/camel-ride' },
            { label: 'Safari de Adrenalina en Buggy', href: 'activities/buggy' },
            { label: 'Vuelo en Globo Aerostático al Amanecer', href: 'activities/hot-air-balloon' },
            { label: 'Parapente en las Montañas del Atlas', href: 'activities/paragliding' },
            { label: 'Cena y Espectáculo Nómada en el Desierto', href: 'activities/dinner-show' },
          ],
          brand: [
            { label: 'Sobre Marragafay', href: 'about' },
            { label: 'Opiniones de Clientes', href: 'reviews' },
            { label: 'Nuestro Blog', href: 'blog' },
            { label: 'Carreras', href: 'about' },
            { label: 'Preguntas Frecuentes', href: 'about' },
          ],
          packs: [
            { label: 'Paquete Descubrimiento Agafay', href: 'packages/basic' },
            { label: 'Escapada VIP de Lujo', href: 'packages/luxe' },
            { label: 'Paquete Atardecer Romántico', href: 'packages/comfort' },
          ],
          booking: [
            { label: 'Reservar una Experiencia', href: 'packs', arrow: true },
            { label: 'Contactar al Conserje', href: 'contact', arrow: true },
          ],
        },
        ar: {
          experiencesPacks: [
            { label: 'بصمة مراكفاي: ملاذ أكفاي', href: 'packages/comfort' },
            { label: 'ملاذ فاخر في الصحراء لكبار الشخصيات', href: 'packages/luxe' },
            { label: 'رحلة استكشاف كاملة', href: 'packages/basic' },
          ],
          experiencesActivities: [
            { label: 'مغامرة الدراجات الرباعية', href: 'activities/quad-biking' },
            { label: 'ركوب الجمال التقليدي', href: 'activities/camel-ride' },
            { label: 'سفاري عربات الباجي', href: 'activities/buggy' },
            { label: 'رحلة منطاد الهواء الساخن', href: 'activities/hot-air-balloon' },
            { label: 'الطيران المظلي في جبال الأطلس', href: 'activities/paragliding' },
            { label: 'عشاء بدوي وعروض في الصحراء', href: 'activities/dinner-show' },
          ],
          brand: [
            { label: 'عن مراكفاي', href: 'about' },
            { label: 'آراء العملاء', href: 'reviews' },
            { label: 'مدونتنا', href: 'blog' },
            { label: 'وظائف', href: 'about' },
            { label: 'الأسئلة الشائعة', href: 'about' },
          ],
          packs: [
            { label: 'باقة اكتشاف أكفاي', href: 'packages/basic' },
            { label: 'ملاذ فاخر لكبار الشخصيات', href: 'packages/luxe' },
            { label: 'باقة غروب الشمس الرومانسية', href: 'packages/comfort' },
          ],
          booking: [
            { label: 'احجز تجربة', href: 'packs', arrow: true },
            { label: 'تواصل مع خدمة العملاء', href: 'contact', arrow: true },
          ],
        }
      };
      return dictionaries[pathLang];
    })(),
    languages: [
      { code: 'en', label: 'English', dir: 'ltr' },
      { code: 'fr', label: 'Français', dir: 'ltr' },
      { code: 'es', label: 'Español', dir: 'ltr' },
      { code: 'ar', label: 'العربية', dir: 'rtl' },
    ],
  };

  // ─── State ──────────────────────────────────────────────────────
  let isMenuOpen = false;
  let isLangDropdownOpen = false;
  let scrollPosition = 0;
  
  // ─── Utility: Get Base Path ─────────────────────────────────────
  function getBasePath() {
    const path = window.location.pathname;
    if (path.includes('/packages/') || path.includes('/activities/')) {
      return '../';
    }
    return '';
  }
  const basePath = getBasePath();

  // ─── UI Strings Dictionary ──────────────────────────────────────────────
  const pathLang = window.location.pathname.split('/').find(p => ['en', 'fr', 'es', 'ar'].includes(p)) || 'en';
  const UI_STR = {
    en: {
      activities: 'Activities', packs: 'Packs', book: 'Book', experiences: 'Experiences',
      brand: 'The Brand', stay: 'Stay with us', directBooking: 'Direct booking', bookExp: 'Book Your Experience'
    },
    fr: {
      activities: 'Activités', packs: 'Forfaits', book: 'Réserver', experiences: 'Expériences',
      brand: 'La Marque', stay: 'Séjournez chez nous', directBooking: 'Réservation directe', bookExp: 'Réservez Votre Expérience'
    },
    es: {
      activities: 'Actividades', packs: 'Paquetes', book: 'Reservar', experiences: 'Experiencias',
      brand: 'La Marca', stay: 'Quédate con nosotros', directBooking: 'Reserva directa', bookExp: 'Reserva Tu Experiencia'
    },
    ar: {
      activities: 'أنشطة', packs: 'باقات', book: 'احجز', experiences: 'تجارب',
      brand: 'العلامة التجارية', stay: 'ابق معنا', directBooking: 'حجز مباشر', bookExp: 'احجز تجربتك'
    }
  }[pathLang];


  // ─── DOM Ready ──────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', init);

  function init() {
    const isMobile = window.innerWidth <= 768;
    injectNavbarHTML();
    injectMenuOverlayHTML(isMobile);
    initLanguageDisplay();
    bindEvents();
    setActivePage();
    handleScroll(); // Initial check
  }

  function initLanguageDisplay() {
    const pathParts = window.location.pathname.split('/');
    const currentLang = pathParts.find(p => ['en', 'fr', 'es', 'ar'].includes(p)) || 'en';
    const langData = CONFIG.languages.find(l => l.code === currentLang);
    if (langData) {
      const codeEl = document.querySelector('.lang-code');
      if (codeEl) codeEl.textContent = langData.code.toUpperCase();

      const displaySpan = document.querySelector('#languageDropdown span');
      if (displaySpan) displaySpan.textContent = langData.code.toUpperCase();

      document.querySelectorAll('.lang-option').forEach(opt => {
        opt.classList.toggle('active', opt.dataset.lang === langData.code);
      });
      document.querySelectorAll('.mobile-lang-item').forEach(opt => {
        opt.classList.toggle('active', opt.dataset.lang === langData.code);
      });
    }
  }

  // ─── Inject Navbar HTML ─────────────────────────────────────────
  function injectNavbarHTML() {
    const existingNav = document.getElementById('ftco-navbar');
    if (!existingNav) return;

    // Determine current page for active state
    const currentPage = getCurrentPage();

    // Build quick links for desktop
    const quickLinksHTML = `
      <div class="nav-quick-links">
        <a href="/${pathLang}/activities" class="nav-quick-link${currentPage.includes('activities') ? ' active' : ''}">${UI_STR.activities}</a>
        <a href="/${pathLang}/packs" class="nav-quick-link${currentPage.includes('packs') ? ' active' : ''}">${UI_STR.packs}</a>
      </div>
    `;

    // Build the new navbar inner content
    const navbarInnerHTML = `
      <div class="navbar-inner">
        <!-- LEFT: Menu Toggle + Quick Links -->
        <div class="nav-left">
          <button class="nav-menu-toggle" id="navMenuToggle" 
                  aria-label="Open navigation menu" 
                  aria-expanded="false"
                  aria-controls="stayhere-menu-overlay">
            <span class="hamburger-icon" aria-hidden="true">
              <span class="bar"></span>
              <span class="bar"></span>
              <span class="bar"></span>
            </span>
            <span class="toggle-label">menu</span>
          </button>
          ${quickLinksHTML}
        </div>

        <!-- CENTER: Logo -->
        <div class="nav-center">
          <a href="/${pathLang}/" class="nav-logo" aria-label="Marragafay - Return to homepage">
            <img src="/images/logo-no-text.png" 
                 alt="Marragafay Logo" 
                 class="nav-logo-img"
                 width="28" height="28"
                 loading="eager">
          </a>
        </div>

        <!-- RIGHT: Language + CTA -->
        <div class="nav-right">
          <button class="nav-lang-selector" id="navLangSelector"
                  aria-label="Select language"
                  aria-expanded="false"
                  aria-haspopup="true">
            <svg class="lang-globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
              <circle cx="12" cy="12" r="10"/>
              <path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1 4-10z"/>
            </svg>
            <span class="lang-code">${pathLang.toUpperCase()}</span>
            <svg class="lang-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <polyline points="6 9 12 15 18 9"/>
            </svg>
          </button>
          <div class="lang-dropdown" id="langDropdown" role="menu">
            ${CONFIG.languages.map(lang => `
              <button class="lang-option${lang.code === pathLang ? ' active' : ''}" 
                      role="menuitem"
                      data-lang="${lang.code}" 
                      ${lang.dir === 'rtl' ? 'dir="rtl"' : ''}>
                ${lang.label}
              </button>
            `).join('')}
          </div>
          <a href="/${pathLang}/packs" class="nav-cta" id="navBookCta">${UI_STR.book}</a>
        </div>
      </div>
    `;

    // Add the new class and content
    existingNav.classList.add('navbar-stayhere');
    existingNav.innerHTML = navbarInnerHTML;

    // Insert spacer after navbar (for fixed positioning)
    const spacer = document.createElement('div');
    spacer.className = 'navbar-spacer';
    spacer.setAttribute('aria-hidden', 'true');
    existingNav.parentNode.insertBefore(spacer, existingNav.nextSibling);

    // Add skip-to-content link before navbar
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.className = 'skip-to-content';
    skipLink.textContent = 'Skip to main content';
    existingNav.parentNode.insertBefore(skipLink, existingNav);
  }

  // ─── Inject Full-Screen Menu Overlay ────────────────────────────
  function injectMenuOverlayHTML(isMobile) {
    const currentPage = getCurrentPage();
    const navbar = document.getElementById('ftco-navbar');
    if (!navbar) return;

    const overlay = document.createElement('div');
    overlay.className = 'stayhere-menu-overlay';
    overlay.id = 'stayhere-menu-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-label', 'Navigation menu');
    overlay.setAttribute('aria-hidden', 'true');

    if (isMobile) {
      overlay.innerHTML = `
        <style>
          details > summary::-webkit-details-marker { display: none; }
          details[open] summary .chevron-icon { transform: rotate(180deg); }
        </style>
        <div class="menu-content-mobile" style="display: flex; flex-direction: column; height: 100%; overflow: hidden;">
          
          <div style="flex: 1; overflow-y: auto; padding: 24px;">
            <!-- EXPERIENCES -->
            <div style="margin-bottom: 32px;">
              <h3 style="font-size: 10px; font-weight: 600; margin-bottom: 16px; text-transform: uppercase; color: #10100E; letter-spacing: normal;">${UI_STR.experiences}</h3>
              
              <!-- Packs Accordion -->
              <details class="group" style="margin-bottom: 16px;">
                <summary style="font-weight: 600; font-size: 14px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; color: #272724; list-style: none;">
                  <div style="display: flex; align-items: center; gap: 6px;">
                    Packs <span style="font-size: 13px; font-weight: 400; color: #b8b5a6;">(3)</span>
                  </div>
                  <svg style="width: 16px; height: 16px; transition: transform 0.2s;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="chevron-icon">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
                  </svg>
                </summary>
                <div style="padding-top: 12px; padding-bottom: 8px; display: flex; flex-direction: column; gap: 12px; padding-left: 16px;">
                  ${CONFIG.menuItems.experiencesPacks.map(item => `
                    <a href="/${pathLang}/${item.href}" style="display: block; font-size: 14px; line-height: 20px; font-weight: 300; color: #5c5c56; text-transform: capitalize; text-decoration: none; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#5c5c56'">
                      ${item.label}
                    </a>
                  `).join('')}
                </div>
              </details>

              <!-- Activities Accordion -->
              <details class="group" style="margin-bottom: 16px;">
                <summary style="font-weight: 600; font-size: 14px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; color: #272724; list-style: none;">
                  <div style="display: flex; align-items: center; gap: 6px;">
                    ${UI_STR.activities} <span style="font-size: 13px; font-weight: 400; color: #b8b5a6;">(6)</span>
                  </div>
                  <svg style="width: 16px; height: 16px; transition: transform 0.2s;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="chevron-icon">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
                  </svg>
                </summary>
                <div style="padding-top: 12px; padding-bottom: 8px; display: flex; flex-direction: column; gap: 12px; padding-left: 16px;">
                  ${CONFIG.menuItems.experiencesActivities.map(item => `
                    <a href="/${pathLang}/${item.href}" style="display: block; font-size: 14px; line-height: 20px; font-weight: 300; color: #5c5c56; text-transform: capitalize; text-decoration: none; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#5c5c56'">
                      ${item.label}
                    </a>
                  `).join('')}
                </div>
              </details>
            </div>

            <!-- THE BRAND -->
            <div style="margin-bottom: 32px;">
              <h3 style="font-size: 10px; font-weight: 600; margin-bottom: 16px; text-transform: uppercase; color: #10100E; letter-spacing: normal;">${UI_STR.brand}</h3>
              <div style="display: flex; flex-direction: column; gap: 2px;">
                ${CONFIG.menuItems.brand.map(item => `
                  <a href="/${pathLang}/${item.href}" style="display: block; font-size: 14px; line-height: 20px; font-weight: 600; color: #171716; text-transform: capitalize; text-decoration: none; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#171716'">
                    ${item.label}
                  </a>
                `).join('')}
              </div>
            </div>

            <!-- STAY WITH US -->
            <div style="margin-bottom: 16px;">
              <h3 style="font-size: 10px; font-weight: 600; margin-bottom: 16px; text-transform: uppercase; color: #10100E; letter-spacing: normal;">${UI_STR.stay}</h3>
              <div style="display: flex; flex-direction: column; gap: 2px;">
                ${CONFIG.menuItems.packs.map(item => `
                  <a href="/${pathLang}/${item.href}" style="display: block; font-size: 14px; line-height: 20px; font-weight: 600; color: #171716; text-decoration: none; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#171716'">
                    ${item.label}
                  </a>
                `).join('')}
              </div>

              <hr style="border: none; border-top: 1px solid #e2e0d3; margin: 24px 0;" />

              <h3 style="font-size: 10px; font-weight: 600; margin-bottom: 12px; text-transform: uppercase; color: #10100E; letter-spacing: normal;">${UI_STR.directBooking}</h3>
              <div style="display: flex; flex-direction: column; gap: 12px;">
                ${CONFIG.menuItems.booking.map(item => `
                  <a href="/${pathLang}/${item.href}" style="display: block; font-size: 14px; font-weight: 400; color: #5c5c56; text-decoration: none; padding-top: 4px;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#5c5c56'">
                    ${item.label} <span class="ml-1"><svg class="w-4 h-4 inline-block fill-current" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"/></svg></span>
                  </a>
                `).join('')}
              </div>
            </div>
            
            <!-- Mobile: Language Options -->
            <div class="mobile-lang-section" style="margin-top: 40px; padding-bottom: 24px;">
              ${CONFIG.languages.map(lang => `
                <button class="mobile-lang-item${lang.code === pathLang ? ' active' : ''}" 
                        data-lang="${lang.code}"
                        ${lang.dir === 'rtl' ? 'dir="rtl"' : ''}>
                  <svg class="mobile-lang-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
                    <circle cx="12" cy="12" r="10"/>
                    <path d="M2 12h20"/>
                  </svg>
                  ${lang.label}
                </button>
              `).join('')}
            </div>
          </div>

          <!-- Sticky Conversion Footer -->
          <div style="margin-top: auto; padding: 16px; border-top: 1px solid #e2e0d3; background-color: #F6F7EA;">
            <button onclick="window.location.href='/${pathLang}/packs'" style="width: 100%; background-color: #523225; color: #F6F7EA; font-weight: 600; padding: 14px 0; border: none; border-radius: 50px; cursor: pointer; transition: opacity 0.2s; font-size: 14px;" onmouseover="this.style.opacity='0.9'" onmouseout="this.style.opacity='1'">
              ${UI_STR.bookExp}
            </button>
          </div>
        </div>
      `;
    } else {
      overlay.innerHTML = `
        <div class="menu-content">
          <!-- Column 1: Experiences -->
          <div class="menu-column">
            <p class="menu-column-title" style="text-transform: capitalize; font-weight: 600; color: #10100E;">${UI_STR.experiences}</p>

            <p class="menu-subgroup-title" style="margin-top:0; display:flex; align-items:center; gap:6px;">
              Packs <span style="font-size:13px; font-weight:400; color:#b8b5a6;">(3)</span>
            </p>
            <ul class="menu-links menu-links--indented">
              ${CONFIG.menuItems.experiencesPacks.map(item => `
                <li class="menu-link-item">
                  <a href="/${pathLang}/${item.href}" class="menu-link menu-link--l3 menu-link--muted${item.href === currentPage ? ' active' : ''}">
                    ${item.label}
                  </a>
                </li>
              `).join('')}
            </ul>

            <p class="menu-subgroup-title" style="display:flex; align-items:center; gap:6px;">
              ${UI_STR.activities} <span style="font-size:13px; font-weight:400; color:#b8b5a6;">(6)</span>
            </p>
            <ul class="menu-links menu-links--indented">
              ${CONFIG.menuItems.experiencesActivities.map(item => `
                <li class="menu-link-item">
                  <a href="/${pathLang}/${item.href}" class="menu-link menu-link--l3 menu-link--muted${item.href === currentPage ? ' active' : ''}">
                    ${item.label}
                  </a>
                </li>
              `).join('')}
            </ul>
          </div>

          <!-- Column 2: The Brand -->
          <div class="menu-column">
            <p class="menu-column-title" style="text-transform: capitalize; font-weight: 600; color: #10100E;">${UI_STR.brand}</p>
            <ul class="menu-links" style="margin-left: 0; padding-left: 0;">
              ${CONFIG.menuItems.brand.map(item => `
                <li class="menu-link-item" style="margin-bottom: 2px;">
                  <a href="/${pathLang}/${item.href}" class="menu-link${item.href === currentPage ? ' active' : ''}" style="font-size: 14px; line-height: 20px; font-weight: 600; color: #171716; text-transform: capitalize; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#171716'">
                    ${item.label}
                  </a>
                </li>
              `).join('')}
            </ul>
          </div>

          <!-- Column 3: Stay with us -->
          <div class="menu-column">
            <p class="menu-column-title" style="text-transform: lowercase;">${UI_STR.stay}</p>

            <ul class="menu-links" style="margin-left: 0; padding-left: 0;">
              ${CONFIG.menuItems.packs.map(item => `
                <li class="menu-link-item" style="margin-bottom: 2px;">
                  <a href="/${pathLang}/${item.href}" class="menu-link${item.href === currentPage ? ' active' : ''}" style="font-size: 14px; line-height: 20px; font-weight: 600; color: #171716; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#171716'">
                    ${item.label}
                  </a>
                </li>
              `).join('')}
            </ul>

            <hr style="border: none; border-top: 1px solid #e2e0d3; margin: 24px 0;" />

            <p style="font-size: 10px; line-height: 15px; font-weight: 600; color: #10100E; text-transform: uppercase; margin-bottom: 12px; margin-top: 0;">${UI_STR.directBooking}</p>
            <ul class="menu-links" style="margin-bottom: 0;">
              ${CONFIG.menuItems.booking.map(item => `
                <li class="menu-link-item" style="margin-bottom: 12px;">
                  <a href="/${pathLang}/${item.href}" class="menu-link${item.href === currentPage ? ' active' : ''}" style="font-size: 14px; font-weight: 400; color: #5c5c56;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#5c5c56'">
                    ${item.label} <span class="ml-1"><svg class="w-4 h-4 inline-block fill-current" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"/></svg></span>
                  </a>
                </li>
              `).join('')}
            </ul>
          </div>
        </div>
      `;
    }

    navbar.appendChild(overlay);

    // Add backdrop
    const backdrop = document.createElement('div');
    backdrop.className = 'stayhere-backdrop';
    backdrop.id = 'stayhere-backdrop';
    backdrop.setAttribute('aria-hidden', 'true');
    document.body.appendChild(backdrop);

    // Show mobile CTA on mobile
    if (isMobile) {
      const mobileCta = overlay.querySelector('.mobile-menu-cta');
      if (mobileCta) mobileCta.style.display = 'block';
    }
  }

  // ─── Event Bindings ─────────────────────────────────────────────
  function bindEvents() {
    // Menu toggle
    const menuToggle = document.getElementById('navMenuToggle');
    if (menuToggle) {
      menuToggle.addEventListener('click', toggleMenu);
    }

    // Language selector
    const langSelector = document.getElementById('navLangSelector');
    if (langSelector) {
      langSelector.addEventListener('click', toggleLangDropdown);
    }

    // Language options
    document.querySelectorAll('.lang-option, .mobile-lang-item').forEach(opt => {
      opt.addEventListener('click', function () {
        selectLanguage(this.dataset.lang);
      });
    });

    // Close menus when clicking outside
    document.addEventListener('click', function (e) {
      // Close lang dropdown
      const langSelector = document.getElementById('navLangSelector');
      const langDropdown = document.getElementById('langDropdown');
      if (langSelector && langDropdown && !langSelector.contains(e.target) && !langDropdown.contains(e.target)) {
        closeLangDropdown();
      }
    });

    // Close menu with Escape key
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        if (isMenuOpen) closeMenu();
        if (isLangDropdownOpen) closeLangDropdown();
      }
    });

    // Scroll handler
    let ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(function () {
          handleScroll();
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });

    // Window resize handler
    let resizeTimer;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(function () {
        // Update mobile CTA visibility
        const mobileCta = document.querySelector('.stayhere-menu-overlay .mobile-menu-cta');
        if (mobileCta) {
          mobileCta.style.display = window.innerWidth <= 768 ? 'block' : 'none';
        }
      }, 250);
    });

    // Close menu when clicking on menu links
    document.querySelectorAll('.stayhere-menu-overlay .menu-link').forEach(link => {
      link.addEventListener('click', function () {
        closeMenu();
      });
    });

    // Close menu when clicking backdrop
    const backdrop = document.getElementById('stayhere-backdrop');
    if (backdrop) {
      backdrop.addEventListener('click', closeMenu);
    }

    // Localhost static dev server safeguard (port 5500 / Live Server):
    // Intercept clean URL navigation locally to append .html so local static servers don't return Cannot GET.
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      document.addEventListener('click', function (e) {
        const anchor = e.target.closest('a');
        if (!anchor) return;
        const rawHref = anchor.getAttribute('href');
        if (!rawHref || rawHref.startsWith('#') || rawHref.startsWith('javascript:') || rawHref.startsWith('http:') || rawHref.startsWith('https:') || rawHref.startsWith('mailto:') || rawHref.startsWith('tel:')) return;
        
        try {
          const targetUrl = new URL(anchor.href, window.location.origin);
          const path = targetUrl.pathname;
          
          if ((path.includes('/packages/') || path.includes('/activities/') || path.endsWith('/packs') || path.endsWith('/activities') || path.endsWith('/about') || path.endsWith('/reviews') || path.endsWith('/contact')) && !path.endsWith('.html')) {
            e.preventDefault();
            targetUrl.pathname = path + '.html';
            window.location.href = targetUrl.toString();
          }
        } catch (err) {
          // Fallback if URL parsing fails
        }
      });
    }
  }

  // ─── Menu Toggle ────────────────────────────────────────────────
  function toggleMenu() {
    if (isMenuOpen) {
      closeMenu();
    } else {
      openMenu();
    }
  }

  function openMenu() {
    isMenuOpen = true;
    scrollPosition = window.scrollY;

    const toggle = document.getElementById('navMenuToggle');
    const overlay = document.getElementById('stayhere-menu-overlay');
    const label = toggle ? toggle.querySelector('.toggle-label') : null;

    if (toggle) {
      toggle.classList.add('is-active');
      toggle.setAttribute('aria-expanded', 'true');
      toggle.setAttribute('aria-label', 'Close navigation menu');
    }

    if (label) label.textContent = 'close';

    if (overlay) {
      overlay.classList.add('is-open');
      overlay.setAttribute('aria-hidden', 'false');
    }

    const backdrop = document.getElementById('stayhere-backdrop');
    if (backdrop) backdrop.classList.add('is-open');

    document.body.classList.add('nav-menu-open');

    // Trap focus inside menu
    trapFocus(overlay);
  }

  function closeMenu() {
    isMenuOpen = false;

    const toggle = document.getElementById('navMenuToggle');
    const overlay = document.getElementById('stayhere-menu-overlay');
    const label = toggle ? toggle.querySelector('.toggle-label') : null;

    if (toggle) {
      toggle.classList.remove('is-active');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Open navigation menu');
    }

    if (label) label.textContent = 'menu';

    if (overlay) {
      overlay.classList.remove('is-open');
      overlay.setAttribute('aria-hidden', 'true');
    }

    const backdrop = document.getElementById('stayhere-backdrop');
    if (backdrop) backdrop.classList.remove('is-open');

    document.body.classList.remove('nav-menu-open');

    // Restore scroll position
    window.scrollTo(0, scrollPosition);

    // Return focus to toggle
    if (toggle) toggle.focus();
  }

  // ─── Language Dropdown ──────────────────────────────────────────
  function toggleLangDropdown(e) {
    e.stopPropagation();
    if (isLangDropdownOpen) {
      closeLangDropdown();
    } else {
      openLangDropdown();
    }
  }

  function openLangDropdown() {
    isLangDropdownOpen = true;
    const selector = document.getElementById('navLangSelector');
    const dropdown = document.getElementById('langDropdown');
    if (selector) selector.setAttribute('aria-expanded', 'true');
    if (dropdown) dropdown.classList.add('is-open');
  }

  function closeLangDropdown() {
    isLangDropdownOpen = false;
    const selector = document.getElementById('navLangSelector');
    const dropdown = document.getElementById('langDropdown');
    if (selector) selector.setAttribute('aria-expanded', 'false');
    if (dropdown) dropdown.classList.remove('is-open');
  }

  function selectLanguage(langCode) {
    const langData = CONFIG.languages.find(l => l.code === langCode);
    if (!langData) return;

    // Lock user preference
    localStorage.setItem('marragafay_lang', langCode);

    // Dynamic Path Replacement (Robust for local dev subfolders and non-prefixed routes)
    var currentPath = window.location.pathname;
    var pathParts = currentPath.split('/');
    var langIndex = pathParts.findIndex(p => ['en', 'fr', 'es', 'ar'].includes(p));

    if (langIndex !== -1) {
      pathParts[langIndex] = langCode;
    } else {
      // Prepend language code as primary path segment after leading slash
      pathParts.splice(1, 0, langCode);
    }

    var newPath = pathParts.join('/');

    // Environment check: Simple static dev servers (e.g. VS Code Live Server on localhost / 127.0.0.1)
    // do not emulate Vercel's cleanUrls: true. Safely append .html only for localhost environments.
    var isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
    if (isLocal) {
      var currentHasHtml = currentPath.endsWith('.html');
      if (currentHasHtml && !newPath.endsWith('.html')) {
        newPath += '.html';
      } else if (!newPath.endsWith('.html') && (newPath.includes('/packages/') || newPath.includes('/activities/'))) {
        newPath += '.html';
      }
    }

    window.location.href = newPath + window.location.search + window.location.hash;
  }

  // ─── Scroll Handler ─────────────────────────────────────────────
  function handleScroll() {
    const navbar = document.getElementById('ftco-navbar');
    if (!navbar) return;

    if (window.scrollY > CONFIG.scrollThreshold) {
      navbar.classList.add('nav-scrolled');
    } else {
      navbar.classList.remove('nav-scrolled');
    }
  }

  // ─── Active Page Detection ──────────────────────────────────────
  function setActivePage() {
    const currentPage = getCurrentPage();

    // Set active on quick links
    document.querySelectorAll('.nav-quick-link').forEach(link => {
      const href = link.getAttribute('href');
      link.classList.toggle('active', href === currentPage);
    });

    // Set active on menu links
    document.querySelectorAll('.stayhere-menu-overlay .menu-link').forEach(link => {
      const href = link.getAttribute('href');
      if (href === currentPage) {
        link.style.color = 'var(--nav-accent)';
        link.style.fontWeight = '600';
      }
    });
  }

  // ─── Utility: Get Current Page ──────────────────────────────────
  function getCurrentPage() {
    const path = window.location.pathname;
    const page = path.split('/').pop() || 'index.html';
    return page === '' ? 'index.html' : page;
  }

  // ─── Utility: Focus Trap ────────────────────────────────────────
  function trapFocus(container) {
    if (!container) return;

    const focusableElements = container.querySelectorAll(
      'a[href], button:not([disabled]), textarea, input, select, [tabindex]:not([tabindex="-1"])'
    );

    if (focusableElements.length === 0) return;

    const firstFocusable = focusableElements[0];
    const lastFocusable = focusableElements[focusableElements.length - 1];

    // Focus first element
    setTimeout(() => firstFocusable.focus(), CONFIG.animationDelay);

    container.addEventListener('keydown', function handleTab(e) {
      if (e.key !== 'Tab') return;

      if (e.shiftKey) {
        if (document.activeElement === firstFocusable) {
          lastFocusable.focus();
          e.preventDefault();
        }
      } else {
        if (document.activeElement === lastFocusable) {
          firstFocusable.focus();
          e.preventDefault();
        }
      }

      // Remove handler when menu closes
      if (!isMenuOpen) {
        container.removeEventListener('keydown', handleTab);
      }
    });
  }

})();
