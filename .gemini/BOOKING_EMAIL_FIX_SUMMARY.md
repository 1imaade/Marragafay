# Booking Email Data Extraction Fix - Summary

## 🎯 Overview
Fixed the `booking-manager.js` to correctly extract and send phone number, total price, and guest information to the email API, resolving the "undefined" values issue.

---

## ✅ Changes Made

### 1. 📱 Phone Number Extraction (js/booking-manager.js)
**Problem:** FormData.get('phone') was returning empty/undefined.

**Solution:**
- Added support for `intl-tel-input` plugin detection
- Checks `window.intlTelInputGlobals.getInstance()` and calls `.getNumber()` for full international format
- Falls back to direct DOM query (`document.getElementById('phone')`)
- Final fallback to FormData as last resort

**Code Location:** Lines 106-130

```javascript
// First, try to get from intl-tel-input plugin if it exists
const phoneInput = document.getElementById('phone') || document.querySelector('input[name="phone"]');
if (phoneInput && window.intlTelInputGlobals) {
    const iti = window.intlTelInputGlobals.getInstance(phoneInput);
    if (iti) {
        phoneNumber = iti.getNumber(); // Gets full international format
    }
}
// Fallback: Get directly from input value or FormData
if (!phoneNumber) {
    phoneNumber = phoneInput?.value || formData.get('phone') || '';
}
```

---

### 2. 💰 Total Price Extraction (js/booking-manager.js)
**Problem:** Price was calculated but not extracting from dynamically updated DOM elements.

**Solution:**
- Searches for displayed price in DOM with multiple selectors:
  - `document.getElementById('total-price')`
  - `document.querySelector('.total-price')`
  - `document.querySelector('[data-total-price]')`
- Extracts numeric value from text like "549 DH" or "1200.00 DH"
- Falls back to calculated price if DOM element not found
- Added console logging for debugging

**Code Location:** Lines 227-249

```javascript
const totalPriceElement = document.getElementById('total-price') || 
                          document.querySelector('.total-price') ||
                          document.querySelector('[data-total-price]');

if (totalPriceElement) {
    const priceText = totalPriceElement.innerText || totalPriceElement.textContent || '';
    const numericMatch = priceText.match(/[\d,]+\.?\d*/);
    if (numericMatch) {
        const extractedPrice = parseFloat(numericMatch[0].replace(/,/g, ''));
        if (!isNaN(extractedPrice) && extractedPrice > 0) {
            total = extractedPrice;
        }
    }
}
```

---

### 3. 📝 Notes & Guests Separation (js/booking-manager.js)
**Problem:** Guest counts were being appended to the notes field, causing confusion.

**Solution:**
- **Guests:** Created separate formatted string: `"2 Adults, 1 Children"`
- **Notes:** Extracted directly from textarea with multiple fallback selectors:
  - `document.getElementById('notes')`
  - `document.querySelector('textarea[name="notes"]')`
  - `document.querySelector('textarea[name="message"]')`
- Defaults to "No special requests" if empty
- Removed the guest count append logic from notes

**Code Location:** Lines 132-148

```javascript
// Format guests as a readable string for email
const guestsFormatted = `${adults} Adults, ${children} Children`;

// Extract notes properly
const notesTextarea = document.getElementById('notes') || 
                      document.querySelector('textarea[name="notes"]') || 
                      document.querySelector('textarea[name="message"]');
const notesValue = notesTextarea?.value || formData.get('notes') || formData.get('message') || '';
const notes = notesValue.trim() || 'No special requests';
```

---

### 4. 🐛 Debugging Console Logs (js/booking-manager.js)
**Added comprehensive logging:**
- Phone extraction source
- Formatted guests string
- Notes value
- Total price extraction (DOM vs calculated)
- **Complete payload before sending to API** (Line 251-263)

**Code Location:** Lines 251-263

```javascript
console.log('📦 Payload to be sent:', {
    name: bookingData.name,
    email: bookingData.email,
    phone_number: bookingData.phone_number,
    date: bookingData.date,
    guests: guestsFormatted,
    adults: bookingData.adults,
    children: bookingData.children,
    package_title: bookingData.package_title,
    total_price: bookingData.total_price,
    notes: bookingData.notes
});
```

---

### 5. 📧 Backend Email Template Updates

#### a) Updated TypeScript Interface (components/emails/BookingNotificationEmail.tsx)
Added `adults?` and `children?` to `BookingEmailProps` interface (Lines 14-15)

#### b) Updated Email Generation (app/actions/send-email.ts)
Now passes `adults` and `children` to email template (Lines 129-130)

#### c) Updated Email Display (components/emails/BookingNotificationEmail.tsx)
- Email now shows: **"2 Adults, 1 Children"** instead of just **"3 Guests"**
- Smart fallback: If adults/children not provided, shows total guest count
- Code Location: Lines 29-33, 81

```typescript
const guestsDisplay = (adults !== undefined && children !== undefined) 
    ? `${adults} Adults, ${children} Children` 
    : `${numberOfGuests} Guest${numberOfGuests > 1 ? 's' : ''}`;
```

---

## 🧪 Testing Instructions

1. **Open Browser Console** when submitting a booking
2. Look for these debug logs:
   - `📱 Phone from intl-tel-input:` or `📱 Phone from direct input:`
   - `👥 Guests formatted:`
   - `📝 Notes:`
   - `💰 Raw price text from DOM:` or `💰 Total Price calculated:`
   - `📦 Payload to be sent:`

3. **Check the payload log** - all fields should now have values:
   - `phone_number` should show full phone (not undefined)
   - `total_price` should show numeric value (not undefined)
   - `notes` should show actual notes or "No special requests" (not guest counts)
   - `adults` and `children` should show proper numbers

4. **Check the email** - should display:
   - Phone number in the 📞 row
   - Total price in the 💰 row (in DH currency)
   - Guests as "X Adults, Y Children" in the 👥 row
   - Notes in the 📝 row (separate from guests)

---

## 📌 What to Check in Your HTML

Make sure your booking form has these elements:

1. **Phone Input:**
   ```html
   <input type="tel" id="phone" name="phone" />
   ```

2. **Total Price Display:**
   ```html
   <h3 id="total-price">549 DH</h3>
   <!-- OR -->
   <span class="total-price">549 DH</span>
   <!-- OR -->
   <div data-total-price>549 DH</div>
   ```

3. **Notes Textarea:**
   ```html
   <textarea id="notes" name="notes"></textarea>
   <!-- OR -->
   <textarea name="message"></textarea>
   ```

---

## 🚀 Expected Result

**Email will now show:**
- ✅ Phone: `+212 612345678` (instead of `undefined`)
- ✅ Total Price: `549 DH` (instead of `undefined`)
- ✅ Guests: `2 Adults, 1 Children` (instead of showing this in notes)
- ✅ Notes: Actual customer notes or "No special requests"
