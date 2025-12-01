// Booking Manager - Handles form submission and Supabase integration

const PRICE_LIST = {
    "Basic": 400,
    "Comfort": 550,
    "Luxe": 800,
    "Quad": 350,
    "Buggy": 600,
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

        // Calculate Price Logic
        let pricePerPerson = 400; // Default fallback
        const titleToCheck = bookingData.package_title || '';

        for (const key in PRICE_LIST) {
            if (titleToCheck.includes(key)) {
                pricePerPerson = PRICE_LIST[key];
                break;
            }
        }

        const total = pricePerPerson * bookingData.guests_count;
        bookingData.total_price = total;


        // Debug log to see what we captured
        console.log('Captured Data:', bookingData);

        // Check for missing critical fields
        if (!bookingData.customer_email || !bookingData.customer_name) {
            // Beautiful error popup for validation
            if (window.Swal) {
                Swal.fire({
                    title: 'Missing Information',
                    text: 'Please fill in all required fields (Name and Email).',
                    icon: 'warning',
                    confirmButtonText: 'OK',
                    confirmButtonColor: '#C19B76',
                    background: '#ffffff'
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

            // Success - Beautiful confirmation popup
            console.log('Booking successful:', data);

            if (window.Swal) {
                Swal.fire({
                    title: 'Reservation Received!',
                    text: 'Thank you! We have received your booking. We will contact you shortly on WhatsApp to confirm the details.',
                    icon: 'success', // Green checkmark
                    confirmButtonText: 'Great!',
                    confirmButtonColor: '#C19B76', // Brand gold/brown color
                    background: '#ffffff',
                    customClass: {
                        popup: 'animated fadeInDown'
                    }
                });
            } else {
                alert('Booking Confirmed!');
            }

            form.reset();

        } catch (error) {
            // Error handling - Beautiful error popup
            console.error('Booking error:', error);

            if (window.Swal) {
                Swal.fire({
                    title: 'Booking Failed',
                    text: 'Error: ' + error.message,
                    icon: 'error',
                    confirmButtonText: 'Try Again',
                    confirmButtonColor: '#C19B76',
                    background: '#ffffff'
                });
            } else {
                alert('Error: ' + error.message);
            }
        }
    }
});
