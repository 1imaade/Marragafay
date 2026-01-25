// Booking Manager - Handles form submission and Supabase integration

const PRICE_LIST = {
    "Basic": 400,
    "Comfort": 600,
    "Luxe": 1200,
    "Quad": 350,
    "Buggy": 850,
    "Camel": 200
};

console.log('Booking Manager Loaded');

/**
 * Send Booking Email Notification
 * 
 * Calls the PUBLIC API endpoint on the Dashboard (Next.js app) to send email notifications.
 * The Dashboard app runs separately on localhost:3000 and provides a CORS-enabled endpoint
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
        // TODO: In production, change to your actual Dashboard URL (e.g., https://dashboard.marragafay.com)
        const DASHBOARD_API_URL = 'http://localhost:3000/api/public/send-booking-email';

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
    if (e.target && (e.target.id === 'bookingForm' || e.target.id === 'booking-form')) {
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
            email: formData.get('email'),
            phone_number: phoneNumber,
            date: formData.get('booking_date') || formData.get('date'), // DB Column: date
            guests: totalGuests,
            adults: adults,
            children: children,
            package_title: formData.get('package_title') || document.title,
            notes: notes
        };

        // Calculate Price Logic with Dynamic Pricing support
        let pricePerPerson = 400; // Default fallback
        const titleToCheck = bookingData.package_title || '';

        // Try to get dynamic price first if function exists
        if (typeof window.getDynamicPrice === 'function') {
            try {
                // Determine if it's a package or activity
                let itemType = 'package';
                let itemName = '';

                // Match against known packages/activities
                if (titleToCheck.includes('Basic')) {
                    itemName = 'Basic';
                } else if (titleToCheck.includes('Comfort')) {
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
                    pricePerPerson = await window.getDynamicPrice(itemType, itemName);
                    console.log(`Dynamic price fetched: ${pricePerPerson} for ${itemType} ${itemName}`);
                }
            } catch (error) {
                console.error('Error fetching dynamic price:', error);
                // Fall back to PRICE_LIST below
            }
        }

        // Fallback to static PRICE_LIST if dynamic pricing didn't work
        if (pricePerPerson === 400) {
            for (const key in PRICE_LIST) {
                if (titleToCheck.includes(key)) {
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
        total = pricePerPerson * totalGuests;

        // ====================================================
        // 💰 FIX 4: TOTAL PRICE FROM DOM (Primary Source)
        // ====================================================
        // The price is displayed in the UI (NOT a form input), e.g., <h2>549 DH</h2>
        // Try to extract from DOM first, then fall back to calculated value
        const totalPriceElement = document.getElementById('total-price') ||
            document.getElementById('totalPrice') ||
            document.querySelector('.total-price') ||
            document.querySelector('.price-display') ||
            document.querySelector('[data-total-price]') ||
            document.querySelector('h2.price') ||
            document.querySelector('h3.price') ||
            document.querySelector('span.price');

        if (totalPriceElement) {
            // Extract text content (e.g., "549 DH" or "1200.00 DH")
            const priceText = totalPriceElement.innerText || totalPriceElement.textContent || '';
            console.log('💰 Found price element! Raw text:', priceText);

            // Clean and extract numeric value
            const numericMatch = priceText.match(/[\d,]+\.?\d*/);
            if (numericMatch) {
                const extractedPrice = parseFloat(numericMatch[0].replace(/,/g, ''));
                if (!isNaN(extractedPrice) && extractedPrice > 0) {
                    total = extractedPrice;
                    console.log('💰 ✅ Total Price extracted from DOM:', total, 'DH');
                } else {
                    console.warn('⚠️ Parsed price is invalid:', extractedPrice);
                }
            } else {
                console.warn('⚠️ Could not parse numeric value from:', priceText);
            }
        } else {
            console.log('💰 No price element found in DOM, using calculated value:', total);
        }

        bookingData.total_price = total;

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
        if (!bookingData.email || !bookingData.name) {

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

        try {
            // Insert into Supabase
            const { data, error } = await supabaseClient
                .from('bookings')
                .insert([bookingData]);

            if (error) throw error;

            // SUCCESS - Display Booking Details Modal
            console.log('Booking successful:', data);

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

            // Prepare booking data for modal
            const confirmedBooking = {
                id: data?.[0]?.id || Math.floor(Math.random() * 10000), // Use returned ID or generate one
                name: bookingData.name,
                email: bookingData.email,
                phone_number: bookingData.phone_number,
                date: bookingData.date,
                guests: bookingData.guests,
                package_title: bookingData.package_title,
                total_price: bookingData.total_price,
                notes: bookingData.notes,
                status: 'confirmed'
            };

            // Show the minimal booking details modal
            if (typeof window.openBookingDetailsModal === 'function') {
                window.openBookingDetailsModal(confirmedBooking);
            } else {
                // Fallback to SweetAlert if modal not loaded
                if (window.Swal) {
                    Swal.fire({
                        title: 'Booking Confirmed',
                        html: 'We have received your request.<br>We will contact you on WhatsApp shortly.',
                        icon: 'success',
                        iconColor: '#C19B76',
                        confirmButtonText: 'Perfect',
                        buttonsStyling: false,
                        customClass: {
                            popup: 'swal2-popup',
                            title: 'swal2-title',
                            htmlContainer: 'swal2-html-container',
                            confirmButton: 'swal2-confirm',
                            icon: 'swal2-icon swal2-success'
                        }
                    });
                } else {
                    alert('Booking Confirmed! We\'ll contact you on WhatsApp shortly.');
                }
            }

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
