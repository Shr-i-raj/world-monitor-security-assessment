# SIH 2026 Problem Statement #163 (NTRO): Security Assessment of World Monitor Application

## Overview
This repository contains the complete security evaluation, vulnerability assessment, penetration testing (VAPT) findings, proof-of-concept exploits, automated security audit runner, hardening code patches, and SIH presentation documentation for **Smart India Hackathon (SIH) 2026 Problem Statement SIH26163 (Serial No. 163)** sponsored by the **National Technical Research Organisation (NTRO)**.

- **Target Application**: World Monitor (`https://www.worldmonitor.app` / `https://github.com/koala73/worldmonitor`)
- **Theme**: Smart Automation / Cybersecurity
- **Category**: Software Edition

---

## Repository Structure

```
.
├── SECURITY_ASSESSMENT_REPORT.md   # Full VAPT Audit Report & Detailed Technical Vulnerability Breakdown
├── SIH_PRESENTATION_DECK.md        # Formatted SIH 2026 Executive Pitch Deck for NTRO Judges
├── README.md                       # Main Repository Documentation & Setup Guide
├── security_tests/
│   └── run_security_audit.py       # Automated Python Security Test Suite (Runs all 7 vulnerability checks)
├── poc_exploits/
│   ├── poc_mcp_ssrf.py             # PoC Demonstrator for MCP Proxy DNS Rebinding SSRF
│   ├── poc_rss_redirect_ssrf.py    # PoC Demonstrator for RSS Proxy Open Redirect SSRF
│   └── poc_cors_reflection.py      # PoC Demonstrator for CORS Origin Reflection
└── security_fixes/
    ├── patch_mcp_proxy_ssrf.ts     # TypeScript patch for socket-pinned DNS resolution
    ├── patch_rss_proxy_redirects.js# JavaScript patch for recursive redirect IP validation
    ├── patch_cors_refusal.js       # CORS refusal header hardening patch
    ├── patch_session_binding.js    # Anonymous session IP subnet binding patch
    └── patch_user_prefs.ts         # User preferences payload size & JSON depth validation patch
```

---

## Vulnerabilities Summary Matrix

| ID | Vulnerability Title | Category | CVSS v3.1 | Severity | Affected Component |
|---|---|---|---|---|---|
| **VULN-01** | DNS Rebinding & TOCTOU SSRF in MCP Proxy | SSRF / DNS Rebind | **8.2** | **High** | `api/mcp-proxy.ts` |
| **VULN-02** | RSS Proxy Domain Allowlist Bypass via Redirection | SSRF / Open Redirect | **7.5** | **High** | `api/rss-proxy.js` |
| **VULN-03** | Webhook Destination DNS Rebinding Gap | SSRF / Webhook Security | **7.2** | **High** | `api/_notification-webhook-ssrf.ts` |
| **VULN-04** | Origin Echo with Credentials in CORS Denials | CORS Misconfig | **6.5** | **Medium** | `api/_cors.js` |
| **VULN-05** | Indefinite Anonymous Session Reuse & Replay | Session Replay | **6.1** | **Medium** | `api/_session.js` |
| **VULN-06** | Client-Side DOM XSS Risk in RSS Feed Parsing | DOM XSS | **6.1** | **Medium** | `src/services/rss.ts` |
| **VULN-07** | Unbounded Prefs JSON Depth Resource Exhaustion | Denial of Service | **5.3** | **Medium** | `api/user-prefs.ts` |

---

## Running the Automated Security Audit Suite

Execute the Python security verification runner:

```bash
python3 security_tests/run_security_audit.py
```

### Sample Output:
```
======================================================================
  SIH 2026 PS #163 (NTRO): World Monitor Automated Security Test Suite
======================================================================
[INFO] Testing VULN-01: MCP Proxy DNS Rebinding / TOCTOU SSRF Protection...
[WARN] VULN-01 Verified: Unpinned fetch in Edge Runtime allows DNS Rebinding to IMDS (169.254.169.254)
[INFO] Testing VULN-02: RSS Proxy Open Redirect SSRF Validation...
[WARN] VULN-02 Verified: Redirect assertion missing IP resolution check on hop 2 -> Private IP reachable!
...
======================================================================
  SUMMARY OF SECURITY AUDIT FINDINGS
======================================================================
  [!] VULN-01: MCP Proxy DNS Rebinding SSRF          : CONFIRMED & REPRODUCIBLE
  [!] VULN-02: RSS Proxy Open Redirect SSRF           : CONFIRMED & REPRODUCIBLE
  [!] VULN-03: Webhook DNS Rebinding Gap              : CONFIRMED & REPRODUCIBLE
  [!] VULN-04: CORS Origin Echoing with Credentials   : CONFIRMED & REPRODUCIBLE
  [!] VULN-05: Anonymous Session Token Replay         : CONFIRMED & REPRODUCIBLE
  [!] VULN-06: Client-Side DOM XSS Risk               : CONFIRMED & REPRODUCIBLE
  [!] VULN-07: User Prefs JSON Depth Exhaustion       : CONFIRMED & REPRODUCIBLE
----------------------------------------------------------------------
Total Verified Vulnerabilities: 7 / 7
Automated Audit Verification Completed Successfully!
======================================================================
```

---

## Submission Details

- **Submission Repository**: [`https://github.com/Shr-i-raj/hackathon-todo.git`](https://github.com/Shr-i-raj/hackathon-todo.git)
- **Prepared For**: SIH 2026 Evaluation Committee & NTRO Representatives.
