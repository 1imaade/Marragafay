/* =========================================== */
/* BOOKING DETAILS MODAL - EXACT IMAGE MATCH */
/* =========================================== */

(function () {
  'use strict';

  function createModalHTML() {
    if (document.getElementById('bookingDetailsModal')) return;

    const modalHTML = `
      <div class="booking-modal-backdrop" id="bookingModalBackdrop"></div>
      <div class="booking-modal" id="bookingDetailsModal">
        <div class="booking-modal-header">
          <div class="booking-modal-title-section">
            <h2 class="booking-modal-title" id="bookingModalTitle">Booking #12345</h2>
            <span class="booking-status-badge confirmed" id="bookingStatusBadge">Confirmed</span>
          </div>
          <button class="booking-modal-close" id="bookingModalClose" aria-label="Close">×</button>
        </div>
        <div class="booking-modal-body">
          <div class="booking-details-grid" id="bookingDetailsGrid"></div>
        </div>
        <div class="booking-modal-footer">
          <button class="booking-modal-btn booking-modal-btn-ghost" id="bookingModalCloseBtn">Close</button>
          <button class="booking-modal-btn booking-modal-btn-primary" id="bookingModalActionBtn">Print Receipt</button>
        </div>
      </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHTML);
  }

  function formatDate(dateString) {
    if (!dateString) return 'Not specified';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  }

  function formatPrice(price) {
    const num = parseFloat(price) || 0;
    return num.toLocaleString('en-US');
  }

  window.openBookingDetailsModal = function (bookingData) {
    createModalHTML();

    const modal = document.getElementById('bookingDetailsModal');
    const backdrop = document.getElementById('bookingModalBackdrop');
    const grid = document.getElementById('bookingDetailsGrid');
    const title = document.getElementById('bookingModalTitle');
    const statusBadge = document.getElementById('bookingStatusBadge');

    // Set title exactly like image
    title.textContent = bookingData.id ? `Booking #${bookingData.id}` : 'Booking #12345';

    // Set status
    const status = bookingData.status || 'confirmed';
    statusBadge.textContent = status.charAt(0).toUpperCase() + status.slice(1);
    statusBadge.className = `booking-status-badge ${status.toLowerCase()}`;

    // Get values
    const guestName = bookingData.name || bookingData.guest_name || 'John Smith';
    const email = bookingData.email || 'john@example.com';
    const phone = bookingData.phone_number || bookingData.phone || '+212 600 123 456';
    const checkInDate = formatDate(bookingData.date || bookingData.booking_date);
    const guests = parseInt(bookingData.guests || bookingData.total_guests || 4);
    const guestsText = guests === 1 ? '1 Guest' : `${guests} Guests`;
    const packageName = bookingData.package_title || 'Luxury Desert Package';
    const price = formatPrice(bookingData.total_price || bookingData.price || 1200);

    // Build grid - EXACTLY matching image layout
    grid.innerHTML = `
      <div class="booking-detail-item">
        <p class="booking-detail-label">GUEST NAME</p>
        <p class="booking-detail-value">${guestName}</p>
      </div>
      <div class="booking-detail-item">
        <p class="booking-detail-label">EMAIL ADDRESS</p>
        <p class="booking-detail-value">${email}</p>
      </div>
      <div class="booking-detail-item">
        <p class="booking-detail-label">PHONE NUMBER</p>
        <p class="booking-detail-value">${phone}</p>
      </div>
      <div class="booking-detail-item">
        <p class="booking-detail-label">CHECK-IN DATE</p>
        <p class="booking-detail-value">${checkInDate}</p>
      </div>
      <div class="booking-detail-item">
        <p class="booking-detail-label">NUMBER OF GUESTS</p>
        <p class="booking-detail-value">${guestsText}</p>
      </div>
      <div class="booking-detail-item">
        <p class="booking-detail-label">PACKAGE</p>
        <p class="booking-detail-value">${packageName}</p>
      </div>
      <div class="booking-detail-item full-width price-item">
        <p class="booking-detail-value price">${price} DH</p>
      </div>
    `;

    // Show modal
    setTimeout(() => {
      backdrop.classList.add('active');
      modal.classList.add('active');
    }, 10);

    document.body.style.overflow = 'hidden';
  };

  window.closeBookingDetailsModal = function () {
    const modal = document.getElementById('bookingDetailsModal');
    const backdrop = document.getElementById('bookingModalBackdrop');
    if (!modal || !backdrop) return;

    modal.classList.remove('active');
    backdrop.classList.remove('active');
    document.body.style.overflow = '';
  };

  window.printBookingReceipt = function () {
    window.print();
  };

  document.addEventListener('DOMContentLoaded', function () {
    createModalHTML();

    document.getElementById('bookingModalClose')?.addEventListener('click', closeBookingDetailsModal);
    document.getElementById('bookingModalCloseBtn')?.addEventListener('click', closeBookingDetailsModal);
    document.getElementById('bookingModalActionBtn')?.addEventListener('click', printBookingReceipt);
    document.getElementById('bookingModalBackdrop')?.addEventListener('click', closeBookingDetailsModal);

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        const modal = document.getElementById('bookingDetailsModal');
        if (modal?.classList.contains('active')) closeBookingDetailsModal();
      }
    });
  });

  console.log('✅ Booking Modal Ready (Image Match)');
})();
