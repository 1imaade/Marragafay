/**
 * Marragafay Frontend Product Data Layer
 *
 * Single Source of Truth for factual product data across the frontend:
 * - Queries Supabase public.pricing table (via supabaseClient or direct REST)
 * - Normalizes product names and aliases into canonical products
 * - Provides centralized canonical fallback data when offline or during initial paint (Zero-Flash)
 * - Binds DOM elements via [data-product] and [data-field] attributes
 */

(function () {
    'use strict';

    var SUPABASE_URL = 'https://bgjohquanepghmlmdiyd.supabase.co';
    var SUPABASE_PUBLISHABLE_KEY = 'sb_publishable_i3RLdEPI2p-B_CYrEw6dlw_3bKe9gzh';

    // ====================================================================
    // CANONICAL FALLBACK MATRIX (OFFICIAL SOURCE OF TRUTH)
    // ====================================================================

    var CANONICAL_FALLBACK = {
        'standard': {
            id: '9a233299-c908-4b91-92f2-789091a313e7',
            key: 'standard',
            type: 'package',
            name: 'Standard',
            title: 'Agafay Evening Experience',
            priceEUR: 45,
            priceMAD: 450,
            duration: '15:30–22:00',
            transport: 'Shared hotel / riad pickup & return',
            facts: { transportMode: 'shared', quadDuration: '1h', camelDuration: '20min' },
            cardSummary: '15:30 — 22:00 · Shared Transfer · 1h Quad · 20min Camel · Dinner & Show',
            includes: [
                'Shared hotel / riad pickup & return',
                '1h quad ride across Agafay',
                '20min camel ride',
                'Pool access & Moroccan mint tea',
                'Sunset photo pause',
                'Traditional Moroccan dinner',
                'Live fire & music show',
                'Bottled water included',
                'Safety gear & briefing'
            ],
            description: 'Shared hotel / riad pickup & return + 1h quad ride across Agafay + 20min camel ride + pool access & Moroccan mint tea + sunset photo pause + traditional Moroccan dinner + live fire & music show + bottled water + safety gear & briefing',
            source: 'fallback'
        },
        'private': {
            id: '0a910941-f45d-4cd9-8aea-57d478d9a61d',
            key: 'private',
            type: 'package',
            name: 'Private',
            title: 'Private Agafay Evening',
            priceEUR: 75,
            priceMAD: 750,
            duration: '15:30–22:00',
            transport: 'Private hotel / riad transfer',
            facts: { transportMode: 'private', quadDuration: '1h30', camelDuration: '20min' },
            cardSummary: '15:30 — 22:00 · Private Transfer · 1h30 Quad · 20min Camel · Guide · Dinner & Show',
            includes: [
                'Private hotel / riad transfer',
                '1h30 private quad session',
                '20min camel ride',
                'Pool access & Moroccan mint tea',
                'Sunset photo pause',
                'Traditional Moroccan dinner',
                'Live fire & music show',
                'Dedicated guide',
                'Desert scarf to wear & keep',
                'Bottled water + soft drink',
                'Moroccan sweets',
                'Safety gear & briefing'
            ],
            description: 'Private hotel / riad transfer + 1h30 private quad session + 20min camel ride + pool access & Moroccan mint tea + sunset photo pause + traditional Moroccan dinner + live fire & music show + dedicated guide + desert scarf to wear & keep + bottled water & soft drink + Moroccan sweets + safety gear & briefing',
            source: 'fallback'
        },
        'private-plus': {
            id: 'e10728b4-026a-40a8-b6b3-b2f95cf3f063',
            key: 'private-plus',
            type: 'package',
            name: 'Private+',
            title: 'Agafay & Atlas — Full-Day Quad',
            priceEUR: 119,
            priceMAD: 1190,
            duration: '09:00–22:00',
            transport: 'Private hotel / riad transfer',
            facts: { transportMode: 'private', quadDuration: '3h', camelDuration: '45min' },
            cardSummary: '09:00 — 22:00 · Private Transfer · 3h Quad · Lunch & Dinner · 45min Camel · Guide',
            includes: [
                'Private hotel / riad transfer',
                '3h private quad exploration across Agafay & the Atlas',
                'Traditional Moroccan lunch',
                'Pool access & Moroccan mint tea',
                '45min camel ride',
                'Sunset pause',
                'Traditional Moroccan dinner',
                'Live fire & music show',
                'Dedicated full-day guide',
                'Desert scarf to wear & keep',
                'Bottled water + soft drink',
                'Moroccan sweets',
                'Safety gear & briefing'
            ],
            description: 'Agafay & Atlas Discovery — Full Day Quad: private hotel / riad transfer + 3h private quad exploration across Agafay & the Atlas + traditional Moroccan lunch + pool access & Moroccan mint tea + 45min camel ride + sunset pause + traditional Moroccan dinner + live fire & music show + dedicated full-day guide + desert scarf to wear & keep + bottled water & soft drink + Moroccan sweets + safety gear & briefing',
            source: 'fallback'
        },
        'buggy': {
            id: '22ab5a90-9889-4aaa-bb14-fe6173eae540',
            key: 'buggy',
            type: 'package',
            name: 'Buggy',
            title: 'Private Agafay Buggy Experience',
            priceEUR: 129,
            priceMAD: 1290,
            duration: 'Flexible',
            transport: 'Private hotel / riad transfer',
            facts: { transportMode: 'private', quadDuration: '1h', camelDuration: '20min' },
            cardSummary: 'Flexible Departure · Private Transfer · 1h Buggy (2 guests/buggy) · 20min Camel · Dinner & Show',
            includes: [
                'Private hotel / riad transfer',
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
            ],
            description: 'Private hotel / riad transfer + 1h private buggy ride + one buggy for two guests + 20min camel ride + pool access & Moroccan mint tea + sunset photo pause + traditional Moroccan dinner + live fire & music show + dedicated guide + bottled water + safety gear & briefing',
            source: 'fallback'
        }
    };

    // Deep clone helper
    function clone(obj) {
        return JSON.parse(JSON.stringify(obj));
    }

    // Active product store initialized with canonical fallback data
    var productStore = {};
    Object.keys(CANONICAL_FALLBACK).forEach(function (k) {
        productStore[k] = clone(CANONICAL_FALLBACK[k]);
    });

    var overrides = {};

    // ====================================================================
    // PRODUCT KEY & ALIAS NORMALIZATION
    // ====================================================================

    function normalizeProductName(name) {
        if (!name || typeof name !== 'string') return '';
        var n = name.trim().toLowerCase().replace(/\s+/g, ' ');

        // Standard / Basic aliases
        if (n === 'standard' || n === 'basic' || n === 'discovery' || n === 'discovery pack' ||
            n === 'discovery-pack' || n === 'agafay discovery' || n === 'agafay-discovery' ||
            n === 'agafay evening experience' || n === 'agafay-evening-experience' ||
            n === 'standard pack' || n === 'standard-pack' || n === 'marragafay discovery') {
            return 'standard';
        }

        // Private / Comfort aliases
        if (n === 'private' || n === 'comfort' || n === 'signature' || n === 'signature pack' ||
            n === 'signature-pack' || n === 'marragafay signature' || n === 'private agafay evening' ||
            n === 'private-agafay-evening' || n === 'private pack' || n === 'private-pack' || n === 'premium') {
            return 'private';
        }

        // Private+ / Luxe aliases
        if (n === 'private+' || n === 'private +' || n === 'private plus' || n === 'private-plus' ||
            n === 'luxe' || n === 'luxury' || n === 'luxury pack' || n === 'luxury-pack' || n === 'vip' ||
            n === 'the marragafay luxury' || n === 'agafay & atlas — full-day quad' ||
            n === 'agafay & atlas - full-day quad' || n === 'agafay and atlas full day quad' ||
            n === 'agafay & atlas' || n === 'private+ pack' || n === 'private-plus pack' ||
            n === 'private-plus-pack' || n === 'luxe pack') {
            return 'private-plus';
        }

        // Buggy aliases
        if (n === 'buggy' || n === 'buggy tour' || n === 'buggy-tour' || n === 'buggy experience' ||
            n === 'buggy-experience' || n === 'private agafay buggy experience' ||
            n === 'private-agafay-buggy-experience' || n === 'agafay buggy adventure marrakech' ||
            n === 'البوغي') {
            return 'buggy';
        }

        return n;
    }

    // ====================================================================
    // ROW PARSING & STORE UPDATE
    // ====================================================================

    function extractTransport(includesList, fallbackTransport) {
        if (!Array.isArray(includesList) || includesList.length === 0) {
            return fallbackTransport;
        }
        for (var i = 0; i < includesList.length; i++) {
            var item = includesList[i];
            if (typeof item === 'string' && /transfer|pickup/i.test(item)) {
                return item;
            }
        }
        return fallbackTransport;
    }

    function parseSupabaseRow(row) {
        if (!row || typeof row !== 'object') return null;
        var rawName = row.activity_name || row.name || '';
        var canonicalKey = normalizeProductName(rawName);
        if (!canonicalKey || !CANONICAL_FALLBACK[canonicalKey]) return null;

        var fb = CANONICAL_FALLBACK[canonicalKey];

        // Parse EUR and MAD prices
        var priceMAD, priceEUR;
        if (row.currency === 'MAD') {
            priceMAD = Number(row.price);
            priceEUR = row.price_eur != null ? Number(row.price_eur) : Math.round(priceMAD / 10);
        } else {
            // currency is EUR
            priceEUR = Number(row.price);
            priceMAD = row.price_eur != null ? Math.round(Number(row.price_eur) * 10) : (priceEUR * 10);
        }

        var includes = Array.isArray(row.includes) && row.includes.length > 0 ? row.includes : fb.includes;
        var transport = extractTransport(includes, fb.transport);

        return {
            id: row.id || fb.id,
            key: canonicalKey,
            type: 'package',
            name: fb.name, // Use canonical title capitalization
            title: fb.title,
            priceEUR: priceEUR,
            priceMAD: priceMAD,
            duration: row.duration || fb.duration,
            transport: transport,
            facts: clone(fb.facts || {}),
            cardSummary: fb.cardSummary,
            includes: includes,
            description: row.description || fb.description,
            source: 'supabase'
        };
    }

    // ====================================================================
    // DATA FETCHING (SUPABASE WITH ZERO-FLASH FALLBACK)
    // ====================================================================

    var fetchPromise = null;

    async function fetchProducts() {
        if (fetchPromise) return fetchPromise;

        fetchPromise = (async function () {
            try {
                var rows = null;

                // 1. Try supabaseClient if available in window
                if (typeof window !== 'undefined' && window.supabaseClient && typeof window.supabaseClient.from === 'function') {
                    try {
                        var res = await window.supabaseClient
                            .from('pricing')
                            .select('*')
                            .eq('active', true);
                        if (!res.error && Array.isArray(res.data) && res.data.length > 0) {
                            rows = res.data;
                        }
                    } catch (e) {
                        console.warn('ProductData: supabaseClient query failed, trying direct REST fetch:', e.message);
                    }
                }

                // 2. Direct REST fetch if supabaseClient was absent or failed
                if (!rows && typeof fetch === 'function') {
                    var endpoint = SUPABASE_URL + '/rest/v1/pricing?select=*&active=eq.true';
                    var controller = typeof AbortController !== 'undefined' ? new AbortController() : null;
                    var timeoutId = controller ? setTimeout(function () { controller.abort(); }, 5000) : null;

                    var fetchRes = await fetch(endpoint, {
                        headers: {
                            'apikey': SUPABASE_PUBLISHABLE_KEY,
                            'Authorization': 'Bearer ' + SUPABASE_PUBLISHABLE_KEY
                        },
                        signal: controller ? controller.signal : undefined
                    });

                    if (timeoutId) clearTimeout(timeoutId);

                    if (fetchRes.ok) {
                        var data = await fetchRes.json();
                        if (Array.isArray(data) && data.length > 0) {
                            rows = data;
                        }
                    }
                }

                // 3. Process fetched rows
                if (rows && rows.length > 0) {
                    rows.forEach(function (row) {
                        var parsed = parseSupabaseRow(row);
                        if (parsed) {
                            productStore[parsed.key] = parsed;
                        }
                    });

                    // Trigger DOM element bindings after data update
                    if (typeof document !== 'undefined') {
                        bindElements(document);
                    }
                }

            } catch (err) {
                console.warn('ProductData: Error fetching live pricing, using canonical fallback:', err.message);
            }

            return getAllProducts();
        })();

        return fetchPromise;
    }

    // ====================================================================
    // QUERY METHODS
    // ====================================================================

    function getProduct(key) {
        var canonicalKey = normalizeProductName(key);
        var base = productStore[canonicalKey] || CANONICAL_FALLBACK[canonicalKey] || null;
        if (!base) return null;

        var result = clone(base);
        if (overrides[canonicalKey]) {
            Object.assign(result, overrides[canonicalKey]);
        }
        return result;
    }

    function getAllProducts() {
        return ['standard', 'private', 'private-plus', 'buggy'].map(function (k) {
            return getProduct(k);
        }).filter(Boolean);
    }

    function setProductOverride(key, partial) {
        var canonicalKey = normalizeProductName(key);
        if (!overrides[canonicalKey]) overrides[canonicalKey] = {};
        Object.assign(overrides[canonicalKey], partial);
        if (typeof document !== 'undefined') {
            bindElements(document);
        }
    }

    function resetOverrides() {
        overrides = {};
        if (typeof document !== 'undefined') {
            bindElements(document);
        }
    }

    // ====================================================================
    // LOCALIZATION ENGINE INTEGRATION
    // ====================================================================

    function detectLocale(root) {
        if (root && typeof root.getAttribute === 'function') {
            var elLang = root.getAttribute('lang');
            if (elLang) {
                var norm = elLang.toLowerCase().slice(0, 2);
                if (norm === 'fr' || norm === 'es' || norm === 'ar') return norm;
            }
        }
        if (typeof document !== 'undefined') {
            var htmlLang = document.documentElement ? document.documentElement.getAttribute('lang') : null;
            if (htmlLang) {
                var norm = htmlLang.toLowerCase().slice(0, 2);
                if (norm === 'fr' || norm === 'es' || norm === 'ar') return norm;
            }
            var path = (window.location && window.location.pathname) || '';
            if (path.indexOf('/fr/') === 0 || path === '/fr') return 'fr';
            if (path.indexOf('/es/') === 0 || path === '/es') return 'es';
            if (path.indexOf('/ar/') === 0 || path === '/ar') return 'ar';
        }
        return 'en';
    }

    function getLocalizationEngine() {
        if (typeof window !== 'undefined' && window.ProductLocalization) {
            return window.ProductLocalization;
        }
        if (typeof globalThis !== 'undefined' && globalThis.ProductLocalization) {
            return globalThis.ProductLocalization;
        }
        return null;
    }

    function getLocalizedProduct(key, locale) {
        var base = getProduct(key);
        if (!base) return null;

        var loc = locale || detectLocale();
        var engine = getLocalizationEngine();
        if (!engine || typeof engine.getLocalizedFields !== 'function') {
            return base;
        }

        var locFields = engine.getLocalizedFields(base.key, loc, base);
        if (!locFields) return base;

        var localized = clone(base);
        // Overlay localized presentation while strictly preserving canonical factual properties
        if (locFields.name) localized.name = locFields.name;
        if (locFields.title) localized.title = locFields.title;
        if (locFields.transport) localized.transport = locFields.transport;
        if (locFields.cardSummary) localized.cardSummary = locFields.cardSummary;
        if (locFields.tag) localized.tag = locFields.tag;
        if (locFields.fromPrice) localized.fromPrice = locFields.fromPrice;
        if (locFields.cta) localized.cta = locFields.cta;
        if (Array.isArray(locFields.includes)) localized.includes = locFields.includes.slice();

        return localized;
    }

    // ====================================================================
    // DOM BINDING ENGINE
    // ====================================================================

    function bindElements(root, locale) {
        if (!root || typeof root.querySelectorAll !== 'function') return;
        var loc = locale || detectLocale(root);

        var boundElements = root.querySelectorAll('[data-product]');
        boundElements.forEach(function (el) {
            var prodKey = el.getAttribute('data-product');
            var field = el.getAttribute('data-field');
            var prod = getLocalizedProduct(prodKey, loc);
            if (!prod || !field) return;

            switch (field) {
                case 'name':
                    el.textContent = prod.name;
                    break;

                case 'title':
                    el.textContent = prod.title || prod.name;
                    break;

                case 'price-eur':
                    if (el.getAttribute('data-format') === 'number') {
                        el.textContent = prod.priceEUR;
                    } else {
                        el.textContent = prod.priceEUR + ' €';
                    }
                    break;

                case 'price-mad':
                    if (el.getAttribute('data-format') === 'number') {
                        el.textContent = prod.priceMAD;
                    } else if (el.getAttribute('data-format') === 'parentheses') {
                        el.textContent = '(' + prod.priceMAD + ' MAD)';
                    } else {
                        el.textContent = '/ ' + prod.priceMAD + ' MAD';
                    }
                    break;

                case 'duration':
                    el.textContent = prod.duration;
                    break;

                case 'transport':
                    el.textContent = prod.transport;
                    break;

                case 'tag':
                    if (prod.tag) {
                        el.textContent = prod.tag;
                    } else {
                        el.textContent = prod.name.toUpperCase() + ' · ' + prod.priceEUR + '€ / guest';
                    }
                    break;

                case 'from-price':
                    if (prod.fromPrice) {
                        el.textContent = prod.fromPrice;
                    } else {
                        el.textContent = 'From ' + prod.priceEUR + '€ / person';
                    }
                    break;

                case 'card-summary':
                    if (prod.cardSummary) {
                        el.textContent = prod.cardSummary;
                    }
                    break;

                case 'inclusions':
                    // If element is a <ul>, dynamically update or confirm items
                    if (el.tagName.toLowerCase() === 'ul' && Array.isArray(prod.includes)) {
                        renderInclusionsList(el, prod.includes);
                    }
                    break;

                case 'cta':
                    if (prod.cta) {
                        el.textContent = prod.cta;
                    }
                    break;

                default:
                    if (prod[field] !== undefined) {
                        el.textContent = String(prod[field]);
                    }
                    break;
            }
        });
    }

    function renderInclusionsList(ulElement, includesList) {
        // Reconcile the static shell with the canonical list before replacing text.
        // Locales previously had different list lengths, which prevented hydration.
        var existingItems = Array.prototype.slice.call(ulElement.querySelectorAll(':scope > li'));
        var template = existingItems[0];
        if (!template) return;

        while (existingItems.length < includesList.length) {
            var clone = template.cloneNode(true);
            ulElement.appendChild(clone);
            existingItems.push(clone);
        }
        while (existingItems.length > includesList.length) {
            existingItems.pop().remove();
        }

        existingItems.forEach(function (li, idx) {
            var textSpan = li.querySelector('span[class*="text-[14px]"]') || li.querySelector('span:last-child') || li;
            textSpan.textContent = includesList[idx];
        });
    }

    // ====================================================================
    // INITIALIZATION
    // ====================================================================

    function init() {
        // Immediate synchronous binding with fallback data (Zero-Flash)
        bindElements(document);

        // Async fetch from Supabase to confirm or hydrate with live data
        fetchProducts();
    }

    if (typeof document !== 'undefined') {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init);
        } else {
            init();
        }
    }

    // ====================================================================
    // EXPORT
    // ====================================================================

    var ProductData = {
        getProduct: getProduct,
        getLocalizedProduct: getLocalizedProduct,
        detectLocale: detectLocale,
        getAllProducts: getAllProducts,
        fetchProducts: fetchProducts,
        bindElements: bindElements,
        normalizeProductName: normalizeProductName,
        parseSupabaseRow: parseSupabaseRow,
        setProductOverride: setProductOverride,
        resetOverrides: resetOverrides,
        CANONICAL_FALLBACK: CANONICAL_FALLBACK
    };

    if (typeof window !== 'undefined') {
        window.ProductData = ProductData;
    }

    if (typeof module !== 'undefined' && module.exports) {
        module.exports = ProductData;
    }

})();
