// First-touch acquisition context for the static Marragafay site.
// The first touch is stable for the browser session. A later explicit campaign
// click is kept separately as last_touch so it cannot overwrite first_touch.
(function (window, document) {
    'use strict';

    const STORAGE_KEY = 'marragafay_attribution_v1';
    const VERSION = 1;
    const SUPPORTED_LANGUAGES = new Set(['en', 'fr', 'es', 'ar']);
    const memoryStorage = { value: null };

    function cleanString(value, maxLength) {
        if (typeof value !== 'string') return '';
        return value
            .replace(/[\u0000-\u001F\u007F]/g, '')
            .trim()
            .slice(0, maxLength);
    }

    function normalizePath(value) {
        const path = cleanString(value || '/', 400).split(/[?#]/)[0];
        return path.startsWith('/') && !path.startsWith('//') ? path || '/' : '/';
    }

    function normalizeReferrer(value) {
        const referrer = cleanString(value, 2_000);
        if (!referrer) return '';
        try {
            const url = new URL(referrer);
            if (!['http:', 'https:'].includes(url.protocol)) return '';
            return `${url.origin}${url.pathname || '/'}`.slice(0, 2_000);
        } catch {
            return '';
        }
    }

    function languageFromDocument() {
        const raw = cleanString(document.documentElement?.lang || navigator.language || 'en', 10).toLowerCase();
        const language = raw.split('-')[0];
        return SUPPORTED_LANGUAGES.has(language) ? language : 'en';
    }

    function referrerHost(referrer) {
        try {
            return new URL(referrer).hostname.toLowerCase().replace(/^www\./, '');
        } catch {
            return '';
        }
    }

    function hostMatches(host, suffix) {
        return host === suffix || host.endsWith(`.${suffix}`);
    }

    function hasCampaign(touch) {
        return Boolean(
            touch?.utm_source || touch?.utm_medium || touch?.utm_campaign ||
            touch?.utm_term || touch?.utm_content || touch?.gclid || touch?.fbclid
        );
    }

    function classifySource(touch) {
        const source = cleanString(touch?.utm_source, 100).toLowerCase();
        const medium = cleanString(touch?.utm_medium, 100).toLowerCase();
        const host = referrerHost(touch?.referrer || '');
        const instagram = source === 'instagram' || source === 'ig' || hostMatches(host, 'instagram.com');
        const facebook = source === 'facebook' || source === 'fb' || hostMatches(host, 'facebook.com');
        const google = source === 'google' || /^google\.[a-z.]+$/.test(host);
        const search = google || ['bing.com', 'yahoo.com', 'duckduckgo.com'].some((domain) => hostMatches(host, domain));
        const paidMedium = /^(cpc|ppc|paid|paid_social|display|retargeting|sponsored)$/i.test(medium);

        if (touch?.gclid) return 'google_ads';
        if (instagram) return 'instagram';
        if (touch?.fbclid) return 'facebook';
        if (facebook) return 'facebook';
        if (google && paidMedium) return 'google_ads';
        if (paidMedium) return 'other_paid';
        if (search) return 'google_organic';
        if (!host && !hasCampaign(touch)) return 'direct';
        if (host) return 'referral';
        if (hasCampaign(touch)) return 'other';
        return 'other';
    }

    function currentTouch() {
        const url = new URL(window.location.href);
        const params = url.searchParams;
        const landingPage = normalizePath(url.pathname || '/');
        return {
            landing_page: landingPage,
            referrer: normalizeReferrer(document.referrer),
            utm_source: cleanString(params.get('utm_source') || '', 100),
            utm_medium: cleanString(params.get('utm_medium') || '', 100),
            utm_campaign: cleanString(params.get('utm_campaign') || '', 200),
            utm_term: cleanString(params.get('utm_term') || '', 200),
            utm_content: cleanString(params.get('utm_content') || '', 200),
            gclid: cleanString(params.get('gclid') || '', 200),
            fbclid: cleanString(params.get('fbclid') || '', 200),
            language: languageFromDocument(),
            first_touch_timestamp: new Date().toISOString(),
            session_entry_path: landingPage
        };
    }

    function storageAreas() {
        const areas = [];
        try {
            if (window.sessionStorage) areas.push(window.sessionStorage);
        } catch {}
        try {
            if (window.localStorage) areas.push(window.localStorage);
        } catch {}
        return areas;
    }

    function readStored() {
        for (const storage of storageAreas()) {
            try {
                const raw = storage.getItem(STORAGE_KEY);
                if (raw) return JSON.parse(raw);
            } catch {}
        }
        return memoryStorage.value;
    }

    function writeStored(value) {
        memoryStorage.value = value;
        for (const storage of storageAreas()) {
            try {
                storage.setItem(STORAGE_KEY, JSON.stringify(value));
                return;
            } catch {}
        }
    }

    function capture() {
        const current = currentTouch();
        const stored = readStored();
        const next = stored && stored.version === VERSION && stored.first_touch
            ? { version: VERSION, first_touch: stored.first_touch, last_touch: stored.last_touch || null }
            : { version: VERSION, first_touch: current, last_touch: hasCampaign(current) ? current : null };

        // Explicit later campaigns become last_touch only. Navigation without
        // campaign parameters never changes either first_touch or last_touch.
        if (stored?.first_touch && hasCampaign(current)) next.last_touch = current;
        writeStored(next);
        return next;
    }

    function clone(value) {
        return JSON.parse(JSON.stringify(value));
    }

    function getBookingAttribution() {
        const stored = capture();
        const effectiveTouch = stored.last_touch && hasCampaign(stored.last_touch)
            ? stored.last_touch
            : stored.first_touch;
        const bookingPage = normalizePath(window.location.pathname || '/');

        return {
            version: VERSION,
            source_category: classifySource(effectiveTouch),
            first_touch: clone(stored.first_touch),
            last_touch: stored.last_touch ? clone(stored.last_touch) : null,
            booking_page: bookingPage
        };
    }

    window.MarragafayAttribution = Object.freeze({
        storageKey: STORAGE_KEY,
        classifySource,
        capture,
        getBookingAttribution
    });

    capture();
})(window, document);
