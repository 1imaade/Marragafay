import { createReadStream, existsSync, readFileSync, statSync } from 'node:fs';
import { createServer } from 'node:http';
import { extname, join, normalize, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import handleBooking from '../api/booking-server.js';
import handlePosthogConfig from '../api/posthog-config.js';

const root = resolve(fileURLToPath(new URL('..', import.meta.url)));
const portFlag = process.argv.indexOf('--port');
const requestedPort = portFlag >= 0 ? process.argv[portFlag + 1] : undefined;
const port = Number(requestedPort || process.env.MARRAGAFAY_DEV_PORT || 5501);

if (!Number.isInteger(port) || port < 1024 || port > 65535) {
  throw new Error('Invalid local development port');
}

loadEnvFile(join(root, '.env.local'));
process.env.NODE_ENV = process.env.NODE_ENV || 'development';
process.env.MARRAGAFAY_DEV_MODE = process.env.MARRAGAFAY_DEV_MODE || 'dry-run';

const mimeTypes = {
  '.css': 'text/css; charset=utf-8',
  '.html': 'text/html; charset=utf-8',
  '.ico': 'image/x-icon',
  '.jpeg': 'image/jpeg',
  '.jpg': 'image/jpeg',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2'
};

function loadEnvFile(path) {
  if (!existsSync(path)) return;
  for (const line of readFileSync(path, 'utf8').split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const separator = trimmed.indexOf('=');
    if (separator < 1) continue;
    const key = trimmed.slice(0, separator).trim();
    let value = trimmed.slice(separator + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    if (!(key in process.env)) process.env[key] = value;
  }
}

function decorateResponse(res) {
  res.status = (statusCode) => {
    res.statusCode = statusCode;
    return res;
  };
  res.json = (value) => {
    if (!res.headersSent) res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.end(JSON.stringify(value));
    return res;
  };
  return res;
}

async function readBody(req) {
  const chunks = [];
  let size = 0;
  for await (const chunk of req) {
    size += chunk.length;
    if (size > 32 * 1024) throw new Error('Request payload is too large');
    chunks.push(chunk);
  }
  if (!chunks.length) return undefined;
  return Buffer.concat(chunks).toString('utf8');
}

function safeStaticPath(pathname) {
  const decoded = decodeURIComponent(pathname);
  const relative = normalize(decoded).replace(/^[/\\]+/, '');
  const candidate = resolve(root, relative || 'index.html');
  if (candidate !== root && !candidate.startsWith(root + '/')) return null;
  return candidate;
}

function serveStatic(req, res, pathname) {
  let filePath = safeStaticPath(pathname);
  if (!filePath) {
    res.statusCode = 403;
    res.end('Forbidden');
    return;
  }

  if (existsSync(filePath) && statSync(filePath).isDirectory()) filePath = join(filePath, 'index.html');
  if (!existsSync(filePath) && !extname(filePath) && existsSync(filePath + '.html')) filePath += '.html';
  if (!existsSync(filePath) || !statSync(filePath).isFile()) {
    res.statusCode = 404;
    res.end('Not Found');
    return;
  }

  res.statusCode = 200;
  res.setHeader('Content-Type', mimeTypes[extname(filePath).toLowerCase()] || 'application/octet-stream');
  res.setHeader('Cache-Control', 'no-store');
  if (req.method === 'HEAD') {
    res.end();
    return;
  }
  createReadStream(filePath).pipe(res);
}

const server = createServer(async (req, rawRes) => {
  const res = decorateResponse(rawRes);
  const url = new URL(req.url || '/', `http://${req.headers.host || `127.0.0.1:${port}`}`);

  try {
    if (url.pathname === '/api/booking') {
      req.body = await readBody(req);
      await handleBooking(req, res);
      return;
    }
    if (url.pathname === '/api/posthog-config') {
      await handlePosthogConfig(req, res);
      return;
    }
    if (!['GET', 'HEAD'].includes(req.method || 'GET')) {
      res.statusCode = 405;
      res.setHeader('Allow', 'GET, HEAD');
      res.end('Method Not Allowed');
      return;
    }
    if (url.pathname === '/' || url.pathname === '/index.html' || /^\/packages\/luxe(?:\.html)?\/?$/.test(url.pathname)) {
      res.statusCode = 308;
      const destination = url.pathname.startsWith('/packages/luxe') ? '/en/packages/luxe' : '/en';
      res.setHeader('Location', `${destination}${url.search}`);
      res.end();
      return;
    }
    serveStatic(req, res, url.pathname);
  } catch (error) {
    console.error('[dev-server] request failed', error?.message || error);
    if (!res.headersSent) res.statusCode = error?.message === 'Request payload is too large' ? 413 : 500;
    if (!res.writableEnded) res.json({ booking_success: false, error: 'Local development server error' });
  }
});

server.listen(port, '127.0.0.1', () => {
  console.log(`[dev-server] Marragafay running at http://127.0.0.1:${port}`);
  console.log('[dev-server] Booking API is in safe dry-run mode; no Supabase rows or emails will be created.');
});
