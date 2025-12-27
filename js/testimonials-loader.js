/**
 * Testimonials Loader - Fetches and displays approved reviews from Supabase
 * Add this script to your index.html after the Supabase CDN script
 */

// ============================================
// CONFIGURATION - Update these with your credentials
// ============================================
const SUPABASE_URL = 'YOUR_SUPABASE_URL_HERE'; // e.g., 'https://xxxxx.supabase.co'
const SUPABASE_ANON_KEY = 'YOUR_SUPABASE_ANON_KEY_HERE';

// ============================================
// SUPABASE CLIENT INITIALIZATION
// ============================================
let supabaseClient;

function initSupabase() {
    try {
        if (typeof supabase === 'undefined') {
            console.error('Supabase SDK not loaded. Make sure to include the CDN script.');
            return false;
        }
        supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
        return true;
    } catch (error) {
        console.error('Error initializing Supabase:', error);
        return false;
    }
}

// ============================================
// FETCH REVIEWS FROM SUPABASE
// ============================================
async function fetchApprovedReviews() {
    try {
        const { data, error } = await supabaseClient
            .from('reviews')
            .select('*')
            .eq('status', 'approved')
            .order('created_at', { ascending: false })
            .limit(6);

        if (error) {
            throw error;
        }

        return data || [];
    } catch (error) {
        console.error('Error fetching reviews:', error);
        throw error;
    }
}

// ============================================
// GENERATE STAR RATING HTML
// ============================================
function generateStarRating(rating) {
    const maxStars = 5;
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0;

    let starsHTML = '';

    // Full stars
    for (let i = 0; i < fullStars; i++) {
        starsHTML += '<i class="fa fa-star" style="color: #b18c58;"></i>';
    }

    // Half star
    if (hasHalfStar) {
        starsHTML += '<i class="fa fa-star-half-alt" style="color: #b18c58;"></i>';
    }

    // Empty stars
    const emptyStars = maxStars - fullStars - (hasHalfStar ? 1 : 0);
    for (let i = 0; i < emptyStars; i++) {
        starsHTML += '<i class="fa fa-star-o" style="color: #b18c58;"></i>';
    }

    return starsHTML;
}

// ============================================
// FORMAT DATE
// ============================================
function formatDate(dateString) {
    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}

// ============================================
// CREATE REVIEW CARD HTML
// ============================================
function createReviewCard(review) {
    const { name, rating, comment, created_at, image_url } = review;

    return `
    <div class="col-md-4 mb-4">
      <div class="testimonial-card">
        <div class="testimonial-header">
          ${image_url ? `
            <img src="${image_url}" alt="${name}" class="testimonial-avatar">
          ` : `
            <div class="testimonial-avatar-placeholder">
              <i class="fa fa-user"></i>
            </div>
          `}
          <div class="testimonial-info">
            <h5 class="testimonial-name">${name}</h5>
            <div class="testimonial-stars">
              ${generateStarRating(rating)}
            </div>
          </div>
        </div>
        <p class="testimonial-comment">${comment}</p>
        <div class="testimonial-date">
          <i class="fa fa-calendar"></i> ${formatDate(created_at)}
        </div>
      </div>
    </div>
  `;
}

// ============================================
// RENDER REVIEWS TO DOM
// ============================================
function renderReviews(reviews) {
    const container = document.getElementById('reviews-container');

    if (!container) {
        console.error('Reviews container not found. Make sure you have a div with id="reviews-container"');
        return;
    }

    // Empty state
    if (reviews.length === 0) {
        container.innerHTML = `
      <div class="col-12 text-center py-5">
        <i class="fa fa-comments-o" style="font-size: 48px; color: #b18c58; margin-bottom: 16px;"></i>
        <h4 style="color: #333;">No Reviews Yet</h4>
        <p style="color: #666;">Be the first to share your experience!</p>
      </div>
    `;
        return;
    }

    // Render review cards
    const reviewsHTML = reviews.map(review => createReviewCard(review)).join('');
    container.innerHTML = reviewsHTML;
}

// ============================================
// SHOW LOADING STATE
// ============================================
function showLoading() {
    const container = document.getElementById('reviews-container');
    if (!container) return;

    container.innerHTML = `
    <div class="col-12 text-center py-5">
      <div class="spinner-border" role="status" style="color: #b18c58; width: 3rem; height: 3rem;">
        <span class="sr-only">Loading reviews...</span>
      </div>
      <p style="margin-top: 16px; color: #666;">Loading testimonials...</p>
    </div>
  `;
}

// ============================================
// SHOW ERROR STATE
// ============================================
function showError(message) {
    const container = document.getElementById('reviews-container');
    if (!container) return;

    container.innerHTML = `
    <div class="col-12 text-center py-5">
      <i class="fa fa-exclamation-triangle" style="font-size: 48px; color: #dc3545; margin-bottom: 16px;"></i>
      <h4 style="color: #333;">Unable to Load Reviews</h4>
      <p style="color: #666;">${message}</p>
      <button onclick="loadTestimonials()" class="btn btn-primary mt-3">Try Again</button>
    </div>
  `;
}

// ============================================
// MAIN FUNCTION - LOAD TESTIMONIALS
// ============================================
async function loadTestimonials() {
    // Show loading state
    showLoading();

    // Initialize Supabase
    if (!initSupabase()) {
        showError('Failed to connect to the database. Please try again later.');
        return;
    }

    try {
        // Fetch reviews
        const reviews = await fetchApprovedReviews();

        // Render reviews
        renderReviews(reviews);
    } catch (error) {
        console.error('Error loading testimonials:', error);
        showError('An error occurred while loading reviews. Please try again later.');
    }
}

// ============================================
// AUTO-LOAD ON PAGE READY
// ============================================
document.addEventListener('DOMContentLoaded', function () {
    loadTestimonials();
});
