/**
 * Dynamic Pricing System
 * Fetches pricing from Supabase and updates all price displays on the page
 */

(function () {
    'use strict';

    console.log('Dynamic Pricing Manager Loaded');

    // Price Cache to avoid repeated queries
    let priceCache = {};
    let cacheTimestamp = null;
    const CACHE_DURATION = 5 * 60 * 1000; // 5 minutes

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
            data.forEach(item => {
                // Map new schema fields to cache key
                // Schema: type, activity_name
                // Cache Key format: type_activity_name (e.g., 'package_Basic')
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
            'package_Basic': { price: 400, currency: 'MAD' },
            'package_Comfort': { price: 600, currency: 'MAD' },
            'package_Luxe': { price: 1200, currency: 'MAD' },
            'activity_Quad Biking': { price: 350, currency: 'MAD' },
            'activity_Buggy': { price: 850, currency: 'MAD' },
            'activity_Camel Ride': { price: 200, currency: 'MAD' },
            'activity_Dinner & Show': { price: 300, currency: 'MAD' },
            'activity_Hot Air Balloon': { price: 1500, currency: 'MAD' },
            'activity_Paragliding': { price: 800, currency: 'MAD' }
        };
    }

    /**
     * Update all price elements on the page
     */
    async function updatePagePrices() {
        const prices = await fetchPricing();

        // Find all elements with data-price-type and data-price-name attributes
        const priceElements = document.querySelectorAll('[data-price-type][data-price-name]');

        priceElements.forEach(element => {
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

                console.log(`Updated price for ${key}: ${priceData.price} ${priceData.currency}`);
            } else {
                console.warn(`No price data found for ${key}`);
            }
        });
    }

    /**
     * Get price for a specific item (for use in booking-manager.js)
     * @param {string} type - 'package' or 'activity'
     * @param {string} name - Name of the item
     * @returns {number} - Price value
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

    /**
     * Initialize pricing system
     */
    async function init() {
        // Check if Supabase client exists
        if (typeof supabaseClient === 'undefined') {
            console.warn('Supabase client not found. Using default prices.');
            return;
        }

        // Update prices on page load
        await updatePagePrices();

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
        fetchPricing,
        updatePagePrices,
        getDynamicPrice: window.getDynamicPrice
    };

})();
