# 🏜️ Marragafay | Agafay Desert Luxury Experiences & Tours

> **Official Website:** [https://marragafay.com](https://marragafay.com)  
> **Brand Focus:** Luxury excursions, private camps, desert dinners, and adventure tours in the Agafay Desert (Marrakech, Morocco).

---

## 📌 Project Overview

**Marragafay** is a high-performance, multilingual static web platform designed to showcase and sell luxury desert experiences with instant loading speeds, high SEO visibility, and seamless mobile booking experiences.

### ✨ Key Features
- 🌐 **Multilingual Support:** Native localized routing across 4 languages:
  - 🇬🇧 English (`/en/`)
  - 🇫🇷 French (`/fr/`)
  - 🇪🇸 Spanish (`/es/`)
  - 🇲🇦 Arabic (`/ar/`) with RTL layout
- ⚡ **Zero-Latency Language Routing:** Root `index.html` acts as a fast language router detecting user preferences.
- 📱 **Mobile-First Luxury UX:** Custom booking modals, responsive image lightboxes, testimonials carousel, and interactive review system.
- 💬 **Direct Lead Generation:** WhatsApp deep-links with pre-filled booking details & Supabase integration for booking inquiries and reviews.

---

## 📂 Directory Structure

```text
marragafay.com/
├── index.html            # Ultra-fast client-side language router
├── vercel.json           # Vercel deployment configuration & security headers
├── .gitignore            # Hardened git ignore (prevents secret leaks)
│
├── en/                   # 🇬🇧 English localized pages
├── fr/                   # 🇫🇷 French localized pages
├── es/                   # 🇪🇸 Spanish localized pages
├── ar/                   # 🇲🇦 Arabic localized pages
│
├── activities/           # Excursion detail pages (camel-ride, quad-biking, etc.)
├── packages/             # Tiered package pages (basic, comfort, luxe)
│
├── css/                  # Stylesheets & component bundles
├── js/                   # Client-side scripts & Supabase client
├── images/               # WebP & optimized media assets
├── fonts/                # Custom brand typography
│
├── docs/                 # Documentation & architectural reference
│   ├── design.md         # Design system tokens, colors, & typography
│   ├── database/         # Supabase SQL schemas
│   ├── brand/            # High-resolution brand assets & logos
│   └── archive/          # Historical migration & implementation notes
│
└── scripts/              # Build & maintenance utilities
    └── maintenance/      # Image optimization & batch processing scripts
```

---

## 🔒 Security & Environment Configuration

### Secrets & API Keys
- Sensitive keys (`SUPABASE_SERVICE_ROLE_KEY`, `RESEND_API_KEY`) **must never** be committed to Git or used in client-side JavaScript.
- `.env.local` is strictly excluded in `.gitignore`.
- Browser client scripts (such as `js/supabase-client.js`) only use the public **`SUPABASE_ANON_KEY`**.
- All Supabase tables (`bookings`, `reviews`, `messages`) should enforce **Row Level Security (RLS)** policies.

---

## 🚀 Deployment

The site is configured for automatic deployment via **Vercel** as a static website:
- **Build Command:** Static (no server build step needed for standard HTML pages).
- **Security Headers:** Configured in `vercel.json` (`X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`).

---

## 🛠️ Developer & AI Agent Guidelines

1. **Keep the Root Directory Clean:** Do not create temporary `.md` summary files or batch `.py` scripts in the root directory. Place documentation in `docs/` and utility scripts in `scripts/maintenance/`.
2. **Preserve Multilingual Parity:** When updating a section or price on an English page (`/en/`), make corresponding updates across `/fr/`, `/es/`, and `/ar/`.
3. **Optimize Images:** Always use modern image formats (WebP) with appropriate `fetchpriority` and responsive `srcset` where appropriate.