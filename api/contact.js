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

    // Clean, Minimalist, Luxury Email Design
    const emailHtml = `
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
          body { margin: 0; padding: 32px 16px; background-color: #f9fafb; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #111827; }
          .wrapper { max-width: 540px; margin: 0 auto; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 12px; overflow: hidden; }
          .header { padding: 28px 32px 20px 32px; border-bottom: 1px solid #f3f4f6; }
          .brand { font-size: 12px; font-weight: 700; letter-spacing: 2.5px; text-transform: uppercase; color: #111827; margin-bottom: 4px; }
          .title { font-size: 18px; font-weight: 600; color: #374151; margin: 0; }
          .body-content { padding: 24px 32px; }
          .info-table { width: 100%; border-collapse: collapse; }
          .info-table td { padding: 10px 0; border-bottom: 1px solid #f3f4f6; font-size: 14px; vertical-align: top; }
          .info-label { width: 36%; color: #6b7280; font-weight: 500; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
          .info-val { width: 64%; color: #111827; font-weight: 600; }
          .message-section { margin-top: 24px; }
          .message-label { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; color: #6b7280; margin-bottom: 8px; }
          .message-box { background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; padding: 14px 16px; font-size: 14px; line-height: 1.5; color: #374151; white-space: pre-wrap; }
          .cta-container { padding: 0 32px 28px 32px; }
          .btn-wa { display: inline-block; background: #111827; color: #ffffff !important; padding: 10px 20px; border-radius: 6px; font-size: 13px; font-weight: 600; text-decoration: none; margin-right: 8px; }
          .btn-reply { display: inline-block; background: #f3f4f6; color: #111827 !important; border: 1px solid #e5e7eb; padding: 10px 20px; border-radius: 6px; font-size: 13px; font-weight: 600; text-decoration: none; }
          .footer { padding: 14px 32px; background: #fafafa; border-top: 1px solid #f3f4f6; font-size: 12px; color: #9ca3af; text-align: center; }
        </style>
      </head>
      <body>
        <div class="wrapper">
          <div class="header">
            <div class="brand">MARRAGAFAY</div>
            <h1 class="title">New Expedition Inquiry</h1>
          </div>
          
          <div class="body-content">
            <table class="info-table">
              <tr>
                <td class="info-label">Customer</td>
                <td class="info-val">${name}</td>
              </tr>
              <tr>
                <td class="info-label">Email</td>
                <td class="info-val"><a href="mailto:${email}" style="color: #111827; text-decoration: none;">${email}</a></td>
              </tr>
              <tr>
                <td class="info-label">Phone / WhatsApp</td>
                <td class="info-val">
                  <a href="https://wa.me/${(phone || '').replace(/[^0-9]/g, '')}" style="color: #111827; text-decoration: none;">
                    ${phone || 'Not provided'}
                  </a>
                </td>
              </tr>
              <tr>
                <td class="info-label">Anticipated Date</td>
                <td class="info-val">${date || 'Flexible Date'}</td>
              </tr>
              <tr>
                <td class="info-label">Group Size</td>
                <td class="info-val">${guests ? guests + ' Guests' : 'Not specified'}</td>
              </tr>
            </table>

            <div class="message-section">
              <div class="message-label">Customer Notes & Requirements</div>
              <div class="message-box">${requirements || 'No additional requirements provided.'}</div>
            </div>
          </div>

          <div class="cta-container">
            ${phone ? `<a href="https://wa.me/${phone.replace(/[^0-9]/g, '')}" class="btn-wa" target="_blank">Chat on WhatsApp</a>` : ''}
            <a href="mailto:${email}?subject=Regarding your Marragafay Expedition Inquiry" class="btn-reply" target="_blank">Reply via Email</a>
          </div>

          <div class="footer">
            Received via marragafay.com · ${new Date().toUTCString()}
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
        subject: `Inquiry: ${name}${guests ? ' (' + guests + ' guests)' : ''}${date ? ' [' + date + ']' : ''}`,
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
