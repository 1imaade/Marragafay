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

    console.log('Dynamic Pricing Manager Loaded');

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
                    console.log('Currency from cache:', parsed.currency);
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
                console.log('Detected country:', country, '→ currency:', currency);
                // Cache it
                try {
                    sessionStorage.setItem(CURRENCY_CACHE_KEY, JSON.stringify({ currency: currency, ts: Date.now() }));
                } catch (_) { /* ignore */ }
                return currency;
            }

            console.log('Detected country:', country, '→ using default EUR');
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

    /**
     * Calculate MAD equivalent for a EUR price.
     */
    function toMAD(eurValue) {
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

        console.log('Currency display updated to', currency, '(' + symbol + ')');
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
    // SUPABASE PRICING (existing logic, unchanged)
    // ====================================================================

    /**
     * Fetch all pricing data from Supabase
     */
    async function fetchPricing() {
        // Check cache first
        if (cacheTimestamp && (Date.now() - cacheTimestamp) < CACHE_DURATION) {
            console.log('Using cached pricing data');
            return priceCache;
        }

        try {
            console.log('Fetching pricing from Supabase...');

            const { data, error } = await supabaseClient
                .from('pricing')
                .select('*')
                .eq('active', true); // Only fetch active prices

            if (error) throw error;

            console.log('Pricing data fetched:', data);

            // Convert array to object for easy lookup
            priceCache = {};
            data.forEach(function (item) {
                priceCache[item.type + '_' + item.activity_name] = {
                    price: item.price,
                    currency: item.currency,
                    id: item.id
                };
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
            'package_Basic': { price: 35, currency: '€' },
            'package_Comfort': { price: 49, currency: '€' },
            'package_Luxe': { price: 89, currency: '€' },
            'activity_Quad Biking': { price: 25, currency: '€' },
            'activity_Buggy': { price: 80, currency: '€' },
            'activity_Camel Ride': { price: 10, currency: '€' },
            'activity_Dinner & Show': { price: 15, currency: '€' },
            'activity_Hot Air Balloon': { price: 150, currency: '€' },
            'activity_Paragliding': { price: 80, currency: '€' }
        };
    }

    /**
     * Update all price elements on the page (Supabase-driven)
     */
    async function updatePagePrices() {
        const prices = await fetchPricing();

        // Find all elements with data-price-type and data-price-name attributes
        const priceElements = document.querySelectorAll('[data-price-type][data-price-name]');

        priceElements.forEach(function (element) {
            const type = element.getAttribute('data-price-type');
            const name = element.getAttribute('data-price-name');
            const key = type + '_' + name;

            const priceData = prices[key];

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

                console.log('Updated price for ' + key + ': ' + priceData.price + ' ' + priceData.currency);
            } else {
                console.warn('No price data found for ' + key);
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
        const key = type + '_' + name;
        const priceData = prices[key];

        if (priceData) {
            return priceData.price;
        }

        // Fallback to hardcoded values
        const defaults = getDefaultPrices();
        return defaults[key] ? defaults[key].price : 0;
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

        console.log('Dynamic pricing initialized successfully');
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
    };

})();
