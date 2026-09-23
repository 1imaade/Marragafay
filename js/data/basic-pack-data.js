/**
 * BASIC PACK DATA (STANDARD)
 * Data configuration for the Standard Pack tour page
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
    heroHighlight: 'Standard Pack',
    breadcrumbParent: 'Packs',
    breadcrumbParentLink: '../packs.html',
    breadcrumbCurrent: 'Agafay Evening Experience',

    // Header Info
    rating: '5.0',
    reviewCount: '120',
    title: 'Agafay Evening Experience',
    label: 'STANDARD',
    description: 'Experience the magic of the Agafay Desert with our essential Standard evening experience. Combining thrilling quad biking, peaceful camel riding, sunset pause, Moroccan dinner, and live show.',

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
            text: 'Activities: 1h Quad & 20min Camel'
        },
        {
            icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
            text: 'Transport: Shared round-trip pickup from your hotel, riad, or another address in Marrakech'
        }
    ],

    // Timeline / Itinerary
    timeline: [
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>',
            title: '15:30 — Shared Pickup & Welcome',
            description: 'Shared round-trip pickup from your hotel, riad, or another address in Marrakech and transfer to our desert camp in Agafay.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
            title: 'Quad Biking Adventure (1 Hour)',
            description: 'Navigate the desert dunes and lunar trails on a 1-hour quad biking ride. Safety gear and briefing included.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
            title: 'Camel Trek & Sunset Photo Pause (20 Min)',
            description: 'Experience a peaceful 20-minute camel trek across the desert ridgeline with a dedicated stop for sunset photos.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>',
            title: 'Pool Access & Traditional Mint Tea',
            description: 'Unwind by the pool with authentic Moroccan mint tea and refreshing bottled water.'
        },
        {
            icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>',
            title: 'Moroccan Dinner & Live Show',
            description: 'Savor a traditional multi-course Moroccan dinner accompanied by live Berber music and a spectacular fire show before returning to Marrakech at 22:00.'
        }
    ],

    // Inclusions
    get inclusions() {
        if (typeof window !== 'undefined' && window.ProductData) {
            var p = window.ProductData.getProduct('standard');
            if (p && Array.isArray(p.includes)) return p.includes;
        }
        return [
            'Shared round-trip pickup from your hotel, riad, or another address in Marrakech',
            '1h quad biking',
            '20min camel ride',
            'Pool access & Moroccan mint tea',
            'Sunset photo pause',
            'Traditional Moroccan dinner',
            'Live fire & music show',
            'Bottled water',
            'Safety gear & briefing'
        ];
    },

    notIncluded: 'Personal purchases, optional tips, extra drinks.',

    // Gallery
    galleryImages: [
        '../images/hotel-2.jpg',
        '../images/destination-2.jpg',
        '../images/destination-3.jpg'
    ],

    // Pricing
    get price() {
        if (typeof window !== 'undefined' && window.ProductData) {
            var p = window.ProductData.getProduct('standard');
            if (p && p.priceEUR) return p.priceEUR + ' €';
        }
        return '45 €';
    }
};
