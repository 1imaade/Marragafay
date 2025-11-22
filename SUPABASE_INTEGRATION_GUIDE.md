# Supabase Booking Integration Guide

## Overview
This guide will help you integrate Supabase with your Marragafay booking system.

## Prerequisites
You mentioned you've already created the Supabase tables:
- `bookings`
- `packages`
- `customers`

## Step 1: Configure Environment Variables

Update your `.env.local` file with your Supabase credentials:

```env
NEXT_PUBLIC_SUPABASE_URL=your-supabase-project-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-supabase-anon-key
```

## Step 2: Standardize Frontend Forms

### Template Form Structure (Source of Truth)

Add this form structure to ALL package and activity pages. The only difference between pages should be the `value` in the hidden `package` input field.

```html
<form id="bookingForm" class="booking-form">
  <!-- Hidden field to identify the package/activity -->
  <input type="hidden" name="package" value="Basic Pack">
  
  <div class="form-group">
    <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Full Name</label>
    <input type="text" name="name" class="booking-input" placeholder="John Doe" required>
  </div>

  <div class="form-group">
    <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Email Address</label>
    <input type="email" name="email" class="booking-input" placeholder="john@example.com" required>
  </div>

  <div class="form-group">
    <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Phone Number</label>
    <div style="display: grid; grid-template-columns: 120px 1fr; gap: 10px;">
      <select name="countryCode" class="booking-input" required>
        <option value="+212" selected>🇲🇦 +212</option>
        <option value="+1">🇺🇸 +1</option>
        <option value="+44">🇬🇧 +44</option>
        <option value="+33">🇫🇷 +33</option>
        <option value="+34">🇪🇸 +34</option>
        <option value="+49">🇩🇪 +49</option>
        <option value="+39">🇮🇹 +39</option>
        <option value="+31">🇳🇱 +31</option>
        <option value="+32">🇧🇪 +32</option>
        <option value="+41">🇨🇭 +41</option>
        <option value="+971">🇦🇪 +971</option>
        <option value="+966">🇸🇦 +966</option>
      </select>
      <input type="tel" name="phone" class="booking-input" placeholder="612345678" required>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
    <div class="form-group">
      <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Date</label>
      <input type="date" name="date" class="booking-input" required>
    </div>
    <div class="form-group">
      <label style="font-size:0.85rem; font-weight:600; margin-bottom:5px; display:block;">Guests</label>
      <select name="guests" class="booking-input" required>
        <option value="1">1 Person</option>
        <option value="2" selected>2 People</option>
        <option value="3">3 People</option>
        <option value="4">4 People</option>
        <option value="5+">5+ Group</option>
      </select>
    </div>
  </div>

  <button type="submit" class="btn-reserve">
    Reserve Now
  </button>
</form>
```

### Package-Specific Values

For each page, update the hidden `package` field value:

- **packages/basic.html**: `value="Basic Pack"`
- **packages/comfort.html**: `value="Comfort Pack"`  
- **packages/premium.html**: `value="Premium Pack"`
- **packages/luxe.html**: `value="Luxe Pack"`
- **packages/vip.html**: `value="VIP Pack"`
- **packages/family.html**: `value="Family Pack"`

For activity pages:
- **activities/quad-biking.html**: `value="Quad Biking"`
- **activities/camel-ride.html**: `value="Camel Ride"`
- **activities/bike-tour.html**: `value="Bike Tour"`
- Etc...

## Step 3: Add Supabase Client

Create a file `js/supabase-client.js`:

```javascript
// Initialize Supabase client
const SUPABASE_URL = 'YOUR_SUPABASE_URL';
const SUPABASE_ANON_KEY = 'YOUR_SUPABASE_ANON_KEY';

const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
```

## Step 4: Add Supabase JS Library

Add this script tag to the `<head>` of all pages with booking forms:

```html
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="../js/supabase-client.js"></script>
```

## Step 5: Add Form Submission Handler

Add this JavaScript to handle form submissions (place before closing `</body>` tag):

```javascript
<script>
document.getElementById('bookingForm').addEventListener('submit', async function(e) {
  e.preventDefault();
  
  // Get form data
  const formData = new FormData(this);
  const countryCode = formData.get('countryCode');
  const phone = formData.get('phone');
  const fullPhone = countryCode + phone;
  
  // Prepare booking data
  const bookingData = {
    customer_name: formData.get('name'),
    customer_email: formData.get('email'),
    phone: fullPhone,
    package_title: formData.get('package'),
    booking_date: formData.get('date'),
    guests_count: parseInt(formData.get('guests')) || 2,
    status: 'pending',
    created_at: new Date().toISOString()
  };
  
  // Show loading state
  const submitBtn = this.querySelector('button[type="submit"]');
  const originalText = submitBtn.textContent;
  submitBtn.textContent = 'Processing...';
  submitBtn.disabled = true;
  
  try {
    // Insert into Supabase
    const { data, error } = await supabase
      .from('bookings')
      .insert([bookingData])
      .select();
    
    if (error) throw error;
    
    // Success message
    alert(`✅ Thank you for your booking!\\n\\nPackage: ${bookingData.package_title}\\nDate: ${bookingData.booking_date}\\nGuests: ${bookingData.guests_count}\\n\\nWe will contact you at ${bookingData.phone} to confirm your reservation.`);
    
    // Reset form
    this.reset();
    
  } catch (error) {
    console.error('Booking error:', error);
    alert('❌ Sorry, there was an error processing your booking. Please try again or contact us directly via WhatsApp.');
  } finally {
    // Reset button
    submitBtn.textContent = originalText;
    submitBtn.disabled = false;
  }
});
</script>
```

## Step 6: Database Schema Reference

Your Supabase `bookings` table should have these columns:

| Column Name      | Data Type    | Description                      |
|-----------------|--------------|----------------------------------|
| id              | uuid (PK)    | Auto-generated unique ID         |
| customer_name   | text         | Customer's full name             |
| customer_email  | text         | Customer's email                 |
| phone           | text         | Full phone with country code     |
| package_title   | text         | Name of package/activity         |
| booking_date    | date         | Requested booking date           |
| guests_count    | integer      | Number of guests                 |
| status          | text         | pending/confirmed/cancelled      |
| created_at      | timestamp    | When booking was created         |

## Step 7: Enable Row Level Security  (RLS)

In your Supabase dashboard, enable RLS for the `bookings` table and add this policy:

**Policy Name**: "Enable insert for all users"
**Policy Type**: INSERT
**Target Roles**: `anon`
**Policy Definition**:
```sql
true
```

This allows anonymous users to insert bookings (they can't read or modify existing ones).

## Step 8: Testing

1. Open any package or activity page
2. Fill out the booking form
3. Submit the form
4. Check your Supabase dashboard → Table Editor → bookings table
5. You should see the new booking entry

## Alternative: Backend API Approach

If you want to use a backend API instead of direct Supabase calls:

### Create API Route

Create file: `Admine_Dashboard/app/api/website/bookings/route.ts`

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY! // Use service role key on server
);

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    
    // Map frontend fields to database fields
    const bookingData = {
      customer_name: body.name,
      customer_email: body.email,
      phone: body.countryCode + body.phone,
      package_title: body.package,
      booking_date: body.date,
      guests_count: parseInt(body.guests) || 2,
      status: 'pending'
    };
    
    // Insert into Supabase
    const { data, error } = await supabase
      .from('bookings')
      .insert([bookingData])
      .select();
    
    if (error) {
      console.error('Supabase error:', error);
      return NextResponse.json(
        { success: false, error: error.message },
        { status: 400 }
      );
    }
    
    return NextResponse.json({ 
      success: true, 
      booking: data[0] 
    });
    
  } catch (error) {
    console.error('API error:', error);
    return NextResponse.json(
      { success: false, error: 'Internal server error' },
      { status: 500 }
    );
  }
}
```

### Update Frontend to Use API

```javascript
document.getElementById('bookingForm').addEventListener('submit', async function(e) {
  e.preventDefault();
  
  const formData = new FormData(this);
  const bookingData = {
    name: formData.get('name'),
    email: formData.get('email'),
    countryCode: formData.get('countryCode'),
    phone: formData.get('phone'),
    package: formData.get('package'),
    date: formData.get('date'),
    guests: formData.get('guests')
  };
  
  const submitBtn = this.querySelector('button[type="submit"]');
  const originalText = submitBtn.textContent;
  submitBtn.textContent = 'Processing...';
  submitBtn.disabled = true;
  
  try {
    const response = await fetch('/api/website/bookings', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(bookingData),
    });
    
    const result = await response.json();
    
    if (result.success) {
      alert('✅ Booking confirmed! We will contact you shortly.');
      this.reset();
    } else {
      throw new Error(result.error);
    }
    
  } catch (error) {
    console.error('Error:', error);
    alert('❌ Booking failed. Please try again or contact us via WhatsApp.');
  } finally {
    submitBtn.textContent = originalText;
    submitBtn.disabled = false;
  }
});
```

## Summary Checklist

- [ ] Add Supabase credentials to `.env.local`
- [ ] Add hidden `package` field to all booking forms
- [ ] Update `package` field value for each page
- [ ] Add Supabase JS library to pages
- [ ] Add form submission handler JavaScript
- [ ] Test booking form on one page
- [ ] Roll out to all pages
- [ ] Enable RLS policies in Supabase
- [ ] Test end-to-end booking flow

## Notes

- The direct Supabase approach is simpler and doesn't require a backend
- The API approach is more secure and gives you more control
- Make sure to replace placeholder Supabase credentials with your actual ones
- Test thoroughly before going live
