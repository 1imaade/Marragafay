// Trusted server-side booking catalog and pricing rules.
// Keep customer-supplied titles and prices out of this module's authority.

export const BOOKING_PRODUCTS = Object.freeze({
  basic: Object.freeze({ id: 'basic', type: 'package', title: 'Agafay Discovery', unitPriceMad: 350, unitPriceEur: 35 }),
  comfort: Object.freeze({ id: 'comfort', type: 'package', title: 'Marragafay Signature', unitPriceMad: 499, unitPriceEur: 49 }),
  luxe: Object.freeze({ id: 'luxe', type: 'package', title: 'The Marragafay Luxury', unitPriceMad: 890, unitPriceEur: 89 }),
  quad: Object.freeze({ id: 'quad', type: 'activity', title: 'Quad Biking', unitPriceMad: 250, unitPriceEur: 25 }),
  buggy: Object.freeze({ id: 'buggy', type: 'activity', title: 'Buggy', unitPriceMad: 800, unitPriceEur: 80 }),
  camel: Object.freeze({ id: 'camel', type: 'activity', title: 'Camel Ride', unitPriceMad: 100, unitPriceEur: 10 }),
  paragliding: Object.freeze({ id: 'paragliding', type: 'activity', title: 'Paragliding', unitPriceMad: 799, unitPriceEur: 80 }),
  'hot-air-balloon': Object.freeze({ id: 'hot-air-balloon', type: 'activity', title: 'Hot Air Balloon', unitPriceMad: 1750, unitPriceEur: 175 }),
  'dinner-show': Object.freeze({ id: 'dinner-show', type: 'activity', title: 'Dinner & Show', unitPriceMad: 250, unitPriceEur: 25 })
});

const PRODUCT_ALIASES = Object.freeze({
  basic: 'basic', discovery: 'basic', 'agafay-discovery': 'basic',
  'agafay discovery': 'basic', 'marragafay discovery': 'basic',
  comfort: 'comfort', signature: 'comfort', premium: 'comfort', 'marragafay signature': 'comfort',
  luxe: 'luxe', luxury: 'luxe', vip: 'luxe', 'the marragafay luxury': 'luxe',
  quad: 'quad', 'quad-biking': 'quad', 'quad biking': 'quad', 'quad agafay adventure': 'quad',
  buggy: 'buggy', 'agafay buggy adventure marrakech': 'buggy',
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
