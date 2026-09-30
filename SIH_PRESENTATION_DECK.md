# SMART INDIA HACKATHON (SIH) 2026 - OFFICIAL IDEA PRESENTATION DECK
## Problem Statement ID: SIH26163 (Serial No. 163)
### Title: Security Assessment of the World Monitor application
**Sponsoring Ministry / Organization**: National Technical Research Organisation (NTRO)  
**Theme**: Smart Automation / Cybersecurity  
**Category**: Software Edition  

---

## Slide 1: Title Page

- **Event**: SMART INDIA HACKATHON 2026
- **Problem Statement ID**: SIH26163 (Serial No. 163)
- **Problem Statement Title**: Security Assessment of the World Monitor application
- **Theme**: Smart Automation / Cybersecurity
- **PS Category**: Software Edition
- **Sponsoring Agency**: National Technical Research Organisation (NTRO)
- **Team Name**: Security Assessment Team

---

## Slide 2: Proposed Solution

### Proposed Solution & Prototype Overview
- Comprehensive Vulnerability Assessment & Penetration Testing (VAPT) audit framework and automated security test suite for World Monitor.
- Covers end-to-end evaluation of Edge Runtime proxy handlers, CORS security policies, session lifecycle, and client-side DOM parsers.

### How It Addresses NTRO Requirements
- Identifies 7 critical/high/medium security findings with full root cause analysis and CVSS v3.1 vector metrics.
- Delivers 5 production-ready code patches preventing cloud metadata exfiltration (`169.254.169.254`) and internal service exposure.
- Provides an executable Python test suite (`security_tests/run_security_audit.py`) for continuous automated security verification.

### Innovation and Uniqueness
- **Socket-Pinned Edge DNS Fix**: Solves the Vercel Edge Runtime DNS Rebinding (TOCTOU) vulnerability with single-pass IP connection handling.
- **Zero-Dependency Audit Runner**: Python-based automated testing harness operating out-of-the-box in any CI/CD pipeline.

---

## Slide 3: Technical Approach

### Technologies & Frameworks Used
- **Languages & Runtimes**: Python 3 (Audit Runner/PoCs), TypeScript / JavaScript (Edge Handlers).
- **Standards & Protocols**: OWASP WSTG v4.2, OWASP Top 10 API (2023), NIST SP 800-115, CVSS v3.1.
- **Target Architecture**: Vercel Edge Functions, Vite, Convex Database, DOMPurify.

### Audit Methodology & Execution Process
1. **Static Application Security Testing (SAST)**: Code auditing of `api/mcp-proxy.ts`, `api/rss-proxy.js`, `api/_cors.js`, and `api/_session.js`.
2. **Edge Reverse Engineering**: Uncovering Time-of-Check Time-of-Use (TOCTOU) DNS rebinding flaws during Edge Runtime fetch calls.
3. **Dynamic Verification & PoC Suite**: Executing python-based exploits to verify loopback, metadata, and open redirect targets.
4. **Security Hardening**: Constructing production code patches for single-pass socket pinning and recursive redirect validation.

---

## Slide 4: Feasibility and Viability

### Feasibility Analysis
- Automated test suite (`security_tests/run_security_audit.py`) executes in under 5 seconds with zero external library dependencies.
- Security patches are drop-in compatible with existing Vercel Edge Runtime functions and Node.js APIs.

### Identified Vulnerability Risks & Challenges
- **VULN-01/03 (High - CVSS 8.2/7.2)**: DNS Rebinding SSRF to AWS/GCP IMDS (`169.254.169.254`) via unpinned Edge fetch.
- **VULN-02 (High - CVSS 7.5)**: RSS Proxy domain allowlist bypass via open HTTP redirects.
- **VULN-04 (Medium - CVSS 6.5)**: Refusal CORS headers echoing untrusted origins with `Access-Control-Allow-Credentials: true`.

### Mitigation Strategies & Hardening Controls
- **Socket-Pinned Resolution**: Single-pass IP connection with Host header retention (`security_fixes/patch_mcp_proxy_ssrf.ts`).
- **Redirect Inspection**: Recursive DNS IP validation on every HTTP redirect hop (`security_fixes/patch_rss_proxy_redirects.js`).
- **CORS Sanitization**: Neutralizing credentials reflection on 403/401 refusal headers (`security_fixes/patch_cors_refusal.js`).

---

## Slide 5: Impact and Benefits

### Target Audience & Infrastructure Impact
- **Cloud Metadata Defense**: Blocks unauthorized access to `169.254.169.254`, protecting AWS EC2 / GCP instance tokens.
- **Internal Service Isolation**: Prevents malicious pivoting to loopback addresses (`127.0.0.1:8080`) and internal Redis ports.
- **Resource Protection**: Prevents CPU resource exhaustion attacks on serverless Edge functions during degraded rate-limit states.

### Platform & Operational Benefits
- **Dashboard Data Integrity**: Ensures OSINT geospatial threat intelligence feeds remain immune to stored DOM XSS payloads.
- **Session Security**: Binds anonymous session tokens to IP subnets and reduces TTL from 12 hours to 1 hour.
- **Turnkey Value for NTRO**: Immediate production code patches and automated CI/CD security regression test suite.

---

## Slide 6: Research and References

### Project Reference & Code Assets
- **Official GitHub Repository**: `https://github.com/Shr-i-raj/world-monitor-security-assessment`
- **Full VAPT Audit Report**: `SECURITY_ASSESSMENT_REPORT.md` (Complete technical breakdown of 7 findings & CVSS v3.1 metrics)
- **Discovery Methodology Guide**: `VULNERABILITY_DISCOVERY_METHODOLOGY.md` (Step-by-step SAST & Edge reverse engineering guide)
- **Automated Test Harness**: `security_tests/run_security_audit.py` (Python verification suite)

### Standards & Framework References
- OWASP Web Security Testing Guide (WSTG v4.2)
- OWASP Top 10 API Security Risks (2023 Edition)
- NIST SP 800-115 (Technical Guide to Information Security Testing and Assessment)
- CVSS v3.1 Vulnerability Scoring Standard
