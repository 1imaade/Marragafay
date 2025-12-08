/**
 * QUAD BIKING ACTIVITY DATA
 * Data configuration for the Quad Biking activity page
 */

const quadBikingData = {
    // Metadata
    formId: 'quadBikingForm',
    navActive: 'activities',

    // Hero Section
    heroImages: [
        '../images/destination-2.jpg',
        '../images/hotel-2.jpg',
        '../images/slide2.jpg',
        '../images/slide3.jpg'
    ],
    heroTitle: 'Agafay',
    heroHighlight: 'Quad Biking',
    breadcrumbParent: 'Activities',
    breadcrumbParentLink: '../activities.html',
    breadcrumbCurrent: 'Quad Biking',

    // Header Info
    rating: '4.9',
    reviewCount: '200',
    title: 'Quad Biking Adventure in Agafay Desert',
    description: 'Experience the ultimate adrenaline rush as you race through the stunning Agafay Desert on powerful quad bikes. Navigate lunar-like landscapes and feel the thrill of off-road adventure.',

    // Highlights
    highlights: [
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
            text: 'Duration: 1-2 Hours'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
            text: 'Location: Agafay Desert'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
            text: 'Expert Instructor'
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
            title: 'Arrival & Safety Briefing',
            description: 'Meet your expert guide and receive comprehensive safety instructions and equipment fitting. Learn the basics of quad bike operation.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
            title: 'Practice Session',
            description: 'Get comfortable with your powerful 300cc quad bike in our practice area before heading into the desert.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
            title: 'Desert Adventure',
            description: 'Race across the dramatic Agafay landscapes, navigate dunes, and experience the thrill of off-road driving in one of Morocco\'s most stunning locations.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>',
            title: 'Photo Stops',
            description: 'Pause at scenic viewpoints for stunning photos of you and your quad against the desert backdrop.'
        }
    ],

    // Inclusions
    inclusions: [
        '300cc Quad Bike',
        'Safety Helmet & Goggles',
        'Safety Briefing',
        'Expert Guide',
        'Mineral Water',
        'Insurance Coverage'
    ],

    notIncluded: 'Hotel Transfer (Available as add-on), Personal Items, Photos (Available for purchase).',

    // Gallery
    galleryImages: [
        '../images/destination-2.jpg',
        '../images/hotel-2.jpg',
        '../images/destination-3.jpg'
    ],

    // Pricing
    price: '350 MAD'
};
