'use server';

import { Resend } from 'resend';

// Import the HTML generator from the email templates
// Note: The function is in a 'use server' file, so we import it directly
import { generateBookingEmailHTML } from '../../components/emails/BookingNotificationEmail';

/**
 * Initialize Resend with API Key from environment variables
 * Make sure RESEND_API_KEY is set in your .env.local file
 */
const resend = new Resend(process.env.RESEND_API_KEY);

/**
 * Admin email address - All booking notifications will be sent here
 */
const ADMIN_EMAIL = 'marragafay@gmail.com';

/**
 * Sender email configuration
 * Using Resend's default domain for testing; update with verified domain in production
 */
const FROM_EMAIL = 'Marragafay <onboarding@resend.dev>';

/**
 * Booking data interface matching the structure from booking-manager.js
 */
export interface BookingData {
    name: string;
    email: string;
    phone_number: string;
    date: string;
    guests: number;
    adults?: number;
    children?: number;
    package_title: string;
    total_price?: number;
    notes?: string;
}

/**
 * Response interface for the email send operation
 */
export interface SendEmailResult {
    success: boolean;
    message?: string;
    error?: string;
    id?: string;
}

/**
 * Server Action: Send Booking Notification Email to Admin
 * 
 * This function sends a beautifully designed email notification to the admin
 * whenever a new booking is submitted.
 * 
 * @param bookingData - The booking details from the form submission
 * @returns Promise<SendEmailResult> - Success status and message/error
 * 
 * @example
 * ```typescript
 * const result = await sendBookingNotification({
 *   name: 'John Doe',
 *   email: 'john@example.com',
 *   phone_number: '+212 6XX-XXXXXX',
 *   date: '2026-02-15',
 *   guests: 4,
 *   package_title: 'Luxury Pack',
 *   total_price: 2400,
 *   notes: 'Celebrating anniversary'
 * });
 * 
 * if (result.success) {
 *   console.log('Email sent successfully!', result.id);
 * } else {
 *   console.error('Failed to send email:', result.error);
 * }
 * ```
 */
export async function sendBookingNotification(bookingData: BookingData): Promise<SendEmailResult> {
    try {
        console.log('📧 [Server Action] sendBookingNotification called');
        console.log('📋 Booking Data:', JSON.stringify(bookingData, null, 2));

        // ============================================
        // 1. VALIDATE INPUT DATA
        // ============================================
        if (!bookingData.name || !bookingData.email) {
            console.log('❌ Validation Error: Missing required fields');
            return {
                success: false,
                error: 'Missing required booking information (name or email)',
            };
        }

        // ============================================
        // 2. CHECK API KEY
        // ============================================
        if (!process.env.RESEND_API_KEY) {
            console.error('❌ RESEND_API_KEY is not set in environment variables');
            return {
                success: false,
                error: 'Email service not configured. Please contact support.',
            };
        }

        // ============================================
        // 3. FORMAT DATA FOR EMAIL
        // ============================================
        const formattedDate = bookingData.date
            ? new Date(bookingData.date).toLocaleDateString('en-US', {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric',
            })
            : 'Not specified';

        // ============================================
        // 4. GENERATE EMAIL HTML
        // ============================================
        console.log('🎨 Generating email HTML...');

        const emailHtml = generateBookingEmailHTML({
            guestName: String(bookingData.name || 'Guest'),
            checkInDate: formattedDate,
            numberOfGuests: Number(bookingData.guests) || 1,
            adults: bookingData.adults,
            children: bookingData.children,
            email: String(bookingData.email || ''),
            phone: String(bookingData.phone_number || 'Not provided'),
            packageTitle: String(bookingData.package_title || 'General Booking'),
            totalPrice: bookingData.total_price ? Number(bookingData.total_price) : undefined,
            notes: bookingData.notes ? String(bookingData.notes) : undefined,
        });

        console.log('✅ Email HTML generated successfully');

        // ============================================
        // 5. CONSTRUCT EMAIL SUBJECT
        // ============================================
        const emailSubject = `New Booking: ${bookingData.name} - ${formattedDate}`;

        // ============================================
        // 6. SEND EMAIL VIA RESEND
        // ============================================
        console.log('📤 Sending email via Resend...');
        console.log('   - To:', ADMIN_EMAIL);
        console.log('   - From:', FROM_EMAIL);
        console.log('   - Subject:', emailSubject);

        const { data, error } = await resend.emails.send({
            from: FROM_EMAIL,
            to: [ADMIN_EMAIL],
            subject: emailSubject,
            html: emailHtml,
            // Optional: Add reply-to so admin can reply directly to guest
            replyTo: bookingData.email,
        });

        if (error) {
            console.error('❌ Resend API Error:', error);
            return {
                success: false,
                error: `Failed to send email: ${error.message || 'Unknown error'}`,
            };
        }

        console.log('✅ Email sent successfully!');
        console.log('📬 Email ID:', data?.id);

        return {
            success: true,
            message: 'Booking notification email sent successfully',
            id: data?.id,
        };

    } catch (error: any) {
        console.error('❌ [Server Action] Unexpected Error:', error);
        return {
            success: false,
            error: error.message || 'An unexpected error occurred while sending the email',
        };
    }
}

/**
 * Helper function to send a test email
 * Useful for verifying the email configuration is working
 */
export async function sendTestEmail(): Promise<SendEmailResult> {
    console.log('🧪 Sending test email...');

    return sendBookingNotification({
        name: 'Test Guest',
        email: 'test@example.com',
        phone_number: '+212 600 000 000',
        date: new Date().toISOString().split('T')[0],
        guests: 2,
        package_title: 'Test Booking - Comfort Pack',
        total_price: 800,
        notes: 'This is a test booking notification',
    });
}
