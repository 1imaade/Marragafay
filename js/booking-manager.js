// Booking Manager - Handles form submission and Supabase integration
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('bookingForm');

    if (!form) {
        console.warn('Booking form not found on this page');
        return;
    }

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        // Collect form data
        const fullName = form.querySelector('[name="full_name"]').value;
        const email = form.querySelector('[name="email"]').value;
        const phone = form.querySelector('[name="phone"]').value;
        const bookingDate = form.querySelector('[name="booking_date"]').value;
        const guests = form.querySelector('[name="guests"]').value;
        const packageTitle = form.querySelector('[name="package_title"]').value;

        // Prepare booking data - Map form fields to correct DB column names
        const bookingData = {
            customer_name: fullName,      // Form: full_name -> DB: customer_name
            customer_email: email,         // Form: email -> DB: customer_email
            phone: phone,                  // Form: phone -> DB: phone (same)
            booking_date: bookingDate,     // Form: booking_date -> DB: booking_date (same)
            guests_count: guests,          // Form: guests -> DB: guests_count
            package_title: packageTitle    // Form: package_title -> DB: package_title (same)
        };

        try {
            // Insert into Supabase
            const { data, error } = await supabaseClient
                .from('bookings')
                .insert([bookingData]);

            if (error) throw error;

            // Success
            alert('Booking Confirmed!');
            form.reset();

        } catch (error) {
            // Error handling
            alert('Error: ' + error.message);
            console.error('Booking error:', error);
        }
    });
});
