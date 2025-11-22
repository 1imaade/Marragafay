/**
 * Universal Booking Form Handler
 * Handles all booking form submissions and sends data to Supabase
 */

(function () {
    'use strict';

    /**
     * Initialize booking form when DOM is ready
     */
    function initBookingForm() {
        const form = document.getElementById('bookingForm');
        if (!form) {
            console.warn('Booking form not found on this page');
            return;
        }

        form.addEventListener('submit', handleBookingSubmit);
        console.log('✅ Booking form handler initialized');
    }

    /**
     * Handle booking form submission
     */
    async function handleBookingSubmit(e) {
        e.preventDefault();

        const form = e.target;
        const formData = new FormData(form);
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.textContent;

        // Extract and validate form data
        const bookingData = {
            customer_name: formData.get('name'),
            customer_email: formData.get('email'),
            phone: formData.get('countryCode') + formData.get('phone'),
            package_title: formData.get('package'),
            booking_date: formData.get('date'),
            guests_count: parseInt(formData.get('guests')) || 2,
            status: 'pending',
            created_at: new Date().toISOString()
        };

        // Validation
        if (!bookingData.customer_name || !bookingData.customer_email || !bookingData.phone || !bookingData.package_title || !bookingData.booking_date) {
            showMessage('error', 'Please fill in all required fields.');
            return;
        }

        // Show loading state
        setButtonLoading(submitBtn, true);

        try {
            // Insert booking into Supabase
            const { data, error } = await supabaseClient
                .from('bookings')
                .insert([bookingData])
                .select();

            if (error) {
                throw error;
            }

            console.log('✅ Booking created:', data[0]);

            // Show success message
            showSuccessMessage(bookingData);

            // Reset form
            form.reset();

        } catch (error) {
            console.error('❌ Booking error:', error);
            showMessage('error', 'Sorry, there was an error processing your booking. Please try again or contact us directly via WhatsApp.');
        } finally {
            setButtonLoading(submitBtn, false, originalBtnText);
        }
    }

    /**
     * Set button loading state
     */
    function setButtonLoading(button, isLoading, originalText = '') {
        if (isLoading) {
            button.dataset.originalText = button.textContent;
            button.textContent = 'Processing...';
            button.disabled = true;
            button.style.opacity = '0.6';
            button.style.cursor = 'not-allowed';
        } else {
            button.textContent = originalText || button.dataset.originalText || 'Reserve Now';
            button.disabled = false;
            button.style.opacity = '1';
            button.style.cursor = 'pointer';
        }
    }

    /**
     * Show success message
     */
    function showSuccessMessage(bookingData) {
        const message = `✅ Thank you for your booking!

📦 Package: ${bookingData.package_title}
📅 Date: ${bookingData.booking_date}
👥 Guests: ${bookingData.guests_count}

We will contact you shortly at ${bookingData.phone} to confirm your reservation.

You will also receive a confirmation email at ${bookingData.customer_email}.`;

        alert(message);
    }

    /**
     * Show generic message
     */
    function showMessage(type, message) {
        const icon = type === 'error' ? '❌' : 'ℹ️';
        alert(`${icon} ${message}`);
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initBookingForm);
    } else {
        initBookingForm();
    }

})();
