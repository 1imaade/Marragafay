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

    // Distinct, Clean, Professional Booking Receipt Email
    const emailHtml = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 24px 12px; background-color: #F4F4F5; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; color: #18181B;">
  
  <div style="max-width: 480px; margin: 0 auto; background-color: #FFFFFF; border: 1px solid #E4E4E7; border-top: 3px solid #18181B; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
    
    <!-- Top Header Banner -->
    <div style="padding: 20px 24px 16px 24px; background-color: #FAFAFA; border-bottom: 1px solid #F4F4F5;">
      <table style="width: 100%; border-collapse: collapse;">
        <tr>
          <td>
            <div style="font-size: 10px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #71717A;">
              MARRAGAFAY BOOKING
            </div>
            <div style="font-size: 16px; font-weight: 700; color: #18181B; margin-top: 2px;">
              ${experienceTitle}
            </div>
          </td>
          <td style="text-align: right; vertical-align: middle;">
            <span style="display: inline-block; background-color: #18181B; color: #FFFFFF; font-size: 10px; font-weight: 700; padding: 3px 8px; border-radius: 4px; letter-spacing: 0.5px; text-transform: uppercase;">
              RESERVATION
            </span>
          </td>
        </tr>
      </table>
    </div>

    <!-- Main Content -->
    <div style="padding: 20px 24px 22px 24px;">
      
      <!-- Key-Value Info -->
      <table style="width: 100%; border-collapse: collapse; margin-bottom: 18px;">
        <tr>
          <td style="padding: 6px 0; width: 110px; font-size: 13px; color: #71717A;">Customer</td>
          <td style="padding: 6px 0; font-size: 14px; font-weight: 600; color: #18181B;">${customerName}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; font-size: 13px; color: #71717A;">WhatsApp</td>
          <td style="padding: 6px 0; font-size: 14px; font-weight: 600; color: #18181B;">
            <a href="${waUrl}" style="color: #18181B; text-decoration: none;">${customerPhone || 'Not provided'}</a>
          </td>
        </tr>
        <tr>
          <td style="padding: 6px 0; font-size: 13px; color: #71717A;">Booking Date</td>
          <td style="padding: 6px 0; font-size: 14px; font-weight: 600; color: #18181B;">${date || 'Flexible'}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; font-size: 13px; color: #71717A;">Guests</td>
          <td style="padding: 6px 0; font-size: 14px; font-weight: 500; color: #18181B;">${adultsCount} Adults, ${childrenCount} Children</td>
        </tr>
      </table>

      <!-- Prominent Total Price Card -->
      <div style="background-color: #FAFAFA; border: 1px solid #E4E4E7; border-radius: 6px; padding: 12px 16px; margin-bottom: 20px;">
        <table style="width: 100%; border-collapse: collapse;">
          <tr>
            <td style="font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; color: #71717A;">
              Total Amount
            </td>
            <td style="text-align: right; font-size: 18px; font-weight: 800; color: #18181B;">
              ${total_price || 'N/A'}
            </td>
          </tr>
        </table>
      </div>

      <!-- Action Button -->
      ${waCleanNumber ? `
      <div>
        <a href="${waUrl}" target="_blank" style="display: block; text-align: center; background-color: #18181B; color: #FFFFFF !important; font-size: 13px; font-weight: 600; padding: 11px 20px; border-radius: 6px; text-decoration: none; letter-spacing: 0.2px;">
          Contact Customer on WhatsApp ↗
        </a>
      </div>
      ` : ''}

    </div>

    <!-- Footer -->
    <div style="padding: 12px 24px; background-color: #FAFAFA; border-top: 1px solid #F4F4F5; font-size: 11px; color: #A1A1AA; text-align: center;">
      Marragafay Experience Booking · ${new Date().toUTCString()}
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
        subject: `🎟️ BOOKING: ${experienceTitle} - ${customerName} (${total_price || ''})`,
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
