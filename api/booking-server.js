// Authoritative server-side booking flow.
// Database persistence is the booking result; notification delivery is secondary.

import { createClient } from '@supabase/supabase-js';
import { calculateTrustedTotal, resolveProduct } from './booking-catalog.js';

const SUPABASE_URL = process.env.SUPABASE_URL || 'https://bgjohquanepghmlmdiyd.supabase.co';
const MAX_BODY_BYTES = 32 * 1024;
const MAX_GUESTS = 30;
const MAX_NAME_LENGTH = 120;
const MAX_PHONE_LENGTH = 40;
const MAX_EMAIL_LENGTH = 254;
const MAX_NOTES_LENGTH = 2_000;
const SUPPORTED_LANGUAGES = new Set(['en', 'fr', 'es', 'ar']);
const ALLOWED_ORIGINS = new Set([
  'https://marragafay.com',
  'https://www.marragafay.com',
  'http://localhost:3000',
  'http://localhost:5500',
  'http://127.0.0.1:5500'
]);

class ValidationError extends Error {}

function setCorsHeaders(req, res) {
  const origin = req.headers?.origin;
  if (ALLOWED_ORIGINS.has(origin)) res.setHeader('Access-Control-Allow-Origin', origin);
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Requested-With');
  res.setHeader('Vary', 'Origin');
}

function scalarValue(body, keys) {
  for (const key of keys) {
    if (Object.prototype.hasOwnProperty.call(body, key)) return body[key];
  }
  return undefined;
}

function safeString(value, field, maxLength, required = false) {
  if (value === undefined || value === null || value === '') {
    if (required) throw new ValidationError(`${field} is required`);
    return '';
  }
  if (typeof value !== 'string') throw new ValidationError(`${field} must be a string`);
  const normalized = value.trim();
  if (required && !normalized) throw new ValidationError(`${field} is required`);
  if (normalized.length > maxLength) throw new ValidationError(`${field} is too long`);
  return normalized;
}

function parseCount(value, field, required = false) {
  if (value === undefined || value === null || value === '') {
    if (required) throw new ValidationError(`${field} is required`);
    return null;
  }
  if (typeof value !== 'string' && typeof value !== 'number') {
    throw new ValidationError(`${field} must be a number`);
  }
  const text = String(value).trim();
  if (!/^\d+$/.test(text)) throw new ValidationError(`${field} must be a whole number`);
  const parsed = Number(text);
  if (!Number.isSafeInteger(parsed) || parsed < 0 || parsed > MAX_GUESTS) {
    throw new ValidationError(`${field} is outside the allowed range`);
  }
  return parsed;
}

function parseJsonBody(req) {
  const contentType = String(req.headers?.['content-type'] || '').toLowerCase();
  const contentLength = Number(req.headers?.['content-length'] || 0);
  if (contentLength > MAX_BODY_BYTES) throw new ValidationError('Request payload is too large');

  if (typeof req.body === 'string') {
    if (Buffer.byteLength(req.body, 'utf8') > MAX_BODY_BYTES) {
      throw new ValidationError('Request payload is too large');
    }
    try {
      return JSON.parse(req.body);
    } catch {
      throw new ValidationError('Request body must be valid JSON');
    }
  }

  if (!contentType.includes('application/json')) {
    throw new ValidationError('Content-Type must be application/json');
  }
  return req.body;
}

export function getMoroccoCalendarDate(now = new Date()) {
  const parts = new Intl.DateTimeFormat('en-US', {
    timeZone: 'Africa/Casablanca',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  }).formatToParts(now);
  const values = Object.fromEntries(parts.map(({ type, value }) => [type, value]));
  return `${values.year}-${values.month}-${values.day}`;
}

function parseDate(value) {
  const date = safeString(value, 'date', 10, true);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) throw new ValidationError('date must use YYYY-MM-DD');
  const [year, month, day] = date.split('-').map(Number);
  const parsed = new Date(Date.UTC(year, month - 1, day));
  if (Number.isNaN(parsed.getTime()) || parsed.getUTCFullYear() !== year || parsed.getUTCMonth() !== month - 1 || parsed.getUTCDate() !== day) {
    throw new ValidationError('date is invalid');
  }
  if (date < getMoroccoCalendarDate()) {
    throw new ValidationError('date cannot be in the past');
  }
  return date;
}

function parsePhone(value) {
  const phone = safeString(value, 'phone', MAX_PHONE_LENGTH, true);
  if (!/^[0-9+().\s-]+$/.test(phone)) throw new ValidationError('phone is invalid');
  const digits = phone.replace(/\D/g, '');
  if (digits.length < 7 || digits.length > 15) throw new ValidationError('phone is invalid');
  return phone;
}

function parseEmail(value) {
  const email = safeString(value, 'email', MAX_EMAIL_LENGTH);
  if (!email) return null;
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) throw new ValidationError('email is invalid');
  return email;
}

function parseLanguage(value) {
  const language = safeString(value || 'en', 'language', 2);
  if (!SUPPORTED_LANGUAGES.has(language)) throw new ValidationError('language is invalid');
  return language;
}

function normalizeBooking(body) {
  if (!body || Array.isArray(body) || typeof body !== 'object') {
    throw new ValidationError('Request body must be an object');
  }

  const product = resolveProduct(scalarValue(body, [
    'product_id', 'productId', 'product', 'package_title', 'package'
  ]));
  if (!product) throw new ValidationError('product_id is invalid');

  const name = safeString(scalarValue(body, ['name', 'full_name']), 'name', MAX_NAME_LENGTH, true);
  const phone = parsePhone(scalarValue(body, ['phone_number', 'phone']));
  const email = parseEmail(scalarValue(body, ['email']));
  const date = parseDate(scalarValue(body, ['date', 'booking_date']));
  const notes = safeString(scalarValue(body, ['notes', 'requests', 'message']), 'notes', MAX_NOTES_LENGTH);
  const language = parseLanguage(scalarValue(body, ['language', 'lang']));
  const children = parseCount(scalarValue(body, ['children']), 'children') ?? 0;

  const adultsValue = scalarValue(body, ['adults']);
  const guestsValue = scalarValue(body, ['guests', 'groupSize', 'group_size']);
  const adults = adultsValue !== undefined && adultsValue !== null && adultsValue !== ''
    ? parseCount(adultsValue, 'adults', true)
    : parseCount(guestsValue, 'guests', true);

  if (adults + children < 1 || adults + children > MAX_GUESTS) {
    throw new ValidationError('guest count is outside the allowed range');
  }
  if (product.id === 'quad' && (adults < 1 || children > adults)) {
    throw new ValidationError('quad bookings require at least one adult and no more children than riders');
  }

  return {
    product,
    name,
    phone,
    email,
    date,
    notes,
    language,
    adults,
    children,
    pricing: calculateTrustedTotal(product, adults, children)
  };
}

function htmlEscape(value) {
  return String(value ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function buildEmailHtml(booking) {
  const safeName = htmlEscape(booking.name);
  const safePhone = htmlEscape(booking.phone);
  const safeDate = htmlEscape(booking.date);
  const safeNotes = htmlEscape(booking.notes || 'No special requests');
  const safeProductTitle = htmlEscape(booking.product.title);
  const safeLanguage = htmlEscape(booking.language);
  const phoneDigits = booking.phone.replace(/\D/g, '');
  const waUrl = phoneDigits ? `https://wa.me/${phoneDigits}` : '';
  const safeWaUrl = htmlEscape(waUrl);
  const waAction = waUrl
    ? `<a href="${safeWaUrl}" target="_blank" rel="noopener" style="display:block;text-align:center;background:#18181B;color:#FFF;font-size:13px;font-weight:600;padding:11px 20px;border-radius:6px;text-decoration:none;">Contact Customer on WhatsApp ↗</a>`
    : '';

  return `<!DOCTYPE html><html><body style="margin:0;padding:24px 12px;background:#F4F4F5;font-family:Arial,sans-serif;color:#18181B;">
  <div style="max-width:480px;margin:0 auto;background:#FFF;border:1px solid #E4E4E7;border-top:3px solid #18181B;border-radius:8px;overflow:hidden;">
    <div style="padding:20px 24px 16px;background:#FAFAFA;border-bottom:1px solid #F4F4F5;"><div style="font-size:10px;font-weight:700;letter-spacing:1.5px;color:#71717A;">MARRAGAFAY BOOKING</div><div style="font-size:16px;font-weight:700;margin-top:2px;">${safeProductTitle}</div></div>
    <div style="padding:20px 24px 22px;"><table style="width:100%;border-collapse:collapse;margin-bottom:18px;">
      <tr><td style="padding:6px 0;width:110px;color:#71717A;">Customer</td><td style="padding:6px 0;font-weight:600;">${safeName}</td></tr>
      <tr><td style="padding:6px 0;color:#71717A;">WhatsApp</td><td style="padding:6px 0;font-weight:600;">${waUrl ? `<a href="${safeWaUrl}" style="color:#18181B;">${safePhone}</a>` : safePhone}</td></tr>
      <tr><td style="padding:6px 0;color:#71717A;">Booking Date</td><td style="padding:6px 0;font-weight:600;">${safeDate}</td></tr>
      <tr><td style="padding:6px 0;color:#71717A;">Guests</td><td style="padding:6px 0;">${booking.adults} Adults, ${booking.children} Children</td></tr>
      <tr><td style="padding:6px 0;color:#71717A;">Language</td><td style="padding:6px 0;">${safeLanguage}</td></tr>
    </table><div style="background:#FAFAFA;border:1px solid #E4E4E7;border-radius:6px;padding:12px 16px;margin-bottom:20px;"><strong>Total Amount</strong><span style="float:right;font-size:18px;">${booking.pricing.totalMad} MAD</span></div><div style="white-space:pre-wrap;background:#F8F8F8;padding:10px 14px;border-radius:4px;margin-bottom:20px;">${safeNotes}</div>${waAction}</div>
  </div></body></html>`;
}

function getSupabaseClient() {
  const serviceRoleKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!serviceRoleKey) throw new Error('SUPABASE_SERVICE_ROLE_KEY is not configured');
  return createClient(SUPABASE_URL, serviceRoleKey, {
    auth: { persistSession: false, autoRefreshToken: false }
  });
}

export function buildBookingRecord(booking) {
  return {
    name: booking.name,
    email: booking.email || null,
    phone_number: booking.phone,
    date: booking.date,
    package_title: booking.product.title,
    notes: booking.notes || null,
    guests: booking.pricing.totalGuests,
    adults: booking.adults,
    children: booking.children,
    total_price: booking.pricing.totalMad,
    status: 'pending',
    payment_status: 'unpaid'
  };
}

async function insertBooking(booking) {
  const supabase = getSupabaseClient();
  const { data, error } = await supabase
    .from('bookings')
    .insert(buildBookingRecord(booking))
    .select('id')
    .single();
  if (error) throw error;
  return data;
}

async function sendNotification(booking, bookingId) {
  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) return { success: false, reason: 'not_configured' };

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 8_000);
  try {
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      signal: controller.signal,
      headers: { Authorization: `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: 'Marragafay Bookings <onboarding@resend.dev>',
        to: [process.env.NOTIFICATION_EMAIL || 'marragafay@gmail.com'],
        ...(booking.email ? { reply_to: booking.email } : {}),
        subject: `BOOKING: ${booking.product.title} - ${booking.name} (${booking.pricing.totalMad} MAD)`,
        html: buildEmailHtml(booking),
        headers: { 'X-Marragafay-Booking-Id': String(bookingId || '') }
      })
    });
    return { success: response.ok, reason: response.ok ? undefined : 'provider_error' };
  } catch {
    return { success: false, reason: 'provider_error' };
  } finally {
    clearTimeout(timeout);
  }
}

export default async function handleBooking(req, res) {
  setCorsHeaders(req, res);

  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).json({ booking_success: false, error: 'Method Not Allowed' });

  try {
    const booking = normalizeBooking(parseJsonBody(req));
    const saved = await insertBooking(booking);
    const notification = await sendNotification(booking, saved?.id);

    return res.status(200).json({
      booking_success: true,
      notification_success: notification.success,
      booking_id: saved?.id ?? null,
      product_id: booking.product.id,
      product_title: booking.product.title,
      trusted_total_mad: booking.pricing.totalMad
    });
  } catch (error) {
    if (error instanceof ValidationError) {
      return res.status(400).json({ booking_success: false, error: error.message });
    }
    console.error('Booking endpoint failure:', error?.code || error?.name || 'internal_error');
    return res.status(500).json({ booking_success: false, error: 'Unable to process booking' });
  }
}
