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

    // Clean, Simple, Professional Email Template
    const emailHtml = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 40px 20px; background-color: #FAFAFA; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; color: #111111;">
  
  <div style="max-width: 520px; margin: 0 auto; background-color: #FFFFFF; border: 1px solid #EAEAEA; border-radius: 8px; padding: 36px 36px 32px 36px;">
    
    <!-- Brand -->
    <div style="font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #666666; margin-bottom: 6px;">
      MARRAGAFAY
    </div>
    
    <div style="font-size: 20px; font-weight: 600; color: #111111; margin-bottom: 24px;">
      New Website Inquiry
    </div>

    <div style="height: 1px; background-color: #EAEAEA; margin-bottom: 24px;"></div>

    <!-- Info List -->
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 24px;">
      <tr>
        <td style="padding: 8px 0; width: 120px; font-size: 13px; color: #777777; vertical-align: top;">Name</td>
        <td style="padding: 8px 0; font-size: 14px; font-weight: 600; color: #111111;">${name}</td>
      </tr>
      <tr>
        <td style="padding: 8px 0; font-size: 13px; color: #777777; vertical-align: top;">Email</td>
        <td style="padding: 8px 0; font-size: 14px; font-weight: 500; color: #111111;">
          <a href="mailto:${email}" style="color: #111111; text-decoration: underline;">${email}</a>
        </td>
      </tr>
      <tr>
        <td style="padding: 8px 0; font-size: 13px; color: #777777; vertical-align: top;">Phone</td>
        <td style="padding: 8px 0; font-size: 14px; font-weight: 500; color: #111111;">
          <a href="https://wa.me/${(phone || '').replace(/[^0-9]/g, '')}" style="color: #111111; text-decoration: none;">${phone || 'Not provided'}</a>
        </td>
      </tr>
      <tr>
        <td style="padding: 8px 0; font-size: 13px; color: #777777; vertical-align: top;">Date</td>
        <td style="padding: 8px 0; font-size: 14px; font-weight: 500; color: #111111;">${date || 'Flexible'}</td>
      </tr>
      <tr>
        <td style="padding: 8px 0; font-size: 13px; color: #777777; vertical-align: top;">Guests</td>
        <td style="padding: 8px 0; font-size: 14px; font-weight: 500; color: #111111;">${guests ? guests + ' Guests' : 'Not specified'}</td>
      </tr>
    </table>

    <div style="height: 1px; background-color: #EAEAEA; margin-bottom: 24px;"></div>

    <!-- Message -->
    <div style="margin-bottom: 28px;">
      <div style="font-size: 13px; color: #777777; margin-bottom: 8px;">Message</div>
      <div style="font-size: 14px; line-height: 1.6; color: #222222; white-space: pre-wrap; background-color: #F8F8F8; padding: 14px 16px; border-radius: 6px;">
${requirements || 'No additional requirements provided.'}
      </div>
    </div>

    <!-- Actions -->
    <div style="margin-bottom: 28px;">
      ${phone ? `<a href="https://wa.me/${phone.replace(/[^0-9]/g, '')}" target="_blank" style="display: inline-block; background-color: #111111; color: #FFFFFF !important; font-size: 13px; font-weight: 500; padding: 10px 18px; border-radius: 6px; text-decoration: none; margin-right: 8px;">WhatsApp</a>` : ''}
      <a href="mailto:${email}?subject=Regarding your Marragafay inquiry" target="_blank" style="display: inline-block; background-color: #FFFFFF; color: #111111 !important; border: 1px solid #CCCCCC; font-size: 13px; font-weight: 500; padding: 10px 18px; border-radius: 6px; text-decoration: none;">
        Reply Email
      </a>
    </div>

    <!-- Footer -->
    <div style="border-top: 1px solid #EAEAEA; padding-top: 18px; font-size: 11px; color: #999999;">
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
        from: 'Marragafay Inquiries <onboarding@resend.dev>',
        to: [TO_EMAIL],
        reply_to: email,
        subject: `New Inquiry: ${name}`,
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
