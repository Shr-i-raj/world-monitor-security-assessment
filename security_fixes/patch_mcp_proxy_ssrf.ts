/**
 * SECURITY PATCH: VULN-01 MCP Proxy DNS Rebinding / TOCTOU SSRF Fix
 * Target: api/mcp-proxy.ts
 */

import net from 'net';
import dns from 'dns/promises';

// Hardened single-pass DNS resolution & socket pinning helper
export async function fetchPinnedUrl(targetUrl: URL, options: RequestInit = {}): Promise<Response> {
  const hostname = targetUrl.hostname;
  
  // 1. Resolve host to IP using Node/System DNS resolver
  const addresses = await dns.resolve4(hostname);
  if (!addresses || addresses.length === 0) {
    throw new Error('DNS resolution failed');
  }

  const resolvedIp = addresses[0];

  // 2. Validate resolved IP against blocked private/reserved IP ranges
  if (isBlockedIpAddress(resolvedIp)) {
    throw new Error('Access to private/local network address is forbidden');
  }

  // 3. Connect directly to resolved IP while maintaining original Host header
  const pinnedTarget = new URL(targetUrl.href);
  pinnedTarget.hostname = resolvedIp;

  const headers = new Headers(options.headers);
  headers.set('Host', hostname);

  return fetch(pinnedTarget.href, {
    ...options,
    headers,
  });
}

function isBlockedIpAddress(ip: string): boolean {
  const parts = ip.split('.').map(Number);
  if (parts.length !== 4) return true;
  
  const [a, b] = parts;
  if (a === 127) return true; // Loopback
  if (a === 10) return true;  // Class A Private
  if (a === 172 && b >= 16 && b <= 31) return true; // Class B Private
  if (a === 192 && b === 168) return true; // Class C Private
  if (a === 169 && b === 254) return true; // Link-Local / Cloud Metadata
  if (a === 0 || a >= 224) return true; // Multicast / Reserved
  
  return false;
}
