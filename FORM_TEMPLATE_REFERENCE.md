# Booking Form Template - Quick Reference

## 📋 Standard Form HTML

Copy this exact form structure to all package and activity pages:

```html
<form id="bookingForm" class="booking-form">
  <!-- IMPORTANT: Update the value below for each page -->
  <input type="hidden" name="package" value="PACKAGE_NAME_HERE">
  
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

## 🔧 Required Scripts for `<head>`

Add these 3 lines before `</head>`:

```html
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="../js/supabase-client.js"></script>
<script src="../js/booking-handler.js"></script>
```

## 📝 Package Name Values

### Packages (`packages/*.html`)
| File | Hidden Input Value |
|------|-------------------|
| `basic.html` | `value="Basic Pack"` |
| `comfort.html` | `value="Comfort Pack"` |
| `premium.html` | `value="Premium Pack"` |
| `luxe.html` | `value="Luxe Pack"` |
| `vip.html` | `value="VIP Pack"` |
| `family.html` | `value="Family Pack"` |

### Activities (`activities/*.html`)
| File | Hidden Input Value |
|------|-------------------|
| `quad-biking.html` | `value="Quad Biking"` |
| `camel-ride.html` | `value="Camel Ride"` |
| `bike-tour.html` | `value="Bike Tour"` |
| `hiking.html` | `value="Hiking"` |
| `hot-air-balloon.html` | `value="Hot Air Balloon"` |
| `[other].html` | `value="[Activity Name]"` |

## ⚠️ Critical Points

1. **Form ID must be**: `id="bookingForm"` (exact match, case-sensitive)
2. **Input names must match**: `name`, `email`, `countryCode`, `phone`, `package`, `date`, `guests`
3. **Hidden package field**: Update `value=""` for each page
4. **Scripts order matters**: Supabase library → client → handler

## ✅ Implementation Steps

For each page:
1. ✅ Open the HTML file
2. ✅ Add 3 script tags to `<head>`
3. ✅ Find/replace existing booking form with template above
4. ✅ Update hidden `package` input value
5. ✅ Save file
6. ✅ Test in browser

## 🧪 Quick Test

1. Open page in browser
2. Open browser console (F12)
3. Look for: `✅ Supabase client initialized`
4. Look for: `✅ Booking form handler initialized`
5. Fill form and submit
6. Check Supabase dashboard for new booking

## 🎯 Field Mapping

| Form Field | Database Column |
|------------|----------------|
| `name` | `customer_name` |
| `email` | `customer_email` |
| `countryCode + phone` | `phone` |
| `package` | `package_title` |
| `date` | `booking_date` |
| `guests` | `guests_count` |

The `booking-handler.js` does this mapping automatically!

---

**Need Help?** See `IMPLEMENTATION_SUMMARY.md` for full details.
