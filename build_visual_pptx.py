#!/usr/bin/env python3
"""
Build High-Impact Visual SIH_PRESENTATION_DECK.pptx (6 Slides)
Uses python-pptx with vibrant cybersecurity dark aesthetics, card containers, glowing accent badges, and structured typography.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_visual_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Tokens
    BG_DARK = RGBColor(7, 9, 14)           # #07090E Deep Cyber Dark
    CARD_BG = RGBColor(18, 26, 43)         # #121A2B Glass Surface Fill
    CARD_BG_ALT = RGBColor(12, 17, 29)     # #0C111D Darker Inner Card
    CYAN_GLOW = RGBColor(0, 242, 254)      # #00F2FE Primary Neon Cyan
    BLUE_GLOW = RGBColor(59, 130, 246)     # #3B82F6 Vibrant Accent Blue
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_BODY = RGBColor(203, 213, 225)    # #CBD5E1 Slate Light Text
    TEXT_MUTED = RGBColor(100, 116, 139)   # #64748B Slate Gray
    ACCENT_YELLOW = RGBColor(245, 158, 11) # #F59E0B Amber Gold
    ACCENT_RED = RGBColor(239, 68, 68)     # #EF4444 Danger Red
    ACCENT_GREEN = RGBColor(16, 185, 129)  # #10B981 Success Green
    ACCENT_PURPLE = RGBColor(139, 92, 246) # #8B5CF6 Vibrant Purple

    def set_bg(slide):
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = BG_DARK

    def add_top_bar(slide, slide_num, category="SMART INDIA HACKATHON 2026 | PS ID: SIH26163"):
        # Top branding bar
        box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(10.0), Inches(0.4))
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"★ {category.upper()}"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = CYAN_GLOW
        p.font.name = "Arial"

        # Sponsoring Agency Tag
        agency_box = slide.shapes.add_textbox(Inches(7.5), Inches(0.4), Inches(3.5), Inches(0.4))
        tf_a = agency_box.text_frame
        p_a = tf_a.paragraphs[0]
        p_a.text = "⚡ NTRO SPONSORING AGENCY"
        p_a.alignment = PP_ALIGN.RIGHT
        p_a.font.size = Pt(10)
        p_a.font.bold = True
        p_a.font.color.rgb = ACCENT_YELLOW
        p_a.font.name = "Arial"

        # Slide Number Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.533), Inches(0.35), Inches(1.0), Inches(0.38))
        badge.fill.solid()
        badge.fill.fore_color.rgb = CARD_BG
        badge.line.color.rgb = CYAN_GLOW
        badge.line.width = Pt(1)
        tf_b = badge.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = f"0{slide_num} / 06"
        p_b.alignment = PP_ALIGN.CENTER
        p_b.font.size = Pt(10)
        p_b.font.bold = True
        p_b.font.color.rgb = CYAN_GLOW

    def add_slide_header(slide, title_text, subtitle_text):
        box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.733), Inches(0.95))
        tf = box.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.font.name = "Arial"
        
        if subtitle_text:
            p2 = tf.add_paragraph()
            p2.text = subtitle_text
            p2.font.size = Pt(12)
            p2.font.color.rgb = TEXT_MUTED
            p2.font.name = "Arial"
            p2.space_before = Pt(4)

    # =========================================================
    # SLIDE 1: TITLE PAGE (Hero Visual)
    # =========================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_bg(slide1)
    
    # Outer Glow Accent Box
    hero = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.7), Inches(11.733), Inches(6.1))
    hero.fill.solid()
    hero.fill.fore_color.rgb = CARD_BG
    hero.line.color.rgb = CYAN_GLOW
    hero.line.width = Pt(2)
    
    tf1 = hero.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "SMART INDIA HACKATHON 2026  |  PROBLEM STATEMENT ID: SIH26163"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    p2 = tf1.add_paragraph()
    p2.text = "SECURITY ASSESSMENT OF WORLD MONITOR"
    p2.font.size = Pt(30)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(10)

    p3 = tf1.add_paragraph()
    p3.text = "Vulnerability Assessment & Penetration Testing (VAPT) Audit, Automated Test Suite & Code Patches"
    p3.font.size = Pt(15)
    p3.font.color.rgb = TEXT_BODY
    p3.space_before = Pt(8)

    # Metadata Grid Box
    meta_box = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(3.3), Inches(10.933), Inches(3.1))
    meta_box.fill.solid()
    meta_box.fill.fore_color.rgb = CARD_BG_ALT
    meta_box.line.color.rgb = RGBColor(51, 65, 85)
    
    tf_meta = meta_box.text_frame
    tf_meta.word_wrap = True
    
    meta_items = [
        ("Problem Statement ID:", "SIH26163 (Serial No. 163)", "Sponsoring Agency:", "National Technical Research Organisation (NTRO)"),
        ("PS Category:", "Software Edition", "Theme / Domain:", "Smart Automation / Cybersecurity"),
        ("Core Deliverables:", "VAPT Audit Report, Discovery Guide, Automated Test Harness, 5 Code Patches", "Team Name:", "Security Assessment Team")
    ]
    
    for idx, (l1, v1, l2, v2) in enumerate(meta_items):
        p = tf_meta.paragraphs[0] if idx == 0 else tf_meta.add_paragraph()
        r1 = p.add_run()
        r1.text = f"•  {l1} "
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = CYAN_GLOW
        
        r2 = p.add_run()
        r2.text = f"{v1}    |    "
        r2.font.size = Pt(13)
        r2.font.color.rgb = TEXT_WHITE
        
        r3 = p.add_run()
        r3.text = f"{l2} "
        r3.font.bold = True
        r3.font.size = Pt(13)
        r3.font.color.rgb = ACCENT_YELLOW

        r4 = p.add_run()
        r4.text = v2
        r4.font.size = Pt(13)
        r4.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(16)

    # =========================================================
    # SLIDE 2: PROPOSED SOLUTION & ARCHITECTURE
    # =========================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_bg(slide2)
    add_top_bar(slide2, 2)
    add_slide_header(slide2, "PROPOSED SOLUTION & PROTOTYPE OVERVIEW", "End-to-End VAPT Audit Framework, Automated Test Harness & Security Patches")

    cards2 = [
        ("VAPT Audit Framework", [
            "Evaluates 7 core vulnerability vectors across Vercel Edge Runtime proxies, CORS policies, session tokens, and DOM parsers.",
            "Maps every finding with root cause analysis, steps to reproduce, and CVSS v3.1 ratings."
        ], CYAN_GLOW, "7 VULNERABILITIES AUDITED"),
        ("NTRO Requirements Met", [
            "Delivers 5 production-ready code patches preventing cloud metadata exfiltration (169.254.169.254) and loopback access.",
            "Includes an executable Python test suite (run_security_audit.py) for CI/CD regression testing."
        ], ACCENT_YELLOW, "5 PRODUCTION PATCHES"),
        ("Key Innovation & Uniqueness", [
            "Socket-Pinned Edge DNS Resolution: Solves Vercel Edge Runtime DNS Rebinding (TOCTOU) via single-pass IP connection handling.",
            "Zero-Dependency Test Harness: Pure Python audit runner executing full security suite in <5s."
        ], ACCENT_GREEN, "< 5s EXECUTION RUNNER")
    ]

    for idx, (title, points, color, badge_text) in enumerate(cards2):
        x = Inches(0.8 + idx * 3.95)
        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.85), Inches(3.8), Inches(5.0))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        card.line.width = Pt(1.5)
        
        tf = card.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = color
        p.space_after = Pt(14)
        
        for pt in points:
            p2 = tf.add_paragraph()
            p2.text = "• " + pt
            p2.font.size = Pt(12.5)
            p2.font.color.rgb = TEXT_BODY
            p2.space_before = Pt(8)

        # Bottom Badge shape inside card
        badge_box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.3), Inches(6.15), Inches(3.2), Inches(0.4))
        badge_box.fill.solid()
        badge_box.fill.fore_color.rgb = CARD_BG_ALT
        badge_box.line.color.rgb = color
        badge_box.line.width = Pt(1)
        tf_b = badge_box.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = badge_text
        p_b.alignment = PP_ALIGN.CENTER
        p_b.font.size = Pt(10)
        p_b.font.bold = True
        p_b.font.color.rgb = color

    # =========================================================
    # SLIDE 3: TECHNICAL APPROACH & METHODOLOGY
    # =========================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_bg(slide3)
    add_top_bar(slide3, 3)
    add_slide_header(slide3, "TECHNICAL APPROACH & AUDIT METHODOLOGY", "Systematic Security Evaluation Process Grounded in OWASP WSTG v4.2 & NIST Standards")

    # Left Column - Tech Stack Card
    card_l = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.85), Inches(4.5), Inches(5.0))
    card_l.fill.solid()
    card_l.fill.fore_color.rgb = CARD_BG
    card_l.line.color.rgb = CYAN_GLOW
    card_l.line.width = Pt(1.5)
    tf_l = card_l.text_frame
    tf_l.word_wrap = True
    
    p = tf_l.paragraphs[0]
    p.text = "Technologies & Frameworks"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    
    t_items = [
        "Audit Suite: Python 3 (Runner & PoC Exploits).",
        "Target Edge APIs: TypeScript / JavaScript.",
        "Security Standards: OWASP WSTG v4.2, OWASP Top 10 API (2023), NIST SP 800-115.",
        "Metrics Standard: CVSS v3.1 Scoring.",
        "Architecture: Vercel Edge Runtime, Convex DB, Vite, DOMPurify."
    ]
    for item in t_items:
        p2 = tf_l.add_paragraph()
        p2.text = "✔  " + item
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_BODY
        p2.space_before = Pt(10)

    # Right Column - Audit Process Steps Card
    card_r = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.5), Inches(1.85), Inches(7.033), Inches(5.0))
    card_r.fill.solid()
    card_r.fill.fore_color.rgb = CARD_BG
    card_r.line.color.rgb = ACCENT_PURPLE
    card_r.line.width = Pt(1.5)
    tf_r = card_r.text_frame
    tf_r.word_wrap = True
    
    p = tf_r.paragraphs[0]
    p.text = "4-Phase Execution Pipeline"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    
    m_steps = [
        ("Phase 1: Static Code Audit (SAST)", "Line-by-line static analysis of Edge handlers (mcp-proxy.ts, rss-proxy.js, _cors.js)."),
        ("Phase 2: Edge Reverse Engineering", "Uncovering Time-of-Check Time-of-Use (TOCTOU) DNS rebinding gaps in Edge fetch calls."),
        ("Phase 3: Dynamic Verification & Exploit PoCs", "Executing Python-based test harness targeting loopback (127.0.0.1) & cloud metadata (169.254.169.254)."),
        ("Phase 4: Security Hardening & Patching", "Constructing production code patches for single-pass socket pinning and recursive redirect validation.")
    ]
    for step_title, step_desc in m_steps:
        p2 = tf_r.add_paragraph()
        p2.text = "▶  " + step_title
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = CYAN_GLOW
        p2.space_before = Pt(8)
        
        p3 = tf_r.add_paragraph()
        p3.text = "    " + step_desc
        p3.font.size = Pt(11.5)
        p3.font.color.rgb = TEXT_BODY
        p3.space_before = Pt(2)

    # =========================================================
    # SLIDE 4: FEASIBILITY & VULNERABILITY MATRIX
    # =========================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_bg(slide4)
    add_top_bar(slide4, 4)
    add_slide_header(slide4, "FEASIBILITY, RISKS & MITIGATION MATRIX", "Identified Security Findings & Code-Level Remediation Strategies")

    # Table of Vulnerabilities & Fixes
    rows, cols = 8, 5
    table_shape = slide4.shapes.add_table(rows, cols, Inches(0.8), Inches(1.85), Inches(11.733), Inches(5.0))
    table = table_shape.table

    table.columns[0].width = Inches(1.2)
    table.columns[1].width = Inches(3.8)
    table.columns[2].width = Inches(1.2)
    table.columns[3].width = Inches(1.2)
    table.columns[4].width = Inches(4.333)

    headers = ["ID", "Vulnerability Finding", "CVSS v3.1", "Severity", "Remediation Strategy & Patch File"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = CARD_BG
        for p in cell.text_frame.paragraphs:
            p.alignment = PP_ALIGN.CENTER
            p.font.size = Pt(12)
            p.font.bold = True
            p.font.color.rgb = CYAN_GLOW

    vulns_matrix = [
        ("VULN-01", "DNS Rebinding / TOCTOU SSRF in MCP Proxy", "8.2", "High", "Single-pass socket pinning (patch_mcp_proxy_ssrf.ts)"),
        ("VULN-02", "RSS Proxy Open Redirect Allowlist Bypass", "7.5", "High", "Recursive DNS IP validation (patch_rss_proxy_redirects.js)"),
        ("VULN-03", "Webhook Destination DNS Rebinding Gap", "7.2", "High", "Pinned IP HTTP dispatch validation (patch_webhook_ssrf.ts)"),
        ("VULN-04", "CORS Origin Echoing with Credentials", "6.5", "Medium", "Neutralizing Allow-Credentials on 403 (patch_cors_refusal.js)"),
        ("VULN-05", "Indefinite Anonymous Session Token Replay", "6.1", "Medium", "IP Subnet token binding & 1h TTL (patch_session_binding.js)"),
        ("VULN-06", "Client-Side DOM XSS Risk in RSS Parser", "6.1", "Medium", "Strict DOMPurify HTML sanitization (src/services/rss.ts)"),
        ("VULN-07", "Unbounded JSON Prefs Resource Exhaustion", "5.3", "Medium", "64KB payload size & depth limits (patch_user_prefs.ts)")
    ]

    for row_idx, data in enumerate(vulns_matrix, start=1):
        for col_idx, text in enumerate(data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_BG if row_idx % 2 == 0 else CARD_BG_ALT
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(11)
                p.font.color.rgb = TEXT_BODY
                if col_idx in [0, 2, 3]:
                    p.alignment = PP_ALIGN.CENTER
                if col_idx == 3:
                    p.font.bold = True
                    p.font.color.rgb = ACCENT_RED if text == "High" else ACCENT_YELLOW

    # =========================================================
    # SLIDE 5: IMPACT & BENEFITS
    # =========================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_bg(slide5)
    add_top_bar(slide5, 5)
    add_slide_header(slide5, "IMPACT AND OPERATIONAL BENEFITS FOR NTRO", "Infrastructure Security, Data Protection & Platform Resilience")

    # Card 1: Infrastructure Security
    c1 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.85), Inches(5.6), Inches(5.0))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = CYAN_GLOW
    c1.line.width = Pt(1.5)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "Infrastructure & Cloud Protection"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    
    b1 = [
        "Cloud Metadata Defense: Neutralizes requests to 169.254.169.254, protecting AWS EC2 / GCP instance tokens.",
        "Internal Service Isolation: Prevents malicious SSRF pivoting to loopback addresses (127.0.0.1:8080) and Redis ports.",
        "Serverless Resource Defense: Mitigates CPU resource exhaustion attacks on Vercel Edge functions."
    ]
    for pt in b1:
        p2 = tf1.add_paragraph()
        p2.text = "🛡️  " + pt
        p2.font.size = Pt(12.5)
        p2.font.color.rgb = TEXT_BODY
        p2.space_before = Pt(14)

    # Card 2: Operational Value
    c2 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.85), Inches(5.733), Inches(5.0))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = ACCENT_YELLOW
    c2.line.width = Pt(1.5)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "Platform Integrity & Turnkey Value"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_YELLOW
    
    b2 = [
        "Threat Dashboard Integrity: Guarantees OSINT threat intelligence feeds remain immune to stored DOM XSS payloads.",
        "Session Hardening: Binds anonymous session tokens to IP subnets and reduces token TTL from 12h to 1h.",
        "Turnkey Value for NTRO: Immediate production-ready code patches and automated CI/CD security regression test runner."
    ]
    for pt in b2:
        p2 = tf2.add_paragraph()
        p2.text = "⚡  " + pt
        p2.font.size = Pt(12.5)
        p2.font.color.rgb = TEXT_BODY
        p2.space_before = Pt(14)

    # =========================================================
    # SLIDE 6: RESEARCH & REFERENCES
    # =========================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_bg(slide6)
    add_top_bar(slide6, 6)
    add_slide_header(slide6, "RESEARCH, REFERENCES & REPOSITORY ASSETS", "Official Code Deliverables & Standard Framework References")

    box_final = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.85), Inches(11.733), Inches(5.0))
    box_final.fill.solid()
    box_final.fill.fore_color.rgb = CARD_BG
    box_final.line.color.rgb = CYAN_GLOW
    box_final.line.width = Pt(2)
    tf_f = box_final.text_frame
    tf_f.word_wrap = True

    p = tf_f.paragraphs[0]
    p.text = "Project Code Assets & Documentation"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    res_pts = [
        "Official GitHub Repository: https://github.com/Shr-i-raj/world-monitor-security-assessment",
        "Full VAPT Audit Report: SECURITY_ASSESSMENT_REPORT.md (Complete breakdown of 7 findings & CVSS v3.1 metrics)",
        "Discovery Methodology Guide: VULNERABILITY_DISCOVERY_METHODOLOGY.md (Step-by-step SAST & Edge reverse engineering guide)",
        "Automated Test Harness: security_tests/run_security_audit.py (Python verification suite)",
        "Security Hardening Patches: security_fixes/ (5 TypeScript / JavaScript patch files)"
    ]
    for pt in res_pts:
        p2 = tf_f.add_paragraph()
        p2.text = "🔗  " + pt
        p2.font.size = Pt(12.5)
        p2.font.color.rgb = TEXT_BODY
        p2.space_before = Pt(8)

    p_head2 = tf_f.add_paragraph()
    p_head2.text = "Industry Standards & Frameworks Followed"
    p_head2.font.size = Pt(15)
    p_head2.font.bold = True
    p_head2.font.color.rgb = ACCENT_YELLOW
    p_head2.space_before = Pt(16)

    stds = "OWASP Web Security Testing Guide (WSTG v4.2)  |  OWASP Top 10 API Security Risks (2023)  |  NIST SP 800-115  |  CVSS v3.1 Standard"
    p_stds = tf_f.add_paragraph()
    p_stds.text = stds
    p_stds.font.size = Pt(12)
    p_stds.font.color.rgb = TEXT_MUTED
    p_stds.space_before = Pt(4)

    prs.save("SIH_PRESENTATION_DECK.pptx")
    print("Successfully built visually stunning 6-slide SIH_PRESENTATION_DECK.pptx!")

if __name__ == "__main__":
    build_visual_deck()
