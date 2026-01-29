// AOS Init - Performance Optimized for 60 FPS
AOS.init({
	duration: 600,  // Reduced from 800ms for faster perceived performance
	easing: 'ease-out-cubic',  // Smoother than 'slide'
	once: true,  // Animate only once (reduces repaints on scroll up)
	offset: 100,  // Trigger animations earlier for smoother feel
	delay: 0,
	disable: function () {
		// Disable on reduced-motion preference (accessibility + performance)
		return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
	},
	// Use passive event listeners for better scroll performance
	useClassNames: false,
	disableMutationObserver: false,
	throttleDelay: 99,  // Throttle scroll events (built-in AOS optimization)
	debounceDelay: 50,  // Debounce window resize events
});

(function ($) {

	"use strict";

	var isMobile = {
		Android: function () {
			return navigator.userAgent.match(/Android/i);
		},
		BlackBerry: function () {
			return navigator.userAgent.match(/BlackBerry/i);
		},
		iOS: function () {
			return navigator.userAgent.match(/iPhone|iPad|iPod/i);
		},
		Opera: function () {
			return navigator.userAgent.match(/Opera Mini/i);
		},
		Windows: function () {
			return navigator.userAgent.match(/IEMobile/i);
		},
		any: function () {
			return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
		}
	};


	$(window).stellar({
		responsive: true,
		parallaxBackgrounds: true,
		parallaxElements: true,
		horizontalScrolling: false,
		hideDistantElements: false,
		scrollProperty: 'scroll'
	});


	var fullHeight = function () {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function () {
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	// loader
	// loader
	// var loader = function () {
	// 	setTimeout(function () {
	// 		if ($('#ftco-loader').length > 0) {
	// 			$('#ftco-loader').removeClass('show');
	// 		}
	// 	}, 1);
	// };
	// loader();

	// Scrollax
	$.Scrollax();

	var carousel = function () {
		$('.carousel-testimony').owlCarousel({
			center: true,
			loop: true,
			items: 1,
			margin: 30,
			stagePadding: 0,
			nav: true,
			navText: ['<span class="ion-ios-arrow-back">', '<span class="ion-ios-arrow-forward">'],
			responsive: {
				0: {
					items: 1
				},
				600: {
					items: 3
				},
				1000: {
					items: 3
				}
			}
		});

		$('.single-slider').owlCarousel({
			animateOut: 'fadeOut',
			animateIn: 'fadeIn',
			autoplay: true,
			loop: true,
			items: 1,
			margin: 0,
			stagePadding: 0,
			nav: true,
			dots: true,
			navText: ['<span class="ion-ios-arrow-back">', '<span class="ion-ios-arrow-forward">'],
			responsive: {
				0: {
					items: 1
				},
				600: {
					items: 1
				},
				1000: {
					items: 1
				}
			}
		});

	};
	carousel();

	$('nav .dropdown').hover(function () {
		var $this = $(this);
		// 	 timer;
		// clearTimeout(timer);
		$this.addClass('show');
		$this.find('> a').attr('aria-expanded', true);
		// $this.find('.dropdown-menu').addClass('animated-fast fadeInUp show');
		$this.find('.dropdown-menu').addClass('show');
	}, function () {
		var $this = $(this);
		// timer;
		// timer = setTimeout(function(){
		$this.removeClass('show');
		$this.find('> a').attr('aria-expanded', false);
		// $this.find('.dropdown-menu').removeClass('animated-fast fadeInUp show');
		$this.find('.dropdown-menu').removeClass('show');
		// }, 100);
	});


	// REMOVED: console.log from dropdown - causes performance overhead

	// scroll
	// scroll (Optimized for Performance)
	var scrollWindow = function () {
		var navbar = $('.ftco_navbar');
		var lastScrollTop = 0;
		var ticking = false;

		$(window).scroll(function () {
			if (!ticking) {
				window.requestAnimationFrame(function () {
					var st = $(window).scrollTop();

					if (st > 20) {
						if (!navbar.hasClass('scrolled')) {
							navbar.addClass('scrolled');
						}
					} else {
						if (navbar.hasClass('scrolled')) {
							navbar.removeClass('scrolled');
						}
					}
					ticking = false;
				});
				ticking = true;
			}
		});
	};
	scrollWindow();

	var isMobile = {
		Android: function () {
			return navigator.userAgent.match(/Android/i);
		},
		BlackBerry: function () {
			return navigator.userAgent.match(/BlackBerry/i);
		},
		iOS: function () {
			return navigator.userAgent.match(/iPhone|iPad|iPod/i);
		},
		Opera: function () {
			return navigator.userAgent.match(/Opera Mini/i);
		},
		Windows: function () {
			return navigator.userAgent.match(/IEMobile/i);
		},
		any: function () {
			return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
		}
	};


	var counter = function () {

		$('#section-counter').waypoint(function (direction) {

			if (direction === 'down' && !$(this.element).hasClass('ftco-animated')) {

				var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',')
				$('.number').each(function () {
					var $this = $(this),
						num = $this.data('number');
					// REMOVED: console.log(num) - performance overhead
					$this.animateNumber(
						{
							number: num,
							numberStep: comma_separator_number_step
						}, 7000
					);
				});

			}

		}, { offset: '95%' });

	}
	counter();

	var contentWayPoint = function () {
		var i = 0;
		$('.ftco-animate').waypoint(function (direction) {

			if (direction === 'down' && !$(this.element).hasClass('ftco-animated')) {

				i++;

				$(this.element).addClass('item-animate');
				setTimeout(function () {

					$('body .ftco-animate.item-animate').each(function (k) {
						var el = $(this);
						setTimeout(function () {
							var effect = el.data('animate-effect');
							if (effect === 'fadeIn') {
								el.addClass('fadeIn ftco-animated');
							} else if (effect === 'fadeInLeft') {
								el.addClass('fadeInLeft ftco-animated');
							} else if (effect === 'fadeInRight') {
								el.addClass('fadeInRight ftco-animated');
							} else {
								el.addClass('fadeInUp ftco-animated');
							}
							el.removeClass('item-animate');
						}, k * 50, 'easeInOutExpo');
					});

				}, 100);

			}

		}, { offset: '95%' });
	};
	contentWayPoint();


	// navigation
	var OnePageNav = function () {
		$(".smoothscroll[href^='#'], #ftco-nav ul li a[href^='#']").on('click', function (e) {
			e.preventDefault();

			var hash = this.hash,
				navToggler = $('.navbar-toggler');
			$('html, body').animate({
				scrollTop: $(hash).offset().top
			}, 700, 'easeInOutExpo', function () {
				window.location.hash = hash;
			});


			if (navToggler.is(':visible')) {
				navToggler.click();
			}
		});
		// REMOVED: console.log from scrollspy - performance overhead
	};
	OnePageNav();


	// Initialize Hero Background Slider with Smooth Zoom
	if ($('.hero-bg-slider').length) {
		$('.hero-bg-slider').owlCarousel({
			items: 1,
			loop: true,
			autoplay: true,
			autoplayTimeout: 15000,   // 15 seconds per slide to match zoom duration
			autoplayHoverPause: false, // Prevent pausing on hover
			smartSpeed: 1000,         // 1 second for fade transition
			animateOut: 'fadeOut',    // Fade out animation
			dots: false,             // No navigation dots
			nav: false,              // No navigation arrows
			touchDrag: false,        // Disable all interactions
			mouseDrag: false,
			pullDrag: false,
			freeDrag: false,
			onInitialized: function () {
				// Ensure content stays on top
				$('.hero-wrap .container').css('position', 'relative').css('z-index', '2');

				// Reset zoom on slide change
				var $slider = $('.hero-bg-slider');
				$slider.on('change.owl.carousel', function () {
					$slider.find('.owl-item').not('.active').find('.slider-bg').css({
						transform: 'scale(1)',
						'-webkit-transform': 'scale(1)'
					});
				});

				// Preload next image
				$slider.on('changed.owl.carousel', function () {
					$slider.find('.owl-item').not('.active').find('img').each(function () {
						var img = new Image();
						img.src = $(this).attr('src');
					});
				});
			}
		});
	}

	// magnific popup
	$('.image-popup').magnificPopup({
		type: 'image',
		closeOnContentClick: true,
		closeBtnInside: false,
		fixedContentPos: true,
		mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
		gallery: {
			enabled: true,
			navigateByImgClick: true,
			preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
		},
		image: {
			verticalFit: true
		},
		zoom: {
			enabled: true,
			duration: 300 // don't foget to change the duration also in CSS
		}
	});

	$('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
		disableOn: 700,
		type: 'iframe',
		mainClass: 'mfp-fade',
		removalDelay: 160,
		preloader: false,

		fixedContentPos: false
	});


	$('.checkin_date, .checkout_date').datepicker({
		'format': 'm/d/yyyy',
		'autoclose': true
	});




})(jQuery);


// Contact Form Handler
document.addEventListener('DOMContentLoaded', function () {
	const contactForm = document.getElementById('contact-form');
	if (contactForm) {
		contactForm.addEventListener('submit', async function (e) {
			e.preventDefault();

			const submitBtn = contactForm.querySelector('button[type="submit"]');
			const originalText = submitBtn.innerText;
			const originalBackground = submitBtn.style.background;

			submitBtn.innerText = 'Sending...';
			submitBtn.disabled = true;

			// Get values
			const formData = new FormData(contactForm);
			const data = {
				name: formData.get('name') || document.querySelector('input[placeholder*="Name"]').value,
				email: formData.get('email') || document.querySelector('input[placeholder*="Email"]').value,
				subject: formData.get('subject') || document.querySelector('input[placeholder*="Subject"]')?.value || 'General Inquiry',
				message: formData.get('message') || document.querySelector('textarea').value,
				status: 'unread'
			};

			try {
				const { error } = await supabaseClient
					.from('messages')
					.insert([data]);

				if (error) throw error;

				// Success UI
				contactForm.reset();
				submitBtn.innerText = 'Message Sent! ✅';
				submitBtn.style.background = '#28a745';
				submitBtn.style.borderColor = '#28a745';
				submitBtn.disabled = false; // Keep it enabled or disabled? User likely wants to see it 'green'

				// Revert after 4 seconds
				setTimeout(() => {
					submitBtn.innerText = originalText;
					submitBtn.style.background = originalBackground;
					submitBtn.style.borderColor = '';
				}, 4000);

			} catch (err) {
				console.error('Error sending message:', err);
				alert('Error: ' + err.message);

				// Revert immediately on error
				submitBtn.innerText = originalText;
				submitBtn.disabled = false;
			}
		});
	}
});
