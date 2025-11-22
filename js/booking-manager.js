// Booking Manager - Handles form submission and Supabase integration
console.log('Booking Manager Loaded');

// Use Event Delegation to handle dynamically rendered forms
document.addEventListener('submit', async function (e) {
    // Check if the submitted element is our booking form
    if (e.target && e.target.id === 'bookingForm') {
        e.preventDefault(); // Stop page reload
        console.log('Form submission detected via Delegation!');

        const form = e.target;
        const formData = new FormData(form);

        // Extract values safely using FormData - with fallbacks for different field names
        const bookingData = {
            customer_name: formData.get('full_name') || formData.get('name'), // Try both common names
            customer_email: formData.get('email'),
            phone: formData.get('phone'),
            booking_date: formData.get('booking_date') || formData.get('date'),
            guests_count: parseInt(formData.get('guests') || '1'),
            package_title: formData.get('package_title') || document.title, // Fallback to page title if hidden input is missing
            notes: formData.get('message') || ''
        };

        // Debug log to see what we captured
        console.log('Captured Data:', bookingData);

        // Check for missing critical fields
        if (!bookingData.customer_email || !bookingData.customer_name) {
            alert('Please fill in all required fields.');
            return;
        }

        try {
            // Insert into Supabase
            const { data, error } = await supabaseClient
                .from('bookings')
                .insert([bookingData]);

            if (error) throw error;

            // Success
            console.log('Booking successful:', data);
            alert('Booking Confirmed!');
            form.reset();

        } catch (error) {
            // Error handling
            console.error('Booking error:', error);
            alert('Error: ' + error.message);
        }
    }
});
