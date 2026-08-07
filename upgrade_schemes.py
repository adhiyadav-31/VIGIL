import os
import re

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update Navigation
html = html.replace('<span class="nav-icon" aria-hidden="true">🏛</span><span class="nav-label">Government Schemes</span>', '<span class="nav-icon" aria-hidden="true">🏛</span><span class="nav-label">Grant & Subsidy Hunter</span>')

# Update Page Content
old_section_pattern = r'<!-- ============ PAGE: GOVERNMENT SCHEMES ============ -->\s*<section class="page" id="page-schemes" data-page="schemes" aria-labelledby="schemes-title">\s*<div class="page-header"><h1 id="schemes-title">Government Schemes</h1><p>Programs your business may currently be eligible for\.</p></div>\s*<div class="reco-grid" id="schemesGrid"></div>\s*</section>'

new_section = '''<!-- ============ PAGE: AI GRANT & SUBSIDY HUNTER ============ -->
      <section class="page page-section" id="page-schemes" data-page="schemes" aria-labelledby="schemes-title" hidden>
        <div class="page-header">
          <div>
            <h1 id="schemes-title" style="margin-bottom:8px; font-size:1.8rem; font-weight:700;">AI Grant & Subsidy Hunter</h1>
            <p class="subtitle">AI automatically checks your profile against 400+ Central and State schemes, MSME loans, and Export incentives.</p>
          </div>
        </div>

        <div class="widget-grid" style="margin-bottom: 24px;">
          <!-- Top Matches -->
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Top Eligible Grants & Subsidies</h3>
            </header>
            <ul class="summary-list">
              <li style="align-items:center;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>PMEGP (Prime Minister's Employment Gen.)</strong><br>
                  <span class="meta">Central Scheme. Up to 35% margin money subsidy.</span>
                </div>
                <span class="badge badge--green">99% Match</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>Credit Guarantee Scheme (CGTMSE)</strong><br>
                  <span class="meta">MSME Loan. Guarantee cover up to ₹500 Lakh.</span>
                </div>
                <span class="badge badge--green">95% Match</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--amber"></span>
                <div style="flex:1;">
                  <strong>RoDTEP (Export Incentives)</strong><br>
                  <span class="meta">Export Incentive. Rebate on central/state/local duties.</span>
                </div>
                <span class="badge badge--amber">72% Match</span>
              </li>
            </ul>
          </article>
          
          <!-- Eligibility & Deadlines -->
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Eligibility Check & Deadlines</h3>
            </header>
            <ul class="summary-list">
              <li>
                <span class="dot dot--green"></span>
                <div>
                  <strong>Why You Qualify for PMEGP:</strong><br>
                  <span class="meta">Your manufacturing turnover (₹1.8L/mo) and NIC code (Textiles) perfectly match the threshold.</span>
                </div>
              </li>
              <li>
                <span class="dot dot--red"></span>
                <div>
                  <strong>Deadline Alert: CGTMSE Application</strong><br>
                  <span class="meta">Your bank's next credit cycle closes on 15th Sept. Application must be submitted by 5th Sept.</span>
                </div>
              </li>
              <li>
                <span class="dot dot--amber"></span>
                <div>
                  <strong>RoDTEP Missing Requirement:</strong><br>
                  <span class="meta">You need to update your IEC (Import Export Code) profile with the DGFT.</span>
                </div>
              </li>
            </ul>
          </article>

          <!-- Auto-fill Agent -->
          <article class="card card--agent" style="grid-column: 1 / -1;">
            <header class="card__header">
              <div>
                <h3>PMEGP Application Auto-Fill Agent</h3>
                <p class="card__subtitle">AI has generated your checklist and prepared your application.</p>
              </div>
              <span class="badge badge--green">Ready to Apply</span>
            </header>
            <div class="agent-body" style="margin-top: 16px;">
              <h4 style="margin-bottom:12px;">Document Compliance Checklist</h4>
              <ul class="summary-list" style="margin-bottom:24px;">
                <li><span class="dot dot--green"></span><div><strong>Udyam Registration:</strong> Attached (Verified)</div></li>
                <li><span class="dot dot--green"></span><div><strong>Aadhaar Card:</strong> Attached (Verified)</div></li>
                <li><span class="dot dot--amber"></span><div><strong>Project Report:</strong> AI draft generated. Requires your review.</div></li>
                <li><span class="dot dot--red"></span><div><strong>Category Certificate (if applicable):</strong> Missing. Please upload.</div></li>
              </ul>
              
              <div style="display: flex; gap: 12px; margin-top: 20px;">
                <button type="button" class="btn btn--primary">⚡ Auto-Fill Application on Portal</button>
                <button type="button" class="btn" style="background:var(--bg-surface-2); border:1px solid var(--border-subtle); color:var(--text-primary);">Review AI Project Report</button>
              </div>
            </div>
          </article>
        </div>
      </section>'''

html = re.sub(old_section_pattern, new_section, html, flags=re.MULTILINE)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
