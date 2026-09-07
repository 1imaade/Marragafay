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

    const INQUIRIES_STORAGE_KEY = 'marragafay_inquiries_v1';

    function generateInquiryId() {
        return 'INQ-' + Date.now().toString(36).toUpperCase() + '-' + Math.random().toString(36).substring(2, 6).toUpperCase();
    }

    function recordInquiry(data) {
        if (!data || !data.inquiry_id) return;
        try {
            const raw = window.localStorage?.getItem(INQUIRIES_STORAGE_KEY);
            const list = raw ? JSON.parse(raw) : [];
            const filtered = Array.isArray(list) ? list.slice(-50) : [];
            filtered.push({
                ...clone(data),
                recorded_at: new Date().toISOString()
            });
            window.localStorage?.setItem(INQUIRIES_STORAGE_KEY, JSON.stringify(filtered));
        } catch {}
    }

    function getBookingAttribution(extraContext = {}) {
        const stored = capture();
        const effectiveTouch = stored.last_touch && hasCampaign(stored.last_touch)
            ? stored.last_touch
            : stored.first_touch;
        const bookingPage = normalizePath(window.location.pathname || '/');
        const inquiryId = extraContext.inquiry_id || generateInquiryId();

        const attribution = {
            version: VERSION,
            inquiry_id: inquiryId,
            source_category: classifySource(effectiveTouch),
            first_touch: clone(stored.first_touch),
            last_touch: stored.last_touch ? clone(stored.last_touch) : null,
            booking_page: bookingPage,
            cta_location: extraContext.cta_location || undefined,
            pack_presented: extraContext.pack_presented || undefined,
            final_requested_pack: extraContext.final_requested_pack || undefined,
            pickup_context: extraContext.pickup_context || undefined
        };

        recordInquiry(attribution);
        return attribution;
    }

    window.MarragafayAttribution = Object.freeze({
        storageKey: STORAGE_KEY,
        inquiriesKey: INQUIRIES_STORAGE_KEY,
        classifySource,
        capture,
        generateInquiryId,
        recordInquiry,
        getBookingAttribution
    });

    capture();
})(window, document);

// Queue manual captures until the asynchronously loaded browser client is ready.
// This site has no user accounts, so these actions intentionally remain personless.
(function (window) {
    'use strict';

    window.MarragafayAnalytics = {
        capture(event, properties) {
            if (window.posthog) {
                window.posthog.capture(event, properties);
                return;
            }
            window.addEventListener('posthog:ready', (readyEvent) => {
                readyEvent.detail.capture(event, properties);
            }, { once: true });
        }
    };
})(window);

// The static site retrieves its public browser configuration from the Vercel
// runtime, allowing PostHog to be initialized once without embedding values in
// the generated HTML files.
(function (window, document) {
    'use strict';

    // Ensure window.posthog exists as a safe no-op shim so calls like window.posthog?.capture() never throw
    window.posthog = window.posthog || {
        capture: function () {},
        identify: function () {},
        reset: function () {},
        get_distinct_id: function () { return ''; },
        onFeatureFlags: function () {},
        isFeatureEnabled: function () { return false; }
    };

    fetch('/api/posthog-config')
        .then((response) => {
            if (!response.ok || response.status === 204) return null;
            return response.json().catch(() => null);
        })
        .then((config) => {
            if (!config || !config.host || !config.token) return;

            const script = document.createElement('script');
            script.async = true;
            script.crossOrigin = 'anonymous';
            script.src = `${config.host.replace('.i.posthog.com', '-assets.i.posthog.com')}/static/array.js`;
            script.onload = () => {
                try {
                    if (window.posthog && typeof window.posthog.init === 'function') {
                        window.posthog.init(config.token, {
                            api_host: config.host,
                            defaults: '2026-05-30',
                            capture_exceptions: {
                                capture_unhandled_errors: true,
                                capture_unhandled_rejections: true,
                                capture_console_errors: false
                            }
                        });
                        window.dispatchEvent(new CustomEvent('posthog:ready', { detail: window.posthog }));
                    }
                } catch (initErr) {
                    console.warn('[PostHog] Init warning:', initErr);
                }
            };
            script.onerror = () => {
                console.warn('[PostHog] Script failed to load (possibly blocked by client/adblocker). Analytics disabled.');
            };
            document.head.appendChild(script);
        })
        .catch((error) => {
            console.warn('[PostHog] Config unavailable, analytics gracefully disabled:', error?.message || error);
        });
})(window, document);
