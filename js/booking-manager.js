// Booking Manager - Handles form submission and Supabase integration
//
// ═══════════════════════════════════════════════════════════════════
// 🚨  BACKEND PAYLOAD PROTECTION — READ BEFORE MODIFYING
// ═══════════════════════════════════════════════════════════════════
// The Admin Dashboard expects total_price in MOROCCAN DIRHAM (MAD).
// All front-end prices are displayed in EUR (or GBP/USD via the
// currency system), but the value INSERTED into the Supabase
// `bookings` table MUST always be MAD.
//
// The conversion happens at line ~276:
//   bookingData.total_price = total * 10
//   (1 EUR = 10 MAD — hardcoded, not user-configurable)
//
// Rules:
//  - NEVER remove or change the `* 10` multiplier.
//  - NEVER send EUR, USD, or GBP strings to the database.
//  - If you add a new pricing path, convert to MAD before assigning
//    to `bookingData.total_price`.
// ═══════════════════════════════════════════════════════════════════

const PRICE_LIST = {
    "Basic": 35,
    "Comfort": 49,
    "Luxe": 89,
    "Quad": 25,
    "Buggy": 80,
    "Camel": 10
};

console.log('Booking Manager Loaded');

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
        console.log('\n🚀 ========================================');
        console.log('📧 INSIDE sendBookingEmailNotification()');
        console.log('🚀 ========================================');
        console.log('📋 Received bookingData object:');
        console.log(bookingData);
        console.log('🔍 Specific fields:');
        console.log('   - phone_number:', bookingData.phone_number);
        console.log('   - total_price:', bookingData.total_price);
        console.log('🚀 ========================================\n');

        // Call the public API endpoint on the Dashboard (Next.js app)
        const DASHBOARD_API_URL = 'https://admin.marragafay.com/api/public/send-booking-email';

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
        };

        console.log('📤 PAYLOAD BEING SENT TO API:');
        console.log(payload);
        console.log('📤 JSON.stringify result:');
        console.log(JSON.stringify(payload, null, 2));
        console.log('\n');

        const response = await fetch(DASHBOARD_API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        const result = await response.json();

        if (!response.ok) {
            console.warn('⚠️ Dashboard API returned error:', result.error);
            return { success: false, error: result.error };
        }

        console.log('✅ Email notification sent via Dashboard API');
        return result;

    } catch (error) {
        console.error('❌ Failed to call Dashboard API:', error);
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
document.addEventListener('submit', async function (e) {
    // Check if the submitted element is our booking form (support both old and new IDs for GTM)
    if (e.target && (e.target.id === 'bookingForm' || e.target.id === 'booking-form' || e.target.id === 'booking-form-activity')) {
        e.preventDefault(); // Stop page reload
        console.log('Form submission detected via Delegation!');

        const form = e.target;

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

        // Calculate Price Logic with Dynamic Pricing support
        let pricePerPerson = 35; // Default fallback
        const titleToCheck = bookingData.package_title || '';

        // Dynamically extract the base price from the DOM (Ultimate Source of Truth)
        const formContainer = submitBtn ? submitBtn.closest('section') || document : document;
        const domPriceElement = formContainer.querySelector('.text-\\[32px\\].font-bold') || formContainer.querySelector('[data-price]');
        if (domPriceElement) {
            const extracted = parseInt(domPriceElement.textContent.replace(/\\D/g, ''));
            if (!isNaN(extracted) && extracted > 0) {
                pricePerPerson = extracted;
                console.log("💰 Extracted Base Price from DOM:", pricePerPerson);
            }
        }

        // Try to get dynamic price first if function exists
        if (typeof window.getDynamicPrice === 'function') {
            try {
                // Determine if it's a package or activity
                let itemType = 'package';
                let itemName = '';

                // Match against known packages/activities
                if (titleToCheck.includes('Basic') || titleToCheck.includes('Agafay Discovery') || titleToCheck.includes('Discovery')) {
                    itemName = 'Basic';
                } else if (titleToCheck.includes('Comfort') || titleToCheck.includes('Signature') || titleToCheck.includes('Marragafay Signature')) {
                    itemName = 'Comfort';
                } else if (titleToCheck.includes('Luxe') || titleToCheck.includes('Luxury')) {
                    itemName = 'Luxe';
                } else if (titleToCheck.includes('Quad')) {
                    itemType = 'activity';
                    itemName = 'Quad Biking';
                } else if (titleToCheck.includes('Buggy')) {
                    itemType = 'activity';
                    itemName = 'Buggy';
                } else if (titleToCheck.includes('Camel')) {
                    itemType = 'activity';
                    itemName = 'Camel Ride';
                }

                if (itemName) {
                    const apiPrice = await window.getDynamicPrice(itemType, itemName);
                    if (apiPrice) {
                        pricePerPerson = apiPrice;
                        console.log(`Dynamic API price fetched: ${pricePerPerson} for ${itemType} ${itemName}`);
                    }
                }
            } catch (error) {
                console.error('Error fetching dynamic API price:', error);
            }
        }

        // Fallback to static PRICE_LIST if DOM extraction and dynamic pricing both failed/defaulted
        if (pricePerPerson === 35 && !domPriceElement) {
            for (const key in PRICE_LIST) {
                if (titleToCheck.includes(key) ||
                    (key === 'Basic' && titleToCheck.includes('Discovery')) ||
                    (key === 'Comfort' && titleToCheck.includes('Signature')) ||
                    (key === 'Luxe' && titleToCheck.includes('Luxury'))) {
                    pricePerPerson = PRICE_LIST[key];
                    break;
                }
            }
        }

        // Calculate Total Price
        // Logic: Currently treating children as full price unless specific discount logic is added here.
        // User requested: "check if I have a discount logic, otherwise count them normally".

        let total = 0;

        // Future-proof: If we add child pricing later, we can do:
        // const childPrice = pricePerPerson * 0.5; // Example 50%
        // total = (adults * pricePerPerson) + (children * childPrice);

        // Current Logic: Standard per-person pricing for all
        // Dynamic Extra Activities (Future-proofing or implementation placeholder)
        let extraActivitiesPrice = 0;
        // Extract extras if they exist in the form
        // Example: formData.getAll('extras').forEach(...)

        let basePackageTotal = pricePerPerson * totalGuests;
        total = basePackageTotal + extraActivitiesPrice;

        console.log('💰 Base Package Total:', basePackageTotal, '€');
        console.log('💰 Extra Activities Total:', extraActivitiesPrice, '€');
        console.log('💰 Final Calculated Total:', total, '€');

        // 🚨 BACKEND PROTECTION: total_price MUST be in MAD for Supabase
        // The Admin Dashboard expects MAD values. 1 EUR = 10 MAD.
        // Do NOT change this multiplier — see header comment at top of file.
        bookingData.total_price = total * 10;

        // Safety audit: warn if price looks like it might NOT be in MAD
        if (bookingData.total_price < 50 || bookingData.total_price > 100000) {
            console.warn(
                '⚠️  AUDIT: total_price =', bookingData.total_price,
                '(MAD). If this looks wrong, verify the EUR→MAD conversion.'
            );
        }

        // ====================================================
        // 🐛 DEBUGGING: Log the complete payload
        // ====================================================
        console.log('\n========================================');
        console.log('📦 FINAL PAYLOAD BEFORE SENDING TO API');
        console.log('========================================');
        console.log('🔍 Captured Phone:', phoneNumber);
        console.log('🔍 Captured Price:', total);
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
            total_price: total,  // Show the actual variable being sent
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

        // Check for missing critical fields
        if (!bookingData.name || !bookingData.phone_number) {

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
            // 📧 SEND EMAIL NOTIFICATION (Background)
            // ============================================
            // Don't await this - let it run in background to not block UI
            sendBookingEmailNotification(bookingData)
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

            localStorage.setItem('recentBooking', JSON.stringify({ name: bookingData.name, date: bookingData.date, package_name: bookingData.package_title, guests_total: bookingData.guests, total_price: total, whatsapp: bookingData.phone_number }));
            // Forcibly trigger a JavaScript redirect to the new dedicated success page
            window.location.href = '../success.html';

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
