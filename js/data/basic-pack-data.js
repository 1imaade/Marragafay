/**
 * BASIC PACK DATA
 * Data configuration for the Basic Pack tour page
 */

const basicPackData = {
    // Metadata
    formId: 'basicPackForm',
    navActive: 'packs',

    // Hero Section
    heroImages: [
        '../images/hotel-2.jpg',
        '../images/slide2.jpg',
        '../images/slide3.jpg',
        '../images/slide4.jpg'
    ],
    heroTitle: 'Agafay',
    heroHighlight: 'Basic Pack',
    breadcrumbParent: 'Packs',
    breadcrumbParentLink: '../packs.html',
    breadcrumbCurrent: 'Basic Pack',

    // Header Info
    rating: '5.0',
    reviewCount: '120',
    title: 'Agafay Desert Basic Pack',
    description: 'Experience the magic of the Agafay Desert with our essential adventure package. Combining thrill and tradition, this is the perfect introduction to Moroccan desert life.',

    // Highlights
    highlights: [
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
            text: 'Duration: 4 Hours'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
            text: 'Location: Agafay Desert'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
            text: 'Guide: Included'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
            text: 'Transport: Optional'
        }
    ],

    // Timeline / Itinerary
    timeline: [
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>',
            title: 'Pickup & Welcome',
            description: 'Your journey begins with a warm welcome and transfer to our luxury camp in the heart of Agafay (if transport selected).'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
            title: 'Quad Biking Adventure (1 Hour)',
            description: 'Feel the adrenaline as you race across the lunar landscapes on our powerful 300cc quads. Safety gear and briefing included.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
            title: 'Camel Trek Sunset (20 Min)',
            description: 'Slow down the pace with a traditional camel ride as the sun sets, painting the desert sky in hues of orange and purple.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>',
            title: 'Dinner & Show',
            description: 'Conclude your evening with a feast of Moroccan delicacies (Tajine, Couscous) accompanied by live Gnaoua music and fire eaters.'
        }
    ],

    // Inclusions
    inclusions: [
        '1 Hour Quad Biking',
        '20 Min Camel Ride',
        'Traditional Dinner',
        'Live Cultural Show',
        'Safety Equipment',
        'Mineral Water'
    ],

    notIncluded: 'Hotel Transfer (Extra), Alcoholic Beverages.',

    // Gallery
    galleryImages: [
        '../images/hotel-2.jpg',
        '../images/destination-2.jpg',
        '../images/destination-3.jpg'
    ],

    // Pricing
    price: '400 MAD'
};
