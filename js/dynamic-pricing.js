/**
 * Dynamic Pricing & Currency System
 *
 * TWO responsibilities:
 * 1. Fetch live pricing from Supabase (existing).
 * 2. Detect visitor's country via GeoIP and swap EUR displays to
 *    their local currency (GBP / USD / EUR).  Always appends a muted
 *    MAD equivalent so customers see the base Moroccan price.
 *
 * IMPORTANT — Display only.  Every total_price sent to the Supabase
 * bookings table MUST be in MAD.  See booking-manager.js.
 */

(function () {
    'use strict';

    // ====================================================================
    // CURRENCY CONFIGURATION
    // ====================================================================

    /**
     * Hard-coded exchange rate: 1 EUR = 10 MAD.
     * USD and GBP use the same ratio so the displayed number stays the
     * same — only the currency symbol changes.
     */
    const EUR_TO_MAD = 10;

    const CURRENCY_CONFIG = {
        GBP: { symbol: '£', code: 'GBP', label: 'GBP' },
        USD: { symbol: '$',      code: 'USD', label: 'USD' },
        EUR: { symbol: '€', code: 'EUR', label: 'EUR' },
    };

    /** Country-code → target currency (ISO 3166-1 alpha-2). */
    const COUNTRY_CURRENCY = {
        GB: 'GBP',
        US: 'USD',
        CA: 'USD',
    };

    const DEFAULT_CURRENCY = 'EUR';

    // sessionStorage key for caching the detected currency
    const CURRENCY_CACHE_KEY = 'mrg_currency';
    const CURRENCY_CACHE_TTL = 4 * 60 * 60 * 1000; // 4 hours

    // ====================================================================
    // PRICE CACHE (Supabase)
    // ====================================================================

    let priceCache = {};
    let cacheTimestamp = null;
    const CACHE_DURATION = 5 * 60 * 1000; // 5 minutes

    // ====================================================================
    // CURRENCY DETECTION
    // ====================================================================

    /**
     * Detect the visitor's preferred currency via GeoIP.
     * Falls back to EUR on any error.
     */
    async function detectUserCurrency() {
        // 1. Check sessionStorage
        try {
            const cached = sessionStorage.getItem(CURRENCY_CACHE_KEY);
            if (cached) {
                const parsed = JSON.parse(cached);
                if (parsed && parsed.currency && Date.now() - parsed.ts < CURRENCY_CACHE_TTL) {
                    return parsed.currency;
                }
            }
        } catch (_) { /* ignore */ }

        // 2. GeoIP lookup (3 s timeout)
        try {
            const controller = new AbortController();
            const timeoutId = setTimeout(function () { controller.abort(); }, 3000);

            const res = await fetch('https://get.geojs.io/v1/ip/country.json', {
                signal: controller.signal,
            });
            clearTimeout(timeoutId);

            if (!res.ok) throw new Error('HTTP ' + res.status);

            const data = await res.json();
            const country = data.country; // ISO 3166-1 alpha-2

            if (country && COUNTRY_CURRENCY[country]) {
                const currency = COUNTRY_CURRENCY[country];
                // Cache it
                try {
                    sessionStorage.setItem(CURRENCY_CACHE_KEY, JSON.stringify({ currency: currency, ts: Date.now() }));
                } catch (_) { /* ignore */ }
                return currency;
            }

        } catch (err) {
            console.warn('GeoIP failed, falling back to EUR:', err.message);
        }

        // 3. Fallback
        try {
            sessionStorage.setItem(CURRENCY_CACHE_KEY, JSON.stringify({ currency: DEFAULT_CURRENCY, ts: Date.now() }));
        } catch (_) { /* ignore */ }
        return DEFAULT_CURRENCY;
    }

    /**
     * Return the config object for a currency code.
     */
    function getCurrencyConfig(currency) {
        return CURRENCY_CONFIG[currency] || CURRENCY_CONFIG[DEFAULT_CURRENCY];
    }

    // ====================================================================
    // PRODUCT KEY NORMALIZATION & ALIASES
    // ====================================================================

    /**
     * Normalize product type ('pack' / 'package' / 'activity')
     */
    function normalizeType(type) {
        if (!type || typeof type !== 'string') return 'package';
        var t = type.trim().toLowerCase();
        if (t === 'pack' || t === 'package' || t === 'packages' || t === 'packs') return 'package';
        if (t === 'activity' || t === 'activities') return 'activity';
        return t;
    }

    /**
     * Normalize product name to canonical ID
     */
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

        // Buggy aliases (can be classified as package or activity)
        if (n === 'buggy' || n === 'buggy tour' || n === 'buggy-tour' || n === 'buggy experience' ||
            n === 'buggy-experience' || n === 'private agafay buggy experience' ||
            n === 'private-agafay-buggy-experience' || n === 'agafay buggy adventure marrakech' ||
            n === 'البوغي') {
            return 'buggy';
        }

        // Other activities
        if (n === 'quad' || n === 'quad biking' || n === 'quad-biking' || n === 'quad agafay adventure') {
            return 'quad-biking';
        }
        if (n === 'camel' || n === 'camel ride' || n === 'camel-ride' || n === 'agafay camel ride marrakech') {
            return 'camel-ride';
        }
        if (n === 'dinner-show' || n === 'dinner & show' || n === 'dinner and show' ||
            n === 'dinner' || n === 'diner' || n === 'agafay dinner show marrakech') {
            return 'dinner-show';
        }
        if (n === 'hot-air-balloon' || n === 'hot air balloon' || n === 'balloon' ||
            n === 'marrakech sunrise hot air balloon experience') {
            return 'hot-air-balloon';
        }
        if (n === 'paragliding' || n === 'parapente') {
            return 'paragliding';
        }
        if (n === 'horse riding' || n === 'horse-riding' || n === 'horseback riding in agafay desert') {
            return 'horse-riding';
        }
        if (n === 'bike tour' || n === 'bike-tour' || n === 'mountain bike tour in agafay desert') {
            return 'bike-tour';
        }

        return n;
    }

    // Canonical single source of truth in Moroccan Dirhams (MAD)
    const CANONICAL_PRICES_MAD = {
        // Canonical normalized keys
        'package_standard': 450,
        'package_private': 750,
        'package_private-plus': 1190,
        'package_buggy': 1290,
        'activity_buggy': 1290,
        'activity_quad-biking': 250,
        'activity_camel-ride': 100,
        'activity_dinner-show': 250,
        'activity_hot-air-balloon': 1750,
        'activity_paragliding': 799,
        'activity_horse-riding': 550,
        'activity_bike-tour': 300,

        // New Supabase names (type="pack" or "package")
        'pack_Standard': 450,
        'pack_Private': 750,
        'pack_Private+': 1190,
        'pack_Buggy': 1290,
        'package_Standard': 450,
        'package_Private': 750,
        'package_Private+': 1190,
        'package_Buggy': 1290,
        'Standard': 450,
        'Private': 750,
        'Private+': 1190,
        'Buggy': 1290,

        // Legacy keys (for backward compatibility)
        'package_Basic': 450,
        'package_Comfort': 750,
        'package_Luxe': 1190,
        'Basic': 450,
        'Comfort': 750,
        'Luxe': 1190,
        'activity_Quad Biking': 250,
        'activity_Buggy': 1290,
        'activity_Camel Ride': 100,
        'activity_Dinner & Show': 250,
        'activity_Hot Air Balloon': 1750,
        'activity_Paragliding': 799,
        'Quad Biking': 250,
        'Camel Ride': 100,
        'Dinner & Show': 250,
        'Hot Air Balloon': 1750,
        'Paragliding': 799
    };

    /**
     * Calculate MAD equivalent for a EUR price or retrieve canonical MAD price.
     */
    function toMAD(eurValue, itemKey) {
        if (itemKey) {
            if (CANONICAL_PRICES_MAD[itemKey]) {
                return CANONICAL_PRICES_MAD[itemKey];
            }
            var norm = normalizeProductName(itemKey);
            if (norm && CANONICAL_PRICES_MAD['package_' + norm]) {
                return CANONICAL_PRICES_MAD['package_' + norm];
            }
            if (norm && CANONICAL_PRICES_MAD['activity_' + norm]) {
                return CANONICAL_PRICES_MAD['activity_' + norm];
            }
        }
        if (typeof window !== 'undefined' && window.location.pathname) {
            var path = window.location.pathname.toLowerCase();
            if (path.includes('paragliding')) return CANONICAL_PRICES_MAD['activity_paragliding'];
            if (path.includes('hot-air-balloon')) return CANONICAL_PRICES_MAD['activity_hot-air-balloon'];
            if (path.includes('dinner-show')) return CANONICAL_PRICES_MAD['activity_dinner-show'];
            if (path.includes('quad-biking')) return CANONICAL_PRICES_MAD['activity_quad-biking'];
            if (path.includes('camel-ride')) return CANONICAL_PRICES_MAD['activity_camel-ride'];
            if (path.includes('buggy')) return CANONICAL_PRICES_MAD['package_buggy'];
            if (path.includes('/packages/basic') || path.includes('/packages/standard')) return CANONICAL_PRICES_MAD['package_standard'];
            if (path.includes('/packages/comfort') || path.includes('/packages/private')) return CANONICAL_PRICES_MAD['package_private'];
            if (path.includes('/packages/luxe') || path.includes('/packages/private-plus')) return CANONICAL_PRICES_MAD['package_private-plus'];
        }
        return Math.round(eurValue * EUR_TO_MAD);
    }

    // ====================================================================
    // DOM PRICE UPDATER
    // ====================================================================

    /**
     * Inject a small muted MAD subtitle into a price container.
     * Only inserts once (checks for .price-mad).
     */
    function injectMadSubtitle(container, madValue) {
        if (container.querySelector('.price-mad')) return;

        const madEl = document.createElement('small');
        madEl.className = 'price-mad';
        madEl.style.cssText = 'font-size:0.7em;opacity:0.7;display:block;line-height:1.2;';
        madEl.textContent = '/ ' + madValue + ' MAD';
        container.appendChild(madEl);
    }

    /**
     * Replace the currency symbol inside a DOM element.
     * Handles text like "10 €" or inline <small>€</small>.
     */
    function replaceCurrencySymbol(root, symbol) {
        if (!root || root.nodeType === 3) return;

        // Walk text nodes inside this root
        const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
        let node;
        while ((node = walker.nextNode())) {
            if (node.textContent.indexOf('€') !== -1) {
                node.textContent = node.textContent.replace(/€/g, symbol);
            }
        }

        // Also handle <small> that contains just the symbol
        const smallEls = root.querySelectorAll('small');
        smallEls.forEach(function (sm) {
            if (sm.textContent.trim() === '€' || sm.textContent.trim() === 'EUR') {
                sm.textContent = symbol;
            }
        });
    }

    /**
     * Main entry: scan every known price pattern and apply the
     * detected currency.
     */
    function updatePriceDisplays(currency) {
        var config = getCurrencyConfig(currency);
        var symbol = config.symbol;

        // ----------------------------------------------------------
        // Pattern 1 — Package cards  (.package-price)
        // Structure: <div class="package-price">
        //              <span>35 <small>€</small></span>
        //              <small>/person</small>
        //            </div>
        // ----------------------------------------------------------
        document.querySelectorAll('.package-price').forEach(function (el) {
            var span = el.querySelector('span');
            if (!span) return;

            // Extract the numeric value
            var text = span.textContent || '';
            var match = text.match(/([\d,]+(?:\.\d+)?)/);
            if (!match) return;

            var eurValue = parseFloat(match[1].replace(/,/g, ''));
            if (isNaN(eurValue)) return;

            // Replace € symbol
            replaceCurrencySymbol(span, symbol);

            // MAD subtitle
            injectMadSubtitle(el, toMAD(eurValue));
        });

        // ----------------------------------------------------------
        // Pattern 2 — Activity grid  (.activity-grid-price-amount)
        // Structure: <span class="activity-grid-price-amount">10 €</span>
        // ----------------------------------------------------------
        document.querySelectorAll('.activity-grid-price-amount').forEach(function (el) {
            var text = el.textContent || '';
            var match = text.match(/([\d,]+(?:\.\d+)?)/);
            if (!match) return;

            var eurValue = parseFloat(match[1].replace(/,/g, ''));
            if (isNaN(eurValue)) return;

            replaceCurrencySymbol(el, symbol);

            // Find the parent .activity-grid-price and inject MAD there
            var parent = el.closest('.activity-grid-price') || el.parentElement;
            injectMadSubtitle(parent, toMAD(eurValue));
        });

        // ----------------------------------------------------------
        // Pattern 3 — Checkout total  (#checkout-total-price)
        // Structure: <span id="checkout-total-price">35 €</span>
        // ----------------------------------------------------------
        var checkoutEl = document.getElementById('checkout-total-price');
        if (checkoutEl) {
            var text = checkoutEl.textContent || '';
            var match = text.match(/([\d,]+(?:\.\d+)?)/);
            if (match) {
                var eurValue = parseFloat(match[1].replace(/,/g, ''));
                if (!isNaN(eurValue)) {
                    replaceCurrencySymbol(checkoutEl, symbol);
                    // Inject after the element or wrap
                    var madEl = document.createElement('small');
                    madEl.className = 'price-mad';
                    madEl.style.cssText = 'font-size:0.6em;opacity:0.7;margin-left:8px;font-weight:400;';
                    madEl.textContent = '/ ' + toMAD(eurValue) + ' MAD';
                    checkoutEl.parentNode.appendChild(madEl);
                }
            }
        }

        // ----------------------------------------------------------
        // Pattern 4 — Tour sidebar  (.price-tag)
        // Structure: <div class="price-tag">35 €</div>
        // ----------------------------------------------------------
        document.querySelectorAll('.price-tag').forEach(function (el) {
            var text = el.textContent || '';
            var match = text.match(/([\d,]+(?:\.\d+)?)/);
            if (!match) return;

            var eurValue = parseFloat(match[1].replace(/,/g, ''));
            if (isNaN(eurValue)) return;

            replaceCurrencySymbol(el, symbol);

            // Inject MAD subtitle directly below the price tag, inside its wrapper div
            injectMadSubtitle(el.parentElement, toMAD(eurValue));
        });

        // ----------------------------------------------------------
        // Pattern 5 — Mobile bar  (.mobile-price)
        // Structure: <div class="mobile-price">35 € <span>per person</span></div>
        // ----------------------------------------------------------
        document.querySelectorAll('.mobile-price').forEach(function (el) {
            // Idempotency: skip if .price-mad already exists (prevents dupes
            // when updatePriceDisplays runs twice post-Supabase)
            if (el.querySelector('.price-mad')) return;

            var text = el.textContent || '';
            var match = text.match(/([\d,]+(?:\.\d+)?)/);
            if (!match) return;

            var eurValue = parseFloat(match[1].replace(/,/g, ''));
            if (isNaN(eurValue)) return;

            replaceCurrencySymbol(el, symbol);

            // Inject MAD subtitle into the .mobile-bottom-bar
            var madEl = document.createElement('small');
            madEl.className = 'price-mad';
            madEl.style.cssText = 'font-size:0.6em;opacity:0.7;margin-left:4px;';
            madEl.textContent = '/ ' + toMAD(eurValue) + ' MAD';
            el.appendChild(madEl);
        });

        // ----------------------------------------------------------
        // Pattern 6 — Modal price banner  (.price-amount)
        // Structure: <div class="price-amount"></div>  (populated by JS)
        // ----------------------------------------------------------
        document.querySelectorAll('.modal-price .price-amount').forEach(function (el) {
            var text = el.textContent || '';
            var match = text.match(/([\d,]+(?:\.\d+)?)/);
            if (!match) return;

            var eurValue = parseFloat(match[1].replace(/,/g, ''));
            if (isNaN(eurValue)) return;

            // price-amount contains just the number (no € symbol usually),
            // but we add the symbol explicitly.
            if (text.indexOf('€') === -1 && text.indexOf('$') === -1 && text.indexOf('£') === -1) {
                el.textContent = text.trim() + ' ' + symbol;
            } else {
                replaceCurrencySymbol(el, symbol);
            }

            var parent = el.closest('.modal-price') || el.parentElement;
            injectMadSubtitle(parent, toMAD(eurValue));
        });

    }

    /**
     * Re-run the price display updater (useful after modals open etc.).
     */
    window.refreshCurrencyDisplay = function () {
        detectUserCurrency().then(function (currency) {
            updatePriceDisplays(currency);
        });
    };

    // ====================================================================
    // SUPABASE PRICING
    // ====================================================================

    /**
     * Fetch all pricing data from Supabase
     */
    async function fetchPricing() {
        // Check cache first
        if (cacheTimestamp && (Date.now() - cacheTimestamp) < CACHE_DURATION) {
            return priceCache;
        }

        try {
            const { data, error } = await supabaseClient
                .from('pricing')
                .select('*')
                .eq('active', true); // Only fetch active prices

            if (error) throw error;

            // Convert array to object for easy lookup
            priceCache = {};
            data.forEach(function (item) {
                var rawName = item.activity_name || item.name || '';
                var rawType = item.type || '';
                var normType = normalizeType(rawType);
                var normName = normalizeProductName(rawName);

                var priceEntry = {
                    price: item.price,
                    currency: item.currency || '€',
                    id: item.id
                };

                // Canonical normalized key
                if (normType && normName) {
                    priceCache[normType + '_' + normName] = priceEntry;
                }

                // Raw exact key
                if (rawType && rawName) {
                    priceCache[rawType + '_' + rawName] = priceEntry;
                }

                // Supabase type="pack" / "package" cross-lookup
                if (rawName) {
                    priceCache['pack_' + rawName] = priceEntry;
                    priceCache['package_' + rawName] = priceEntry;
                }

                // Cross-alias mappings for seamless legacy and modern lookups
                if (normName === 'standard') {
                    priceCache['package_Basic'] = priceEntry;
                    priceCache['pack_Basic'] = priceEntry;
                    priceCache['package_Standard'] = priceEntry;
                    priceCache['pack_Standard'] = priceEntry;
                } else if (normName === 'private') {
                    priceCache['package_Comfort'] = priceEntry;
                    priceCache['pack_Comfort'] = priceEntry;
                    priceCache['package_Private'] = priceEntry;
                    priceCache['pack_Private'] = priceEntry;
                } else if (normName === 'private-plus') {
                    priceCache['package_Luxe'] = priceEntry;
                    priceCache['pack_Luxe'] = priceEntry;
                    priceCache['package_Private+'] = priceEntry;
                    priceCache['pack_Private+'] = priceEntry;
                } else if (normName === 'buggy') {
                    priceCache['package_Buggy'] = priceEntry;
                    priceCache['pack_Buggy'] = priceEntry;
                    priceCache['activity_Buggy'] = priceEntry;
                    priceCache['package_buggy'] = priceEntry;
                    priceCache['activity_buggy'] = priceEntry;
                }
            });

            cacheTimestamp = Date.now();
            return priceCache;

        } catch (error) {
            console.error('Error fetching pricing:', error);
            // Return default fallback prices if Supabase fails
            return getDefaultPrices();
        }
    }

    /**
     * Fallback prices if Supabase is unavailable
     */
    function getDefaultPrices() {
        return {
            // Canonical normalized keys
            'package_standard': { price: 45, currency: '€' },
            'package_private': { price: 75, currency: '€' },
            'package_private-plus': { price: 119, currency: '€' },
            'package_buggy': { price: 129, currency: '€' },
            'activity_buggy': { price: 129, currency: '€' },
            'activity_quad-biking': { price: 25, currency: '€' },
            'activity_camel-ride': { price: 10, currency: '€' },
            'activity_dinner-show': { price: 25, currency: '€' },
            'activity_hot-air-balloon': { price: 175, currency: '€' },
            'activity_paragliding': { price: 80, currency: '€' },
            'activity_horse-riding': { price: 55, currency: '€' },
            'activity_bike-tour': { price: 30, currency: '€' },

            // New Supabase names (type="pack" or "package")
            'pack_Standard': { price: 45, currency: '€' },
            'pack_Private': { price: 75, currency: '€' },
            'pack_Private+': { price: 119, currency: '€' },
            'pack_Buggy': { price: 129, currency: '€' },
            'package_Standard': { price: 45, currency: '€' },
            'package_Private': { price: 75, currency: '€' },
            'package_Private+': { price: 119, currency: '€' },
            'package_Buggy': { price: 129, currency: '€' },
            'Standard': { price: 45, currency: '€' },
            'Private': { price: 75, currency: '€' },
            'Private+': { price: 119, currency: '€' },
            'Buggy': { price: 129, currency: '€' },

            // Legacy keys (for backward compatibility)
            'package_Basic': { price: 45, currency: '€' },
            'package_Comfort': { price: 75, currency: '€' },
            'package_Luxe': { price: 119, currency: '€' },
            'Basic': { price: 45, currency: '€' },
            'Comfort': { price: 75, currency: '€' },
            'Luxe': { price: 119, currency: '€' },
            'activity_Quad Biking': { price: 25, currency: '€' },
            'activity_Buggy': { price: 129, currency: '€' },
            'activity_Camel Ride': { price: 10, currency: '€' },
            'activity_Dinner & Show': { price: 25, currency: '€' },
            'activity_Hot Air Balloon': { price: 175, currency: '€' },
            'activity_Paragliding': { price: 80, currency: '€' },
            'Quad Biking': { price: 25, currency: '€' },
            'Camel Ride': { price: 10, currency: '€' },
            'Dinner & Show': { price: 25, currency: '€' },
            'Hot Air Balloon': { price: 175, currency: '€' },
            'Paragliding': { price: 80, currency: '€' }
        };
    }

    /**
     * Update all price elements on the page (Supabase-driven)
     */
    async function updatePagePrices() {
        const prices = await fetchPricing();
        const defaults = getDefaultPrices();

        // Find all elements with data-price-type and data-price-name attributes
        const priceElements = document.querySelectorAll('[data-price-type][data-price-name]');

        priceElements.forEach(function (element) {
            const type = element.getAttribute('data-price-type');
            const name = element.getAttribute('data-price-name');
            const normType = normalizeType(type);
            const normName = normalizeProductName(name);

            const lookupKeys = [
                normType + '_' + normName,
                type + '_' + name,
                (normType === 'package' ? 'pack_' : 'activity_') + name,
                (normType === 'pack' ? 'package_' : 'activity_') + name,
                normName === 'buggy' ? 'package_buggy' : null,
                normName === 'buggy' ? 'activity_buggy' : null,
                name
            ].filter(Boolean);

            let priceData = null;
            for (let i = 0; i < lookupKeys.length; i++) {
                const k = lookupKeys[i];
                if (prices[k]) {
                    priceData = prices[k];
                    break;
                }
            }

            if (!priceData) {
                for (let i = 0; i < lookupKeys.length; i++) {
                    const k = lookupKeys[i];
                    if (defaults[k]) {
                        priceData = defaults[k];
                        break;
                    }
                }
            }

            if (priceData) {
                // Update the price value
                const priceValue = element.querySelector('.price-value');
                const currencyElement = element.querySelector('.price-currency');

                if (priceValue) {
                    priceValue.textContent = priceData.price;
                }

                if (currencyElement) {
                    currencyElement.textContent = priceData.currency;
                }

            } else {
                console.warn('No price data found for ' + type + '_' + name);
            }
        });
    }

    /**
     * Get price for a specific item (for use in booking-manager.js)
     * @param {string} type - 'package' or 'activity'
     * @param {string} name - Name of the item
     * @returns {number} - Price value in EUR
     */
    window.getDynamicPrice = async function (type, name) {
        const prices = await fetchPricing();
        const defaults = getDefaultPrices();
        const normType = normalizeType(type);
        const normName = normalizeProductName(name);

        const lookupKeys = [
            normType + '_' + normName,
            type + '_' + name,
            (normType === 'package' ? 'pack_' : 'activity_') + name,
            (normType === 'pack' ? 'package_' : 'activity_') + name,
            normName === 'buggy' ? 'package_buggy' : null,
            normName === 'buggy' ? 'activity_buggy' : null,
            name
        ].filter(Boolean);

        for (let i = 0; i < lookupKeys.length; i++) {
            const k = lookupKeys[i];
            if (prices[k]) {
                return prices[k].price;
            }
        }

        for (let i = 0; i < lookupKeys.length; i++) {
            const k = lookupKeys[i];
            if (defaults[k]) {
                return defaults[k].price;
            }
        }

        return 0;
    };

    // ====================================================================
    // INITIALIZATION
    // ====================================================================

    async function init() {
        // 1. Detect currency and update DOM displays
        const currency = await detectUserCurrency();
        updatePriceDisplays(currency);

        // 2. Supabase-based pricing (optional)
        if (typeof supabaseClient === 'undefined') {
            console.warn('Supabase client not found. Using static prices.');
            return;
        }

        await updatePagePrices();

        // 3. Re-apply currency display in case Supabase changed prices
        updatePriceDisplays(currency);

    }

    // Auto-initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Export for use in other modules
    window.DynamicPricing = {
        fetchPricing: fetchPricing,
        updatePagePrices: updatePagePrices,
        getDynamicPrice: window.getDynamicPrice,
        detectUserCurrency: detectUserCurrency,
        updatePriceDisplays: updatePriceDisplays,
        refreshCurrencyDisplay: window.refreshCurrencyDisplay,
        normalizeType: normalizeType,
        normalizeProductName: normalizeProductName,
        getDefaultPrices: getDefaultPrices,
        CANONICAL_PRICES_MAD: CANONICAL_PRICES_MAD,
        toMAD: toMAD
    };

})();
