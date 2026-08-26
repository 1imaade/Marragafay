// Booking Manager - handles browser submission through the authoritative API.
// Product and price authority lives in api/booking-catalog.js on the server.

// ═══════════════════════════════════════════════════════════════════
// 🌐 SMART INTERNATIONAL PHONE & WHATSAPP AUTO-DETECTION
// ═══════════════════════════════════════════════════════════════════
(function () {
    const COUNTRY_CALLING_CODES = {
        'fr': '+33', 'gb': '+44', 'uk': '+44', 'us': '+1', 'ca': '+1',
        'es': '+34', 'ma': '+212', 'de': '+49', 'it': '+39', 'be': '+32',
        'ch': '+41', 'nl': '+31', 'pt': '+351', 'ae': '+971', 'sa': '+966',
        'qa': '+974', 'kw': '+965', 'au': '+61', 'ie': '+353', 'se': '+46',
        'no': '+47', 'dk': '+45', 'pl': '+48'
    };

    function detectVisitorPrefix() {
        try {
            const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
            const userLang = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
            const langCode = userLang.split('-')[0];
            const countryCode = (userLang.split('-')[1] || '').toLowerCase();

            if (timeZone.includes('Paris')) return '+33';
            if (timeZone.includes('London')) return '+44';
            if (timeZone.includes('Madrid')) return '+34';
            if (timeZone.includes('Berlin') || timeZone.includes('Frankfurt')) return '+49';
            if (timeZone.includes('Rome')) return '+39';
            if (timeZone.includes('Brussels')) return '+32';
            if (timeZone.includes('Amsterdam')) return '+31';
            if (timeZone.includes('Zurich') || timeZone.includes('Geneva')) return '+41';
            if (timeZone.includes('Lisbon')) return '+351';
            if (timeZone.includes('Casablanca')) return '+212';
            if (timeZone.includes('Dubai')) return '+971';
            if (timeZone.includes('Riyadh')) return '+966';
            if (timeZone.includes('New_York') || timeZone.includes('Chicago') || timeZone.includes('Los_Angeles')) return '+1';
            if (timeZone.includes('Toronto') || timeZone.includes('Vancouver')) return '+1';
            if (timeZone.includes('Sydney') || timeZone.includes('Melbourne')) return '+61';

            if (countryCode && COUNTRY_CALLING_CODES[countryCode]) return COUNTRY_CALLING_CODES[countryCode];
            if (COUNTRY_CALLING_CODES[langCode]) return COUNTRY_CALLING_CODES[langCode];
        } catch (e) {}
        return '+212';
    }

    const detectedPrefix = detectVisitorPrefix();

    function formatInternationalNumber(raw) {
        if (!raw) return '';
        let cleaned = raw.trim().replace(/[\s\-\(\)]/g, '');
        if (cleaned.startsWith('+')) return cleaned;
        if (cleaned.startsWith('00')) return '+' + cleaned.substring(2);
        if (cleaned.startsWith('0')) return detectedPrefix + ' ' + cleaned.substring(1);
        if (/^\d{8,11}$/.test(cleaned)) return detectedPrefix + ' ' + cleaned;
        return detectedPrefix + ' ' + cleaned;
    }

    function initPhoneInputs() {
        const phoneInputs = document.querySelectorAll('input[type="tel"], input[name="phone"], input[name="phone_number"]');
        phoneInputs.forEach(input => {
            if (input.dataset.smartPhoneAttached) return;
            input.dataset.smartPhoneAttached = 'true';

            if (detectedPrefix && input.placeholder && input.placeholder.includes('+212')) {
                input.placeholder = detectedPrefix + ' 600...';
            }

            // Enforce LTR phone input on Arabic pages so + and digits type correctly
            if (document.documentElement.lang === 'ar' || document.documentElement.dir === 'rtl') {
                input.style.direction = 'ltr';
                input.style.textAlign = 'right';
            }

            input.addEventListener('focus', function () {
                if (!this.value.trim()) {
                    this.value = detectedPrefix + ' ';
                }
            });

            input.addEventListener('blur', function () {
                if (this.value.trim() === detectedPrefix || this.value.trim() === '+') {
                    this.value = '';
                } else if (this.value.trim()) {
                    this.value = formatInternationalNumber(this.value);
                }
            });

            input.addEventListener('input', function () {
                if (this.value.startsWith('++')) {
                    this.value = '+' + this.value.replace(/^\++/, '');
                }
            });
        });
    }

    function initDateInputs() {
        try {
            const today = new Date().toISOString().split('T')[0];
            const dateInputs = document.querySelectorAll('input[type="date"]');
            dateInputs.forEach(input => {
                input.min = today;
            });
        } catch (e) {}
    }

    window.formatInternationalPhone = formatInternationalNumber;

    function initAllFormHelpers() {
        initPhoneInputs();
        initDateInputs();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAllFormHelpers);
    } else {
        initAllFormHelpers();
    }
    document.addEventListener('click', () => setTimeout(initAllFormHelpers, 300));
})();

/**
 * Send Booking Email Notification
 * 
 * Calls the PUBLIC API endpoint on the Dashboard (Next.js app) to send email notifications.
 * The Dashboard app (admin.marragafay.com) provides a CORS-enabled endpoint
 * that this static site can call to trigger email notifications via Resend.
 * 
 * @param {Object} bookingData - The booking data to include in the email
 * @returns {Promise<{success: boolean, error?: string, id?: string}>}
 */
async function sendBookingEmailNotification(bookingData) {
    try {
        const attribution = typeof window.MarragafayAttribution?.getBookingAttribution === 'function'
            ? window.MarragafayAttribution.getBookingAttribution()
            : undefined;

        const payload = {
            name: bookingData.name,
            email: bookingData.email,
            phone_number: bookingData.phone_number,
            date: bookingData.date,
            guests: bookingData.guests,
            adults: bookingData.adults,
            children: bookingData.children,
            package_title: bookingData.package_title,
            total_price: bookingData.total_price,
            notes: bookingData.notes,
            language: document.documentElement.lang || 'en',
            ...(attribution ? { attribution } : {})
        };

        // Determine API endpoint (use live Vercel endpoint when testing on local dev server)
        const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
        const endpoint = isLocal ? 'https://www.marragafay.com/api/booking' : '/api/booking';

        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            if (response.ok) {
                const result = await response.json();
                return result;
            }
        } catch (errApi) {
            console.warn('Primary email dispatch error:', errApi);
            // Fallback for live production
            if (!isLocal) {
                try {
                    const response2 = await fetch('/api/booking.js', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                    if (response2.ok) {
                        return await response2.json();
                    }
                } catch (e2) {}
            }
        }

        return { success: true };

    } catch (error) {
        console.error('❌ Failed to send booking email notification:', error);
        // Don't throw - we don't want email failure to break the booking flow
        return { success: false, error: error.message };
    }
}


// Dynamically load SweetAlert2 if not already present
if (!window.Swal) {
    console.log('Loading SweetAlert2...');

    // Load SweetAlert2 JS from CDN
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/sweetalert2@11';
    script.async = true;
    document.head.appendChild(script);

    script.onload = () => {
        console.log('SweetAlert2 loaded successfully!');
    };
}

// Use Event Delegation to handle dynamically rendered forms
// Retained only as a migration reference; active forms use the handler below.
/*
document.addEventListener('booking-legacy-submit', async function (e) {
    // Check if the submitted element is our booking form (support both old and new IDs for GTM)
    if (e.target && (e.target.id === 'bookingForm' || e.target.id === 'booking-form' || e.target.id === 'booking-form-activity')) {
        e.preventDefault(); // Stop page reload
        console.log('Form submission detected via Delegation!');

        const form = e.target;

        // Anti-Spam & Double Submission Guard
        if (form.dataset.submitting === 'true') {
            console.warn('⚠️ Booking already in progress, ignoring duplicate click.');
            return;
        }
        form.dataset.submitting = 'true';

        // UX: Immediate feedback & prevent double submission
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.dataset.originalText = submitBtn.innerText;
            submitBtn.innerText = 'Processing...';
        }

        const formData = new FormData(form);

        // ====================================================
        // 📱 FIX 1: PHONE NUMBER EXTRACTION (Split Fields)
        // ====================================================
        let phoneNumber = '';

        // Strategy 1: Try to find Country Code (select) + Phone Number (input) - SPLIT FIELDS
        const countryCodeElement = document.getElementById('country-code') ||
            document.querySelector('select[name="country_code"]') ||
            document.querySelector('select[name="countryCode"]') ||
            document.querySelector('.country-code-select');

        const phoneInputElement = document.getElementById('phone') ||
            document.getElementById('phone-number') ||
            document.querySelector('input[name="phone"]') ||
            document.querySelector('input[name="phone_number"]') ||
            document.querySelector('.phone-input');

        if (countryCodeElement && phoneInputElement) {
            // Combine country code and phone number
            const countryCode = countryCodeElement.value || '';
            const phoneNum = phoneInputElement.value || '';
            phoneNumber = `${countryCode} ${phoneNum}`.trim();
            console.log('📱 Phone from split fields (Country + Number):', phoneNumber);
        }

        // Strategy 2: Try intl-tel-input plugin if split fields not found
        if (!phoneNumber && phoneInputElement && window.intlTelInputGlobals) {
            try {
                const iti = window.intlTelInputGlobals.getInstance(phoneInputElement);
                if (iti) {
                    phoneNumber = iti.getNumber();
                    console.log('📱 Phone from intl-tel-input:', phoneNumber);
                }
            } catch (e) {
                console.warn('intl-tel-input not found, trying fallback');
            }
        }

        // Strategy 3: Fallback to single phone input or FormData
        if (!phoneNumber) {
            phoneNumber = phoneInputElement?.value || formData.get('phone') || formData.get('phone_number') || '';
            console.log('📱 Phone from single input/FormData:', phoneNumber);
        }

        // Automatic International Country Code Formatting
        if (phoneNumber && phoneNumber !== 'Not provided') {
            if (typeof window.formatInternationalPhone === 'function') {
                phoneNumber = window.formatInternationalPhone(phoneNumber);
            }
        }

        // Final fallback
        if (!phoneNumber) {
            phoneNumber = 'Not provided';
            console.warn('⚠️ Could not extract phone number from any source');
        }

        // ====================================================
        // 👥 FIX 2: GUESTS FORMATTING
        // ====================================================
        const adults = parseInt(formData.get('adults') || formData.get('guests') || '1');
        const children = parseInt(formData.get('children') || '0');
        const totalGuests = adults + children;

        // Format guests as a readable string for email
        const guestsFormatted = `${adults} Adults, ${children} Children`;
        console.log('👥 Guests formatted:', guestsFormatted);

        // ====================================================
        // 📝 FIX 3: NOTES EXTRACTION
        // ====================================================
        const notesTextarea = document.getElementById('notes') ||
            document.querySelector('textarea[name="notes"]') ||
            document.querySelector('textarea[name="message"]');
        const notesValue = notesTextarea?.value || formData.get('notes') || formData.get('message') || '';
        const notes = notesValue.trim() || 'No special requests';
        console.log('📝 Notes:', notes);

        const bookingData = {
            name: formData.get('full_name') || formData.get('name'),
            email: formData.get('email') || (phoneNumber && phoneNumber !== 'Not provided' ? phoneNumber.replace(/[\s+\-]/g, '') + "@marragafay.local" : "no-email-provided@marragafay.local"),
            phone_number: phoneNumber,
            date: formData.get('booking_date') || formData.get('date'), // DB Column: date
            guests: totalGuests,
            adults: adults,
            children: children,
            package_title: formData.get('package_title') || document.title,
            notes: notes
        };

        // ====================================================
        // 💰 CANONICAL PRICING CALCULATION (MAD Base Truth)
        // ====================================================
        const titleToCheck = bookingData.package_title || '';
        let itemType = 'package';
        let itemName = 'Basic'; // Default fallback

        // Item identification from title or URL
        if (titleToCheck.includes('Basic') || titleToCheck.includes('Agafay Discovery') || titleToCheck.includes('Discovery') || window.location.pathname.includes('/basic')) {
            itemType = 'package';
            itemName = 'Basic';
        } else if (titleToCheck.includes('Comfort') || titleToCheck.includes('Signature') || titleToCheck.includes('Marragafay Signature') || window.location.pathname.includes('/comfort')) {
            itemType = 'package';
            itemName = 'Comfort';
        } else if (titleToCheck.includes('Luxe') || titleToCheck.includes('Luxury') || window.location.pathname.includes('/luxe')) {
            itemType = 'package';
            itemName = 'Luxe';
        } else if (titleToCheck.includes('Quad') || window.location.pathname.includes('quad-biking')) {
            itemType = 'activity';
            itemName = 'Quad Biking';
        } else if (titleToCheck.includes('Buggy') || titleToCheck.includes('البوغي') || window.location.pathname.includes('buggy')) {
            itemType = 'activity';
            itemName = 'Buggy';
        } else if (titleToCheck.includes('Camel') || titleToCheck.includes('جمال') || window.location.pathname.includes('camel-ride')) {
            itemType = 'activity';
            itemName = 'Camel Ride';
        } else if (titleToCheck.includes('Dinner') || titleToCheck.includes('عشاء') || window.location.pathname.includes('dinner-show')) {
            itemType = 'activity';
            itemName = 'Dinner & Show';
        } else if (titleToCheck.includes('Paragliding') || titleToCheck.includes('Parapente') || titleToCheck.includes('طيران شراعي') || window.location.pathname.includes('paragliding')) {
            itemType = 'activity';
            itemName = 'Paragliding';
        } else if (titleToCheck.includes('Balloon') || titleToCheck.includes('منطاد') || window.location.pathname.includes('hot-air-balloon')) {
            itemType = 'activity';
            itemName = 'Hot Air Balloon';
        }

        // Canonical MAD price per person (e.g. 799 MAD for Paragliding, 800 MAD for Buggy, 350 MAD for Basic)
        let canonicalPriceMAD = CANONICAL_PRICES_MAD[itemName] || 350;

        // Try to fetch dynamic price override from Supabase pricing table if configured
        if (typeof window.getDynamicPrice === 'function') {
            try {
                const apiPrice = await window.getDynamicPrice(itemType, itemName);
                if (apiPrice && !isNaN(apiPrice)) {
                    // If the dynamic pricing API returns MAD price directly
                    if (apiPrice > 100) {
                        canonicalPriceMAD = apiPrice;
                    }
                }
            } catch (error) {
                console.error('Error fetching dynamic API price:', error);
            }
        }

        const isQuad = (itemName === 'Quad Biking');
        const isBuggy = (itemName === 'Buggy');
        const isDinner = (itemName === 'Dinner & Show');

        // Quad Validation: Children under 16 ride only as passengers (max 1 child per adult driver)
        if (isQuad) {
            if (adults < 1) {
                if (window.Swal) {
                    Swal.fire({
                        icon: 'warning',
                        title: 'Adult Required',
                        text: 'Children under 16 must be accompanied by at least one adult rider.',
                        confirmButtonColor: '#523225'
                    });
                } else {
                    alert('Children under 16 must be accompanied by at least one adult rider.');
                }
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = submitBtn.dataset.originalText || 'Book now';
                }
                delete form.dataset.submitting;
                return;
            }
            if (children > adults) {
                if (window.Swal) {
                    Swal.fire({
                        icon: 'warning',
                        title: 'Quad Capacity Limit',
                        text: 'Each paying rider can accompany a maximum of one child passenger under 16.',
                        confirmButtonColor: '#523225'
                    });
                } else {
                    alert('Each paying rider can accompany a maximum of one child passenger under 16.');
                }
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = submitBtn.dataset.originalText || 'Book now';
                }
                delete form.dataset.submitting;
                return;
            }
        }

        // Billable calculation:
        // - Quad: adults * 250 (children under 16 join FREE as passengers, max 1 per adult)
        // - Buggy: Math.max(2, totalGuests) * 800 (minimum 2 paying guests)
        // - Dinner & Show: adults * 250 (children under 12 join FREE)
        // - Paragliding, Camel, Balloon & Packs: totalGuests * canonicalPriceMAD
        const billableGuests = (isQuad || isDinner) ? adults : (isBuggy ? Math.max(2, totalGuests) : totalGuests);
        let baseTotalMAD = 0;
        if (isQuad || isDinner) {
            baseTotalMAD = adults * 250;
        } else {
            baseTotalMAD = canonicalPriceMAD * billableGuests;
        }

        // Safely initialize optional extras in MAD (default 0 MAD)
        let extraActivitiesPriceMAD = 0;

        // Calculate total in Moroccan Dirhams (MAD) for Supabase backend
        let totalMAD = baseTotalMAD + extraActivitiesPriceMAD;

        // 🚨 BACKEND PROTECTION: Supabase bookings table stores total_price in MAD
        bookingData.total_price = totalMAD;

        console.log('💰 Item Name:', itemName, `(${itemType})`);
        console.log('💰 Canonical Base Price (MAD/person):', canonicalPriceMAD);
        console.log('💰 Billable Guests:', billableGuests, `(Total Guests: ${totalGuests})`);
        console.log('💰 Base Total (MAD):', baseTotalMAD);
        console.log('💰 Extras Total (MAD):', extraActivitiesPriceMAD);
        console.log('💰 Final Calculated total_price (MAD):', bookingData.total_price);

        // Safety audit: warn if price looks abnormal
        if (bookingData.total_price < 50 || bookingData.total_price > 100000) {
            console.warn(
                '⚠️  AUDIT: total_price =', bookingData.total_price,
                '(MAD). If this looks wrong, verify the MAD calculation.'
            );
        }

        // ====================================================
        // 🐛 DEBUGGING: Log the complete payload
        // ====================================================
        console.log('\n========================================');
        console.log('📦 FINAL PAYLOAD BEFORE SENDING TO API');
        console.log('========================================');
        console.log('🔍 Captured Phone:', phoneNumber);
        console.log('🔍 Captured Price (MAD):', bookingData.total_price);
        console.log('\n📧 Complete Email Payload:');
        console.log({
            name: bookingData.name,
            email: bookingData.email,
            phone_number: phoneNumber,  // Show the actual variable being sent
            date: bookingData.date,
            guests_total: bookingData.guests,
            guests_formatted: guestsFormatted,
            adults: bookingData.adults,
            children: bookingData.children,
            package_title: bookingData.package_title,
            total_price: bookingData.total_price,  // Show the actual variable being sent
            notes: bookingData.notes
        });
        console.log('========================================\n');

        // Phone Number Validation - Only allow numbers, spaces, +, and -
        const phoneRegex = /^[0-9\s+\-]+$/;
        if (bookingData.phone_number && !phoneRegex.test(bookingData.phone_number)) {
            // Re-enable button if validation fails
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerText = submitBtn.dataset.originalText || 'Book Now';
            }

            // Beautiful error popup for phone validation
            if (window.Swal) {
                Swal.fire({
                    title: 'Invalid Phone Number',
                    text: 'Please enter a valid phone number using only numbers, spaces, +, and - characters.',
                    icon: 'warning',
                    confirmButtonText: 'Got it',
                    confirmButtonColor: '#bc6c25',
                    background: '#fff',
                    color: '#333',
                    showClass: {
                        popup: 'animate__animated animate__fadeIn animate__faster'
                    },
                    hideClass: {
                        popup: 'animate__animated animate__fadeOut animate__faster'
                    },
                    customClass: {
                        popup: 'swal-clean-popup',
                        title: 'swal-clean-title',
                        confirmButton: 'swal-clean-btn'
                    }
                });
            } else {
                alert('Please enter a valid phone number (numbers, spaces, +, and - only).');
            }
            return;
        }

        // Validate date is not in the past
        if (bookingData.date) {
            const today = new Date().toISOString().split('T')[0];
            if (bookingData.date < today) {
                form.dataset.submitting = 'false';
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = submitBtn.dataset.originalText || 'Book Now';
                }
                if (window.Swal) {
                    Swal.fire({
                        title: 'Invalid Date',
                        text: 'Please select today or a future date for your booking.',
                        icon: 'warning',
                        confirmButtonText: 'Got it',
                        confirmButtonColor: '#bc6c25'
                    });
                } else {
                    alert('Please select today or a future date for your booking.');
                }
                return;
            }
        }

        // Check for missing critical fields
        if (!bookingData.name || !bookingData.phone_number) {
            form.dataset.submitting = 'false';

            // Re-enable button if validation fails
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerText = submitBtn.dataset.originalText || 'Book Now';
            }

            // Beautiful error popup for validation
            if (window.Swal) {
                Swal.fire({
                    title: 'Almost There',
                    text: 'Please complete all required fields.',
                    icon: 'info',
                    confirmButtonText: 'Got it',
                    confirmButtonColor: '#bc6c25',
                    background: '#fff',
                    color: '#333',
                    showClass: {
                        popup: 'animate__animated animate__fadeIn animate__faster'
                    },
                    hideClass: {
                        popup: 'animate__animated animate__fadeOut animate__faster'
                    },
                    customClass: {
                        popup: 'swal-clean-popup',
                        title: 'swal-clean-title',
                        confirmButton: 'swal-clean-btn'
                    }
                });
            } else {
                alert('Please fill in all required fields.');
            }
            return;
        }

        console.log("Supabase Payload Payload:", { name: bookingData.name, phone: bookingData.phone_number, date: bookingData.date, adults: bookingData.adults, children: bookingData.children, package_name: bookingData.package_title });

        try {
            // Insert into Supabase
            const { data, error } = await supabaseClient
                .from('bookings')
                .insert([bookingData]);

            if (error) {
                console.error("Supabase Insertion Error:", error);
                alert("Booking failed. Please check the console.");
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = submitBtn.dataset.originalText || 'Book Now';
                }
                return;
            }

            // SUCCESS - Display Booking Details Modal
            console.log('Booking successful:', data);

            // Decrement scarcity slot count if tracking is active on this form
            var slotKey = e.target ? e.target.dataset.slotsKey : null;
            if (slotKey && typeof window.decrementSlotCount === 'function') {
                window.decrementSlotCount(slotKey);
            }

            // ============================================
            // 📧 SEND EMAIL NOTIFICATION (Blocking)
            // ============================================
            // Await this to ensure the fetch request completes before the browser redirects.
            await sendBookingEmailNotification(bookingData)
                .then(result => {
                    if (result.success) {
                        console.log('✅ Email notification sent successfully:', result.id);
                    } else {
                        console.warn('⚠️ Email notification failed:', result.error);
                    }
                })
                .catch(err => {
                    console.error('❌ Email notification error:', err);
                });

            localStorage.setItem('recentBooking', JSON.stringify({
                name: bookingData.name,
                date: bookingData.date,
                package_name: bookingData.package_title,
                guests_total: bookingData.guests,
                total_price_eur: bookingData.total_eur || total,
                total_price_mad: bookingData.total_mad || bookingData.total_price,
                customer_currency: 'EUR',
                accounting_currency: 'MAD',
                total_price: bookingData.total_eur || total,
                whatsapp: bookingData.phone_number
            }));

            // Redirect to appropriate language success page (compatible with both local Live Server and Vercel)
            const currentPath = window.location.pathname;
            let targetSuccess = '/success.html';
            if (currentPath.includes('/en/')) targetSuccess = '/en/success.html';
            else if (currentPath.includes('/fr/')) targetSuccess = '/fr/success.html';
            else if (currentPath.includes('/es/')) targetSuccess = '/es/success.html';
            else if (currentPath.includes('/ar/')) targetSuccess = '/ar/success.html';

            window.location.href = targetSuccess;

        } catch (error) {
            // Error handling - Beautiful error popup
            console.error('Booking error detail:', error);

            // Re-enable button on error
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerText = submitBtn.dataset.originalText || 'Book Now';
            }

            if (window.Swal) {
                Swal.fire({
                    title: 'Something Went Wrong',
                    text: 'Please try again or contact us directly.',
                    icon: 'error',
                    confirmButtonText: 'Retry',
                    confirmButtonColor: '#bc6c25',
                    background: '#fff',
                    color: '#333',
                    showClass: {
                        popup: 'animate__animated animate__fadeIn animate__faster'
                    },
                    hideClass: {
                        popup: 'animate__animated animate__fadeOut animate__faster'
                    },
                    customClass: {
                        popup: 'swal-clean-popup',
                        title: 'swal-clean-title',
                        confirmButton: 'swal-clean-btn'
                    }
                });
            } else {
                alert('Error: ' + (error.message || 'Unknown error'));
            }
        }
    }
});
*/

// Active booking path: browser sends normalized input only. The server owns
// product resolution, validation, persistence, and trusted MAD pricing.
(function () {
    'use strict';

    const PRODUCT_BY_PATH = [
        ['/packages/basic', 'basic'], ['/packages/comfort', 'comfort'], ['/packages/luxe', 'luxe'],
        ['/activities/quad-biking', 'quad'], ['/activities/buggy', 'buggy'],
        ['/activities/camel-ride', 'camel'], ['/activities/paragliding', 'paragliding'],
        ['/activities/hot-air-balloon', 'hot-air-balloon'], ['/activities/dinner-show', 'dinner-show']
    ];

    window.MarragafayBookingManagerHandlesSubmit = true;

    function firstValue(formData, names) {
        for (const name of names) {
            const value = formData.get(name);
            if (value !== null && String(value).trim() !== '') return String(value).trim();
        }
        return '';
    }

    function productIdForForm(form, formData) {
        const dataProduct = form.dataset.productId || form.dataset.product;
        if (dataProduct) return dataProduct;

        const explicit = firstValue(formData, ['product_id', 'productId', 'product']);
        if (explicit) return explicit;

        const path = window.location.pathname.toLowerCase();
        const pathMatch = PRODUCT_BY_PATH.find(([fragment]) => path.includes(fragment));
        if (pathMatch) return pathMatch[1];

        const modal = form.closest('#packageModal, #activityModal');
        const modalTitle = modal?.querySelector('.modal-title')?.textContent || '';
        const title = `${firstValue(formData, ['package_title', 'title', 'activity'])} ${modalTitle}`.toLowerCase();
        if (title.includes('comfort') || title.includes('signature')) return 'comfort';
        if (title.includes('luxe') || title.includes('luxury') || title.includes('vip')) return 'luxe';
        if (title.includes('quad')) return 'quad';
        if (title.includes('buggy')) return 'buggy';
        if (title.includes('camel')) return 'camel';
        if (title.includes('paragliding') || title.includes('parapente')) return 'paragliding';
        if (title.includes('balloon') || title.includes('منطاد')) return 'hot-air-balloon';
        if (title.includes('dinner') || title.includes('diner') || title.includes('عشاء')) return 'dinner-show';
        // Never guess a product for an unrecognized homepage/modal state.
        return '';
    }

    function formPayload(form) {
        const formData = new FormData(form);
        const phoneInput = form.querySelector('input[name="phone"], input[name="phone_number"], input[type="tel"]');
        const countryCode = form.querySelector('select[name="country_code"], select[name="countryCode"], .country-code-select');
        let phone = firstValue(formData, ['phone_number', 'phone']);
        if (countryCode?.value && phone && !phone.trim().startsWith('+')) phone = `${countryCode.value} ${phone}`.trim();
        if (typeof window.formatInternationalPhone === 'function' && phone) phone = window.formatInternationalPhone(phone);
        if (!phone && phoneInput) phone = phoneInput.value.trim();

        const groupSize = firstValue(formData, ['groupSize', 'group_size']);
        const adults = firstValue(formData, ['adults']);
        const children = firstValue(formData, ['children']) || '0';
        const guests = adults || firstValue(formData, ['guests']) || groupSize;
        const notes = firstValue(formData, ['notes', 'requests', 'message']);
        const language = document.documentElement.lang || (window.location.pathname.match(/^\/(en|fr|es|ar)(?:\/|$)/)?.[1]) || 'en';
        const attribution = typeof window.MarragafayAttribution?.getBookingAttribution === 'function'
            ? window.MarragafayAttribution.getBookingAttribution()
            : undefined;

        return {
            product_id: productIdForForm(form, formData),
            name: firstValue(formData, ['full_name', 'name']),
            email: firstValue(formData, ['email']),
            phone,
            date: firstValue(formData, ['booking_date', 'date']),
            adults: adults || undefined,
            children,
            guests,
            notes,
            language,
            ...(attribution ? { attribution } : {})
        };
    }

    function emitBookingConversion(result, payload) {
        const bookingId = typeof result?.booking_id === 'string' ? result.booking_id : '';
        if (!bookingId || !Array.isArray(window.dataLayer)) return;

        const eventKey = `marragafay_booking_event_v1:${bookingId}`;
        const customerTotalEur = Number(result.trusted_total_eur);
        const accountingTotalMad = Number(result.trusted_total_mad);
        if (!Number.isFinite(customerTotalEur) || !Number.isFinite(accountingTotalMad)) return;

        let dedupeStorage = null;
        try { dedupeStorage = window.sessionStorage; } catch {}
        if (!dedupeStorage) {
            try { dedupeStorage = window.localStorage; } catch {}
        }
        if (dedupeStorage) {
            try {
                if (dedupeStorage.getItem(eventKey)) return;
                dedupeStorage.setItem(eventKey, '1');
            } catch {}
        }

        window.dataLayer.push({
            event: 'booking_request_submitted',
            product_id: result.product_id,
            product_type: result.product_type,
            customer_total_eur: customerTotalEur,
            accounting_total_mad: accountingTotalMad,
            source_category: result.source_category || payload.attribution?.source_category || 'other',
            language: payload.language
        });
    }

    function showBookingError(message) {
        if (window.Swal) {
            window.Swal.fire({ title: 'Booking unavailable', text: message || 'Please try again or contact us directly.', icon: 'error', confirmButtonColor: '#bc6c25' });
        } else {
            window.alert(message || 'Please try again or contact us directly.');
        }
    }

    document.addEventListener('submit', async function (event) {
        const form = event.target;
        if (!(form instanceof HTMLFormElement) || !form.matches('.booking-form, #bookingForm, #booking-form, #booking-form-activity')) return;
        if (form.dataset.bookingUnsupported === 'true') {
            event.preventDefault();
            showBookingError('This option is currently available by direct contact only.');
            return;
        }
        if (form.dataset.submitting === 'true') return;
        event.preventDefault();
        form.dataset.submitting = 'true';

        const submitButton = form.querySelector('button[type="submit"]');
        const originalText = submitButton?.innerText || '';
        if (submitButton) {
            submitButton.disabled = true;
            submitButton.innerText = 'Processing...';
        }

        try {
            const payload = formPayload(form);
            const response = await fetch('/api/booking', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const result = await response.json().catch(() => ({}));
            if (!response.ok || !result.booking_success) throw new Error(result.error || 'Unable to process booking');

            // The API has already persisted the booking when this event fires.
            // The booking id makes the event idempotent for refreshes/retries.
            emitBookingConversion(result, payload);

            localStorage.setItem('recentBooking', JSON.stringify({
                booking_id: result.booking_id,
                name: payload.name,
                date: payload.date,
                package_name: result.product_title || payload.product_id,
                guests_total: Number(payload.adults || payload.guests || 0) + Number(payload.children || 0),
                total_price_eur: result.trusted_total_eur,
                total_price_mad: result.trusted_total_mad,
                customer_currency: 'EUR',
                accounting_currency: 'MAD',
                total_price: result.trusted_total_eur,
                whatsapp: payload.phone
            }));

            const slotKey = form.dataset.slotsKey;
            if (slotKey && typeof window.decrementSlotCount === 'function') window.decrementSlotCount(slotKey);

            const path = window.location.pathname;
            const target = path.includes('/en/') ? '/en/success.html' : path.includes('/fr/') ? '/fr/success.html' : path.includes('/es/') ? '/es/success.html' : path.includes('/ar/') ? '/ar/success.html' : '/success.html';
            window.location.href = target;
        } catch (error) {
            console.error('Booking submission failed:', error?.message || 'request_failed');
            showBookingError(error?.message);
        } finally {
            form.dataset.submitting = 'false';
            if (submitButton) {
                submitButton.disabled = false;
                submitButton.innerText = originalText;
            }
        }
    });
})();
