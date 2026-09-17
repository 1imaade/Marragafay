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

// One privacy-safe, provider-neutral event contract for the static site.
// PostHog and the existing GTM dataLayer are sinks; neither is required for
// commercial actions to continue.
(function (window, document) {
    'use strict';

    const EVENTS = Object.freeze([
        'product_view', 'pack_cta_click', 'whatsapp_click', 'booking_open',
        'booking_start', 'booking_submit', 'booking_success', 'booking_failure'
    ]);
    const PRODUCT_IDS = new Set(['standard', 'private', 'private-plus', 'buggy']);
    const DEDUPE_EVENTS = new Set(['product_view', 'booking_submit', 'booking_success', 'booking_failure']);
    const SESSION_KEY = 'marragafay_analytics_session_v1';
    const sent = new Set();

    function safeString(value, max = 200) {
        return typeof value === 'string' ? value.replace(/[\u0000-\u001F\u007F]/g, '').trim().slice(0, max) : undefined;
    }

    function sessionId() {
        try {
            let value = window.sessionStorage.getItem(SESSION_KEY);
            if (!value) {
                value = `s_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 10)}`;
                window.sessionStorage.setItem(SESSION_KEY, value);
            }
            return value;
        } catch { return 's_ephemeral'; }
    }

    function locale() {
        const value = (document.documentElement?.lang || 'en').toLowerCase().split('-')[0];
        return ['en', 'fr', 'es', 'ar'].includes(value) ? value : 'en';
    }

    function attribution() {
        try {
            const value = window.MarragafayAttribution?.capture?.();
            const touch = value?.last_touch || value?.first_touch || {};
            return {
                source_category: safeString(window.MarragafayAttribution?.classifySource?.(touch) || 'direct', 40),
                utm_source: safeString(touch.utm_source, 100),
                utm_medium: safeString(touch.utm_medium, 100),
                utm_campaign: safeString(touch.utm_campaign, 200),
                utm_term: safeString(touch.utm_term, 200),
                utm_content: safeString(touch.utm_content, 200),
                gclid: safeString(touch.gclid, 200),
                fbclid: safeString(touch.fbclid, 200),
                referrer_category: safeString(window.MarragafayAttribution?.classifySource?.({ referrer: touch.referrer }) || 'direct', 40)
            };
        } catch { return { source_category: 'other', referrer_category: 'other' }; }
    }

    function productId(value) {
        const normalized = safeString(value, 60)?.toLowerCase().replace(/\s+/g, '-');
        const aliases = { basic: 'standard', comfort: 'private', luxe: 'private-plus', 'private+': 'private-plus' };
        const canonical = aliases[normalized] || normalized;
        return PRODUCT_IDS.has(canonical) ? canonical : undefined;
    }

    function capture(event, properties = {}, dedupeKey) {
        if (!EVENTS.includes(event)) return false;
        const key = dedupeKey || (DEDUPE_EVENTS.has(event) ? `${event}:${location.pathname}:${properties.product_id || ''}` : null);
        if (key && sent.has(key)) return false;
        if (key) sent.add(key);

        const source = attribution();
        const payload = {
            event,
            timestamp: new Date().toISOString(),
            session_id: sessionId(),
            locale: locale(),
            page_path: safeString(window.location.pathname || '/', 400),
            ...source,
            ...properties
        };
        Object.keys(payload).forEach((key) => {
            if (payload[key] === undefined || payload[key] === null || payload[key] === '') delete payload[key];
        });

        try { if (Array.isArray(window.dataLayer)) window.dataLayer.push(payload); } catch {}
        try {
            if (window.MarragafayAnalytics.debug) console.debug('[MarragafayAnalytics]', payload);
            if (typeof window.posthog?.capture === 'function') window.posthog.capture(event, payload);
        } catch {}
        return true;
    }

    function productFrom(element) {
        const node = element?.closest?.('[data-product]') || element;
        return productId(node?.getAttribute?.('data-product')) || productId(document.querySelector('[data-product]')?.getAttribute('data-product'));
    }

    function ctaLocation(element) {
        return safeString(element?.dataset?.ctaLocation || element?.id || element?.getAttribute?.('aria-label') || 'cta', 100);
    }

    function initTracking() {
        const products = new Set();
        document.querySelectorAll('[data-product]').forEach((element) => {
            const id = productId(element.getAttribute('data-product'));
            if (id) products.add(id);
        });
        products.forEach((id) => capture('product_view', { product_id: id }, `product_view:${location.pathname}:${id}`));

        document.addEventListener('click', (event) => {
            const element = event.target?.closest?.('a,button');
            if (!element) return;
            const href = element.getAttribute('href') || '';
            const isWhatsApp = /(^|:)\/\/(wa\.me|(?:[^/]+\.)?whatsapp\.com)\b/i.test(href);
            if (isWhatsApp) return;
            const isCommercial = element.matches('[data-package], [data-product], .booking-btn, #cta-book-now, .btn-reserve, [href*="/packages/"]');
            if (isCommercial) capture('pack_cta_click', {
                product_id: productFrom(element),
                cta_location: ctaLocation(element)
            });
        }, { passive: true });

        const scanVisibleBookingForms = () => document.querySelectorAll('.booking-form, #bookingForm, #booking-form, #booking-form-activity').forEach((form) => {
            if (form.offsetParent !== null) capture('booking_open', { product_id: productFrom(form), cta_location: ctaLocation(form) }, `booking_open:${location.pathname}:${form.id || 'form'}`);
            if (form.dataset.analyticsBound === 'true') return;
            form.dataset.analyticsBound = 'true';
            let started = false;
            form.addEventListener('input', () => {
                if (!started) { started = true; capture('booking_start', { product_id: productFrom(form) }, `booking_start:${location.pathname}:${form.id || 'form'}`); }
            }, { passive: true });
        });
        scanVisibleBookingForms();

        // Modal booking forms can be injected or become visible after a CTA.
        document.addEventListener('click', () => window.setTimeout(scanVisibleBookingForms, 0), { passive: true });
    }

    window.MarragafayAnalytics = { EVENTS, PRODUCT_IDS, capture, productId, debug: false };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initTracking, { once: true });
    else initTracking();
})(window, document);

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
