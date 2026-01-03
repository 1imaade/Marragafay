/* =========================================== */
/* BOOKING WIDGETS JAVASCRIPT */
/* Handles form validation, date selection, and redirections */
/* =========================================== */

(function ($) {
  'use strict';

  // Initialize when document is ready
  $(document).ready(function () {
    initMainSearchWidget();
    initQuickBookingWidget();
    initDatePickers();
    initGuestCounter();
    parseURLParameters();
  });

  /* ========================================= */
  /* GUEST COUNTER FUNCTIONALITY */
  /* ========================================= */

  function initGuestCounter() {
    const guestCounter = $('.guest-counter');
    const guestPopup = $('.guest-popup');

    if (guestCounter.length === 0) return;

    // Click handler for guest counter
    guestCounter.on('click', function (e) {
      e.stopPropagation();

      // Close any other open popups first
      $('.guest-popup.show').not(guestPopup).removeClass('show');

      // Toggle current popup
      guestPopup.toggleClass('show');

      // Toggle active state for arrow icon
      guestCounter.toggleClass('active');

      // Update counter button states
      updateCounterButtonStates();
    });

    // Click outside to close popup
    $(document).on('click', function (e) {
      if (!$(e.target).closest('.guest-counter').length && !$(e.target).closest('.guest-popup').length) {
        guestPopup.removeClass('show');
        guestCounter.removeClass('active');
      }
    });

    // Counter button handlers
    $('.counter-btn').on('click', function () {
      const target = $(this).data('target');
      const isPlus = $(this).hasClass('plus');
      const input = $(`#${target}Count`);

      let currentValue = parseInt(input.val()) || 0;
      const min = parseInt(input.attr('min')) || 0;
      const max = parseInt(input.attr('max')) || 50;

      if (isPlus && currentValue < max) {
        currentValue++;
      } else if (!isPlus && currentValue > min) {
        currentValue--;
      }

      input.val(currentValue);
      updateGuestDisplay();
      updateCounterButtonStates();
    });

    // Initialize guest display and counter states
    updateGuestDisplay();
    updateCounterButtonStates();
  }

  function updateGuestDisplay() {
    const adults = parseInt($('#adultsCount').val()) || 0;
    const children = parseInt($('#childrenCount').val()) || 0;
    const total = adults + children;

    let displayText = '';
    if (total === 0) {
      displayText = 'Select Guests';
    } else if (total === 1) {
      displayText = '1 Guest';
    } else {
      displayText = `${total} Guests`;
    }

    $('.guest-display').text(displayText);
  }

  function updateCounterButtonStates() {
    $('.counter-btn').each(function () {
      const target = $(this).data('target');
      const input = $(`#${target}Count`);
      const currentValue = parseInt(input.val()) || 0;
      const min = parseInt(input.attr('min')) || 0;
      const max = parseInt(input.attr('max')) || 50;

      // Disable minus button if at minimum
      $(this).siblings('.minus').prop('disabled', currentValue <= min);

      // Disable plus button if at maximum
      $(this).siblings('.plus').prop('disabled', currentValue >= max);
    });
  }

  /* ========================================= */
  /* MAIN SEARCH WIDGET (Home Page Hero) */
  /* ========================================= */

  function initMainSearchWidget() {
    const form = $('#mainSearchForm');

    if (form.length === 0) return;

    // Form submission handler
    form.on('submit', function (e) {
      e.preventDefault();

      // Validate form
      if (!validateMainSearchForm()) {
        return false;
      }

      // Get form values
      const activityType = $('#activityType').val();
      const bookingDate = $('#bookingDate').val();
      const numAdults = $('#adultsCount').val();
      const numChildren = $('#childrenCount').val();

      // Build URL parameters
      const params = new URLSearchParams();
      if (activityType) params.append('activity', activityType);
      if (bookingDate) params.append('date', bookingDate);
      if (numAdults) params.append('adults', numAdults);
      if (numChildren) params.append('children', numChildren);

      // Show loading state
      const submitBtn = form.find('.btn-search');
      submitBtn.addClass('loading');
      submitBtn.text('Searching...');

      // Redirect to packs page with parameters
      setTimeout(function () {
        window.location.href = 'packs.html?' + params.toString();
      }, 500);

      return false;
    });

    // Real-time validation
    $('#activityType, #bookingDate, #numAdults, #numChildren').on('change', function () {
      clearError($(this).closest('.form-group'));
    });
  }

  function validateMainSearchForm() {
    let isValid = true;

    // Validate activity type
    const activityType = $('#activityType');
    if (!activityType.val()) {
      showError(activityType.closest('.form-group'), 'Please select an activity type');
      isValid = false;
    }

    // Validate date
    const bookingDate = $('#bookingDate');
    if (!bookingDate.val()) {
      showError(bookingDate.closest('.form-group'), 'Please select a date');
      isValid = false;
    } else {
      // Check if date is not in the past
      const selectedDate = new Date(bookingDate.val());
      const today = new Date();
      today.setHours(0, 0, 0, 0);

      if (selectedDate < today) {
        showError(bookingDate.closest('.form-group'), 'Please select a future date');
        isValid = false;
      }
    }

    // Validate number of people (adults and children)
    const numAdults = $('#adultsCount');
    const numChildren = $('#childrenCount');

    if (!numAdults.val() || parseInt(numAdults.val()) < 1) {
      showError(numAdults.closest('.form-group'), 'Please enter at least 1 adult');
      isValid = false;
    } else if (parseInt(numAdults.val()) > 50) {
      showError(numAdults.closest('.form-group'), 'Maximum 50 adults per booking');
      isValid = false;
    }

    if (parseInt(numChildren.val()) > 50) {
      showError(numChildren.closest('.form-group'), 'Maximum 50 children per booking');
      isValid = false;
    }

    return isValid;
  }

  /* ========================================= */
  /* QUICK BOOKING WIDGET (Packs & Activities Pages) */
  /* ========================================= */

  function initQuickBookingWidget() {
    const form = $('#quickBookingForm');

    if (form.length === 0) return;

    // Form submission handler
    form.on('submit', function (e) {
      e.preventDefault();

      // Validate form
      if (!validateQuickBookingForm()) {
        return false;
      }

      // Get form values
      const bookingDate = $('#quickBookingDate').val();
      const numAdults = $('#quickNumAdults').val();
      const numChildren = $('#quickNumChildren').val();

      // Get current page parameters (if any)
      const urlParams = new URLSearchParams(window.location.search);
      const activityType = urlParams.get('activity');

      // Build URL parameters for checkout
      const params = new URLSearchParams();
      if (activityType) params.append('activity', activityType);
      if (bookingDate) params.append('date', bookingDate);
      if (numAdults) params.append('adults', numAdults);
      if (numChildren) params.append('children', numChildren);
      params.append('source', getCurrentPage());

      // Show loading state
      const submitBtn = form.find('.btn-book');
      submitBtn.addClass('loading');
      submitBtn.text('Processing...');

      // Redirect to checkout page with parameters
      setTimeout(function () {
        window.location.href = 'checkout.html?' + params.toString();
      }, 500);

      return false;
    });

    // Real-time validation
    $('#quickBookingDate, #quickNumAdults, #quickNumChildren').on('change', function () {
      clearError($(this).closest('.form-group'));
    });
  }

  function validateQuickBookingForm() {
    let isValid = true;

    // Validate date
    const bookingDate = $('#quickBookingDate');
    if (!bookingDate.val()) {
      showError(bookingDate.closest('.form-group'), 'Please select a date');
      isValid = false;
    } else {
      // Check if date is not in the past
      const selectedDate = new Date(bookingDate.val());
      const today = new Date();
      today.setHours(0, 0, 0, 0);

      if (selectedDate < today) {
        showError(bookingDate.closest('.form-group'), 'Please select a future date');
        isValid = false;
      }
    }

    // Validate number of people (adults and children)
    const numAdults = $('#quickNumAdults');
    const numChildren = $('#quickNumChildren');

    if (!numAdults.val() || parseInt(numAdults.val()) < 1) {
      showError(numAdults.closest('.form-group'), 'Please enter at least 1 adult');
      isValid = false;
    } else if (parseInt(numAdults.val()) > 50) {
      showError(numAdults.closest('.form-group'), 'Maximum 50 adults per booking');
      isValid = false;
    }

    if (parseInt(numChildren.val()) > 50) {
      showError(numChildren.closest('.form-group'), 'Maximum 50 children per booking');
      isValid = false;
    }

    return isValid;
  }

  /* ========================================= */
  /* DATE PICKER INITIALIZATION */
  /* ========================================= */

  function initDatePickers() {
    // Get today's date in YYYY-MM-DD format
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    const todayDate = `${year}-${month}-${day}`;

    // Initialize datepicker for main search widget
    if ($('#bookingDate').length > 0) {
      $('#bookingDate').attr('min', todayDate);
      $('#bookingDate').datepicker({
        format: 'yyyy-mm-dd',
        startDate: new Date(),
        autoclose: true,
        todayHighlight: true,
        orientation: 'bottom auto'
      });
    }

    // Initialize datepicker for quick booking widget
    if ($('#quickBookingDate').length > 0) {
      $('#quickBookingDate').attr('min', todayDate);
      $('#quickBookingDate').datepicker({
        format: 'yyyy-mm-dd',
        startDate: new Date(),
        autoclose: true,
        todayHighlight: true,
        orientation: 'bottom auto'
      });
    }

    // Set min date for ALL date inputs on the page (including modal forms)
    $('input[type="date"]').each(function () {
      $(this).attr('min', todayDate);
    });

    console.log(`Date validation applied: min date set to ${todayDate}`);
  }

  /* ========================================= */
  /* URL PARAMETER PARSING */
  /* ========================================= */

  function parseURLParameters() {
    const urlParams = new URLSearchParams(window.location.search);

    // Parse parameters for packs.html page
    if (window.location.pathname.includes('packs.html')) {
      const activity = urlParams.get('activity');
      const date = urlParams.get('date');
      const adults = urlParams.get('adults');
      const children = urlParams.get('children');

      // Display search parameters if present
      if (activity || date || adults || children) {
        displaySearchResults(activity, date, adults, children);
      }

      // Pre-fill quick booking form if parameters exist
      if (date) $('#quickBookingDate').val(date);
      if (adults) $('#quickNumAdults').val(adults);
      if (children) $('#quickNumChildren').val(children);
    }

    // Parse parameters for checkout.html page
    if (window.location.pathname.includes('checkout.html')) {
      const activity = urlParams.get('activity');
      const date = urlParams.get('date');
      const adults = urlParams.get('adults');
      const children = urlParams.get('children');
      const source = urlParams.get('source');

      // Display booking summary
      displayBookingSummary(activity, date, adults, children, source);
    }
  }

  function displaySearchResults(activity, date, adults, children) {
    // Create a search summary banner
    const summaryHTML = `
      <div class="search-summary" style="background: linear-gradient(45deg, #d4af37, #bc6c25); color: white; padding: 20px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <h4 style="margin: 0 0 10px 0; font-size: 1.3rem; font-weight: 600;">Search Results</h4>
        <div style="display: flex; gap: 20px; flex-wrap: wrap; font-size: 0.95rem;">
          ${activity ? `<div><strong>Activity:</strong> ${formatActivityName(activity)}</div>` : ''}
          ${date ? `<div><strong>Date:</strong> ${formatDate(date)}</div>` : ''}
          ${adults ? `<div><strong>Adults:</strong> ${adults}</div>` : ''}
          ${children ? `<div><strong>Children:</strong> ${children}</div>` : ''}
        </div>
      </div>
    `;

    // Insert before the first section
    $('.ftco-section').first().prepend(summaryHTML);
  }

  function displayBookingSummary(activity, date, adults, children, source) {
    // This will be populated in the checkout page
    if ($('#bookingSummary').length > 0) {
      const summaryHTML = `
        <div class="booking-details">
          <h4>Booking Details</h4>
          ${activity ? `<p><strong>Activity:</strong> ${formatActivityName(activity)}</p>` : ''}
          ${date ? `<p><strong>Date:</strong> ${formatDate(date)}</p>` : ''}
          ${adults ? `<p><strong>Adults:</strong> ${adults}</p>` : ''}
          ${children ? `<p><strong>Children:</strong> ${children}</p>` : ''}
          ${source ? `<p><strong>Booked from:</strong> ${source}</p>` : ''}
        </div>
      `;
      $('#bookingSummary').html(summaryHTML);
    }
  }

  /* ========================================= */
  /* UTILITY FUNCTIONS */
  /* ========================================= */

  function showError(formGroup, message) {
    formGroup.addClass('has-error');
    let errorElement = formGroup.find('.form-error');

    if (errorElement.length === 0) {
      errorElement = $('<div class="form-error"></div>');
      formGroup.append(errorElement);
    }

    errorElement.text(message).show();
  }

  function clearError(formGroup) {
    formGroup.removeClass('has-error');
    formGroup.find('.form-error').hide();
  }

  function getCurrentPage() {
    const path = window.location.pathname;
    if (path.includes('packs.html')) return 'Packs Page';
    if (path.includes('activities.html')) return 'Activities Page';
    return 'Unknown';
  }

  function formatActivityName(activity) {
    const activityNames = {
      'desert-tour': 'Desert Tour (Full Day)',
      'overnight-camp': 'Overnight Camp',
      'quad-biking': 'Quad Biking Only'
    };
    return activityNames[activity] || activity;
  }

  function formatDate(dateString) {
    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
  }

  /* ========================================= */
  /* NUMBER INPUT RESTRICTIONS */
  /* ========================================= */

  // Prevent negative numbers and enforce max values
  $('input[type="number"]').on('input', function () {
    const value = parseInt($(this).val());
    const min = parseInt($(this).attr('min')) || 1;
    const max = parseInt($(this).attr('max')) || 50;

    if (value < min) {
      $(this).val(min);
    } else if (value > max) {
      $(this).val(max);
    }
  });

})(jQuery);
