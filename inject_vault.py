import os
import re

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add to navigation
old_nav = '<li><a href="#" class="nav-item" data-page="knowledge"><span class="nav-icon" aria-hidden="true">▥</span><span class="nav-label">Knowledge Base</span></a></li>'
new_nav = '''<li><a href="#" class="nav-item" data-page="vault"><span class="nav-icon" aria-hidden="true">🔒</span><span class="nav-label">Secure Vault</span></a></li>
        <li><a href="#" class="nav-item" data-page="knowledge"><span class="nav-icon" aria-hidden="true">▥</span><span class="nav-label">Knowledge Base</span></a></li>'''
html = html.replace(old_nav, new_nav)

# Add page section
new_page = """
      <!-- ============ PAGE: SECURE VAULT ============ -->
      <section id="page-vault" class="page page-section" data-page="vault" hidden>
        <div class="page-header">
          <div>
            <h2>Secure Financial Vault</h2>
            <p class="subtitle">Encrypted, owner-only access to sensitive business documents.</p>
          </div>
        </div>
        
        <!-- Locked State -->
        <div id="vault-locked" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 60px 20px; text-align: center;">
          <div style="font-size: 3rem; margin-bottom: 20px;">🔒</div>
          <h3 style="margin-bottom: 12px;">Vault is Locked</h3>
          <p class="meta" style="margin-bottom: 32px; max-width: 400px;">This area contains highly sensitive financial and tax documents. Please enter your Owner Master Password to decrypt.</p>
          
          <div class="card" style="width: 100%; max-width: 400px; text-align: left;">
            <div class="form-field">
              <label for="vault-password">Master Password</label>
              <input type="password" id="vault-password" placeholder="Enter password to decrypt" />
            </div>
            <button id="btn-unlock-vault" class="btn btn--primary btn--full" style="margin-top: 16px;">Decrypt & Unlock Vault</button>
          </div>
        </div>

        <!-- Unlocked State -->
        <div id="vault-unlocked" class="widget-grid" style="display: none; margin-bottom: 24px;">
          
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Financial Statements</h3>
            </header>
            <ul class="summary-list">
              <li style="align-items:center;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>Balance Sheet (FY 23-24)</strong><br>
                  <span class="meta">Audited. Uploaded on 12 May 2024.</span>
                </div>
                <span class="badge badge--green">Encrypted</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>Cash Flow Projections (Q3)</strong><br>
                  <span class="meta">AI Generated. Uploaded on 01 Aug 2024.</span>
                </div>
                <span class="badge badge--green">Encrypted</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--amber"></span>
                <div style="flex:1;">
                  <strong>Bank Statements (Last 6 Months)</strong><br>
                  <span class="meta">HDFC Current Account. Uploaded on 05 Aug 2024.</span>
                </div>
                <span class="badge badge--amber">Encrypted</span>
              </li>
            </ul>
          </article>
          
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Tax & Legal Documents</h3>
            </header>
            <ul class="summary-list">
              <li style="align-items:center;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>GST Returns (GSTR-3B)</strong><br>
                  <span class="meta">July 2024. Uploaded on 20 Aug 2024.</span>
                </div>
                <span class="badge badge--green">Encrypted</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>Tax Returns (ITR-4)</strong><br>
                  <span class="meta">AY 2024-25. Uploaded on 15 Jul 2024.</span>
                </div>
                <span class="badge badge--green">Encrypted</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--amber"></span>
                <div style="flex:1;">
                  <strong>Loan Documents</strong><br>
                  <span class="meta">Working Capital Sanction Letter. Uploaded on 10 Jan 2024.</span>
                </div>
                <span class="badge badge--amber">Encrypted</span>
              </li>
            </ul>
          </article>

        </div>
      </section>
"""

html = html.replace('</main>', new_page + '\n    </main>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
