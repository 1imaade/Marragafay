(function () {
  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement('script');
      s.src = src; s.async = true; s.onload = resolve; s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  function ensureRoot() {
    var root = document.getElementById('page-root');
    if (!root) {
      root = document.createElement('div');
      root.id = 'page-root';
      document.body.insertBefore(root, document.body.firstChild);
    }
    return root;
  }

  function hideLegacy() {
    var style = document.createElement('style');
    style.setAttribute('data-basic-refactor', 'true');
    style.textContent = 'body > :not(#page-root):not(script){display:none !important;}';
    document.head.appendChild(style);
  }

  function initHeroSlider() {
    if (!window.jQuery || !window.jQuery.fn || !window.jQuery.fn.owlCarousel) return;
    var $ = window.jQuery;
    if ($('.hero-bg-slider').length) {
      $('.hero-bg-slider').owlCarousel({
        items: 1,
        loop: true,
        autoplay: true,
        autoplayTimeout: 15000,
        autoplayHoverPause: false,
        smartSpeed: 1000,
        animateOut: 'fadeOut',
        dots: false,
        nav: false,
        touchDrag: false,
        mouseDrag: false,
        pullDrag: false,
        freeDrag: false,
        onInitialized: function () {
          $('.hero-wrap .container').css('position', 'relative').css('z-index', '2');
          var $slider = $('.hero-bg-slider');
          $slider.on('change.owl.carousel', function () {
            $slider.find('.owl-item').not('.active').find('.slider-bg').css({
              transform: 'scale(1)',
              '-webkit-transform': 'scale(1)'
            });
          });
          $slider.on('changed.owl.carousel', function () {
            $slider.find('.owl-item').not('.active').find('img').each(function () {
              var img = new Image();
              img.src = $(this).attr('src');
            });
          });
        }
      });
    }
  }

  function renderBasic() {
    var data = {
      title: "Agafay Desert Basic Pack",
      subTitle: "Packs",
      price: "400 MAD",
      description: "Experience the magic of the Agafay Desert with our essential adventure package. Combining thrill and tradition, this is the perfect introduction to Moroccan desert life.",
      heroImages: [
        "../images/hotel-2.jpg",
        "../images/slide2.jpg",
        "../images/slide3.jpg",
        "../images/slide4.jpg"
      ],
      rating: "5.0",
      reviews: "120+",
      heroTitleHtml: "Agafay <span style=\"color: #d4af37; text-shadow: 0 0 5px rgba(255, 255, 255, 0.3);\">Basic Pack</span>",
      breadcrumbs: [
        { href: "../index.html", label: "Home" },
        { href: "../packs.html", label: "Packs" },
        { label: "Basic Pack" }
      ],
      highlights: [
        { icon: "clock", text: "Duration: 4 Hours" },
        { icon: "mapPin", text: "Location: Agafay Desert" },
        { icon: "user", text: "Guide: Included" },
        { icon: "bus", text: "Transport: Optional" }
      ],
      timeline: [
        { title: "Pickup & Welcome", text: "Your journey begins with a warm welcome and transfer to our luxury camp in the heart of Agafay (if transport selected).", icon: "bus" },
        { title: "Quad Biking Adventure (1 Hour)", text: "Feel the adrenaline as you race across the lunar landscapes on our powerful 300cc quads. Safety gear and briefing included.", icon: "clock" },
        { title: "Camel Trek Sunset (20 Min)", text: "Slow down the pace with a traditional camel ride as the sun sets, painting the desert sky in hues of orange and purple.", icon: "star" },
        { title: "Dinner & Show", text: "Conclude your evening with a feast of Moroccan delicacies (Tajine, Couscous) accompanied by live Gnaoua music and fire eaters.", icon: "check" }
      ],
      included: [
        "1 Hour Quad Biking",
        "20 Min Camel Ride",
        "Traditional Dinner",
        "Live Cultural Show",
        "Safety Equipment",
        "Mineral Water"
      ],
      notIncluded: "Hotel Transfer (Extra), Alcoholic Beverages.",
      gallery: [
        "../images/hotel-2.jpg",
        "../images/destination-2.jpg",
        "../images/destination-3.jpg"
      ]
    };

    ensureRoot();
    hideLegacy();
    if (window.TourPageTemplate && typeof TourPageTemplate.render === 'function') {
      TourPageTemplate.render(data, 'page-root');
      initHeroSlider();
    } else {
      loadScript('../js/TourPageTemplate.js')
        .then(function () { TourPageTemplate.render(data, 'page-root'); initHeroSlider(); })
        .catch(function (err) { console.error('Failed to load TourPageTemplate.js', err); });
    }
  }

  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    setTimeout(renderBasic, 0);
  } else {
    document.addEventListener('DOMContentLoaded', renderBasic);
  }
})();
