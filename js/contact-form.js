/**
 * Contact Form - Supabase Integration
 * Handles contact form submission and saves messages to Supabase
 */

(function () {
    'use strict';

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    function init() {
        const contactForm = document.getElementById('contact-form');

        if (!contactForm) {
            console.warn('Contact form not found on this page');
            return;
        }

        console.log('Contact form initialized');

        // Add submit event listener
        contactForm.addEventListener('submit', handleFormSubmit);
    }

    async function handleFormSubmit(e) {
        e.preventDefault();

        // Get form elements
        const nameInput = document.getElementById('contact-name');
        const emailInput = document.getElementById('contact-email');
        const subjectInput = document.getElementById('contact-subject');
        const messageInput = document.getElementById('contact-message');
        const messageEl = document.getElementById('contact-form-message');
        const submitBtn = contactForm.querySelector('button[type="submit"]');

        // Get values
        const name = nameInput.value.trim();
        const email = emailInput.value.trim();
        const subject = subjectInput.value.trim();
        const message = messageInput.value.trim();

        // Validate fields
        if (!name || !email || !subject || !message) {
            showMessage(messageEl, 'Please fill in all fields.', 'error');
            return;
        }

        // Basic email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            showMessage(messageEl, 'Please enter a valid email address.', 'error');
            return;
        }

        // Disable submit button
        const originalText = submitBtn.textContent;
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';

        try {
            // Check if Supabase client exists
            if (typeof supabaseClient === 'undefined') {
                throw new Error('Supabase client not initialized. Please check your configuration.');
            }

            console.log('Submitting contact form to Supabase...');

            // Insert message into Supabase
            const { data, error } = await supabaseClient
                .from('messages')
                .insert([{
                    name: name,
                    email: email,
                    subject: subject,
                    message: message,
                    created_at: new Date().toISOString()
                }]);

            if (error) {
                console.error('Supabase error:', error);
                throw error;
            }

            console.log('Message submitted successfully:', data);

            // Show success message
            showMessage(messageEl, 'Thank you! Your message has been sent successfully. We\'ll get back to you soon!', 'success');

            // Clear form
            contactForm.reset();

        } catch (error) {
            console.error('Error submitting contact form:', error);
            showMessage(messageEl, 'Failed to send message. Please try again or contact us directly at marragafay@gmail.com', 'error');
        } finally {
            // Re-enable submit button
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
        }
    }

    function showMessage(el, message, type) {
        if (!el) return;

        el.textContent = message;
        el.style.display = 'block';

        if (type === 'success') {
            el.style.background = '#d4edda';
            el.style.color = '#155724';
            el.style.border = '1px solid #c3e6cb';
        } else if (type === 'error') {
            el.style.background = '#f8d7da';
            el.style.color = '#721c24';
            el.style.border = '1px solid #f5c6cb';
        }

        // Auto-hide success message after 5 seconds
        if (type === 'success') {
            setTimeout(() => {
                el.style.display = 'none';
            }, 5000);
        }
    }

})();
