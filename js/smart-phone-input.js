/**
 * Smart Phone & WhatsApp Auto-Country Code Handler for Marragafay
 * Automatically detects visitor's country and ensures international prefix is ALWAYS present
 * Zero design changes - preserves exact visual appearance and compact pill layouts
 */

(function () {
    'use strict';

    // Map common browser locales & timezones to international dialing codes
    const COUNTRY_CALLING_CODES = {
        'fr': '+33',  // France
        'gb': '+44',  // UK
        'uk': '+44',  // UK
        'us': '+1',   // USA
        'ca': '+1',   // Canada
        'es': '+34',  // Spain
        'ma': '+212', // Morocco
        'de': '+49',  // Germany
        'it': '+39',  // Italy
        'be': '+32',  // Belgium
        'ch': '+41',  // Switzerland
        'nl': '+31',  // Netherlands
        'pt': '+351', // Portugal
        'ae': '+971', // UAE
        'sa': '+966', // Saudi Arabia
        'qa': '+974', // Qatar
        'kw': '+965', // Kuwait
        'au': '+61',  // Australia
        'ie': '+353', // Ireland
        'se': '+46',  // Sweden
        'no': '+47',  // Norway
        'dk': '+45',  // Denmark
        'pl': '+48'   // Poland
    };

    let detectedPrefix = '+212'; // Default fallback (Morocco)

    // Detect visitor country prefix from browser timezone and locale
    function detectVisitorPrefix() {
        try {
            const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
            const userLang = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
            const langCode = userLang.split('-')[0];
            const countryCode = (userLang.split('-')[1] || '').toLowerCase();

            // 1. Timezone detection (very accurate for travel tourists)
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

            // 2. Language region detection
            if (countryCode && COUNTRY_CALLING_CODES[countryCode]) {
                return COUNTRY_CALLING_CODES[countryCode];
            }
            if (COUNTRY_CALLING_CODES[langCode]) {
                return COUNTRY_CALLING_CODES[langCode];
            }
        } catch (e) {
            console.warn('Smart phone detection fallback:', e);
        }
        return '+212';
    }

    detectedPrefix = detectVisitorPrefix();

    function formatPhoneNumber(rawNumber) {
        if (!rawNumber) return '';
        let cleaned = rawNumber.trim().replace(/[\s\-\(\)]/g, '');

        // If user already typed + or 00, format cleanly
        if (cleaned.startsWith('+')) {
            return cleaned;
        }
        if (cleaned.startsWith('00')) {
            return '+' + cleaned.substring(2);
        }

        // If number starts with 0 (e.g. 0612345678), strip the leading 0 and attach detected country code
        if (cleaned.startsWith('0')) {
            return detectedPrefix + ' ' + cleaned.substring(1);
        }

        // If user typed 9 digits without leading 0 (e.g. 612345678), attach country prefix
        if (/^\d{8,11}$/.test(cleaned)) {
            return detectedPrefix + ' ' + cleaned;
        }

        // Fallback: prepend detected country prefix
        return detectedPrefix + ' ' + cleaned;
    }

    // Attach listeners to all phone inputs
    function initSmartPhoneInputs() {
        const phoneInputs = document.querySelectorAll('input[type="tel"], input[name="phone"], input[name="phone_number"]');

        phoneInputs.forEach(input => {
            if (input.dataset.smartPhoneInit) return;
            input.dataset.smartPhoneInit = 'true';

            // Update placeholder dynamically based on detected country (e.g. +33 600... or +44 700...)
            if (detectedPrefix && input.placeholder && input.placeholder.includes('+212')) {
                input.placeholder = detectedPrefix + ' 600...';
            }

            // On focus: If empty, pre-fill the detected country code
            input.addEventListener('focus', function () {
                if (!this.value.trim()) {
                    this.value = detectedPrefix + ' ';
                }
            });

            // On blur: If user only left "+33 " or "+212 ", clear it
            input.addEventListener('blur', function () {
                if (this.value.trim() === detectedPrefix || this.value.trim() === '+') {
                    this.value = '';
                } else if (this.value.trim()) {
                    this.value = formatPhoneNumber(this.value);
                }
            });

            // On input: Prevent accidental double pluses
            input.addEventListener('input', function () {
                if (this.value.startsWith('++')) {
                    this.value = '+' + this.value.replace(/^\++/, '');
                }
            });
        });
    }

    // Global helper exposed for booking-manager.js
    window.formatInternationalPhone = formatPhoneNumber;
    window.detectedVisitorCountryCode = detectedPrefix;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSmartPhoneInputs);
    } else {
        initSmartPhoneInputs();
    }

    // Re-run whenever modals or dynamic elements appear
    document.addEventListener('click', () => setTimeout(initSmartPhoneInputs, 300));
})();
