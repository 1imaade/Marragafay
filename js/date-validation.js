/**
 * Date Validation Script
 * Dynamically sets the minimum date to today's date for all date inputs
 * Ensures users cannot select past dates
 */

(function () {
    'use strict';

    // Function to get today's date in YYYY-MM-DD format
    function getTodayDate() {
        const today = new Date();
        const year = today.getFullYear();
        const month = String(today.getMonth() + 1).padStart(2, '0');
        const day = String(today.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    }

    // Function to set minimum date for all date inputs
    function setMinDateForAllInputs() {
        const todayDate = getTodayDate();
        const dateInputs = document.querySelectorAll('input[type="date"]');

        dateInputs.forEach(function (input) {
            input.setAttribute('min', todayDate);
            console.log(`Set min date for ${input.id || 'date input'}: ${todayDate}`);
        });
    }

    // Run when DOM is fully loaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setMinDateForAllInputs);
    } else {
        // DOM is already loaded
        setMinDateForAllInputs();
    }

    // Also run after a short delay to catch any dynamically added inputs
    setTimeout(setMinDateForAllInputs, 500);

    console.log('Date validation script loaded successfully');
})();
