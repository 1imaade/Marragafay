/**
 * HOT AIR BALLOON ACTIVITY DATA
 * Data configuration for the Hot Air Balloon activity page
 */

const hotAirBalloonData = {
    // Metadata
    formId: 'hotAirBalloonForm',
    navActive: 'activities',

    // Hero Section
    heroImages: [
        '/images/activites/hote-aire.webp',
        '/images/activites/hote-aire.jpeg'
    ],
    heroTitle: 'Marrakech',
    heroHighlight: 'Hot Air Balloon',
    breadcrumbParent: 'Activities',
    breadcrumbParentLink: '../activities.html',
    breadcrumbCurrent: 'Marrakech Sunrise Hot Air Balloon Experience',

    // Header Info
    rating: '4.8',
    reviewCount: 'Marragafay Guest Reviews',
    title: 'Marrakech Sunrise Hot Air Balloon Experience',
    description: 'Experience an early-morning hot air balloon flight near Marrakech with round-trip transport and a Moroccan breakfast included.',

    // Highlights
    highlights: [
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
            text: 'Duration: 4–5 Hours Total (Flight Approx. 40–60 Min)'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
            text: 'Location: Marrakech Countryside'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>',
            text: 'Timing: Early-Morning Pickup'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
            text: 'Transport: Marrakech Round-Trip Included'
        }
    ],

    // Timeline / Itinerary
    timeline: [
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
            title: 'Early-Morning Marrakech Pickup',
            description: 'Meet the driver at the arranged pickup point in Marrakech and travel to the balloon launch area outside the city.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
            title: 'Arrival & Balloon Preparation',
            description: 'Meet the flight team, receive the safety briefing and prepare for takeoff while the balloon is readied for the flight.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
            title: 'Hot Air Balloon Flight',
            description: 'Enjoy approximately 40–60 minutes in the air, depending on weather, wind and safety conditions.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>',
            title: 'Moroccan Breakfast & Return',
            description: 'After landing, enjoy a Moroccan breakfast before the return journey to Marrakech.'
        }
    ],

    // Inclusions
    inclusions: [
        'Marrakech Pickup',
        'Round-Trip Transport',
        'Hot Air Balloon Flight (Approx. 40–60 Min)',
        'Balloon Pilot / Flight Crew',
        'Pre-Flight Safety Briefing',
        'Moroccan Breakfast',
        'Return to Marrakech'
    ],

    notIncluded: 'Personal expenses & tips.',

    // Pricing
    price: '175 €'
};
