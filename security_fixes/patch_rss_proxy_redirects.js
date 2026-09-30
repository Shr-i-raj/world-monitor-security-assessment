/**
 * SECURITY PATCH: VULN-02 RSS Proxy Open Redirect SSRF Fix
 * Target: api/rss-proxy.js
 */

import { isAllowedDomain } from './_rss-allowed-domain-match.js';
import { isBlockedNotificationResolvedAddress } from './_notification-webhook-ssrf.ts';

class RssProxyPolicyError extends Error {
  constructor(message, status = 403) {
    super(message);
    this.name = 'RssProxyPolicyError';
    this.status = status;
  }
}

/**
 * Hardened redirect validator: Inspects protocol, domain allowlist, AND IP resolution
 */
export async function assertAllowedRedirectSecure(url) {
  if (url.protocol !== 'http:' && url.protocol !== 'https:') {
    throw new RssProxyPolicyError('Redirect protocol not allowed', 403);
  }

  if (!isAllowedDomain(url.hostname)) {
    throw new RssProxyPolicyError('Redirect to disallowed domain', 403);
  }

  // Check IP resolution for target hostname to prevent open redirect SSRF
  if (isBlockedNotificationResolvedAddress(url.hostname)) {
    throw new RssProxyPolicyError('Redirect target resolves to forbidden address', 403);
  }
}
