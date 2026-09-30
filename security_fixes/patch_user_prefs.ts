/**
 * SECURITY PATCH: VULN-07 User Preferences JSON Depth & Size Limits Fix
 * Target: api/user-prefs.ts
 */

const MAX_PREFS_BYTES = 64 * 1024; // 64 KB Max Limit
const MAX_JSON_DEPTH = 10;

export function validatePrefsPayload(rawBody: string): { valid: boolean; error?: string } {
  if (rawBody.length > MAX_PREFS_BYTES) {
    return { valid: false, error: 'Preferences payload size exceeds maximum limit of 64KB' };
  }

  try {
    const parsed = JSON.parse(rawBody);
    const depth = getObjectDepth(parsed);
    if (depth > MAX_JSON_DEPTH) {
      return { valid: false, error: 'JSON nesting depth exceeds maximum allowed limit' };
    }
  } catch (e) {
    return { valid: false, error: 'Invalid JSON body' };
  }

  return { valid: true };
}

function getObjectDepth(obj: any): number {
  if (obj === null || typeof obj !== 'object') return 0;
  let maxDepth = 0;
  for (const key of Object.keys(obj)) {
    maxDepth = Math.max(maxDepth, getObjectDepth(obj[key]));
  }
  return 1 + maxDepth;
}
