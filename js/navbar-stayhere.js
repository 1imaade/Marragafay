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
    menuItems: {
      experiencesPacks: [
        { label: 'Marragafay Signature Agafay Escape', href: 'packages/comfort.html' },
        { label: 'Marragafay VIP Luxury Desert Retreat', href: 'packages/luxe.html' },
        { label: 'Marragafay Complete Discovery Expedition', href: 'packages/basic.html' },
      ],
      experiencesActivities: [
        { label: 'Marragafay Extreme Quad Biking Adventure', href: 'activities/quad-biking.html' },
        { label: 'Marragafay Traditional Camel Ride Trek', href: 'activities/camel-ride.html' },
        { label: 'Marragafay Dune Buggy Adrenaline Safari', href: 'activities/buggy.html' },
        { label: 'Marragafay Sunrise Hot Air Balloon Flight', href: 'activities/hot-air-balloon.html' },
        { label: 'Marragafay Atlas Mountains Paragliding', href: 'activities/paragliding.html' },
        { label: 'Marragafay Nomadic Desert Dinner & Show', href: 'activities/dinner-show.html' },
      ],
      brand: [
        { label: 'About Marragafay', href: 'about.html' },
        { label: 'Customer Reviews', href: 'reviews.html' },
        { label: 'Our Blog', href: 'blog.html' },
        { label: 'Careers', href: 'about.html' },
        { label: 'FAQ', href: 'about.html' },
      ],
      packs: [
        { label: 'Agafay Discovery Pack', href: 'packages/basic.html' },
        { label: 'VIP Luxury Escape', href: 'packages/luxe.html' },
        { label: 'Romantic Sunset Pack', href: 'packages/comfort.html' },
      ],
      booking: [
        { label: 'Book an Experience', href: 'packs.html', arrow: true },
        { label: 'Contact Concierge', href: 'contact.html', arrow: true },
      ],
    },
    languages: [
      { code: 'en', label: 'English', dir: 'ltr' },
      { code: 'fr', label: 'Français', dir: 'ltr' },
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

  // ─── DOM Ready ──────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', init);

  function init() {
    injectNavbarHTML();
    injectMenuOverlayHTML();
    bindEvents();
    setActivePage();
    handleScroll(); // Initial check
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
        <a href="${basePath}activities.html" class="nav-quick-link${currentPage === 'activities.html' ? ' active' : ''}">Activities</a>
        <a href="${basePath}packs.html" class="nav-quick-link${currentPage === 'packs.html' ? ' active' : ''}">Packs</a>
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
          <a href="${basePath}index.html" class="nav-logo" aria-label="Marragafay - Return to homepage">
            <img src="${basePath}images/logo-no-text.png" 
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
              <path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
            </svg>
            <span class="lang-code">EN</span>
            <svg class="lang-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <polyline points="6 9 12 15 18 9"/>
            </svg>
          </button>
          <div class="lang-dropdown" id="langDropdown" role="menu">
            ${CONFIG.languages.map(lang => `
              <button class="lang-option${lang.code === 'en' ? ' active' : ''}" 
                      role="menuitem"
                      data-lang="${lang.code}" 
                      ${lang.dir === 'rtl' ? 'dir="rtl"' : ''}>
                ${lang.label}
              </button>
            `).join('')}
          </div>
          <a href="${basePath}packs.html" class="nav-cta" id="navBookCta">Book</a>
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
  function injectMenuOverlayHTML() {
    const currentPage = getCurrentPage();
    const isMobile = window.innerWidth <= 768;
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
              <h3 style="font-size: 10px; font-weight: 600; margin-bottom: 16px; text-transform: uppercase; color: #10100E; letter-spacing: normal;">Experiences</h3>
              
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
                    <a href="${basePath}${item.href}" style="display: block; font-size: 14px; line-height: 20px; font-weight: 300; color: #5c5c56; text-transform: capitalize; text-decoration: none; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#5c5c56'">
                      ${item.label}
                    </a>
                  `).join('')}
                </div>
              </details>

              <!-- Activities Accordion -->
              <details class="group" style="margin-bottom: 16px;">
                <summary style="font-weight: 600; font-size: 14px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; color: #272724; list-style: none;">
                  <div style="display: flex; align-items: center; gap: 6px;">
                    Activities <span style="font-size: 13px; font-weight: 400; color: #b8b5a6;">(6)</span>
                  </div>
                  <svg style="width: 16px; height: 16px; transition: transform 0.2s;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="chevron-icon">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
                  </svg>
                </summary>
                <div style="padding-top: 12px; padding-bottom: 8px; display: flex; flex-direction: column; gap: 12px; padding-left: 16px;">
                  ${CONFIG.menuItems.experiencesActivities.map(item => `
                    <a href="${basePath}${item.href}" style="display: block; font-size: 14px; line-height: 20px; font-weight: 300; color: #5c5c56; text-transform: capitalize; text-decoration: none; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#5c5c56'">
                      ${item.label}
                    </a>
                  `).join('')}
                </div>
              </details>
            </div>

            <!-- THE BRAND -->
            <div style="margin-bottom: 32px;">
              <h3 style="font-size: 10px; font-weight: 600; margin-bottom: 16px; text-transform: uppercase; color: #10100E; letter-spacing: normal;">The Brand</h3>
              <div style="display: flex; flex-direction: column; gap: 2px;">
                ${CONFIG.menuItems.brand.map(item => `
                  <a href="${basePath}${item.href}" style="display: block; font-size: 14px; line-height: 20px; font-weight: 600; color: #171716; text-transform: capitalize; text-decoration: none; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#171716'">
                    ${item.label}
                  </a>
                `).join('')}
              </div>
            </div>

            <!-- STAY WITH US -->
            <div style="margin-bottom: 16px;">
              <h3 style="font-size: 10px; font-weight: 600; margin-bottom: 16px; text-transform: uppercase; color: #10100E; letter-spacing: normal;">Stay with us</h3>
              <div style="display: flex; flex-direction: column; gap: 2px;">
                ${CONFIG.menuItems.packs.map(item => `
                  <a href="${basePath}${item.href}" style="display: block; font-size: 14px; line-height: 20px; font-weight: 600; color: #171716; text-decoration: none; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#171716'">
                    ${item.label}
                  </a>
                `).join('')}
              </div>

              <hr style="border: none; border-top: 1px solid #e2e0d3; margin: 24px 0;" />

              <h3 style="font-size: 10px; font-weight: 600; margin-bottom: 12px; text-transform: uppercase; color: #10100E; letter-spacing: normal;">Direct booking</h3>
              <div style="display: flex; flex-direction: column; gap: 12px;">
                ${CONFIG.menuItems.booking.map(item => `
                  <a href="${basePath}${item.href}" style="display: block; font-size: 14px; font-weight: 400; color: #5c5c56; text-decoration: none; padding-top: 4px;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#5c5c56'">
                    ${item.label} &rarr;
                  </a>
                `).join('')}
              </div>
            </div>
            
            <!-- Mobile: Language Options -->
            <div class="mobile-lang-section" style="margin-top: 40px; padding-bottom: 24px;">
              ${CONFIG.languages.map(lang => `
                <button class="mobile-lang-item${lang.code === 'en' ? ' active' : ''}" 
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
            <button onclick="window.location.href='${basePath}book.html'" style="width: 100%; background-color: #523225; color: #F6F7EA; font-weight: 600; padding: 14px 0; border: none; border-radius: 50px; cursor: pointer; transition: opacity 0.2s; font-size: 14px;" onmouseover="this.style.opacity='0.9'" onmouseout="this.style.opacity='1'">
              Book Your Experience
            </button>
          </div>
        </div>
      `;
    } else {
      overlay.innerHTML = `
        <div class="menu-content">
          <!-- Column 1: Experiences -->
          <div class="menu-column">
            <p class="menu-column-title" style="text-transform: capitalize; font-weight: 600; color: #10100E;">Experiences</p>

            <p class="menu-subgroup-title" style="margin-top:0; display:flex; align-items:center; gap:6px;">
              Packs <span style="font-size:13px; font-weight:400; color:#b8b5a6;">(3)</span>
            </p>
            <ul class="menu-links menu-links--indented">
              ${CONFIG.menuItems.experiencesPacks.map(item => `
                <li class="menu-link-item">
                  <a href="${basePath}${item.href}" class="menu-link menu-link--l3 menu-link--muted${item.href === currentPage ? ' active' : ''}">
                    ${item.label}
                  </a>
                </li>
              `).join('')}
            </ul>

            <p class="menu-subgroup-title" style="display:flex; align-items:center; gap:6px;">
              Activities <span style="font-size:13px; font-weight:400; color:#b8b5a6;">(6)</span>
            </p>
            <ul class="menu-links menu-links--indented">
              ${CONFIG.menuItems.experiencesActivities.map(item => `
                <li class="menu-link-item">
                  <a href="${basePath}${item.href}" class="menu-link menu-link--l3 menu-link--muted${item.href === currentPage ? ' active' : ''}">
                    ${item.label}
                  </a>
                </li>
              `).join('')}
            </ul>
          </div>

          <!-- Column 2: The Brand -->
          <div class="menu-column">
            <p class="menu-column-title" style="text-transform: capitalize; font-weight: 600; color: #10100E;">The Brand</p>
            <ul class="menu-links" style="margin-left: 0; padding-left: 0;">
              ${CONFIG.menuItems.brand.map(item => `
                <li class="menu-link-item" style="margin-bottom: 2px;">
                  <a href="${basePath}${item.href}" class="menu-link${item.href === currentPage ? ' active' : ''}" style="font-size: 14px; line-height: 20px; font-weight: 600; color: #171716; text-transform: capitalize; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#171716'">
                    ${item.label}
                  </a>
                </li>
              `).join('')}
            </ul>
          </div>

          <!-- Column 3: Stay with us -->
          <div class="menu-column">
            <p class="menu-column-title" style="text-transform: lowercase;">Stay with us</p>

            <ul class="menu-links" style="margin-left: 0; padding-left: 0;">
              ${CONFIG.menuItems.packs.map(item => `
                <li class="menu-link-item" style="margin-bottom: 2px;">
                  <a href="${basePath}${item.href}" class="menu-link${item.href === currentPage ? ' active' : ''}" style="font-size: 14px; line-height: 20px; font-weight: 600; color: #171716; -webkit-font-smoothing: antialiased;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#171716'">
                    ${item.label}
                  </a>
                </li>
              `).join('')}
            </ul>

            <hr style="border: none; border-top: 1px solid #e2e0d3; margin: 24px 0;" />

            <p style="font-size: 10px; line-height: 15px; font-weight: 600; color: #10100E; text-transform: uppercase; margin-bottom: 12px; margin-top: 0;">Direct booking</p>
            <ul class="menu-links" style="margin-bottom: 0;">
              ${CONFIG.menuItems.booking.map(item => `
                <li class="menu-link-item" style="margin-bottom: 12px;">
                  <a href="${basePath}${item.href}" class="menu-link${item.href === currentPage ? ' active' : ''}" style="font-size: 14px; font-weight: 400; color: #5c5c56;" onmouseover="this.style.color='#523225'" onmouseout="this.style.color='#5c5c56'">
                    ${item.label} &rarr;
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

    // Update displayed code
    const codeEl = document.querySelector('.lang-code');
    if (codeEl) codeEl.textContent = langCode.toUpperCase();

    // Update active states
    document.querySelectorAll('.lang-option').forEach(opt => {
      opt.classList.toggle('active', opt.dataset.lang === langCode);
    });
    document.querySelectorAll('.mobile-lang-item').forEach(opt => {
      opt.classList.toggle('active', opt.dataset.lang === langCode);
    });

    closeLangDropdown();
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
