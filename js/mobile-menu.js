document.addEventListener('DOMContentLoaded', function() {
  // Elements
  const mobileMenuToggle = document.querySelector('.navbar-toggler');
  const mobileMenuOverlay = document.createElement('div');
  const mobileMenuClose = document.createElement('div');
  
  // Create mobile menu structure
  function createMobileMenu() {
    // Create overlay
    mobileMenuOverlay.className = 'mobile-menu-overlay';
    
    // Create menu content
    const menuContent = document.createElement('div');
    menuContent.className = 'mobile-menu-content';
    
    // Clone the main navigation
    const mainNav = document.querySelector('.navbar-nav').cloneNode(true);
    mainNav.className = 'mobile-menu-nav';
    
    // Remove language switcher from mobile menu
    const languageSwitcher = mainNav.querySelector('.nav-item.dropdown');
    if (languageSwitcher) {
      languageSwitcher.remove();
    }
    
    // Add active class to current page link
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    mainNav.querySelectorAll('.nav-link').forEach(link => {
      const linkHref = link.getAttribute('href');
      if (linkHref === currentPath || 
          (currentPath === '' && linkHref === 'index.html')) {
        link.classList.add('active');
      }
      
      // Close menu when a link is clicked
      link.addEventListener('click', function(e) {
        closeMobileMenu();
      });
    });
    
    // Create close button
    mobileMenuClose.className = 'mobile-menu-close';
    mobileMenuClose.setAttribute('aria-label', 'Close menu');
    
    // Assemble the menu
    menuContent.appendChild(mainNav);
    mobileMenuOverlay.appendChild(menuContent);
    document.body.appendChild(mobileMenuOverlay);
    document.body.appendChild(mobileMenuClose);
    
    // Add event listeners
    mobileMenuToggle.addEventListener('click', toggleMobileMenu);
    mobileMenuClose.addEventListener('click', closeMobileMenu);
    
    // Close menu when clicking outside content
    mobileMenuOverlay.addEventListener('click', function(e) {
      if (e.target === mobileMenuOverlay) {
        closeMobileMenu();
      }
    });
    
    // Close menu with Escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && mobileMenuOverlay.classList.contains('active')) {
        closeMobileMenu();
      }
    });
  }
  
  // Toggle mobile menu
  function toggleMobileMenu() {
    if (mobileMenuOverlay.classList.contains('active')) {
      closeMobileMenu();
    } else {
      openMobileMenu();
    }
  }
  
  // Open mobile menu
  function openMobileMenu() {
    document.body.classList.add('menu-open');
    document.body.classList.add('no-scroll'); // Prevent scrolling
    mobileMenuOverlay.classList.add('active');
    mobileMenuToggle.setAttribute('aria-expanded', 'true');
    
    // Change the menu icon to close icon
    const menuIcon = mobileMenuToggle.querySelector('.icon-menu');
    if (menuIcon) {
      menuIcon.classList.remove('icon-menu');
      menuIcon.classList.add('icon-close');
    }
  }
  
  // Close mobile menu
  function closeMobileMenu() {
    document.body.classList.remove('menu-open');
    document.body.classList.remove('no-scroll'); // Re-enable scrolling
    mobileMenuOverlay.classList.remove('active');
    mobileMenuToggle.setAttribute('aria-expanded', 'false');
    
    // Change the close icon back to menu icon
    const closeIcon = mobileMenuToggle.querySelector('.icon-close');
    if (closeIcon) {
      closeIcon.classList.remove('icon-close');
      closeIcon.classList.add('icon-menu');
    }
  }
  
  // Initialize the mobile menu
  if (mobileMenuToggle) {
    createMobileMenu();
  }
});
