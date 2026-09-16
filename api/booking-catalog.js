// Trusted server-side booking catalog and pricing rules.
// Keep customer-supplied titles and prices out of this module's authority.

export const BOOKING_PRODUCTS = Object.freeze({
  basic: Object.freeze({ id: 'basic', type: 'package', title: 'Agafay Evening Experience', unitPriceMad: 450, unitPriceEur: 45 }),
  comfort: Object.freeze({ id: 'comfort', type: 'package', title: 'Private Agafay Evening', unitPriceMad: 750, unitPriceEur: 75 }),
  luxe: Object.freeze({ id: 'luxe', type: 'package', title: 'Agafay & Atlas — Full-Day Quad', unitPriceMad: 1190, unitPriceEur: 119 }),
  buggy: Object.freeze({ id: 'buggy', type: 'package', title: 'Private Agafay Buggy Experience', unitPriceMad: 1290, unitPriceEur: 129 }),
  quad: Object.freeze({ id: 'quad', type: 'activity', title: 'Quad Biking', unitPriceMad: 250, unitPriceEur: 25 }),
  camel: Object.freeze({ id: 'camel', type: 'activity', title: 'Camel Ride', unitPriceMad: 100, unitPriceEur: 10 }),
  paragliding: Object.freeze({ id: 'paragliding', type: 'activity', title: 'Paragliding', unitPriceMad: 799, unitPriceEur: 80 }),
  'hot-air-balloon': Object.freeze({ id: 'hot-air-balloon', type: 'activity', title: 'Hot Air Balloon', unitPriceMad: 1750, unitPriceEur: 175 }),
  'dinner-show': Object.freeze({ id: 'dinner-show', type: 'activity', title: 'Dinner & Show', unitPriceMad: 250, unitPriceEur: 25 })
});

const PRODUCT_ALIASES = Object.freeze({
  basic: 'basic', standard: 'basic', discovery: 'basic', 'agafay-discovery': 'basic',
  'agafay discovery': 'basic', 'marragafay discovery': 'basic',
  'agafay evening experience': 'basic', 'agafay-evening-experience': 'basic',
  comfort: 'comfort', private: 'comfort', signature: 'comfort', premium: 'comfort', 'marragafay signature': 'comfort',
  'private agafay evening': 'comfort', 'private-agafay-evening': 'comfort',
  luxe: 'luxe', luxury: 'luxe', 'private+': 'luxe', 'private plus': 'luxe', 'private-plus': 'luxe', vip: 'luxe', 'the marragafay luxury': 'luxe',
  'agafay & atlas — full-day quad': 'luxe', 'agafay & atlas - full-day quad': 'luxe', 'agafay-atlas-full-day-quad': 'luxe',
  'agafay and atlas full day quad': 'luxe', 'agafay & atlas': 'luxe',
  quad: 'quad', 'quad-biking': 'quad', 'quad biking': 'quad', 'quad agafay adventure': 'quad',
  buggy: 'buggy', 'private agafay buggy experience': 'buggy', 'private-agafay-buggy-experience': 'buggy', 'agafay buggy adventure marrakech': 'buggy',
  camel: 'camel', 'camel-ride': 'camel', 'camel ride': 'camel', 'agafay camel ride marrakech': 'camel',
  paragliding: 'paragliding', parapente: 'paragliding',
  balloon: 'hot-air-balloon', 'hot-air-balloon': 'hot-air-balloon', 'hot air balloon': 'hot-air-balloon',
  'dinner-show': 'dinner-show', 'dinner & show': 'dinner-show', dinner: 'dinner-show', diner: 'dinner-show',
  'agafay dinner show marrakech': 'dinner-show'
});

function normalizeKey(value) {
  return typeof value === 'string' ? value.trim().toLowerCase().replace(/\s+/g, ' ') : '';
}

export function resolveProduct(value) {
  const key = normalizeKey(value).replace(/_/g, '-');
  const productId = PRODUCT_ALIASES[key];
  return productId ? BOOKING_PRODUCTS[productId] : null;
}

export function calculateTrustedTotal(product, adults, children) {
  const totalGuests = adults + children;
  let billableGuests = totalGuests;

  if (product.id === 'quad' || product.id === 'dinner-show') {
    billableGuests = adults;
  } else if (product.id === 'buggy') {
    billableGuests = Math.max(2, totalGuests);
  }

  return {
    totalGuests,
    billableGuests,
    totalMad: product.unitPriceMad * billableGuests,
    totalEur: product.unitPriceEur * billableGuests
  };
}
