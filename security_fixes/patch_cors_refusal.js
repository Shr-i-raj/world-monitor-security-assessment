/**
 * SECURITY PATCH: VULN-04 CORS Origin Refusal Credentials Reflection Fix
 * Target: api/_cors.js
 */

/**
 * Hardened CORS refusal headers:
 * Removes Access-Control-Allow-Credentials: true on origin refusal responses
 * to prevent unauthorized cross-origin reading of error payloads.
 */
export function getOriginDeniedCorsHeadersSecure(req, methods = 'GET, OPTIONS') {
  return {
    'Access-Control-Allow-Origin': 'null',
    'Access-Control-Allow-Credentials': 'false',
    'Access-Control-Allow-Methods': methods,
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Max-Age': '3600',
    'Vary': 'Origin',
  };
}
