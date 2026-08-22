// Vercel Serverless Function: api/booking.js
// Handles automatic email notifications for tour/activity/package bookings via Resend

export default async function handler(req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method Not Allowed' });
  }

  try {
    const {
      name,
      email,
      phone_number,
      phone,
      date,
      package_title,
      guests,
      adults,
      children,
      total_price,
      notes
    } = req.body || {};

    const customerName = name || 'Customer';
    const customerEmail = email || '';
    const customerPhone = phone_number || phone || '';
    const experienceTitle = package_title || 'Agafay Experience';

    if (!customerName || !customerEmail) {
      return res.status(400).json({ success: false, error: 'Name and email are required' });
    }

    const RESEND_API_KEY = process.env.RESEND_API_KEY;
    const TO_EMAIL = process.env.NOTIFICATION_EMAIL || 'marragafay@gmail.com';

    if (!RESEND_API_KEY) {
      console.error('RESEND_API_KEY not configured in environment');
      return res.status(500).json({ success: false, error: 'Server email configuration missing' });
    }

    // Format guest details
    let guestsFormatted = '';
    if (adults || children) {
      guestsFormatted = `${adults || 1} Adults${children ? ', ' + children + ' Children' : ''}${guests ? ' (' + guests + ' Total)' : ''}`;
    } else {
      guestsFormatted = `${guests ? guests + ' Guests' : 'Not specified'}`;
    }

    // Clean, Simple, Professional Compact Booking Email Template
    const emailHtml = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 20px 12px; background-color: #FAFAFA; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; color: #111111;">
  
  <div style="max-width: 500px; margin: 0 auto; background-color: #FFFFFF; border: 1px solid #EAEAEA; border-radius: 6px; padding: 22px 24px 18px 24px;">
    
    <!-- Brand -->
    <div style="font-size: 11px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #666666; margin-bottom: 4px;">
      MARRAGAFAY · RESERVATION
    </div>
    
    <div style="font-size: 17px; font-weight: 600; color: #111111; margin-bottom: 16px;">
      New Booking: ${experienceTitle}
    </div>

    <div style="height: 1px; background-color: #EAEAEA; margin-bottom: 16px;"></div>

    <!-- Info List -->
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 16px;">
      <tr>
        <td style="padding: 5px 0; width: 115px; font-size: 13px; color: #777777; vertical-align: top;">Experience</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 600; color: #111111;">${experienceTitle}</td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">Customer</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 600; color: #111111;">${customerName}</td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">Email</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 500; color: #111111;">
          <a href="mailto:${customerEmail}" style="color: #111111; text-decoration: underline;">${customerEmail}</a>
        </td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">Phone</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 500; color: #111111;">
          <a href="https://wa.me/${customerPhone.replace(/[^0-9]/g, '')}" style="color: #111111; text-decoration: none;">${customerPhone || 'Not provided'}</a>
        </td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">Booking Date</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 500; color: #111111;">${date || 'Flexible'}</td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">Guests</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 500; color: #111111;">${guestsFormatted}</td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">Total Amount</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 700; color: #111111;">${total_price || 'N/A'}</td>
      </tr>
    </table>

    <div style="height: 1px; background-color: #EAEAEA; margin-bottom: 16px;"></div>

    <!-- Notes -->
    <div style="margin-bottom: 20px;">
      <div style="font-size: 12px; font-weight: 500; color: #777777; margin-bottom: 6px;">Special Requests & Notes</div>
      <div style="font-size: 13.5px; line-height: 1.55; color: #222222; white-space: pre-wrap; background-color: #F8F8F8; padding: 10px 14px; border-radius: 4px;">
${notes || 'No special requests specified.'}
      </div>
    </div>

    <!-- Actions -->
    <div style="margin-bottom: 20px;">
      ${customerPhone ? `<a href="https://wa.me/${customerPhone.replace(/[^0-9]/g, '')}" target="_blank" style="display: inline-block; background-color: #111111; color: #FFFFFF !important; font-size: 12.5px; font-weight: 500; padding: 8px 16px; border-radius: 4px; text-decoration: none; margin-right: 6px;">WhatsApp Customer</a>` : ''}
      <a href="mailto:${customerEmail}?subject=Booking Confirmation: ${experienceTitle}" target="_blank" style="display: inline-block; background-color: #FFFFFF; color: #111111 !important; border: 1px solid #CCCCCC; font-size: 12.5px; font-weight: 500; padding: 8px 16px; border-radius: 4px; text-decoration: none;">
        Reply Email
      </a>
    </div>

    <!-- Footer -->
    <div style="border-top: 1px solid #EAEAEA; padding-top: 12px; font-size: 11px; color: #999999;">
      Sent from Marragafay website · ${new Date().toUTCString()}
    </div>

  </div>

</body>
</html>
`;

    // Call Resend API
    const resendResponse = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${RESEND_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: 'Marragafay Bookings <onboarding@resend.dev>',
        to: [TO_EMAIL],
        reply_to: customerEmail,
        subject: `⚡ New Booking: ${experienceTitle} - ${customerName}`,
        html: emailHtml
      })
    });

    const resendData = await resendResponse.json();

    if (!resendResponse.ok) {
      console.error('Resend API error:', resendData);
      return res.status(resendResponse.status).json({ success: false, error: resendData });
    }

    return res.status(200).json({ success: true, data: resendData });

  } catch (error) {
    console.error('Server error sending booking email:', error);
    return res.status(500).json({ success: false, error: error.message });
  }
}
