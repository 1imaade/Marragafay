// Temporary, read-only production credential probe. Remove after verification.

const SUPABASE_URL = process.env.SUPABASE_URL || 'https://bgjohquanepghmlmdiyd.supabase.co';
const SERVER_USER_AGENT = 'Marragafay-Booking-Server/1.0';

export default async function supabaseSecretCheck(req, res) {
  if (req.method !== 'GET') return res.status(405).json({ ok: false, error: 'method_not_allowed' });

  const secretKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!secretKey) return res.status(500).json({ ok: false, error: 'secret_not_configured' });

  const response = await fetch(`${SUPABASE_URL}/rest/v1/pricing?select=id&limit=1`, {
    headers: {
      apikey: secretKey,
      'User-Agent': SERVER_USER_AGENT
    }
  });
  const payload = await response.json().catch(() => null);

  console.info('Supabase secret read probe:', JSON.stringify({
    runtime: 'node_serverless',
    explicit_user_agent: true,
    status: response.status,
    code: payload?.code || null,
    message: typeof payload?.message === 'string' ? payload.message.slice(0, 160) : null
  }));

  return res.status(response.ok ? 200 : 502).json({
    ok: response.ok,
    supabase_status: response.status,
    error_code: payload?.code || null,
    error_message: typeof payload?.message === 'string' ? payload.message.slice(0, 160) : null
  });
}
