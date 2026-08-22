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

    // Clean, High-End Minimalist Email with Perfected Spacing & UX
    const emailHtml = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>New Expedition Inquiry</title>
</head>
<body style="margin: 0; padding: 40px 15px; background-color: #F8F9FA; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #111827; -webkit-font-smoothing: antialiased;">
  
  <div style="max-width: 580px; margin: 0 auto; background-color: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 16px; overflow: hidden; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);">
    
    <!-- Top Brand & Header Section -->
    <div style="padding: 36px 36px 24px 36px; border-bottom: 1px solid #F3F4F6;">
      <div style="font-size: 11px; font-weight: 700; letter-spacing: 2.5px; text-transform: uppercase; color: #9CA3AF; margin-bottom: 8px;">
        MARRAGAFAY · EXPEDITIONS
      </div>
      <h1 style="margin: 0 0 6px 0; font-size: 22px; font-weight: 700; color: #111827; letter-spacing: -0.3px; line-height: 1.3;">
        New Expedition Inquiry
      </h1>
      <div style="font-size: 13px; color: #6B7280;">
        Submitted via marragafay.com contact form
      </div>
    </div>

    <!-- Main Content Section -->
    <div style="padding: 28px 36px 32px 36px;">
      
      <!-- Key-Value Info Table -->
      <table style="width: 100%; border-collapse: collapse; margin-bottom: 32px;">
        
        <tr>
          <td style="padding: 13px 0; border-bottom: 1px solid #F3F4F6; width: 34%; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; color: #6B7280; vertical-align: middle;">
            Client Name
          </td>
          <td style="padding: 13px 0; border-bottom: 1px solid #F3F4F6; width: 66%; font-size: 15px; font-weight: 600; color: #111827; vertical-align: middle;">
            ${name}
          </td>
        </tr>

        <tr>
          <td style="padding: 13px 0; border-bottom: 1px solid #F3F4F6; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; color: #6B7280; vertical-align: middle;">
            Email Address
          </td>
          <td style="padding: 13px 0; border-bottom: 1px solid #F3F4F6; font-size: 15px; font-weight: 500; color: #111827; vertical-align: middle;">
            <a href="mailto:${email}" style="color: #111827; text-decoration: underline; text-underline-offset: 3px;">${email}</a>
          </td>
        </tr>

        <tr>
          <td style="padding: 13px 0; border-bottom: 1px solid #F3F4F6; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; color: #6B7280; vertical-align: middle;">
            Phone / WhatsApp
          </td>
          <td style="padding: 13px 0; border-bottom: 1px solid #F3F4F6; font-size: 15px; font-weight: 600; color: #111827; vertical-align: middle;">
            <a href="https://wa.me/${(phone || '').replace(/[^0-9]/g, '')}" style="color: #111827; text-decoration: none; display: inline-flex; align-items: center;">
              ${phone || 'Not provided'} <span style="font-size: 12px; margin-left: 4px; color: #6B7280;">↗</span>
            </a>
          </td>
        </tr>

        <tr>
          <td style="padding: 13px 0; border-bottom: 1px solid #F3F4F6; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; color: #6B7280; vertical-align: middle;">
            Target Date
          </td>
          <td style="padding: 13px 0; border-bottom: 1px solid #F3F4F6; font-size: 15px; font-weight: 600; color: #111827; vertical-align: middle;">
            ${date || 'Flexible Date'}
          </td>
        </tr>

        <tr>
          <td style="padding: 13px 0; border-bottom: 1px solid #F3F4F6; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; color: #6B7280; vertical-align: middle;">
            Group Size
          </td>
          <td style="padding: 13px 0; border-bottom: 1px solid #F3F4F6; font-size: 15px; font-weight: 600; color: #111827; vertical-align: middle;">
            ${guests ? guests + ' Guests' : 'Not specified'}
          </td>
        </tr>

      </table>

      <!-- Notes / Special Requirements Section -->
      <div style="margin-bottom: 32px;">
        <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #6B7280; margin-bottom: 10px;">
          Client Notes & Special Requirements
        </div>
        <div style="background-color: #F9FAFB; border: 1px solid #E5E7EB; border-radius: 10px; padding: 18px 20px; font-size: 14px; line-height: 1.65; color: #374151; white-space: pre-wrap;">
${requirements || 'No special requirements specified.'}
        </div>
      </div>

      <!-- Quick Action Buttons -->
      <div>
        <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #6B7280; margin-bottom: 12px;">
          Quick Actions
        </div>
        <table style="border-collapse: collapse;">
          <tr>
            <td style="padding-right: 12px;">
              <a href="https://wa.me/${(phone || '').replace(/[^0-9]/g, '')}" target="_blank" style="display: inline-block; background-color: #111827; color: #FFFFFF !important; font-size: 13px; font-weight: 600; padding: 12px 22px; border-radius: 8px; text-decoration: none; letter-spacing: 0.3px;">
                Chat on WhatsApp
              </a>
            </td>
            <td>
              <a href="mailto:${email}?subject=Regarding your Marragafay Expedition Inquiry" target="_blank" style="display: inline-block; background-color: #F3F4F6; color: #111827 !important; border: 1px solid #E5E7EB; font-size: 13px; font-weight: 600; padding: 12px 22px; border-radius: 8px; text-decoration: none; letter-spacing: 0.3px;">
                Reply via Email
              </a>
            </td>
          </tr>
        </table>
      </div>

    </div>

    <!-- Footer -->
    <div style="padding: 20px 36px; background-color: #FAFAFA; border-top: 1px solid #F3F4F6; font-size: 12px; color: #9CA3AF; text-align: center; line-height: 1.5;">
      Marragafay Luxury Agafay Experiences · Automated Notification<br>
      <span style="font-size: 11px; color: #D1D5DB;">${new Date().toUTCString()}</span>
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
        subject: `🌟 Inquiry: ${name}${guests ? ' (' + guests + ' guests)' : ''}${date ? ' [' + date + ']' : ''}`,
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
