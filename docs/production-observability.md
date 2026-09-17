# Marragafay production observability

## Booking logs

`/api/booking` writes safe structured Vercel runtime logs. Each request has a `request_id` from `x-request-id`, Vercel's request id, or a generated UUID. Logs include only route state: stage, canonical product id, locale, guest count, pricing source, HTTP status, safe error code, and duration.

Stages are `request_parsing`, `product_resolution_and_pricing`, `supabase_booking_insert`, `notification_email`, and `response_serialization`. A failure log includes `request_id`, stage, status, and a bounded safe error message. Customer identity, notes, pickup details, secrets, and credential headers are never logged.

## Pricing fallback

When live Supabase pricing cannot be used, the server emits a `pricing_fallback` warning with the canonical product id, request id, and a reason category (`timeout`, `supabase_unavailable`, or `invalid_supabase_product`). A normal production booking should return `pricing_source: "supabase"`.

## Safe debugging workflow

1. Find the request timestamp or `request_id` in Vercel Production Logs.
2. Identify the first failed stage and safe error code.
3. Compare the response status with the stage: validation is 400; server/database failures are 500.
4. Confirm `pricing_source` and trusted totals in the response; never use client-submitted prices as evidence.
5. If the insert succeeded but notification failed, treat the booking row as authoritative and investigate notification delivery separately.

There is intentionally no public health endpoint: it would add a public surface without improving the existing Vercel logs and safe booking response diagnostics.
