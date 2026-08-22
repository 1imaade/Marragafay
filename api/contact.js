// Vercel Serverless Function: api/contact.js
// Handles automatic email notifications for expedition contact form inquiries via Resend

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
    const { name, email, phone, date, guests, requirements } = req.body || {};

    if (!name || !email) {
      return res.status(400).json({ success: false, error: 'Name and email are required' });
    }

    const RESEND_API_KEY = process.env.RESEND_API_KEY;
    const TO_EMAIL = process.env.NOTIFICATION_EMAIL || 'marragafay@gmail.com';

    if (!RESEND_API_KEY) {
      console.error('RESEND_API_KEY not configured in environment');
      return res.status(500).json({ success: false, error: 'Server email configuration missing' });
    }

    // Customer initials
    const initials = (name || 'Guest')
      .split(' ')
      .filter(Boolean)
      .map(n => n[0])
      .join('')
      .substring(0, 2)
      .toUpperCase();

    // Clean, High-End Bento Luxury Email Design
    const emailHtml = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>New Expedition Request</title>
</head>
<body style="margin: 0; padding: 48px 16px; background-color: #F6F7F9; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #111827; -webkit-font-smoothing: antialiased;">
  
  <table role="presentation" style="max-width: 580px; width: 100%; margin: 0 auto; background-color: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 20px; overflow: hidden; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03); border-collapse: separate;">
    
    <!-- Top Header Bar -->
    <tr>
      <td style="padding: 32px 36px 24px 36px; border-bottom: 1px solid #F3F4F6;">
        <table role="presentation" style="width: 100%; border-collapse: collapse;">
          <tr>
            <td>
              <div style="font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #6B7280;">
                MARRAGAFAY CONCIERGE
              </div>
              <div style="font-size: 20px; font-weight: 700; color: #111827; margin-top: 4px;">
                New Expedition Request
              </div>
            </td>
            <td style="text-align: right; vertical-align: middle;">
              <span style="display: inline-block; background-color: #ECFDF5; border: 1px solid #A7F3D0; color: #065F46; font-size: 11px; font-weight: 600; padding: 4px 10px; border-radius: 9999px; letter-spacing: 0.5px;">
                ● LIVE INQUIRY
              </span>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- Customer Profile Header Card -->
    <tr>
      <td style="padding: 28px 36px 20px 36px;">
        <table role="presentation" style="width: 100%; background-color: #F9FAFB; border: 1px solid #E5E7EB; border-radius: 12px; padding: 18px 20px;">
          <tr>
            <td style="width: 48px; vertical-align: middle;">
              <div style="width: 44px; height: 44px; border-radius: 50%; background-color: #111827; color: #FFFFFF; font-size: 15px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; text-align: center; line-height: 44px;">
                ${initials}
              </div>
            </td>
            <td style="padding-left: 14px; vertical-align: middle;">
              <div style="font-size: 17px; font-weight: 700; color: #111827; line-height: 1.2;">
                ${name}
              </div>
              <div style="font-size: 13px; color: #6B7280; margin-top: 4px;">
                <a href="mailto:${email}" style="color: #4B5563; text-decoration: none;">${email}</a> · 
                <a href="https://wa.me/${(phone || '').replace(/[^0-9]/g, '')}" style="color: #111827; font-weight: 600; text-decoration: none;">${phone || 'No phone'}</a>
              </div>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- Bento 2-Column Summary Cards (Date & Group Size) -->
    <tr>
      <td style="padding: 0 36px 24px 36px;">
        <table role="presentation" style="width: 100%; border-collapse: separate; border-spacing: 12px 0; margin-left: -12px; margin-right: -12px;">
          <tr>
            <td style="width: 50%; background-color: #FAFAFA; border: 1px solid #E5E7EB; border-radius: 12px; padding: 16px 20px;">
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #6B7280; margin-bottom: 6px;">
                Anticipated Date
              </div>
              <div style="font-size: 16px; font-weight: 700; color: #111827;">
                ${date || 'Flexible Date'}
              </div>
            </td>
            <td style="width: 50%; background-color: #FAFAFA; border: 1px solid #E5E7EB; border-radius: 12px; padding: 16px 20px;">
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #6B7280; margin-bottom: 6px;">
                Group Size
              </div>
              <div style="font-size: 16px; font-weight: 700; color: #111827;">
                ${guests ? guests + ' Guests' : 'Not specified'}
              </div>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- Special Requirements & Notes -->
    <tr>
      <td style="padding: 0 36px 28px 36px;">
        <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #6B7280; margin-bottom: 10px;">
          Custom Requirements & Notes
        </div>
        <div style="background-color: #FFFFFF; border: 1px solid #E5E7EB; border-left: 3px solid #111827; border-radius: 8px; padding: 18px 20px; font-size: 14px; line-height: 1.6; color: #374151; white-space: pre-wrap;">
${requirements || 'No special requirements specified.'}
        </div>
      </td>
    </tr>

    <!-- Fast Action Buttons -->
    <tr>
      <td style="padding: 0 36px 32px 36px;">
        <table role="presentation" style="width: 100%; border-collapse: collapse;">
          <tr>
            <td style="padding-right: 10px; width: 50%;">
              <a href="https://wa.me/${(phone || '').replace(/[^0-9]/g, '')}" target="_blank" style="display: block; text-align: center; background-color: #111827; color: #FFFFFF !important; font-size: 13px; font-weight: 600; padding: 14px 20px; border-radius: 10px; text-decoration: none; letter-spacing: 0.3px;">
                Chat on WhatsApp ↗
              </a>
            </td>
            <td style="padding-left: 10px; width: 50%;">
              <a href="mailto:${email}?subject=Regarding your Marragafay Expedition Request" target="_blank" style="display: block; text-align: center; background-color: #FFFFFF; color: #111827 !important; border: 1px solid #D1D5DB; font-size: 13px; font-weight: 600; padding: 14px 20px; border-radius: 10px; text-decoration: none; letter-spacing: 0.3px;">
                Reply via Email ✉
              </a>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- Footer Summary -->
    <tr>
      <td style="padding: 20px 36px; background-color: #FAFAFA; border-top: 1px solid #F3F4F6; font-size: 12px; color: #9CA3AF; text-align: center; line-height: 1.6;">
        Automatically saved to <strong style="color: #6B7280;">Supabase Database</strong> · Marragafay Agafay Desert<br>
        <span style="font-size: 11px; color: #CBD5E1;">${new Date().toUTCString()}</span>
      </td>
    </tr>

  </table>

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
        from: 'Marragafay Inquiries <onboarding@resend.dev>',
        to: [TO_EMAIL],
        reply_to: email,
        subject: `🌟 Expedition Request: ${name}${guests ? ' (' + guests + ' guests)' : ''}${date ? ' [' + date + ']' : ''}`,
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
    console.error('Server error sending email:', error);
    return res.status(500).json({ success: false, error: error.message });
  }
}
