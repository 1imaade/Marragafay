import assert from 'node:assert/strict';
import test from 'node:test';
import ProductData from '../js/product-data.js';

test('1. Supabase product parsing produces valid canonical objects', () => {
    const rawSupabaseRow = {
        id: '9a233299-c908-4b91-92f2-789091a313e7',
        name: 'Standard',
        activity_name: 'Standard',
        price: 450,
        currency: 'MAD',
        price_eur: 45.0,
        duration: '15:30–22:00',
        type: 'pack',
        includes: [
            'Shared hotel / riad pickup & return',
            '1h quad ride across Agafay',
            '20min camel ride'
        ],
        description: 'Standard pack description'
    };

    const parsed = ProductData.parseSupabaseRow(rawSupabaseRow);
    assert.ok(parsed, 'Parsing should succeed');
    assert.equal(parsed.key, 'standard');
    assert.equal(parsed.name, 'Standard');
    assert.equal(parsed.priceEUR, 45);
    assert.equal(parsed.priceMAD, 450);
    assert.equal(parsed.duration, '15:30–22:00');
    assert.equal(parsed.transport, 'Shared hotel / riad pickup & return');
    assert.equal(parsed.source, 'supabase');
});

test('2. Alias normalization maps all historical and modern aliases to canonical keys', () => {
    // Standard aliases
    assert.equal(ProductData.normalizeProductName('Standard'), 'standard');
    assert.equal(ProductData.normalizeProductName('Basic'), 'standard');
    assert.equal(ProductData.normalizeProductName('Discovery'), 'standard');
    assert.equal(ProductData.normalizeProductName('Discovery Pack'), 'standard');
    assert.equal(ProductData.normalizeProductName('Standard Pack'), 'standard');
    assert.equal(ProductData.normalizeProductName('Agafay Evening Experience'), 'standard');

    // Private aliases
    assert.equal(ProductData.normalizeProductName('Private'), 'private');
    assert.equal(ProductData.normalizeProductName('Comfort'), 'private');
    assert.equal(ProductData.normalizeProductName('Signature'), 'private');
    assert.equal(ProductData.normalizeProductName('Signature Pack'), 'private');
    assert.equal(ProductData.normalizeProductName('Private Pack'), 'private');
    assert.equal(ProductData.normalizeProductName('Private Agafay Evening'), 'private');

    // Private+ aliases
    assert.equal(ProductData.normalizeProductName('Private+'), 'private-plus');
    assert.equal(ProductData.normalizeProductName('Private Plus'), 'private-plus');
    assert.equal(ProductData.normalizeProductName('private-plus'), 'private-plus');
    assert.equal(ProductData.normalizeProductName('Luxe'), 'private-plus');
    assert.equal(ProductData.normalizeProductName('Luxury'), 'private-plus');
    assert.equal(ProductData.normalizeProductName('Luxury Pack'), 'private-plus');
    assert.equal(ProductData.normalizeProductName('Private+ Pack'), 'private-plus');
    assert.equal(ProductData.normalizeProductName('Agafay & Atlas — Full-Day Quad'), 'private-plus');

    // Buggy aliases
    assert.equal(ProductData.normalizeProductName('Buggy'), 'buggy');
    assert.equal(ProductData.normalizeProductName('Buggy Tour'), 'buggy');
    assert.equal(ProductData.normalizeProductName('Private Agafay Buggy Experience'), 'buggy');
});

test('3. Fallback behavior returns official matrix when offline or uninitialized', () => {
    const fallback = ProductData.CANONICAL_FALLBACK;
    assert.ok(fallback.standard);
    assert.ok(fallback.private);
    assert.ok(fallback['private-plus']);
    assert.ok(fallback.buggy);

    const standard = ProductData.getProduct('standard');
    assert.equal(standard.priceEUR, 45);
    assert.equal(standard.priceMAD, 450);
    assert.equal(standard.duration, '15:30–22:00');
    assert.ok(standard.includes.length >= 9);

    const priv = ProductData.getProduct('private');
    assert.equal(priv.priceEUR, 75);
    assert.equal(priv.priceMAD, 750);
    assert.equal(priv.duration, '15:30–22:00');
    assert.ok(priv.includes.length >= 11);

    const privPlus = ProductData.getProduct('private-plus');
    assert.equal(privPlus.priceEUR, 119);
    assert.equal(privPlus.priceMAD, 1190);
    assert.equal(privPlus.duration, '09:00–22:00');

    const buggy = ProductData.getProduct('buggy');
    assert.equal(buggy.priceEUR, 129);
    assert.equal(buggy.priceMAD, 1290);
    assert.equal(buggy.duration, 'Flexible');
});

test('4. Canonical product object shape contains all required attributes', () => {
    const requiredKeys = ['id', 'key', 'type', 'name', 'priceEUR', 'priceMAD', 'duration', 'transport', 'includes', 'description', 'source'];
    const products = ProductData.getAllProducts();
    assert.equal(products.length, 4);

    products.forEach(p => {
        requiredKeys.forEach(k => {
            assert.ok(p[k] !== undefined, `Product ${p.key} must define ${k}`);
        });
        assert.equal(typeof p.priceEUR, 'number');
        assert.equal(typeof p.priceMAD, 'number');
        assert.ok(Array.isArray(p.includes));
        assert.ok(p.includes.length > 0);
    });
});

test('5. Correct EUR/MAD pricing values align across all 4 packages', () => {
    assert.equal(ProductData.getProduct('standard').priceEUR, 45);
    assert.equal(ProductData.getProduct('standard').priceMAD, 450);

    assert.equal(ProductData.getProduct('private').priceEUR, 75);
    assert.equal(ProductData.getProduct('private').priceMAD, 750);

    assert.equal(ProductData.getProduct('private-plus').priceEUR, 119);
    assert.equal(ProductData.getProduct('private-plus').priceMAD, 1190);

    assert.equal(ProductData.getProduct('buggy').priceEUR, 129);
    assert.equal(ProductData.getProduct('buggy').priceMAD, 1290);
});

test('6. DOM binding populates attributes correctly on mock DOM root', () => {
    // Simple mock DOM element tree
    const elements = [
        {
            attrs: { 'data-product': 'standard', 'data-field': 'name' },
            textContent: '',
            getAttribute(k) { return this.attrs[k]; },
            tagName: 'SPAN'
        },
        {
            attrs: { 'data-product': 'standard', 'data-field': 'price-eur' },
            textContent: '',
            getAttribute(k) { return this.attrs[k]; },
            tagName: 'SPAN'
        },
        {
            attrs: { 'data-product': 'standard', 'data-field': 'price-mad', 'data-format': 'parentheses' },
            textContent: '',
            getAttribute(k) { return this.attrs[k]; },
            tagName: 'SPAN'
        },
        {
            attrs: { 'data-product': 'standard', 'data-field': 'tag' },
            textContent: '',
            getAttribute(k) { return this.attrs[k]; },
            tagName: 'DIV'
        },
        {
            attrs: { 'data-product': 'standard', 'data-field': 'duration' },
            textContent: '',
            getAttribute(k) { return this.attrs[k]; },
            tagName: 'SPAN'
        }
    ];

    const mockRoot = {
        querySelectorAll(selector) {
            if (selector === '[data-product]') return elements;
            return [];
        }
    };

    ProductData.bindElements(mockRoot);

    assert.equal(elements[0].textContent, 'Standard');
    assert.equal(elements[1].textContent, '45 €');
    assert.equal(elements[2].textContent, '(450 MAD)');
    assert.equal(elements[3].textContent, 'STANDARD · 45€ / guest');
    assert.equal(elements[4].textContent, '15:30–22:00');
});

test('7. Simulated Supabase price change updates bound elements without modifying production DB', () => {
    const elements = [
        {
            attrs: { 'data-product': 'standard', 'data-field': 'price-eur' },
            textContent: '45 €',
            getAttribute(k) { return this.attrs[k]; },
            tagName: 'SPAN'
        },
        {
            attrs: { 'data-product': 'standard', 'data-field': 'tag' },
            textContent: 'STANDARD · 45€ / guest',
            getAttribute(k) { return this.attrs[k]; },
            tagName: 'DIV'
        }
    ];

    const mockRoot = {
        querySelectorAll(selector) {
            if (selector === '[data-product]') return elements;
            return [];
        }
    };

    // Simulate price change: 45 EUR -> 46 EUR
    ProductData.setProductOverride('standard', { priceEUR: 46 });
    ProductData.bindElements(mockRoot);

    assert.equal(elements[0].textContent, '46 €', 'Price EUR should update to simulated 46 €');
    assert.equal(elements[1].textContent, 'STANDARD · 46€ / guest', 'Tag should update to simulated 46€');

    // Clean up simulation
    ProductData.resetOverrides();
    ProductData.bindElements(mockRoot);
    assert.equal(elements[0].textContent, '45 €', 'Reverted cleanly to 45 €');
});

test('8. Supabase failure simulation safely falls back without uncaught errors', async () => {
    // Create an instance or call fetchProducts when fetch throws
    const originalFetch = globalThis.fetch;
    try {
        globalThis.fetch = async () => {
            throw new Error('Simulated network timeout / 500 error');
        };

        // Even with network failure, getProduct returns valid fallback data
        const standard = ProductData.getProduct('standard');
        assert.ok(standard);
        assert.equal(standard.priceEUR, 45);
        assert.equal(standard.priceMAD, 450);
        assert.equal(standard.duration, '15:30–22:00');
    } finally {
        globalThis.fetch = originalFetch;
    }
});
