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
      phone_number,
      phone,
      date,
      package_title,
      adults,
      children,
      guests,
      total_price
    } = req.body || {};

    const customerName = name || 'Customer';
    const customerPhone = phone_number || phone || '';
    const experienceTitle = package_title || 'Agafay Experience';
    const adultsCount = adults || guests || 1;
    const childrenCount = children || 0;

    const RESEND_API_KEY = process.env.RESEND_API_KEY;
    const TO_EMAIL = process.env.NOTIFICATION_EMAIL || 'marragafay@gmail.com';

    if (!RESEND_API_KEY) {
      console.error('RESEND_API_KEY not configured in environment');
      return res.status(500).json({ success: false, error: 'Server email configuration missing' });
    }

    const waCleanNumber = (customerPhone || '').replace(/[^0-9]/g, '');
    const waUrl = waCleanNumber ? `https://wa.me/${waCleanNumber}` : '#';

    // Clean, Simple, Compact Booking Template (Exact Requested Fields Only)
    const emailHtml = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 20px 12px; background-color: #FAFAFA; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; color: #111111;">
  
  <div style="max-width: 480px; margin: 0 auto; background-color: #FFFFFF; border: 1px solid #EAEAEA; border-radius: 6px; padding: 22px 24px 18px 24px;">
    
    <!-- Brand -->
    <div style="font-size: 11px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #666666; margin-bottom: 4px;">
      MARRAGAFAY · RESERVATION
    </div>
    
    <div style="font-size: 17px; font-weight: 600; color: #111111; margin-bottom: 16px;">
      New Booking: ${experienceTitle}
    </div>

    <div style="height: 1px; background-color: #EAEAEA; margin-bottom: 16px;"></div>

    <!-- Info List -->
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
      <tr>
        <td style="padding: 5px 0; width: 115px; font-size: 13px; color: #777777; vertical-align: top;">Experience</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 600; color: #111111;">${experienceTitle}</td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">Customer</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 600; color: #111111;">${customerName}</td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">WhatsApp</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 500; color: #111111;">
          <a href="${waUrl}" style="color: #111111; text-decoration: none;">${customerPhone || 'Not provided'}</a>
        </td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">Date</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 500; color: #111111;">${date || 'Flexible'}</td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">Adults</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 500; color: #111111;">${adultsCount}</td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">Children</td>
        <td style="padding: 5px 0; font-size: 14px; font-weight: 500; color: #111111;">${childrenCount}</td>
      </tr>
      <tr>
        <td style="padding: 5px 0; font-size: 13px; color: #777777; vertical-align: top;">Total Price</td>
        <td style="padding: 5px 0; font-size: 15px; font-weight: 700; color: #111111;">${total_price || 'N/A'}</td>
      </tr>
    </table>

    <!-- Actions: Only Contact Customer on WhatsApp -->
    ${waCleanNumber ? `
    <div style="margin-bottom: 20px;">
      <a href="${waUrl}" target="_blank" style="display: inline-block; background-color: #111111; color: #FFFFFF !important; font-size: 13px; font-weight: 500; padding: 10px 18px; border-radius: 4px; text-decoration: none;">
        Contact Customer on WhatsApp
      </a>
    </div>
    ` : ''}

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
