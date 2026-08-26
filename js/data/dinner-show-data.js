/**
 * DINNER SHOW ACTIVITY DATA
 * Moroccan Dinner & Live Show in Agafay
 * Verified operational data — do NOT add unverified claims.
 */
const dinnerShowData = {
    formId: 'dinnerShowForm',
    navActive: 'activities',
    heroImages: [
        '/images/activites/show.webp',
        '/images/activites/show.jpeg'
    ],
    heroTitle: 'Agafay',
    heroHighlight: 'Dinner & Show',
    breadcrumbParent: 'Activities',
    breadcrumbParentLink: '../activities.html',
    breadcrumbCurrent: 'Moroccan Dinner & Live Show in Agafay',

    // Header Info
    rating: '4.8',
    reviewCount: 'Marragafay Guest Reviews',
    title: 'Moroccan Dinner & Live Show in Agafay',
    description: 'Enjoy a traditional Moroccan dinner in the Agafay atmosphere followed by live traditional entertainment and a fire show.',

    // Highlights
    highlights: [
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
            text: 'Location: Agafay Camp · Meeting Point'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
            text: 'Live Traditional Entertainment'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
            text: 'Evening Experience'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
            text: 'Transport: Not Included · Agafay Meeting Point'
        }
    ],

    // Timeline / Itinerary (4 conservative verified steps)
    timeline: [
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>',
            title: 'Arrival at the Agafay Camp',
            description: 'Arrive at the camp and settle into the Agafay atmosphere before the evening begins.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>',
            title: 'Relax Before Dinner',
            description: 'Guests arriving early may enjoy complimentary pool access before dinner.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>',
            title: 'Traditional Moroccan Dinner',
            description: 'Enjoy a Moroccan dinner featuring traditional local dishes such as salads, tajine and couscous. Menu may vary.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
            title: 'Live Entertainment & Fire Show',
            description: 'Enjoy traditional live music and evening entertainment, including the fire show.'
        }
    ],

    // Inclusions (7 verified items)
    inclusions: [
        'Traditional Moroccan Dinner',
        'Local Cuisine — Salads, Tajine & Couscous (Menu May Vary)',
        'Live Traditional Entertainment',
        'Traditional Music',
        'Fire Show',
        'Complimentary Pool Access Before Dinner (Early Arrivals)',
        'Children Under 12 Free'
    ],

    notIncluded: 'Marrakech transport · Personal expenses & tips.',

    // Pricing
    price: '25 €'
};
