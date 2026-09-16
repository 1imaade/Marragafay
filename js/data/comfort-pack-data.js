/**
 * COMFORT PACK DATA (PRIVATE)
 * Data configuration for the Private Pack tour page
 */

const comfortPackData = {
    // Metadata
    formId: 'comfortPackForm',
    navActive: 'packs',

    // Hero Section
    heroImages: [
        '../images/hotel-2.jpg',
        '../images/slide2.jpg',
        '../images/slide3.jpg',
        '../images/slide4.jpg'
    ],
    heroTitle: 'Agafay',
    heroHighlight: 'Private Pack',
    breadcrumbParent: 'Packs',
    breadcrumbParentLink: '../packs.html',
    breadcrumbCurrent: 'Private Agafay Evening',

    // Header Info
    rating: '5.0',
    reviewCount: '95',
    title: 'Private Agafay Evening',
    label: 'PRIVATE',
    description: 'Elevate your desert evening with our fully Private experience. Featuring private door-to-door transfer, 1h30 private quad, 20min camel trek, dedicated guide, desert scarf to keep, Moroccan dinner, live show, and Moroccan sweets.',

    // Highlights
    highlights: [
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
            text: 'Schedule: 15:30 — 22:00'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
            text: 'Location: Agafay Desert'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
            text: 'Guide: Dedicated Guide Included'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
            text: 'Transport: Private Round-Trip Transfer'
        }
    ],

    // Timeline / Itinerary
    timeline: [
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>',
            title: '15:30 — Private Transfer & Desert Welcome',
            description: 'Enjoy seamless, private round-trip transportation directly from your Marrakech hotel or riad to our desert camp.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
            title: '1h30 Private Quad Biking',
            description: 'Extended 90-minute private quad biking session with your dedicated guide navigating scenic dunes and private desert tracks.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
            title: '20min Camel Trek & Sunset Pause',
            description: 'Tranquil 20-minute camel trek with a dedicated pause at a prime vantage point to watch the Agafay sunset.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>',
            title: 'Pool Access, Mint Tea & Desert Scarf',
            description: 'Relax by the pool with Moroccan mint tea, receive an authentic desert scarf (cheche) to wear and keep, and enjoy bottled water + soft drinks.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>',
            title: 'Moroccan Dinner, Live Show & Moroccan Sweets',
            description: 'Delicious traditional Moroccan dinner paired with live Gnawa music, fire performers, and sweet pastries before private return at 22:00.'
        }
    ],

    // Inclusions
    inclusions: [
        'Private round-trip transfer',
        '1h30 private quad',
        '20min camel',
        'Pool + mint tea',
        'Sunset pause',
        'Dinner + live show',
        'Dedicated guide',
        'Desert scarf to wear & keep',
        'Bottled water + soft drink',
        'Moroccan sweets',
        'Safety gear & briefing'
    ],

    notIncluded: 'Personal purchases, gratuities (optional).',

    // Gallery
    galleryImages: [
        '../images/hotel-2.jpg',
        '../images/destination-2.jpg',
        '../images/destination-3.jpg'
    ],

    // Pricing
    price: '75 €'
};
