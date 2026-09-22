import assert from 'node:assert/strict';
import test from 'node:test';
import handleBooking, { buildBookingRecord } from '../api/booking-server.js';
import { calculateTrustedTotal, resolveProduct, resolveServerProduct } from '../api/booking-catalog.js';
import { setServerPriceOverride, resetServerPriceOverrides, clearServerCache, STABLE_SUPABASE_IDS } from '../api/server-product-data.js';
import ProductData from '../js/product-data.js';

function createResponse() {
  return {
    headers: {},
    statusCode: 200,
    setHeader(name, value) { this.headers[name.toLowerCase()] = value; },
    status(code) { this.statusCode = code; return this; },
    json(value) { this.body = value; this.ended = true; return this; },
    end() { this.ended = true; return this; }
  };
}

async function request(body, method = 'POST') {
  const req = {
    method,
    headers: { 'content-type': 'application/json', origin: 'http://127.0.0.1:5501' },
    body: JSON.stringify(body)
  };
  const res = createResponse();
  await handleBooking(req, res);
  return res;
}

test.before(() => {
  process.env.NODE_ENV = 'test';
  process.env.MARRAGAFAY_DEV_MODE = 'dry-run';
});

test('catalog totals use authoritative pack pricing', () => {
  assert.deepEqual(calculateTrustedTotal(resolveProduct('basic'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 900, totalEur: 90
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('standard'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 900, totalEur: 90
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('discovery pack'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 900, totalEur: 90
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('comfort'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 1500, totalEur: 150
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('private'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 1500, totalEur: 150
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('signature pack'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 1500, totalEur: 150
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('luxe'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 2380, totalEur: 238
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('private+'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 2380, totalEur: 238
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('luxury pack'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 2380, totalEur: 238
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('buggy'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 2580, totalEur: 258
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('buggy tour'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 2580, totalEur: 258
  });
});

test('valid request completes the local dry-run flow with attribution', async () => {
  const tomorrow = new Date(Date.now() + 86_400_000).toISOString().slice(0, 10);
  const res = await request({
    product_id: 'comfort',
    name: 'Local QA',
    phone: '+212600000000',
    date: tomorrow,
    adults: 2,
    children: 0,
    language: 'en',
    pickup: 'QA Riad (private round-trip transfer)',
    attribution: {
      inquiry_id: 'INQ-LOCAL-QA',
      booking_page: '/en/packages/comfort.html',
      pack_presented: 'comfort',
      final_requested_pack: 'comfort',
      pickup_context: 'QA Riad (private round-trip transfer)'
    }
  });

  assert.equal(res.statusCode, 200);
  assert.equal(res.body.booking_success, true);
  assert.equal(res.body.dry_run, true);
  assert.equal(res.body.trusted_total_mad, 1500);
  assert.equal(res.body.trusted_total_eur, 150);
  assert.match(res.body.booking_id, /^local-dry-run-/);
});

test('invalid request is rejected before persistence', async () => {
  const res = await request({});
  assert.equal(res.statusCode, 400);
  assert.equal(res.body.booking_success, false);
  assert.equal(res.body.error, 'product_id is invalid');
});

test('non-POST methods are rejected', async () => {
  const res = await request({}, 'GET');
  assert.equal(res.statusCode, 405);
  assert.equal(res.body.booking_success, false);
});

test('dynamic pricing normalization and defaults pass audit checks', async () => {
  const fs = await import('node:fs');
  const path = await import('node:path');
  const vm = await import('node:vm');

  const code = fs.readFileSync(path.resolve('./js/dynamic-pricing.js'), 'utf8');
  const context = {
    window: {
      location: { pathname: '/en/packs.html', hostname: '127.0.0.1' },
      sessionStorage: { getItem: () => null, setItem: () => {} },
      localStorage: { getItem: () => null, setItem: () => {} },
      addEventListener: () => {},
      ProductData
    },
    document: {
      documentElement: { lang: 'en' },
      querySelectorAll: () => [],
      getElementById: () => null,
      addEventListener: () => {},
      readyState: 'complete'
    },
    navigator: { language: 'en-US' },
    Intl, Date, Math, setTimeout, clearTimeout, console,
    supabaseClient: {
      from: () => ({
        select: () => ({
          eq: async () => ({
            data: [
              { type: 'pack', activity_name: 'Standard', price: 45, currency: '€', id: 1 },
              { type: 'pack', activity_name: 'Private', price: 75, currency: '€', id: 2 },
              { type: 'pack', activity_name: 'Private+', price: 119, currency: '€', id: 3 },
              { type: 'pack', activity_name: 'Buggy', price: 129, currency: '€', id: 4 }
            ],
            error: null
          })
        })
      })
    }
  };
  vm.createContext(context);
  vm.runInContext(code, context);
  const dp = context.window.DynamicPricing;

  // Type Normalization
  assert.equal(dp.normalizeType('pack'), 'package');
  assert.equal(dp.normalizeType('package'), 'package');
  assert.equal(dp.normalizeType('activity'), 'activity');

  // Product Name Normalization
  assert.equal(dp.normalizeProductName('Standard'), 'standard');
  assert.equal(dp.normalizeProductName('Basic'), 'standard');
  assert.equal(dp.normalizeProductName('Discovery Pack'), 'standard');
  assert.equal(dp.normalizeProductName('Private'), 'private');
  assert.equal(dp.normalizeProductName('Comfort'), 'private');
  assert.equal(dp.normalizeProductName('Signature Pack'), 'private');
  assert.equal(dp.normalizeProductName('Private+'), 'private-plus');
  assert.equal(dp.normalizeProductName('Luxe'), 'private-plus');
  assert.equal(dp.normalizeProductName('Luxury Pack'), 'private-plus');
  assert.equal(dp.normalizeProductName('Buggy'), 'buggy');
  assert.equal(dp.normalizeProductName('Buggy Tour'), 'buggy');

  // Default Fallback Prices
  const defaults = dp.getDefaultPrices();
  assert.equal(defaults['package_Basic'].price, 45);
  assert.equal(defaults['package_Comfort'].price, 75);
  assert.equal(defaults['package_Luxe'].price, 119);
  assert.equal(defaults['package_Buggy'].price, 129);
  assert.equal(defaults['activity_Buggy'].price, 129);
  assert.equal(defaults['package_Standard'].price, 45);
  assert.equal(defaults['package_Private'].price, 75);
  assert.equal(defaults['package_Private+'].price, 119);

  // MAD Mappings
  assert.equal(dp.CANONICAL_PRICES_MAD['activity_Buggy'], 1290);
  assert.equal(dp.CANONICAL_PRICES_MAD['package_Basic'], undefined);
  assert.equal(ProductData.getProduct('standard').priceMAD, 450);
  assert.equal(ProductData.getProduct('private').priceMAD, 750);
  assert.equal(ProductData.getProduct('private-plus').priceMAD, 1190);
  assert.equal(ProductData.getProduct('buggy').priceMAD, 1290);

  // Dynamic Price Queries with Supabase Mock
  assert.equal(await dp.getDynamicPrice('pack', 'Standard'), 45);
  assert.equal(await dp.getDynamicPrice('package', 'Basic'), 45);
  assert.equal(await dp.getDynamicPrice('pack', 'Private'), 75);
  assert.equal(await dp.getDynamicPrice('package', 'Comfort'), 75);
  assert.equal(await dp.getDynamicPrice('pack', 'Private+'), 119);
  assert.equal(await dp.getDynamicPrice('package', 'Luxe'), 119);
  assert.equal(await dp.getDynamicPrice('pack', 'Buggy'), 129);
  assert.equal(await dp.getDynamicPrice('activity', 'Buggy'), 129);
  assert.equal(await dp.getDynamicPrice('package', 'Buggy'), 129);
});

test('server product resolver resolves live Supabase products with stable UUIDs', async () => {
  const standard = await resolveServerProduct('standard');
  assert.ok(standard);
  assert.equal(standard.canonicalKey, 'standard');
  assert.equal(standard.supabaseId, STABLE_SUPABASE_IDS.standard);
  assert.equal(standard.unitPriceEur, 45);
  assert.equal(standard.unitPriceMad, 450);

  const priv = await resolveServerProduct('private');
  assert.ok(priv);
  assert.equal(priv.canonicalKey, 'private');
  assert.equal(priv.supabaseId, STABLE_SUPABASE_IDS.private);
  assert.equal(priv.unitPriceEur, 75);
  assert.equal(priv.unitPriceMad, 750);

  const privPlus = await resolveServerProduct('private-plus');
  assert.ok(privPlus);
  assert.equal(privPlus.canonicalKey, 'private-plus');
  assert.equal(privPlus.supabaseId, STABLE_SUPABASE_IDS['private-plus']);
  assert.equal(privPlus.unitPriceEur, 119);
  assert.equal(privPlus.unitPriceMad, 1190);

  const buggy = await resolveServerProduct('buggy');
  assert.ok(buggy);
  assert.equal(buggy.canonicalKey, 'buggy');
  assert.equal(buggy.supabaseId, STABLE_SUPABASE_IDS.buggy);
  assert.equal(buggy.unitPriceEur, 129);
  assert.equal(buggy.unitPriceMad, 1290);
});

test('server product resolver normalizes legacy aliases to canonical packages', async () => {
  const aliases = [
    { input: 'basic', expectedKey: 'standard', expectedEur: 45 },
    { input: 'discovery pack', expectedKey: 'standard', expectedEur: 45 },
    { input: 'Agafay Evening Experience', expectedKey: 'standard', expectedEur: 45 },
    { input: 'comfort', expectedKey: 'private', expectedEur: 75 },
    { input: 'signature pack', expectedKey: 'private', expectedEur: 75 },
    { input: 'Private Agafay Evening', expectedKey: 'private', expectedEur: 75 },
    { input: 'luxe', expectedKey: 'private-plus', expectedEur: 119 },
    { input: 'luxury', expectedKey: 'private-plus', expectedEur: 119 },
    { input: 'private+', expectedKey: 'private-plus', expectedEur: 119 },
    { input: 'buggy tour', expectedKey: 'buggy', expectedEur: 129 }
  ];

  for (const { input, expectedKey, expectedEur } of aliases) {
    const resolved = await resolveServerProduct(input);
    assert.ok(resolved, `Should resolve alias ${input}`);
    assert.equal(resolved.canonicalKey, expectedKey);
    assert.equal(resolved.unitPriceEur, expectedEur);
  }
});

test('client price tampering is completely ignored by the booking endpoint', async () => {
  const tomorrow = new Date(Date.now() + 86_400_000).toISOString().slice(0, 10);
  const tamperedPayload = {
    product_id: 'standard',
    name: 'Tamper Attempt',
    phone: '+212611111111',
    date: tomorrow,
    adults: 2,
    children: 0,
    // Tampered fields that client might attempt to submit:
    total_price: 1,
    total: 1,
    priceEUR: 1,
    priceMAD: 1,
    unitPriceEur: 1,
    unitPriceMad: 1
  };

  const res = await request(tamperedPayload);
  assert.equal(res.statusCode, 200);
  assert.equal(res.body.booking_success, true);
  // Trusted total must be 45 * 2 = 90 EUR / 900 MAD, not 1!
  assert.equal(res.body.trusted_total_mad, 900, 'Server must calculate 900 MAD, ignoring client tampering');
  assert.equal(res.body.trusted_total_eur, 90, 'Server must calculate 90 EUR, ignoring client tampering');
});

test('dynamic server price simulation updates trusted calculation', async () => {
  const tomorrow = new Date(Date.now() + 86_400_000).toISOString().slice(0, 10);

  // Simulate price change: Standard 45 EUR -> 46 EUR (460 MAD)
  setServerPriceOverride('standard', {
    unitPriceEur: 46,
    unitPriceMad: 460,
    priceEUR: 46,
    priceMAD: 460
  });

  try {
    const res = await request({
      product_id: 'standard',
      name: 'Simulation User',
      phone: '+212622222222',
      date: tomorrow,
      adults: 2,
      children: 0
    });

    assert.equal(res.statusCode, 200);
    assert.equal(res.body.trusted_total_eur, 92, '2 guests @ 46€ must equal 92€');
    assert.equal(res.body.trusted_total_mad, 920, '2 guests @ 460 MAD must equal 920 MAD');
  } finally {
    resetServerPriceOverrides();
  }

  // After reset, pricing returns to standard 45€
  const revertedRes = await request({
    product_id: 'standard',
    name: 'Standard User',
    phone: '+212622222222',
    date: tomorrow,
    adults: 2,
    children: 0
  });
  assert.equal(revertedRes.body.trusted_total_eur, 90);
  assert.equal(revertedRes.body.trusted_total_mad, 900);
});

test('server fallback handles Supabase failures gracefully', async () => {
  const originalFetch = globalThis.fetch;
  const originalWarn = console.warn;
  const warnings = [];
  console.warn = (...args) => {
    warnings.push(args.join(' '));
  };

  try {
    // Simulate network error to Supabase
    globalThis.fetch = async (url) => {
      if (typeof url === 'string' && url.includes('supabase.co')) {
        throw new Error('Simulated network timeout connecting to Supabase');
      }
      return originalFetch(url);
    };

    const fallbackProduct = await resolveServerProduct('standard');
    assert.ok(fallbackProduct);
    assert.equal(fallbackProduct.source, 'fallback');
    assert.equal(fallbackProduct.unitPriceEur, 45);
    assert.equal(fallbackProduct.unitPriceMad, 450);

    const tomorrow = new Date(Date.now() + 86_400_000).toISOString().slice(0, 10);
    const res = await request({
      product_id: 'standard',
      name: 'Offline Booking',
      phone: '+212633333333',
      date: tomorrow,
      adults: 2,
      children: 0
    });

    assert.equal(res.statusCode, 200);
    assert.equal(res.body.booking_success, true);
    assert.equal(res.body.trusted_total_eur, 90);
    assert.equal(res.body.trusted_total_mad, 900);
    assert.equal(res.body.pricing_source, 'fallback');

    // Verify operational warning was triggered
    const hasFallbackWarning = warnings.some(w =>
      w.includes('[MARRAGAFAY][PRICING] Supabase unavailable — fallback pricing used')
    );
    assert.ok(hasFallbackWarning, 'Operational warning must be logged when fallback is used');
  } finally {
    globalThis.fetch = originalFetch;
    console.warn = originalWarn;
  }
});

test('Buggy billing strictly enforces minimum 2 guests rule', async () => {
  const buggyProduct = await resolveServerProduct('buggy');
  assert.ok(buggyProduct);

  // 1 guest: billed for 2 (258€ / 2580 MAD)
  const calc1 = calculateTrustedTotal(buggyProduct, 1, 0);
  assert.equal(calc1.totalGuests, 1);
  assert.equal(calc1.billableGuests, 2);
  assert.equal(calc1.totalEur, 258);
  assert.equal(calc1.totalMad, 2580);

  // 2 guests: billed for 2 (258€ / 2580 MAD)
  const calc2 = calculateTrustedTotal(buggyProduct, 2, 0);
  assert.equal(calc2.totalGuests, 2);
  assert.equal(calc2.billableGuests, 2);
  assert.equal(calc2.totalEur, 258);
  assert.equal(calc2.totalMad, 2580);

  // 3 guests: billed for 3 (387€ / 3870 MAD)
  const calc3 = calculateTrustedTotal(buggyProduct, 3, 0);
  assert.equal(calc3.totalGuests, 3);
  assert.equal(calc3.billableGuests, 3);
  assert.equal(calc3.totalEur, 387);
  assert.equal(calc3.totalMad, 3870);
});

test('persisted booking record and response use identical trusted calculations', async () => {
  const product = await resolveServerProduct('private');
  const pricing = calculateTrustedTotal(product, 2, 0);

  const booking = {
    name: 'Consistency Test',
    email: 'test@marragafay.com',
    phone: '+212644444444',
    date: '2026-10-01',
    product,
    pricing,
    adults: 2,
    children: 0,
    notes: 'Test notes',
    attribution: null
  };

  const record = buildBookingRecord(booking);
  assert.equal(record.total_price, pricing.totalMad);
  assert.equal(record.guests, pricing.totalGuests);
  assert.equal(record.package_title, product.title);
});
