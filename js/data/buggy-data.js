/**
 * BUGGY EXPERIENCE DATA
 */
const buggyRidingData = {
    formId: 'buggyRidingForm',
    navActive: 'packages',
    heroImages: ['/images/activites/buggy.webp', '/gallery-pages/buggy/bug-1.jpg', '/gallery-pages/buggy/bug-2.jpg', '/gallery-pages/buggy/bug-3.jpg'],
    heroTitle: 'Agafay',
    heroHighlight: 'Buggy Experience',
    breadcrumbParent: 'Packages',
    breadcrumbParentLink: '../packs.html',
    breadcrumbCurrent: 'Buggy Experience from Marrakech',
    rating: '5.0',
    reviewCount: '180',
    title: 'Private Buggy Experience from Marrakech',
    label: 'BUGGY',
    description: 'A private Buggy experience starting in Marrakech with round-trip transfer, a 1-hour buggy session, a 20-minute camel ride, pool access and mint tea, dinner and live show, cold bottled water, a dedicated guide, and safety equipment with briefing. One 2-seat buggy serves two guests; minimum booking is two guests.',
    highlights: [
        { icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>', text: 'Schedule: Flexible departure (subject to availability)' },
        { icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>', text: 'Location: Agafay Desert' },
        { icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>', text: 'Vehicle: 1h Private Buggy (2 guests per buggy, min 2 guests)' },
        { icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>', text: 'Transport: Private Round-Trip Transfer' }
    ],
    timeline: [
        { icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>', title: 'Private Transfer & Arrival', description: 'Private round-trip transfer from Marrakech, safety briefing, and equipment fitting.' },
        { icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>', title: '1h Private Buggy Driving', description: 'One hour private buggy driving across Agafay terrain with dedicated guide assistance (2 guests per buggy).' },
        { icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>', title: '20min Camel Ride & Sunset Pause', description: 'Scenic camel ride and sunset pause overlooking the desert horizon.' },
        { icon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>', title: 'Dinner, Live Show & Pool Access', description: 'Relax by the pool with mint tea followed by a traditional Moroccan dinner with live music and fire performance.' }
    ],
    // Inclusions
    get inclusions() {
        if (typeof window !== 'undefined' && window.ProductData) {
            var p = window.ProductData.getProduct('buggy');
            if (p && Array.isArray(p.includes)) return p.includes;
        }
        return [
            'Private round-trip pickup from your Marrakech hotel, riad, or another address',
            '1h private buggy ride',
            'One buggy for two guests',
            '20min camel ride',
            'Pool access & Moroccan mint tea',
            'Sunset photo pause',
            'Traditional Moroccan dinner',
            'Live fire & music show',
            'Dedicated guide',
            'Bottled water included',
            'Safety gear & briefing'
        ];
    },
    notIncluded: 'Personal purchases, gratuities (optional).',
    galleryImages: ['/images/activites/buggy.webp', '/gallery-pages/buggy/bug-1.jpg', '/gallery-pages/buggy/bug-2.jpg', '/gallery-pages/buggy/bug-3.jpg'],
    get price() {
        if (typeof window !== 'undefined' && window.ProductData) {
            var p = window.ProductData.getProduct('buggy');
            if (p && p.priceEUR) return p.priceEUR + ' €';
        }
        return '129 €';
    }
};
