# SMART INDIA HACKATHON (SIH) 2026 - PRESENTATION DECK
## Problem Statement ID: SIH26163 (Serial No. 163)
### Title: Security Assessment of the World Monitor Application
**Sponsoring Ministry / Organization**: National Technical Research Organisation (NTRO)  
**Theme**: Smart Automation / Cybersecurity  
**Category**: Software Edition  

---

## Slide 1: Title & Team Overview

- **Project Title**: Comprehensive Security Assessment & Hardening Framework for World Monitor
- **Problem Statement ID**: SIH26163 (S.No 163)
- **Sponsoring Agency**: National Technical Research Organisation (NTRO)
- **Category**: Software Edition
- **Domain**: Cybersecurity & Smart Automation

---

## Slide 2: Problem Statement & Background

### Context & Challenge
- **Target Application**: World Monitor (`https://www.worldmonitor.app` / `https://github.com/koala73/worldmonitor`)
- **App Nature**: Real-time geospatial monitoring, threat intelligence, RSS feed aggregation, and OSINT visualization platform.
- **Challenge Description**: Conduct an authorized security assessment to identify vulnerabilities affecting confidentiality, integrity, or availability, generate proof-of-concept (PoC) exploits, evaluate business impact, and provide actionable code-level mitigations.

### Key Assessment Areas
1. Authentication & Session Management
2. Authorization & Access Control (RBAC)
3. Input Validation & Data Handling (XSS / Injection)
4. API Security & Server-Side Request Forgery (SSRF)
5. Client-Side Security Controls & CORS Policies

---

## Slide 3: Proposed Solution & Methodology

### Our Approach
We performed a systematic VAPT audit adhering to **OWASP Web Security Testing Guide (WSTG v4.2)**, **OWASP Top 10 API Security Risks (2023)**, and **NIST SP 800-115**.

### Key Deliverables Produced
1. **Full VAPT Audit Report (`SECURITY_ASSESSMENT_REPORT.md`)**: Complete technical breakdown of 7 identified vulnerabilities with CVSS v3.1 ratings.
2. **Automated Security Audit Suite (`security_tests/run_security_audit.py`)**: Executable Python testing harness for continuous security verification.
3. **Proof-of-Concept Exploit Demonstrators (`poc_exploits/`)**: Safe, controlled PoC scripts validating SSRF, CORS reflection, and session reuse.
4. **Security Hardening Code Patches (`security_fixes/`)**: Production-ready TypeScript/JavaScript patches for edge functions, proxy handlers, and CORS rules.

---

## Slide 4: Key Security Findings & CVSS Matrix

| Vulnerability Title | Category | CVSS v3.1 | Severity | Affected Component |
|---|---|---|---|---|
| **DNS Rebinding & TOCTOU SSRF** | SSRF / DNS Rebind | **8.2** | **High** | `api/mcp-proxy.ts` |
| **RSS Proxy Allowlist Bypass** | SSRF / Open Redirect | **7.5** | **High** | `api/rss-proxy.js` |
| **Webhook DNS Rebinding Gap** | SSRF / Webhook Security | **7.2** | **High** | `api/_notification-webhook-ssrf.ts` |
| **CORS Origin Echo with Credentials** | CORS Misconfig | **6.5** | **Medium** | `api/_cors.js` |
| **Indefinite Anonymous Session Reuse** | Session Replay | **6.1** | **Medium** | `api/_session.js` |
| **Client-Side DOM XSS Risk** | DOM XSS | **6.1** | **Medium** | `src/services/rss.ts` |
| **Unbounded Prefs JSON Exhaustion** | Denial of Service | **5.3** | **Medium** | `api/user-prefs.ts` |

---

## Slide 5: Deep Dive: SSRF & DNS Rebinding in Edge Proxies

### Critical Vulnerability: DNS Rebinding TOCTOU in MCP Proxy (`api/mcp-proxy.ts`)
- **Root Cause**: Edge Runtime fetch executes a **second DNS lookup** at HTTP socket creation time after initial IP check.
- **Attack Vector**: Attacker sets DNS TTL = 0. 1st lookup returns public IP (passes filter); 2nd lookup returns `169.254.169.254` (AWS IMDS metadata) or `127.0.0.1`.
- **Our Remediation**: Created `patch_mcp_proxy_ssrf.ts` introducing socket-pinned single-pass IP connection handling with Host header retention.

```
Attacker DNS (TTL=0) ──> Check Phase: 1.1.1.1 (Allowed) 
                     ──> Fetch Phase: 169.254.169.254 (REBOUND -> IMDS Leaked)
```

---

## Slide 6: Proof of Concept & Automated Test Suite

### Automated Test Suite (`security_tests/run_security_audit.py`)
- Python-based test runner capable of executing against target or local mock environments.
- Automatically tests and verifies all 7 findings in under 5 seconds.
- Provides clean JSON/Console diagnostic outputs for CI/CD integration.

### Command to Execute Suite:
```bash
python3 security_tests/run_security_audit.py
```

---

## Slide 7: Security Hardening Patches Developed

We provided production-ready source code patches:
1. `security_fixes/patch_mcp_proxy_ssrf.ts`: Socket-pinned DNS resolution.
2. `security_fixes/patch_rss_proxy_redirects.js`: Recursive IP validation on redirect hops.
3. `security_fixes/patch_cors_refusal.js`: Neutralized credentials reflection on 403/401 errors.
4. `security_fixes/patch_session_binding.js`: Client IP subnet binding & 1-hour session TTL.
5. `security_fixes/patch_user_prefs.ts`: Max payload size (64KB) and JSON depth limit checks.

---

## Slide 8: Business Impact & Scalability

### Impact for NTRO & World Monitor Users
- **Data Protection**: Prevents cloud metadata theft (`169.254.169.254`), protecting cloud credentials and internal database strings.
- **System Availability**: Mitigates resource exhaustion attacks on serverless Edge functions.
- **Platform Integrity**: Ensures OSINT monitoring dashboards remain free from stored DOM XSS payload injection.

---

## Slide 9: Conclusion & GitHub Repository

### Summary of Accomplishments
- Handled end-to-end security assessment requirements for SIH 2026 PS #163.
- Delivered full documentation, automated audit runner, PoCs, and code patches.
- Published complete work to official project GitHub repository.

**GitHub Repository**: [`https://github.com/Shr-i-raj/world-monitor-security-assessment.git`](https://github.com/Shr-i-raj/world-monitor-security-assessment.git)
