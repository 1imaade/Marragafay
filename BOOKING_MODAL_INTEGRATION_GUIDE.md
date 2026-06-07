# Booking Details Modal - Integration Guide

## Overview
A minimalist, 2-tone booking details modal has been created to display booking confirmations with a clean, first-class boarding pass aesthetic.

## Files Created

### 1. CSS Styles
**File:** `css/booking-details-modal.css`
- Pure white background with dark grey text
- Gold accents (`#C19B76`) for status badges and primary button
- 2-column grid layout for booking information
- Responsive design with mobile optimization
- Smooth animations and transitions

### 2. JavaScript Controller
**File:** `js/booking-details-modal.js`
- Creates modal HTML structure dynamically
- Opens modal with booking data: `openBookingDetailsModal(bookingData)`
- Closes modal: `closeBookingDetailsModal()`
- Print receipt functionality
- Keyboard (ESC) and backdrop click handlers

### 3. Updated Booking Manager
**File:** `js/booking-manager.js` (modified)
- Now displays the new modal instead of SweetAlert after successful booking
- Falls back to SweetAlert if modal script not loaded

## Integration Steps

### Step 1: Add CSS to HTML Pages
Add this line in the `<head>` section of your HTML files, **after** the existing CSS files:

```html
<!-- Booking Details Modal CSS -->
<link rel="stylesheet" href="css/booking-details-modal.css">
```

**Add to these files:**
- `index.html`
- `packs.html`
- `activities.html`
- Any other pages with booking forms

### Step 2: Add JavaScript Before Closing `</body>`
Add these lines **before** the closing `</body>` tag, ideally near other JS includes:

```html
<!-- Booking Details Modal JS -->
<script src="js/booking-details-modal.js"></script>
```

**Recommended placement:**
```html
<!-- Global Lightbox JS -->
<script src="js/global-lightbox.js"></script>

<!-- Booking Details Modal JS -->
<script src="js/booking-details-modal.js"></script>

<!-- Other scripts -->
</body>
```

## Usage

### Display Modal Programmatically
You can open the modal from anywhere in your JavaScript:

```javascript
// Example booking data
const bookingData = {
  id: 12345,
  name: "John Doe",
  email: "john@example.com",
  phone_number: "+212 600 123 456",
  date: "2026-02-15",
  guests: 4,
  package_title: "Luxury Desert Package",
  total_price: 1200,
  notes: "Vegetarian meals please",
  status: "confirmed" // or "pending"
};

// Open the modal
openBookingDetailsModal(bookingData);
```

### Close Modal
```javascript
closeBookingDetailsModal();
```

### Print Receipt
```javascript
printBookingReceipt();
```

## Booking Data Fields

The modal accepts the following fields in the `bookingData` object:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | Number | No | Booking ID (random generated if missing) |
| `name` / `guest_name` | String | Yes | Guest's full name |
| `email` | String | Yes | Guest's email address |
| `phone_number` / `phone` | String | No | Phone number |
| `date` / `booking_date` | String | Yes | Check-in date (YYYY-MM-DD) |
| `guests` / `total_guests` | Number | Yes | Number of guests |
| `package_title` | String | No | Package/activity name |
| `total_price` / `price` | Number | Yes | Total price in DH |
| `notes` | String | No | Additional notes |
| `status` | String | No | "confirmed" or "pending" (default: "pending") |

## Design Features

### ✅ 2-Tone Minimalist Style
- **Background:** Pure white (`#ffffff`)
- **Text:** Dark grey/black (`#111827`)
- **Accents:** Gold (`#C19B76`) for borders, badges, and buttons
- **Typography:** Clean sans-serif font stack

### ✅ Structured Layout
**Header:**
- Booking ID title (left)
- Status badge (pill shape with gold/green)
- Close button (minimalist X icon)

**Body:**
- 2-column grid on desktop
- Single column on mobile
- Labels in uppercase grey (`#6b7280`)
- Values in bold dark (`#111827`)
- Price highlighted in gold

**Footer:**
- [Close] ghost button
- [Print Receipt] gold-bordered button (right-aligned)

### ✅ Responsive Design
- Desktop: 600px max-width, 2-column grid
- Mobile: 95% width, single column, full-width buttons
- Smooth scrolling for long content
- Custom scrollbar styling

### ✅ Accessibility
- ESC key to close
- Click outside to close
- Keyboard navigation
- ARIA labels
- Focus management
- Body scroll lock when open

## Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- IE11+ (with minor degradation)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Example Implementation

See `index.html` (lines ~5595-5614) for script placement reference:

```html
<!DOCTYPE html>
<html>
<head>
  <!-- Other CSS -->
  <link rel="stylesheet" href="css/booking-details-modal.css">
</head>
<body>
  
  <!-- Your page content -->
  
  <!-- Scripts at bottom -->
  <script src="js/booking-manager.js"></script>
  <script src="js/booking-details-modal.js"></script>
</body>
</html>
```

## Testing Checklist

- [ ] Modal opens with complete booking data
- [ ] All fields display correctly
- [ ] Status badge shows correct color (confirmed=green, pending=gold)
- [ ] Close button works
- [ ] Click outside closes modal
- [ ] ESC key closes modal
- [ ] Print button triggers print dialog
- [ ] Mobile responsive layout works
- [ ] Scrolling works for long content
- [ ] Body scroll is locked when modal is open
- [ ] Body scroll is restored when modal closes

## Customization

### Change Colors
Edit `css/booking-details-modal.css`:

```css
.booking-detail-value.price {
  color: #C19B76; /* Change gold accent color */
}

.booking-modal-btn-primary {
  border: 2px solid #C198; /* Change button border */
}
```

### Add More Fields
Edit `js/booking-details-modal.js` around line 100 in the `gridHTML` section:

```javascript
<div class="booking-detail-item">
  <p class="booking-detail-label">Your Label</p>
  <p class="booking-detail-value">${bookingData.yourField || 'N/A'}</p>
</div>
```

## Support

For issues or questions, review:
1. Browser console for JavaScript errors
2. Network tab to ensure CSS/JS files load
3. Check that `openBookingDetailsModal` is defined in global scope

---

**Last Updated:** January 2026  
**Version:** 1.0.0  
**Status:** Production Ready ✅
