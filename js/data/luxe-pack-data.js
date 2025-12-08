/**
 * LUXE PACK DATA
 * Data configuration for the Luxe Pack tour page
 */

const luxePackData = {
    // Metadata
    formId: 'luxePackForm',
    navActive: 'packs',

    // Hero Section
    heroImages: [
        '../images/hotel-2.jpg',
        '../images/slide2.jpg',
        '../images/slide3.jpg',
        '../images/slide4.jpg'
    ],
    heroTitle: 'Agafay',
    heroHighlight: 'Luxe Pack',
    breadcrumbParent: 'Packs',
    breadcrumbParentLink: '../packs.html',
    breadcrumbCurrent: 'Luxe Pack',

    // Header Info
    rating: '5.0',
    reviewCount: '78',
    title: 'Agafay Desert Luxe Pack',
    description: 'The ultimate desert luxury experience. An exclusive, all-encompassing journey featuring the finest adventures, gourmet dining, and VIP treatment throughout your entire desert escape.',

    // Highlights
    highlights: [
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
            text: 'Duration: Full Day (8 Hours)'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
            text: 'Location: Exclusive Agafay Area'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
            text: 'Personal Concierge'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
            text: 'Luxury SUV Transport'
        }
    ],

    // Timeline / Itinerary
    timeline: [
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>',
            title: 'VIP Pickup & Breakfast',
            description: 'Luxury SUV pickup from your riad/hotel with champagne welcome and gourmet breakfast at our exclusive desert pavilion.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
            title: 'All-Access Adventure (3 Hours)',
            description: 'Unlimited quad biking, buggy racing, and dune bashing with your personal instructor. All premium equipment and refreshments included.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
            title: 'Luxury Lounge & Spa Treatment',
            description: 'Relax in our air-conditioned premium lounge with traditional hammam spa treatment, massage, and afternoon tea service.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
            title: 'Private Camel Caravan (1 Hour)',
            description: 'Exclusive private camel caravan with your personal guide, photographer, and Berber storyteller through untouched desert landscapes.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>',
            title: 'Chef\'s Table Dinner Experience',
            description: 'Private dining experience with our master chef preparing an exclusive 7-course tasting menu featuring rare Moroccan ingredients and wine pairing.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>',
            title: 'Private Entertainment & Return',
            description: 'Exclusive live performance by renowned Moroccan artists, bonfire ceremony, and luxury vehicle return with complimentary photo album.'
        }
    ],

    // Inclusions
    inclusions: [
        'Luxury SUV Transfer',
        'Personal Concierge Service',
        'Gourmet Breakfast',
        '3 Hours All Activities',
        'Spa & Hammam Treatment',
        '1 Hour Private Camel Trek',
        '7-Course Chef\'s Dinner',
        'Premium Wine Pairing',
        'Private Entertainment',
        'Professional Photography',
        'Stargazing with Astronomer',
        'Photo Album & Video',
        'All Premium Equipment',
        'Unlimited Beverages'
    ],

    notIncluded: 'Personal Purchases, Gratuities (at your discretion).',

    // Gallery
    galleryImages: [
        '../images/hotel-2.jpg',
        '../images/destination-2.jpg',
        '../images/destination-3.jpg'
    ],

    // Pricing
    price: '1200 MAD'
};
