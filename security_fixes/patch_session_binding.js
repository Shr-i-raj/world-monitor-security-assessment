/**
 * SECURITY PATCH: VULN-05 Session Subnet Binding & Reduced TTL Fix
 * Target: api/_session.js
 */

const SESSION_TTL_MS = 60 * 60 * 1000; // Reduced from 12 hours to 1 hour
const PREFIX = 'wms_';

export function deriveIpSubnet(req) {
  const ip = req.headers.get('x-forwarded-for')?.split(',')[0]?.trim() || '';
  const parts = ip.split('.');
  if (parts.length === 4) {
    return `${parts[0]}.${parts[1]}.${parts[2]}.0/24`;
  }
  return 'unknown_subnet';
}

export async function issueBoundSessionToken(req) {
  const subnet = deriveIpSubnet(req);
  const payload = {
    iat: Date.now(),
    exp: Date.now() + SESSION_TTL_MS,
    sub: subnet,
    n: crypto.randomUUID(),
  };
  return payload;
}
