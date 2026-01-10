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
    // Check if the submitted element is our booking form
    if (e.target && e.target.id === 'bookingForm') {
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

        // Extract values safely using FormData
        const adults = parseInt(formData.get('adults') || formData.get('guests') || '1');
        const children = parseInt(formData.get('children') || '0');
        const totalGuests = adults + children;

        const bookingData = {
            name: formData.get('full_name') || formData.get('name'),
            email: formData.get('email'),
            phone_number: formData.get('phone'),
            date: formData.get('booking_date') || formData.get('date'), // DB Column: date
            guests: totalGuests,
            adults: adults,
            children: children,
            package_title: formData.get('package_title') || document.title,
            notes: formData.get('message') || ''
        };

        // Append breakdown to notes just in case
        if (children > 0) {
            bookingData.notes += ` (Adults: ${adults}, Children: ${children})`;
        }

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

        bookingData.total_price = total;


        // Debug log to see what we captured
        console.log('Captured Data:', bookingData);

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

            // SUCCESS - 5-Star Luxury Hotel Confirmation
            console.log('Booking successful:', data);

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
                    },
                    allowOutsideClick: true,
                    allowEscapeKey: true,
                    showCloseButton: false,
                    focusConfirm: true
                }).then(() => {
                    // Fresh state for next booking
                    window.location.reload();
                });
            } else {
                alert('Booking Confirmed! We\'ll contact you on WhatsApp shortly.');
                window.location.reload();
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
