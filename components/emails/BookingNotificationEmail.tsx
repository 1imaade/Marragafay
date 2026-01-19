'use server';

/**
 * Booking Email Template - Pure HTML Version
 * 
 * A luxury Black & Gold email template for booking notifications
 * Uses inline styles for maximum email client compatibility
 */

interface BookingEmailProps {
    guestName: string;
    checkInDate: string;
    numberOfGuests: number;
    adults?: number;
    children?: number;
    email: string;
    phone: string;
    packageTitle: string;
    totalPrice?: number;
    notes?: string;
}

/**
 * Generate HTML string for the booking notification email
 * @param props - The booking details to include in the email
 * @returns Complete HTML string ready to be sent via email
 */
export function generateBookingEmailHTML(props: BookingEmailProps): string {
    const { guestName, checkInDate, numberOfGuests, adults, children, email, phone, packageTitle, totalPrice, notes } = props;

    // Format guests display with breakdown if available
    const guestsDisplay = (adults !== undefined && children !== undefined)
        ? `${adults} Adults, ${children} Children`
        : `${numberOfGuests} Guest${numberOfGuests > 1 ? 's' : ''}`;

    return `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Booking Request</title>
</head>
<body style="margin: 0; padding: 0; background-color: #0a0a0a; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
    <div style="background-color: #0a0a0a; padding: 40px 20px; min-height: 100vh;">
        <table cellpadding="0" cellspacing="0" role="presentation" style="max-width: 600px; margin: 0 auto; background: linear-gradient(145deg, #1a1a1a 0%, #0d0d0d 100%); border-radius: 16px; overflow: hidden; border: 1px solid #2a2a2a; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);">
            <!-- Header -->
            <tr>
                <td style="background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%); padding: 40px 30px; text-align: center; border-bottom: 2px solid #C19B76;">
                    <h1 style="margin: 0 0 10px 0; font-size: 28px; font-weight: 700; color: #C19B76; letter-spacing: 1px;">New Booking Request 🔔</h1>
                    <p style="margin: 0; font-size: 14px; color: #888888; letter-spacing: 0.5px;">A new reservation has been submitted</p>
                </td>
            </tr>

            <!-- Gold Divider -->
            <tr>
                <td style="padding: 0 30px;">
                    <div style="height: 3px; background: linear-gradient(90deg, transparent 0%, #C19B76 50%, transparent 100%); margin: 0;"></div>
                </td>
            </tr>

            <!-- Body -->
            <tr>
                <td style="padding: 30px;">
                    <!-- Details Table -->
                    <table cellpadding="0" cellspacing="0" role="presentation" style="width: 100%; border-collapse: collapse;">
                        <tbody>
                            <tr>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #888888; font-size: 14px; width: 40%;">👤 Guest Name</td>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #ffffff; font-size: 14px; font-weight: 600;">${escapeHtml(guestName)}</td>
                            </tr>
                            <tr>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #888888; font-size: 14px;">📦 Package/Activity</td>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #ffffff; font-size: 14px; font-weight: 600;">${escapeHtml(packageTitle)}</td>
                            </tr>
                            <tr>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #888888; font-size: 14px;">📅 Check-in Date</td>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #ffffff; font-size: 14px; font-weight: 600;">${escapeHtml(checkInDate)}</td>
                            </tr>
                            <tr>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #888888; font-size: 14px;">👥 Number of Guests</td>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #ffffff; font-size: 14px; font-weight: 600;">${guestsDisplay}</td>
                            </tr>
                            <tr>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #888888; font-size: 14px;">📧 Email</td>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; font-size: 14px;">
                                    <a href="mailto:${escapeHtml(email)}" style="color: #C19B76; text-decoration: none; font-weight: 600;">${escapeHtml(email)}</a>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #888888; font-size: 14px;">📞 Phone</td>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; font-size: 14px;">
                                    <a href="tel:${escapeHtml(phone)}" style="color: #C19B76; text-decoration: none; font-weight: 600;">${escapeHtml(phone)}</a>
                                </td>
                            </tr>
                            ${totalPrice ? `
                            <tr>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #888888; font-size: 14px;">💰 Total Price</td>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #C19B76; font-size: 18px; font-weight: 700;">${totalPrice} DH</td>
                            </tr>
                            ` : ''}
                            ${notes && notes.trim() ? `
                            <tr>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #888888; font-size: 14px;">📝 Notes</td>
                                <td style="padding: 15px 0; border-bottom: 1px solid #2a2a2a; color: #ffffff; font-size: 14px;">${escapeHtml(notes)}</td>
                            </tr>
                            ` : ''}
                        </tbody>
                    </table>

                    <!-- WhatsApp Button -->
                    <table cellpadding="0" cellspacing="0" role="presentation" style="width: 100%; margin-top: 30px;">
                        <tr>
                            <td style="text-align: center;">
                                <a href="https://wa.me/${phone?.replace(/[^0-9]/g, '')}" style="display: inline-block; background: linear-gradient(135deg, #C19B76 0%, #a07d5a 100%); color: #0a0a0a; text-decoration: none; padding: 14px 32px; border-radius: 8px; font-weight: 600; font-size: 14px; letter-spacing: 0.5px; box-shadow: 0 4px 15px rgba(193, 155, 118, 0.3);">
                                    Contact on WhatsApp →
                                </a>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>

            <!-- Footer -->
            <tr>
                <td style="padding: 30px; text-align: center; border-top: 1px solid #2a2a2a;">
                    <div style="height: 1px; background: linear-gradient(90deg, transparent 0%, #C19B76 50%, transparent 100%); margin-bottom: 20px;"></div>
                    <p style="margin: 0 0 8px 0; font-size: 13px; color: #C19B76; font-weight: 500;">Sent from Marragafay System</p>
                    <p style="margin: 0; font-size: 12px; color: #666666;">© ${new Date().getFullYear()} Marragafay. All rights reserved.</p>
                </td>
            </tr>
        </table>
    </div>
</body>
</html>
    `.trim();
}

/**
 * Helper function to escape HTML special characters
 * Prevents XSS vulnerabilities in email content
 */
function escapeHtml(text: string): string {
    if (!text) return '';
    return String(text)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}
