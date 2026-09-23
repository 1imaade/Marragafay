/**
 * LUXE PACK DATA (PRIVATE+)
 * Data configuration for the Private+ Pack tour page
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
    heroHighlight: 'Private+ Pack',
    breadcrumbParent: 'Packs',
    breadcrumbParentLink: '../packs.html',
    breadcrumbCurrent: 'Private+ Full-Day Agafay Experience',

    // Header Info
    rating: '5.0',
    reviewCount: '78',
    title: 'Private+ Full-Day Agafay Experience',
    label: 'PRIVATE+',
    description: 'A full-day Agafay experience with private round-trip transfer, 3h private quad exploration, lunch and dinner reserved exclusively for your group, pool access, 45min camel ride, sunset pause, live show, a dedicated full-day guide, a cheche gift, Moroccan pastry gift, cold bottled water, and one soft drink. The route is confirmed before the experience.',

    // Highlights
    highlights: [
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
            text: 'Schedule: 09:00 — 22:00 (Full Day)'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
            text: 'Location: Agafay Desert'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
            text: 'Guide: Dedicated Full-Day Guide'
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
            title: '09:00 — Private Morning Pickup',
            description: 'Private round-trip pickup from your hotel, riad, or another address in Marrakech for your full-day experience.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
            title: '3h Private Quad Exploration in Agafay',
            description: 'A 3-hour private quad exploration in Agafay with your dedicated full-day guide. The exact route is confirmed before the experience.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>',
            title: 'Group Lunch & Pool Relaxation',
            description: 'Enjoy a Moroccan lunch reserved exclusively for your group, followed by pool access and traditional mint tea.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
            title: '45min Camel Trek & Sunset Pause',
            description: 'Extended 45-minute camel trek through pristine dunes with a dedicated sunset pause.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>',
            title: 'Group Dinner, Live Show & Return',
            description: 'Enjoy a Moroccan dinner reserved exclusively for your group, followed by the live show and private transfer back to Marrakech.'
        }
    ],

    // Inclusions
    get inclusions() {
        if (typeof window !== 'undefined' && window.ProductData) {
            var p = window.ProductData.getProduct('private-plus');
            if (p && Array.isArray(p.includes)) return p.includes;
        }
        return [
            'Private round-trip pickup from your hotel, riad, or another address in Marrakech',
            '3h private quad exploration in Agafay',
            'Moroccan lunch reserved exclusively for your group',
            'Pool access & Moroccan mint tea',
            '45min camel ride',
            'Sunset pause',
            'Moroccan dinner reserved exclusively for your group',
            'Live fire & music show',
            'Dedicated full-day guide',
            'Desert scarf to wear & keep',
            'Bottled water + soft drink',
            'Moroccan sweets',
            'Safety gear & briefing'
        ];
    },

    notIncluded: 'Personal purchases, gratuities (optional).',

    // Gallery
    galleryImages: [
        '../images/hotel-2.jpg',
        '../images/destination-2.jpg',
        '../images/destination-3.jpg'
    ],

    // Pricing
    get price() {
        if (typeof window !== 'undefined' && window.ProductData) {
            var p = window.ProductData.getProduct('private-plus');
            if (p && p.priceEUR) return p.priceEUR + ' €';
        }
        return '119 €';
    }
};
