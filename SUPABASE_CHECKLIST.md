# Supabase Integration - Implementation Checklist

## ✅ Completed
- [x] Created Supabase client configuration (`js/supabase-client.js`)
- [x] Created universal booking form handler (`js/booking-handler.js`)
- [x] Created backend API route (`Admine_Dashboard/app/api/website/bookings/route.ts`)
- [x] Created environment template (`.env.local`)
- [x] Created comprehensive integration guide (`SUPABASE_INTEGRATION_GUIDE.md`)

## 🔧 Configuration Required

### 1. Supabase Credentials Setup
- [ ] Go to your Supabase dashboard: https://app.supabase.com
- [ ] Navigate to: Settings > API
- [ ] Copy your Project URL
- [ ] Copy your `anon` `public` key
- [ ] Copy your `service_role` key (keep this secret!)
- [ ] Update `.env.local` with these values
- [ ] Update `js/supabase-client.js` with Project URL and Anon Key

### 2. Database Schema Verification
- [ ] Verify `bookings` table exists in Supabase
- [ ] Confirm table has these columns:
  - [ ] `id` (uuid, primary key, auto-generated)
  - [ ] `customer_name` (text)
  - [ ] `customer_email` (text)
  - [ ] `phone` (text)
  - [ ] `package_title` (text)
  - [ ] `booking_date` (date)
  - [ ] `guests_count` (integer)
  - [ ] `status` (text, default: 'pending')
  - [ ] `created_at` (timestamp, default: now())

### 3. Row Level Security (RLS) Setup
- [ ] Enable RLS on `bookings` table
- [ ] Create INSERT policy for `anon` role:
  ```sql
  CREATE POLICY "Enable insert for anon users" ON bookings
  FOR INSERT TO anon
  WITH CHECK (true);
  ```

## 📝 Frontend Implementation

### Package Pages (`packages/*.html`)
Update each package page with the standardized form:

- [ ] **packages/basic.html** ✓ (Source of Truth)
  - [ ] Add Supabase scripts to `<head>`
  - [ ] Ensure form has `id="bookingForm"`
  - [ ] Add hidden input: `<input type="hidden" name="package" value="Basic Pack">`

- [ ] **packages/comfort.html**
  - [ ] Add Supabase scripts to `<head>`
  - [ ] Copy standardized form from basic.html
  - [ ] Update hidden input value to: `"Comfort Pack"`

- [ ] **packages/premium.html**
  - [ ] Add Supabase scripts to `<head>`
  - [ ] Copy standardized form from basic.html
  - [ ] Update hidden input value to: `"Premium Pack"`

- [ ] **packages/luxe.html**
  - [ ] Add Supabase scripts to `<head>`
  - [ ] Copy standardized form from basic.html
  - [ ] Update hidden input value to: `"Luxe Pack"`

- [ ] **packages/vip.html** (if exists)
  - [ ] Add Supabase scripts to `<head>`
  - [ ] Copy standardized form from basic.html
  - [ ] Update hidden input value to: `"VIP Pack"`

- [ ] **packages/family.html** (if exists)
  - [ ] Add Supabase scripts to `<head>`
  - [ ] Copy standardized form from basic.html
  - [ ] Update hidden input value to: `"Family Pack"`

### Activity Pages (`activities/*.html`)

- [ ] **activities/quad-biking.html**
  - [ ] Add Supabase scripts to `<head>`
  - [ ] Add/update booking form
  - [ ] Set hidden input value to: `"Quad Biking"`

- [ ] **activities/camel-ride.html**
  - [ ] Add Supabase scripts to `<head>`
  - [ ] Add/update booking form
  - [ ] Set hidden input value to: `"Camel Ride"`

- [ ] **activities/bike-tour.html**
  - [ ] Add Supabase scripts to `<head>`
  - [ ] Add/update booking form
  - [ ] Set hidden input value to: `"Bike Tour"`

- [ ] **activities/[other-activities].html**
  - [ ] Repeat for all activity pages
  - [ ] Set appropriate package names

### Scripts to Add to Each Page

Add these lines to the `<head>` section of every page with a booking form:

```html
<!-- Supabase Integration -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="../js/supabase-client.js"></script>
<script src="../js/booking-handler.js"></script>
```

## 🧪 Testing

### Local Testing
- [ ] Test booking form on `packages/basic.html`
- [ ] Fill out form with test data
- [ ] Submit and check for success message
- [ ] Verify booking appears in Supabase dashboard
- [ ] Test with invalid data (empty fields)
- [ ] Test phone number with different country codes

### Cross-Page Testing
- [ ] Test one booking form per package type
- [ ] Verify correct package name is saved
- [ ] Test on different browsers (Chrome, Firefox, Safari)
- [ ] Test on mobile devices

### Database Verification
- [ ] Open Supabase dashboard > Table Editor > bookings
- [ ] Confirm test bookings appear
- [ ] Verify all fields are populated correctly
- [ ] Check phone numbers include country codes
- [ ] Confirm dates are in correct format

## 🚀 Deployment

### Before Going Live
- [ ] Remove any test bookings from database
- [ ] Verify all Supabase credentials are correct
- [ ] Test on production environment
- [ ] Ensure RLS policies are properly configured
- [ ] Set up email notifications (optional)
- [ ] Configure backup/export for bookings

### Post-Launch
- [ ] Monitor Supabase dashboard for new bookings
- [ ] Set up alerts for new bookings (optional)
- [ ] Document the booking management workflow
- [ ] Train staff on viewing/managing bookings

## 📊 Monitoring & Maintenance

- [ ] Check Supabase dashboard regularly for new bookings
- [ ] Monitor API usage and quotas
- [ ] Review booking data for insights
- [ ] Update form fields if needed
- [ ] Regularly export booking data as backup

## 🆘 Troubleshooting

If bookings aren't working:

1. **Check Browser Console** for JavaScript errors
2. **Verify Supabase Credentials** in both `.env.local` and `js/supabase-client.js`
3. **Check RLS Policies** - ensure INSERT is allowed for `anon` role
4. **Verify Table Schema** matches the expected columns
5. **Test Network Requests** in browser DevTools > Network tab
6. **Check Supabase Logs** in dashboard for error details

## 📚 Resources

- **Integration Guide**: `SUPABASE_INTEGRATION_GUIDE.md`
- **Supabase Docs**: https://supabase.com/docs
- **JavaScript Client Docs**: https://supabase.com/docs/reference/javascript
- **RLS Guide**: https://supabase.com/docs/guides/auth/row-level-security

---

**Last Updated**: 2025-11-22
**Status**: Ready for Implementation
**Priority**: High
