// Authoritative server-side product data and pricing resolver.
// Fetches live product pricing from Supabase with stable UUID verification,
// strict validation, resilient timeout, and automatic local fallback.

import { BOOKING_PRODUCTS, resolveProduct as resolveFallbackProduct } from './booking-catalog.js';

const SUPABASE_URL = process.env.SUPABASE_URL || 'https://bgjohquanepghmlmdiyd.supabase.co';
const SUPABASE_PUBLISHABLE_KEY = process.env.SUPABASE_PUBLISHABLE_KEY || 'sb_publishable_i3RLdEPI2p-B_CYrEw6dlw_3bKe9gzh';

// Stable UUIDs for primary packages
export const STABLE_SUPABASE_IDS = Object.freeze({
  standard: '9a233299-c908-4b91-92f2-789091a313e7',
  private: '0a910941-f45d-4cd9-8aea-57d478d9a61d',
  'private-plus': 'e10728b4-026a-40a8-b6b3-b2f95cf3f063',
  buggy: '22ab5a90-9889-4aaa-bb14-fe6173eae540'
});

// Mapping from canonical key to booking-catalog fallback ID
const CANONICAL_TO_FALLBACK_ID = Object.freeze({
  standard: 'basic',
  private: 'comfort',
  'private-plus': 'luxe',
  buggy: 'buggy',
  quad: 'quad',
  camel: 'camel',
  paragliding: 'paragliding',
  'hot-air-balloon': 'hot-air-balloon',
  'dinner-show': 'dinner-show'
});

// Normalization aliases
const ALIAS_MAP = Object.freeze({
  standard: 'standard', basic: 'standard', discovery: 'standard',
  'discovery pack': 'standard', 'discovery-pack': 'standard',
  'agafay discovery': 'standard', 'agafay-discovery': 'standard',
  'marragafay discovery': 'standard', 'agafay evening experience': 'standard',
  'agafay-evening-experience': 'standard', 'standard pack': 'standard',
  'standard-pack': 'standard',

  private: 'private', comfort: 'private', signature: 'private',
  'signature pack': 'private', 'signature-pack': 'private',
  'marragafay signature': 'private', 'private agafay evening': 'private',
  'private-agafay-evening': 'private', 'private pack': 'private',
  'private-pack': 'private', premium: 'private',

  'private+': 'private-plus', 'private +': 'private-plus',
  'private plus': 'private-plus', 'private-plus': 'private-plus',
  luxe: 'private-plus', luxury: 'private-plus', 'luxury pack': 'private-plus',
  'luxury-pack': 'private-plus', vip: 'private-plus',
  'the marragafay luxury': 'private-plus', 'agafay & atlas — full-day quad': 'private-plus',
  'agafay & atlas - full-day quad': 'private-plus', 'agafay and atlas full day quad': 'private-plus',
  'agafay & atlas': 'private-plus', 'private+ pack': 'private-plus',
  'private-plus pack': 'private-plus', 'private-plus-pack': 'private-plus',

  buggy: 'buggy', 'buggy tour': 'buggy', 'buggy-tour': 'buggy',
  'buggy experience': 'buggy', 'buggy-experience': 'buggy',
  'private agafay buggy experience': 'buggy', 'private-agafay-buggy-experience': 'buggy',
  'agafay buggy adventure marrakech': 'buggy',

  quad: 'quad', 'quad-biking': 'quad', 'quad biking': 'quad', 'quad agafay adventure': 'quad',
  camel: 'camel', 'camel-ride': 'camel', 'camel ride': 'camel', 'agafay camel ride marrakech': 'camel',
  paragliding: 'paragliding', parapente: 'paragliding',
  balloon: 'hot-air-balloon', 'hot-air-balloon': 'hot-air-balloon', 'hot air balloon': 'hot-air-balloon',
  'dinner-show': 'dinner-show', 'dinner & show': 'dinner-show', dinner: 'dinner-show', diner: 'dinner-show',
  'agafay dinner show marrakech': 'dinner-show'
});

export function normalizeCanonicalKey(value) {
  if (typeof value !== 'string') return '';
  const key = value.trim().toLowerCase().replace(/\s+/g, ' ').replace(/_/g, '-');
  return ALIAS_MAP[key] || key;
}

// Test simulation overrides
let serverPriceOverrides = {};

export function setServerPriceOverride(canonicalKey, overrideData) {
  const norm = normalizeCanonicalKey(canonicalKey);
  serverPriceOverrides[norm] = Object.freeze({ ...overrideData });
}

export function resetServerPriceOverrides() {
  serverPriceOverrides = {};
}

export function clearServerCache() {
  // Maintained for test suite compatibility (caching is disabled for booking consistency)
}

async function fetchSupabasePricingRows(timeoutMs = 2500) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const endpoint = `${SUPABASE_URL}/rest/v1/pricing?select=*&active=eq.true`;
    const response = await fetch(endpoint, {
      method: 'GET',
      signal: controller.signal,
      headers: {
        apikey: SUPABASE_PUBLISHABLE_KEY,
        Authorization: `Bearer ${SUPABASE_PUBLISHABLE_KEY}`,
        'Content-Type': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error(`Supabase pricing fetch returned HTTP ${response.status}`);
    }

    const rows = await response.json();
    if (!Array.isArray(rows)) {
      throw new Error('Supabase pricing response is not an array');
    }

    return rows;
  } finally {
    clearTimeout(timer);
  }
}

function findMatchingRow(rows, canonicalKey) {
  if (!Array.isArray(rows) || rows.length === 0) return null;

  // 1. Stable UUID lookup
  const stableId = STABLE_SUPABASE_IDS[canonicalKey];
  if (stableId) {
    const byId = rows.find(r => r.id === stableId);
    if (byId) return byId;
  }

  // 2. Name / activity_name normalization lookup
  return rows.find(r => {
    const rowName = r.activity_name || r.name || '';
    return normalizeCanonicalKey(rowName) === canonicalKey;
  }) || null;
}

function validateAndBuildProduct(row, canonicalKey, fallbackProduct) {
  if (!row || typeof row !== 'object') return null;

  // Validate active status
  const isActive = row.active === true || row.is_active === true;
  if (!isActive) return null;

  // Validate prices
  let priceMAD, priceEUR;
  if (row.currency === 'MAD') {
    priceMAD = Number(row.price);
    priceEUR = row.price_eur != null ? Number(row.price_eur) : Math.round(priceMAD / 10);
  } else {
    // currency EUR
    priceEUR = Number(row.price);
    // Public EUR fares are rounded independently from the official MAD fare.
    // Keep the reviewed local MAD price rather than applying a 10:1 estimate.
    priceMAD = fallbackProduct?.unitPriceMad;
  }

  if (!Number.isFinite(priceMAD) || priceMAD <= 0) return null;
  if (!Number.isFinite(priceEUR) || priceEUR <= 0) return null;

  // Normalize type
  const rawType = String(row.type || '').toLowerCase();
  const type = (rawType === 'pack' || rawType === 'package' || rawType === 'packages' || rawType === 'packs')
    ? 'package'
    : 'activity';

  // Ensure type matches fallback expectation
  if (fallbackProduct && fallbackProduct.type !== type) {
    return null;
  }

  const fallbackId = CANONICAL_TO_FALLBACK_ID[canonicalKey] || fallbackProduct?.id || canonicalKey;
  const title = fallbackProduct?.title || row.activity_name || row.name || canonicalKey;

  return Object.freeze({
    id: fallbackId,
    canonicalKey,
    supabaseId: row.id || STABLE_SUPABASE_IDS[canonicalKey] || null,
    type,
    title,
    name: row.activity_name || row.name || fallbackProduct?.name || canonicalKey,
    unitPriceMad: priceMAD,
    unitPriceEur: priceEUR,
    priceMAD,
    priceEUR,
    duration: row.duration || null,
    source: 'supabase'
  });
}

function buildFallbackProduct(canonicalKey, fallbackProduct) {
  if (!fallbackProduct) return null;
  const fallbackId = CANONICAL_TO_FALLBACK_ID[canonicalKey] || fallbackProduct.id;

  return Object.freeze({
    id: fallbackId,
    canonicalKey,
    supabaseId: STABLE_SUPABASE_IDS[canonicalKey] || null,
    type: fallbackProduct.type,
    title: fallbackProduct.title,
    name: fallbackProduct.title,
    unitPriceMad: fallbackProduct.unitPriceMad,
    unitPriceEur: fallbackProduct.unitPriceEur,
    priceMAD: fallbackProduct.unitPriceMad,
    priceEUR: fallbackProduct.unitPriceEur,
    duration: null,
    source: 'fallback'
  });
}

export async function resolveServerProduct(identifier, observability = {}) {
  const canonicalKey = normalizeCanonicalKey(identifier);
  if (!canonicalKey) return null;

  const fallbackId = CANONICAL_TO_FALLBACK_ID[canonicalKey] || canonicalKey;
  const fallbackProduct = BOOKING_PRODUCTS[fallbackId] || resolveFallbackProduct(identifier);

  // Check test simulation overrides first
  if (serverPriceOverrides[canonicalKey]) {
    const base = buildFallbackProduct(canonicalKey, fallbackProduct);
    if (!base) return null;
    return Object.freeze({
      ...base,
      ...serverPriceOverrides[canonicalKey],
      source: 'simulation'
    });
  }

  // Attempt live Supabase resolution
  try {
    const rows = await fetchSupabasePricingRows();
    const matchedRow = findMatchingRow(rows, canonicalKey);
    const validProduct = validateAndBuildProduct(matchedRow, canonicalKey, fallbackProduct);
    if (validProduct) {
      return validProduct;
    }
    console.warn('[MARRAGAFAY][PRICING] Supabase unavailable — fallback pricing used', JSON.stringify({ event: 'pricing_fallback', product_id: canonicalKey, request_id: observability.requestId || null, reason_category: 'invalid_supabase_product' }));
  } catch (err) {
    // Supabase failure or timeout - safely fall back to local catalog
    console.warn('[MARRAGAFAY][PRICING] Supabase unavailable — fallback pricing used', JSON.stringify({ event: 'pricing_fallback', product_id: canonicalKey, request_id: observability.requestId || null, reason_category: err?.name === 'AbortError' ? 'timeout' : 'supabase_unavailable' }));
  }

  // Safe local fallback
  return buildFallbackProduct(canonicalKey, fallbackProduct);
}
