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
      console.warn('RESEND_API_KEY not configured in environment');
      return res.status(500).json({ success: false, error: 'Server email configuration missing' });
    }

    // Format clean HTML email
    const emailHtml = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="utf-8">
        <style>
          body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f6f7ea; color: #10100E; margin: 0; padding: 24px; }
          .card { max-width: 600px; margin: 0 auto; background: #ffffff; border: 1px solid rgba(16,16,14,0.1); border-radius: 16px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }
          .header { background: #10100E; color: #F6F7EA; padding: 28px 32px; text-align: left; }
          .header h1 { margin: 0 0 4px 0; font-size: 20px; text-transform: uppercase; letter-spacing: 2px; font-weight: 700; color: #F6F7EA; }
          .header p { margin: 0; font-size: 13px; opacity: 0.7; }
          .content { padding: 32px; }
          .field { margin-bottom: 20px; border-bottom: 1px solid #f0f0f0; padding-bottom: 16px; }
          .field:last-child { border-bottom: none; }
          .label { font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 700; color: #523225; margin-bottom: 4px; }
          .value { font-size: 16px; font-weight: 500; color: #10100E; }
          .message-box { background: #F6F7EA; border-left: 4px solid #523225; padding: 16px; border-radius: 4px; font-size: 15px; line-height: 1.5; color: #272724; white-space: pre-wrap; margin-top: 8px; }
          .actions { padding: 0 32px 32px 32px; display: flex; gap: 12px; }
          .btn { display: inline-block; background: #25D366; color: #ffffff !important; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 14px; }
          .btn-email { background: #523225; }
          .footer { background: #f9f9f6; padding: 16px 32px; font-size: 12px; color: #888888; text-align: center; border-top: 1px solid #eee; }
        </style>
      </head>
      <body>
        <div class="card">
          <div class="header">
            <h1>Marragafay Inquiries</h1>
            <p>New Expedition Inquiry received from website</p>
          </div>
          
          <div class="content">
            <div class="field">
              <div class="label">Customer Name</div>
              <div class="value">${name}</div>
            </div>

            <div class="field">
              <div class="label">Email Address</div>
              <div class="value"><a href="mailto:${email}" style="color: #523225; text-decoration: none;">${email}</a></div>
            </div>

            <div class="field">
              <div class="label">Phone / WhatsApp</div>
              <div class="value">
                <a href="https://wa.me/${(phone || '').replace(/[^0-9]/g, '')}" style="color: #25D366; font-weight: 600; text-decoration: none;">
                  ${phone || 'Not provided'} ↗
                </a>
              </div>
            </div>

            <div class="field">
              <div class="label">Anticipated Date & Guests</div>
              <div class="value">${date || 'Flexible Date'} · ${guests ? guests + ' Guests' : 'Group size not specified'}</div>
            </div>

            <div class="field">
              <div class="label">Inquiry Details & Requirements</div>
              <div class="message-box">${requirements || 'No special requirements specified.'}</div>
            </div>
          </div>

          <div class="actions">
            ${phone ? `<a href="https://wa.me/${phone.replace(/[^0-9]/g, '')}" class="btn" target="_blank">Chat on WhatsApp</a>` : ''}
            <a href="mailto:${email}?subject=Regarding your Marragafay Expedition Inquiry" class="btn btn-email" target="_blank">Reply via Email</a>
          </div>

          <div class="footer">
            Received via Marragafay Contact Form · ${new Date().toUTCString()}
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
        subject: `🌟 New Expedition Inquiry: ${name}${guests ? ' (' + guests + ' guests)' : ''}${date ? ' [' + date + ']' : ''}`,
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
