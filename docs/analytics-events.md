# Marragafay analytics events

Marragafay uses one privacy-safe browser event contract. Events are sent to the existing PostHog integration and the existing GTM/GA `dataLayer` when available. Analytics is best-effort and never blocks rendering, booking, or WhatsApp navigation.

## Events

| Event | Trigger | Required properties | Optional properties |
| --- | --- | --- | --- |
| `product_view` | A canonical product is present on a page | `product_id` | attribution fields |
| `pack_cta_click` | A commercial pack/booking CTA is clicked | `cta_location` | `product_id` |
| `whatsapp_click` | A WhatsApp link is activated | `cta_location` | `product_id`, `inquiry_id` |
| `booking_open` | A visible booking form is available | `page_path` | `product_id` |
| `booking_start` | A visitor meaningfully edits the booking form | `page_path` | `product_id` |
| `booking_submit` | Client validation passes and the request is sent | `product_id`, `guest_count` | `locale` |
| `booking_success` | The server returns `booking_success: true` | `product_id`, trusted totals, `pricing_source` | `guest_count`, `inquiry_id` |
| `booking_failure` | A booking request fails | `error_stage`, `safe_error_code` | `product_id` |

## Dimensions and attribution

Every event carries `timestamp`, `session_id`, `locale`, `page_path`, `source_category`, and safe campaign dimensions when present: `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`, `gclid`, `fbclid`, and `referrer_category`. Existing first-touch attribution persists in browser storage; a later campaign updates last-touch only. `inquiry_id` is reused when already associated with the action.

Canonical product IDs are `standard`, `private`, `private-plus`, and `buggy`. Localized display names must not be used as identifiers.

## Privacy

Analytics must never contain customer name, email, phone, pickup/address, notes, raw form content, credentials, secrets, or authorization headers. Booking success totals always come from the trusted server response, never from DOM or client price calculations.

## Funnel definitions

- Pack view rate = product views ÷ sessions
- CTA rate = pack CTA clicks ÷ product views
- Booking start rate = booking starts ÷ booking opens
- Booking completion rate = booking successes ÷ booking submits
- WhatsApp intent rate = WhatsApp clicks ÷ product views
- Visitor → booking rate = booking successes ÷ sessions
