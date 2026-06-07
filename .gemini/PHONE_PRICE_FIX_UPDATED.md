# 🔧 Booking Email Fix - Phone & Price Extraction (UPDATED)

## ⚠️ Issue
The email notification was receiving `undefined` for:
- **Phone Number** - Because it's split into two separate fields (Country Code select + Phone input)
- **Total Price** - Because it's displayed as a text element (e.g., `<h2>549 DH</h2>`), NOT a form input

---

## ✅ Solution Applied

### 1. 📱 PHONE NUMBER - Split Fields Support

**Problem:** Phone consists of:
- A `<select>` dropdown for country code (e.g., `+212`)
- An `<input>` field for the phone number

**Solution - 3 Strategies:**

#### Strategy 1: **Split Fields** (Primary) ✅
Searches for BOTH elements and combines them:

```javascript
// Find Country Code Select
const countryCodeElement = document.getElementById('country-code') || 
                           document.querySelector('select[name="country_code"]') ||
                           document.querySelector('select[name="countryCode"]') ||
                           document.querySelector('.country-code-select');

// Find Phone Number Input
const phoneInputElement = document.getElementById('phone') || 
                          document.getElementById('phone-number') ||
                          document.querySelector('input[name="phone"]') ||
                          document.querySelector('input[name="phone_number"]') ||
                          document.querySelector('.phone-input');

// Combine them
if (countryCodeElement && phoneInputElement) {
    const countryCode = countryCodeElement.value || '';
    const phoneNum = phoneInputElement.value || '';
    phoneNumber = `${countryCode} ${phoneNum}`.trim();
    // Result: "+212 612345678"
}
```

#### Strategy 2: **intl-tel-input Plugin** (Fallback)
If split fields not found, tries the intl-tel-input plugin.

#### Strategy 3: **Single Input or FormData** (Final Fallback)
Falls back to a single phone input or FormData.

**Result:** Phone will be combined as `"+212 612345678"` instead of `undefined`

---

### 2. 💰 TOTAL PRICE - DOM Text Extraction

**Problem:** Price is displayed as text (e.g., `<h2>549 DH</h2>`), not a form input, so `formData.get('price')` returns `undefined`.

**Solution - Comprehensive DOM Search:**

The code now searches for the price element using **8 different selectors**:

```javascript
const totalPriceElement = document.getElementById('total-price') ||      // By ID
                          document.getElementById('totalPrice') ||
                          document.querySelector('.total-price') ||       // By class
                          document.querySelector('.price-display') ||
                          document.querySelector('[data-total-price]') || // By data attribute
                          document.querySelector('h2.price') ||           // By tag + class
                          document.querySelector('h3.price') ||
                          document.querySelector('span.price');

if (totalPriceElement) {
    // Extract text: "549 DH" or "1,200.00 DH"
    const priceText = totalPriceElement.innerText || totalPriceElement.textContent;
    
    // Parse numeric value
    const numericMatch = priceText.match(/[\d,]+\.?\d*/);  // Matches: 549 or 1,200.00
    const extractedPrice = parseFloat(numericMatch[0].replace(/,/g, ''));
    
    if (!isNaN(extractedPrice) && extractedPrice > 0) {
        total = extractedPrice;  // ✅ Successfully extracted!
    }
}
```

**What it extracts:**
- `"549 DH"` → `549`
- `"1,200.00 DH"` → `1200`
- `"100 DH"` → `100`

**Result:** Price will be `549` instead of `undefined`

---

### 3. 🔍 ENHANCED DEBUGGING

Added **prominent console logging** to verify captured values:

```javascript
console.log('\n========================================');
console.log('📦 FINAL PAYLOAD BEFORE SENDING TO API');
console.log('========================================');
console.log('🔍 Captured Phone:', phoneNumber);     // Shows: "+212 612345678"
console.log('🔍 Captured Price:', total);           // Shows: 549
console.log('\n📧 Complete Email Payload:');
console.log({
    name: bookingData.name,
    email: bookingData.email,
    phone_number: phoneNumber,    // ← The actual variable being sent
    total_price: total,            // ← The actual variable being sent
    // ... rest of data
});
console.log('========================================\n');
```

**What you'll see in console:**
```
========================================
📦 FINAL PAYLOAD BEFORE SENDING TO API
========================================
🔍 Captured Phone: +212 612345678
🔍 Captured Price: 549

📧 Complete Email Payload:
{
  name: "John Doe",
  email: "john@example.com",
  phone_number: "+212 612345678",  ✅ NOT undefined
  total_price: 549,                 ✅ NOT undefined
  ...
}
========================================
```

---

## 🧪 How to Test

1. **Open your booking form** in the browser
2. **Open Developer Console** (F12)
3. **Fill out and submit** the booking form
4. **Check the console output:**

Look for these specific logs:

### ✅ Phone Number Logs:
```
📱 Phone from split fields (Country + Number): +212 612345678
```
OR (if using intl-tel-input):
```
📱 Phone from intl-tel-input: +212612345678
```
OR (fallback):
```
📱 Phone from single input/FormData: 612345678
```

### ✅ Price Logs:
```
💰 Found price element! Raw text: 549 DH
💰 ✅ Total Price extracted from DOM: 549 DH
```
OR (if no DOM element):
```
💰 No price element found in DOM, using calculated value: 549
```

### ✅ Final Payload Log:
```
🔍 Captured Phone: +212 612345678    ← Should NOT be undefined
🔍 Captured Price: 549                ← Should NOT be undefined
```

---

## 📌 HTML Requirements Checklist

### For Phone to Work:
Your HTML must have **either**:

**Option 1: Split Fields** (Recommended)
```html
<!-- Country Code Select -->
<select id="country-code" name="country_code">
    <option value="+212">+212 (Morocco)</option>
    <option value="+1">+1 (USA)</option>
</select>

<!-- Phone Number Input -->
<input type="tel" id="phone" name="phone" placeholder="612345678" />
```

**Option 2: Single Input with intl-tel-input**
```html
<input type="tel" id="phone" name="phone" />
<!-- intl-tel-input plugin initialized on this element -->
```

### For Price to Work:
Your HTML must display the price using **one of these**:

```html
<!-- Option 1: ID = total-price -->
<h2 id="total-price">549 DH</h2>

<!-- Option 2: Class = total-price -->
<h3 class="total-price">549 DH</h3>

<!-- Option 3: Data attribute -->
<div data-total-price>549 DH</div>

<!-- Option 4: Tag with .price class -->
<span class="price">549 DH</span>
```

---

## 🎯 Expected Email Result

**Before Fix:**
```
📞 Phone: undefined
💰 Total Price: undefined
```

**After Fix:**
```
📞 Phone: +212 612345678
💰 Total Price: 549 DH
👥 Guests: 2 Adults, 1 Children
📝 Notes: Vegetarian meal requested
```

---

## ⚙️ Code Changes Summary

### File: `js/booking-manager.js`

**Lines 103-152:** Phone extraction with split fields support  
**Lines 248-282:** Price extraction from DOM text elements  
**Lines 286-308:** Enhanced debugging console output  

---

## 🚨 Troubleshooting

### If Phone is still `undefined`:

1. **Check console for this warning:**
   ```
   ⚠️ Could not extract phone number from any source
   ```

2. **Verify your HTML:**
   - Inspect the country code select and phone input elements
   - Check their `id`, `name`, or `class` attributes
   - Make sure they match one of the selectors in the code

3. **Add custom selectors if needed:**
   ```javascript
   const countryCodeElement = document.getElementById('YOUR_SELECT_ID') || ...
   const phoneInputElement = document.getElementById('YOUR_INPUT_ID') || ...
   ```

### If Price is still `undefined`:

1. **Check console for this log:**
   ```
   💰 No price element found in DOM, using calculated value: 549
   ```

2. **Verify your HTML:**
   - Use browser DevTools to find the element showing the price
   - Note its `id`, `class`, or tag name
   - Make sure it matches one of the 8 selectors

3. **Add your custom selector if needed:**
   ```javascript
   const totalPriceElement = document.getElementById('YOUR_PRICE_ID') || ...
   ```

---

## 📝 Notes

- The phone number extraction prioritizes split fields (country code + number) as that's the user's current setup
- The price extraction tries DOM first, then falls back to calculation
- All extraction strategies include comprehensive console logging for debugging
- The debugging output is now **highly visible** with separators and emoji markers

---

**Status:** ✅ Ready to test
**Next Steps:** Submit a test booking and check the browser console + email notification
