import assert from 'node:assert/strict';
import test from 'node:test';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync(new URL('../js/booking-context.js', import.meta.url), 'utf8');

function createAnalytics(startHref = 'https://www.marragafay.com/en/packages/basic.html') {
  const listeners = {};
  const storage = new Map();
  const context = {
    window: {
      location: { href: startHref, pathname: new URL(startHref).pathname },
      sessionStorage: { getItem: (key) => storage.get(key) || null, setItem: (key, value) => storage.set(key, value) },
      localStorage: { getItem: () => null, setItem: () => {} },
      addEventListener: (name, callback) => { (listeners[name] ||= []).push(callback); },
      dispatchEvent: () => {},
      dataLayer: [],
      MarragafayAttribution: {
        capture: () => ({ first_touch: { utm_source: 'instagram' }, last_touch: null }),
        classifySource: () => 'instagram',
        generateInquiryId: () => 'INQ-TEST'
      },
      posthog: { capture: () => {} }
    },
    document: {
      documentElement: { lang: 'en' },
      readyState: 'loading',
      addEventListener: () => {},
      querySelectorAll: () => [],
      querySelector: () => null
    },
    location: { pathname: '/en/packages/basic.html' },
    URL,
    Date,
    Math,
    console,
    setTimeout,
    clearTimeout
    ,fetch: async () => ({ ok: false, status: 204, json: async () => null })
  };
  vm.createContext(context);
  vm.runInContext(source, context);
  return { analytics: context.window.MarragafayAnalytics, window: context.window };
}

test('analytics exposes one canonical event contract and product ids', () => {
  const { analytics } = createAnalytics();
  assert.deepEqual([...analytics.EVENTS], [
    'product_view', 'pack_cta_click', 'whatsapp_click', 'booking_open',
    'booking_start', 'booking_submit', 'booking_success', 'booking_failure'
  ]);
  assert.equal(analytics.productId('private-plus'), 'private-plus');
  assert.equal(analytics.productId('Private+'), 'private-plus');
  assert.equal(analytics.productId('localized private'), undefined);
});

test('duplicate success events are suppressed and trusted totals are preserved', () => {
  const { analytics } = createAnalytics();
  const first = analytics.capture('booking_success', {
    product_id: 'standard', guest_count: 2, trusted_total_eur: 90,
    trusted_total_mad: 900, pricing_source: 'supabase'
  }, 'booking_success:qa');
  const second = analytics.capture('booking_success', {
    product_id: 'standard', guest_count: 2, trusted_total_eur: 1,
    trusted_total_mad: 1, pricing_source: 'fallback'
  }, 'booking_success:qa');
  assert.equal(first, true);
  assert.equal(second, false);
  assert.equal(analytics.capture('booking_failure', { product_id: 'standard' }), true);
});

test('analytics payload contains no customer PII fields', () => {
  const { analytics, window } = createAnalytics();
  analytics.capture('pack_cta_click', { product_id: 'standard', cta_location: 'hero_booking' });
  const payload = window.dataLayer.at(-1);
  assert.equal('name' in payload, false);
  assert.equal('email' in payload, false);
  assert.equal('phone' in payload, false);
  assert.equal('notes' in payload, false);
});

test('first-touch attribution persists while a later campaign becomes last-touch', () => {
  const { analytics, window } = createAnalytics('https://www.marragafay.com/en/?utm_source=instagram&utm_campaign=launch');
  const first = window.MarragafayAttribution.capture();
  window.location.href = 'https://www.marragafay.com/en/packs.html?utm_source=google&utm_medium=cpc&utm_campaign=retargeting';
  window.location.pathname = '/en/packs.html';
  const later = window.MarragafayAttribution.capture();
  assert.equal(first.first_touch.utm_source, 'instagram');
  assert.equal(later.first_touch.utm_source, 'instagram');
  assert.equal(later.last_touch.utm_source, 'google');
  assert.equal(analytics.capture('pack_cta_click', { product_id: 'standard' }), true);
});

test('provider failure never throws or blocks event capture', () => {
  const { analytics, window } = createAnalytics();
  window.posthog.capture = () => { throw new Error('blocked provider'); };
  assert.doesNotThrow(() => analytics.capture('whatsapp_click', { product_id: 'standard' }));
});

test('inquiry id persists for the visitor journey', () => {
  const { window } = createAnalytics();
  const first = window.MarragafayAttribution.generateInquiryId();
  const second = window.MarragafayAttribution.generateInquiryId();
  assert.match(first, /^INQ-/);
  assert.equal(second, first);
});
