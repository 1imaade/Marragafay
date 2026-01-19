# 🔄 Email System Architecture - Static Site + Dashboard API

## Overview

**Architecture Pattern:** Static HTML site calls a separate Next.js Dashboard API to send emails.

```
┌─────────────────────────────────────┐
│   STATIC HTML WEBSITE               │
│   (Marragafay Main Site)            │
│                                     │
│   ┌─────────────────────────────┐  │
│   │  booking-manager.js         │  │
│   │  - Saves to Supabase        │  │
│   │  - Calls Dashboard API ─────┼──┼──┐
│   └─────────────────────────────┘  │  │
└─────────────────────────────────────┘  │
                                         │
                                         ↓
┌─────────────────────────────────────────────────┐
│   NEXT.JS DASHBOARD (Email Server)              │
│   Running on localhost:3000                     │
│                                                 │
│   ┌──────────────────────────────────────────┐ │
│   │  PUBLIC API: /api/public/send-booking-email│ │
│   │  - CORS-enabled                          │ │
│   │  - Receives booking data                 │ │
│   │  - Generates luxury email                │ │
│   │  - Sends via Resend ──────────────────┐  │ │
│   └──────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
                                               │
                                               ↓
                                    ┌────────────────┐
                                    │  RESEND API    │
                                    │  Email Service │
                                    └────────────────┘
                                               │
                                               ↓
                                    ┌────────────────────┐
                                    │  marragafay        │
                                    │  @gmail.com        │
                                    └────────────────────┘
```

---

## 📂 File Structure

### Static HTML Site (Main Website)
```
e:\Marragafay\
├── index.html
├── packs.html
└── js/
    └── booking-manager.js     ← UPDATED: Calls Dashboard API
```

### Next.js Dashboard (Email Server)
```
e:\Marragafay\
├── app/
│   ├── actions/
│   │   └── send-email.ts              ← Email logic (Resend integration)
│   └── api/
│       └── public/
│           └── send-booking-email/
│               └── route.ts           ← NEW: Public CORS endpoint
└── components/
    └── emails/
        └── BookingNotificationEmail.tsx   ← Email template
```

---

## 🔑 Key Components

### 1. Public API Endpoint (NEW)
**File:** `app/api/public/send-booking-email/route.ts`

**URL:** `http://localhost:3000/api/public/send-booking-email`

**Features:**
- ✅ CORS enabled (`Access-Control-Allow-Origin: *`)
- ✅ Handles OPTIONS preflight requests
- ✅ POST method for sending emails
- ✅ GET method for health checks
- ✅ Validates booking data
- ✅ Calls Resend to send emails
- ✅ Returns JSON response

**CORS Headers:**
```javascript
{
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization',
}
```

### 2. Updated Booking Manager
**File:** `js/booking-manager.js`

**Changes:**
- Updated `DASHBOARD_API_URL` to `http://localhost:3000/api/public/send-booking-email`
- Calls external Dashboard API instead of same-origin endpoint
- Enhanced error logging
- Non-blocking (background) email sending

**Key Code:**
```javascript
const DASHBOARD_API_URL = 'http://localhost:3000/api/public/send-booking-email';

const response = await fetch(DASHBOARD_API_URL, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(bookingData)
});
```

---

## 🚀 How to Run

### Step 1: Start the Dashboard (Email Server)
```bash
cd e:\Marragafay
npm install  # If not already done
npm run dev  # Starts on http://localhost:3000
```

### Step 2: Open Static Site
Open your static HTML files:
- Via Live Server (VS Code)
- Via local file system
- Via any static server

### Step 3: Test Booking
1. Fill out a booking form on the static site
2. Submit the form
3. Check browser console:
   - `📧 Sending email notification to Dashboard API...`
   - `✅ Email notification sent via Dashboard API`
4. Check `marragafay@gmail.com` inbox for email

---

## 🧪 Testing

### Test 1: Health Check
```bash
curl http://localhost:3000/api/public/send-booking-email
```

**Expected Response:**
```json
{
  "status": "ok",
  "message": "Public Booking Email API is running",
  "endpoint": "/api/public/send-booking-email",
  "method": "POST",
  "timestamp": "2026-01-19T00:58:10.000Z"
}
```

### Test 2: Send Test Email via cURL
```bash
curl -X POST http://localhost:3000/api/public/send-booking-email \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Test Guest\",\"email\":\"test@example.com\",\"phone_number\":\"+212600000000\",\"date\":\"2026-02-15\",\"guests\":2,\"package_title\":\"Test Package\",\"total_price\":500}"
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Booking notification email sent successfully",
  "id": "abc123..."
}
```

### Test 3: From Browser Console
```javascript
fetch('http://localhost:3000/api/public/send-booking-email', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: 'Browser Test',
    email: 'test@test.com',
    phone_number: '+212600000000',
    date: '2026-02-15',
    guests: 2,
    package_title: 'Test Booking',
    total_price: 500
  })
})
.then(r => r.json())
.then(console.log);
```

---

## 🔒 Security Considerations

### Current Setup (Development)
```javascript
'Access-Control-Allow-Origin': '*'  // Allows any origin
```
✅ Good for: Local development and testing  
⚠️ Risk: Anyone can call your API

### Production Recommendations

**Option 1: Restrict to Specific Domain**
```javascript
'Access-Control-Allow-Origin': 'https://marragafay.com'
```

**Option 2: Add API Key Authentication**
```javascript
// In route.ts
const apiKey = request.headers.get('X-API-Key');
if (apiKey !== process.env.INTERNAL_API_KEY) {
  return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
}
```

**Option 3: Rate Limiting**
Use middleware to prevent spam:
```javascript
// Limit to 10 requests per minute per IP
```

---

## 🌐 Production Deployment

### Update URLs

**In `js/booking-manager.js`:**
```javascript
// Development
const DASHBOARD_API_URL = 'http://localhost:3000/api/public/send-booking-email';

// Production
const DASHBOARD_API_URL = 'https://dashboard.marragafay.com/api/public/send-booking-email';
```

**Or use environment detection:**
```javascript
const DASHBOARD_API_URL = window.location.hostname === 'localhost'
  ? 'http://localhost:3000/api/public/send-booking-email'
  : 'https://dashboard.marragafay.com/api/public/send-booking-email';
```

### Deployment Checklist
- [ ] Deploy Dashboard to Vercel/Netlify
- [ ] Add `RESEND_API_KEY` to environment variables
- [ ] Update `DASHBOARD_API_URL` in booking-manager.js
- [ ] Update CORS to specific domain (optional)
- [ ] Test from production static site
- [ ] Verify emails are received

---

## 🐛 Troubleshooting

### Issue: CORS Error in Browser
```
Access to fetch at 'http://localhost:3000/...' from origin 'null' has been blocked by CORS policy
```

**Solution:**
1. Make sure Dashboard is running (`npm run dev`)
2. Check that `route.ts` includes CORS headers
3. For `file://` protocol, use a local server instead

### Issue: "Failed to fetch"
**Possible Causes:**
1. Dashboard not running
2. Wrong port (should be 3000)
3. Firewall blocking request

**Solution:**
```bash
# Check if Dashboard is running
curl http://localhost:3000/api/public/send-booking-email

# If not, start it
npm run dev
```

### Issue: Email not sending
**Checklist:**
1. [ ] `RESEND_API_KEY` in `.env.local`
2. [ ] Dashboard restarted after adding key
3. [ ] Email verified in Resend
4. [ ] Check Dashboard console for errors

---

## 📊 Request Flow

```
1. Customer fills booking form on static site
        ↓
2. JavaScript validates and saves to Supabase
        ↓
3. Shows success modal to customer
        ↓
4. [Background] Calls Dashboard API
        ↓ HTTP POST
   ┌────────────────────────────────────┐
   │  http://localhost:3000/api/public/ │
   │  send-booking-email                │
   │                                    │
   │  1. Receives booking data          │
   │  2. Validates required fields      │
   │  3. Calls sendBookingNotification()│
   │  4. Generates HTML email           │
   │  5. Sends via Resend              │
   │  6. Returns success/error          │
   └────────────────────────────────────┘
        ↓
5. Email arrives at marragafay@gmail.com
        ↓
6. Admin can click to contact customer
```

---

## ✅ Advantages of This Architecture

1. **Separation of Concerns**
   - Static site handles UI
   - Dashboard handles server logic

2. **Security**
   - API keys stay on server
   - No exposure in client code

3. **Scalability**
   - Dashboard can be scaled independently
   - Can serve multiple static sites

4. **Flexibility**
   - Easy to update email logic
   - Can add auth, rate limiting, etc.

5. **Development**
   - Can test each part independently
   - Clear boundaries between systems

---

## 🔧 Environment Variables

### Dashboard (.env.local)
```env
# Resend Email Service
RESEND_API_KEY=re_your_key_here

# Supabase (if Dashboard also uses it)
NEXT_PUBLIC_SUPABASE_URL=your_url
SUPABASE_SERVICE_ROLE_KEY=your_key
```

### Static Site
No environment variables needed! 🎉

---

## 📝 Summary

**What Changed:**
1. ✅ Created public API endpoint with CORS
2. ✅ Updated booking-manager.js to call Dashboard
3. ✅ Email sending now happens on Dashboard server

**What Stayed the Same:**
1. ✅ Booking UI and forms
2. ✅ Supabase integration
3. ✅ Email template design
4. ✅ Success modal behavior

**Next Steps:**
1. Start Dashboard: `npm run dev`
2. Open static site
3. Submit test booking
4. Check inbox!

---

**Status:** ✅ **READY TO USE**  
**Dashboard API:** http://localhost:3000/api/public/send-booking-email  
**Admin Email:** marragafay@gmail.com
