/**
 * Contact Form - Supabase & Automatic Resend Email Integration
 * Handles expedition inquiries, saves to Supabase and sends email notifications
 */

(function () {
    'use strict';

    const SUPABASE_URL = 'https://bgjohquanepghmlmdiyd.supabase.co';
    const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnam9ocXVhbmVwZ2htbG1kaXlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM2ODI3ODIsImV4cCI6MjA3OTI1ODc4Mn0.O1II649nWTZLgChPDOhITaBd3CJaALE2DZ-otzqG4N8';

    // Translations for UI Feedback
    const TRANSLATIONS = {
        en: {
            sending: 'Submitting inquiry...',
            successTitle: 'Inquiry Sent Successfully!',
            successMsg: 'Thank you! Your expedition inquiry has been received. Our concierge team will reach out to you shortly via email and WhatsApp.',
            errorTitle: 'Submission Error',
            errorMsg: 'Could not send your message. Please try again or reach out directly to hello@marragafay.com or +212 672-531624.',
            validationMsg: 'Please fill in your name, email, and phone number.'
        },
        fr: {
            sending: 'Envoi en cours...',
            successTitle: 'Demande envoyée avec succès !',
            successMsg: 'Merci ! Votre demande d\'expédition a bien été reçue. Notre équipe conciergerie vous contactera sous peu par email et WhatsApp.',
            errorTitle: 'Erreur d\'envoi',
            errorMsg: 'Impossible d\'envoyer votre message. Veuillez réessayer ou nous contacter à hello@marragafay.com ou +212 672-531624.',
            validationMsg: 'Veuillez renseigner votre nom, email et numéro de téléphone.'
        },
        es: {
            sending: 'Enviando consulta...',
            successTitle: '¡Consulta enviada con éxito!',
            successMsg: '¡Gracias! Su solicitud de expedición ha sido recibida. Nuestro equipo de conserjería se comunicará con usted en breve por correo electrónico y WhatsApp.',
            errorTitle: 'Error de envío',
            errorMsg: 'No se pudo enviar el mensaje. Inténtelo de nuevo o contáctenos en hello@marragafay.com o +212 672-531624.',
            validationMsg: 'Por favor ingrese su nombre, correo electrónico y número de teléfono.'
        },
        ar: {
            sending: 'جاري إرسال الطلب...',
            successTitle: 'تم إرسال الطلب بنجاح!',
            successMsg: 'شكراً لك! تم استلام طلب رحلتك الاستكشافية بنجاح. سيتواصل معك فريقنا قريباً عبر البريد الإلكتروني وواتساب.',
            errorTitle: 'حدث خطأ',
            errorMsg: 'تعذر إرسال طلبك. يرجى المحاولة مرة أخرى أو التواصل معنا عبر hello@marragafay.com أو +212 672-531624.',
            validationMsg: 'يرجى ملء الاسم والبريد الإلكتروني ورقم الهاتف.'
        }
    };

    function getLang() {
        const path = window.location.pathname;
        if (path.includes('/fr/')) return 'fr';
        if (path.includes('/es/')) return 'es';
        if (path.includes('/ar/')) return 'ar';
        return 'en';
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initContactForm);
    } else {
        initContactForm();
    }

    function initContactForm() {
        const form = document.getElementById('contact-form');
        if (!form) return;

        form.removeAttribute('onsubmit');
        form.addEventListener('submit', handleContactSubmit);
    }

    async function handleContactSubmit(e) {
        e.preventDefault();
        const form = e.target;
        const submitBtn = form.querySelector('button[type="submit"]');
        const lang = getLang();
        const t = TRANSLATIONS[lang] || TRANSLATIONS.en;

        const nameInput = document.getElementById('contact-name');
        const emailInput = document.getElementById('contact-email');
        const phoneInput = document.getElementById('contact-phone');
        const dateInput = document.getElementById('contact-date');
        const guestsInput = document.getElementById('contact-guests');
        const reqInput = document.getElementById('contact-requirements');

        const name = nameInput ? nameInput.value.trim() : '';
        const email = emailInput ? emailInput.value.trim() : '';
        const phone = phoneInput ? phoneInput.value.trim() : '';
        const date = dateInput ? dateInput.value.trim() : '';
        const guests = guestsInput ? guestsInput.value.trim() : '';
        const requirements = reqInput ? reqInput.value.trim() : '';

        // Validation
        if (!name || !email || !phone) {
            displayStatus(form, t.validationMsg, 'error');
            return;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            displayStatus(form, t.validationMsg, 'error');
            return;
        }

        // Disable button & show spinner
        const originalBtnHtml = submitBtn.innerHTML;
        submitBtn.disabled = true;
        submitBtn.style.opacity = '0.7';
        submitBtn.style.cursor = 'not-allowed';
        submitBtn.innerHTML = `
            <span class="inline-flex items-center justify-center gap-2">
                <svg class="animate-spin h-4 w-4 text-current" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" style="animation: spin 1s linear infinite;">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                ${t.sending}
            </span>
        `;

        const detailsList = [];
        if (phone) detailsList.push(`Phone / WhatsApp: ${phone}`);
        if (date) detailsList.push(`Anticipated Date: ${date}`);
        if (guests) detailsList.push(`Group Size: ${guests}`);
        if (requirements) {
            detailsList.push(`\nAdditional Requirements / Notes:\n${requirements}`);
        }

        const messageBody = detailsList.join('\n');
        const subject = `Expedition Inquiry - ${name}${guests ? ' (' + guests + ' guests)' : ''}${date ? ' [' + date + ']' : ''}`;

        const payload = {
            name: name,
            email: email,
            phone: phone,
            date: date,
            guests: guests,
            requirements: requirements,
            subject: subject,
            message: messageBody,
            status: 'unread'
        };

        let supabaseSaved = false;

        try {
            // 1. Save to Supabase (Database)
            try {
                const supabasePayload = {
                    name: payload.name,
                    email: payload.email,
                    subject: payload.subject,
                    message: payload.message,
                    status: 'unread'
                };

                if (typeof supabaseClient !== 'undefined' && supabaseClient && supabaseClient.from) {
                    const { data, error } = await supabaseClient.from('messages').insert([supabasePayload]);
                    if (!error) supabaseSaved = true;
                }

                if (!supabaseSaved) {
                    const response = await fetch(`${SUPABASE_URL}/rest/v1/messages`, {
                        method: 'POST',
                        headers: {
                            'apikey': SUPABASE_ANON_KEY,
                            'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
                            'Content-Type': 'application/json',
                            'Prefer': 'return=representation'
                        },
                        body: JSON.stringify(supabasePayload)
                    });
                    if (response.ok) supabaseSaved = true;
                }
            } catch (errDb) {
                console.warn('Supabase DB save error:', errDb);
            }

            // 2. Send Email via Vercel Serverless Function (/api/contact or /api/contact.js)
            try {
                let emailSent = false;
                try {
                    const res = await fetch('/api/contact', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                    if (res.ok) emailSent = true;
                } catch (e1) {}

                if (!emailSent) {
                    await fetch('/api/contact.js', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                }
            } catch (errApi) {
                console.log('API email notification attempted');
            }

            if (supabaseSaved) {
                displaySuccess(form, t.successMsg, t.successTitle);
                form.reset();
            } else {
                throw new Error('Could not save message to database');
            }

        } catch (err) {
            console.error('Contact form submission error:', err);
            displayStatus(form, t.errorMsg, 'error');
        } finally {
            submitBtn.disabled = false;
            submitBtn.style.opacity = '1';
            submitBtn.style.cursor = 'pointer';
            submitBtn.innerHTML = originalBtnHtml;
        }
    }

    function displaySuccess(form, message, title) {
        let msgBox = document.getElementById('contact-form-message');
        if (!msgBox) {
            msgBox = document.createElement('div');
            msgBox.id = 'contact-form-message';
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.parentNode.insertBefore(msgBox, submitBtn);
            } else {
                form.appendChild(msgBox);
            }
        }

        msgBox.className = 'w-full mb-6 p-6 text-sm transition-all duration-300 bg-[#10100E] text-[#F6F7EA] border border-[#F6F7EA]/20 rounded-xl shadow-lg';

        msgBox.innerHTML = `
            <div class="flex items-center gap-2 mb-2">
                <svg class="w-5 h-5 text-[#4CAF50]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
                <div class="font-bold uppercase tracking-wider text-xs text-white">${title}</div>
            </div>
            <p class="leading-relaxed text-[#F6F7EA]/90 m-0 text-[13px]">${message}</p>
        `;
        msgBox.style.display = 'block';
        msgBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

        setTimeout(() => {
            if (msgBox) {
                msgBox.style.opacity = '0';
                setTimeout(() => {
                    msgBox.style.display = 'none';
                    msgBox.style.opacity = '1';
                }, 400);
            }
        }, 10000);
    }

    function displayStatus(form, message, type) {
        let msgBox = document.getElementById('contact-form-message');
        if (!msgBox) {
            msgBox = document.createElement('div');
            msgBox.id = 'contact-form-message';
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.parentNode.insertBefore(msgBox, submitBtn);
            } else {
                form.appendChild(msgBox);
            }
        }

        msgBox.className = 'w-full mb-6 p-5 text-sm transition-all duration-300 bg-red-50 text-red-900 border border-red-200 rounded-xl';
        msgBox.innerHTML = `<div class="leading-relaxed font-medium">${message}</div>`;
        msgBox.style.display = 'block';
        msgBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
})();
