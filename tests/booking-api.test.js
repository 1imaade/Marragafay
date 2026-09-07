import assert from 'node:assert/strict';
import test from 'node:test';
import handleBooking from '../api/booking-server.js';
import { calculateTrustedTotal, resolveProduct } from '../api/booking-catalog.js';

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
    totalGuests: 2, billableGuests: 2, totalMad: 700, totalEur: 70
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('comfort'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 998, totalEur: 98
  });
  assert.deepEqual(calculateTrustedTotal(resolveProduct('luxe'), 2, 0), {
    totalGuests: 2, billableGuests: 2, totalMad: 1798, totalEur: 178
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
    pickup: 'QA Riad (shared door-to-door, subject to vehicle access)',
    attribution: {
      inquiry_id: 'INQ-LOCAL-QA',
      booking_page: '/en/packages/comfort.html',
      pack_presented: 'comfort',
      final_requested_pack: 'comfort',
      pickup_context: 'QA Riad (shared door-to-door, subject to vehicle access)'
    }
  });

  assert.equal(res.statusCode, 200);
  assert.equal(res.body.booking_success, true);
  assert.equal(res.body.dry_run, true);
  assert.equal(res.body.trusted_total_mad, 998);
  assert.equal(res.body.trusted_total_eur, 98);
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
