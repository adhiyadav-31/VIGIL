import os

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add to navigation
old_nav = '<li><a href="#" class="nav-item" data-page="knowledge"><span class="nav-icon" aria-hidden="true">▥</span><span class="nav-label">Knowledge Base</span></a></li>'
new_nav = '''<li><a href="#" class="nav-item" data-page="blueprint"><span class="nav-icon" aria-hidden="true">⚑</span><span class="nav-label">Success Blueprint</span></a></li>
        <li><a href="#" class="nav-item" data-page="knowledge"><span class="nav-icon" aria-hidden="true">▥</span><span class="nav-label">Knowledge Base</span></a></li>'''
html = html.replace(old_nav, new_nav)

# Add page section
new_page = """
      <!-- ============ PAGE: SUCCESS BLUEPRINT ============ -->
      <section id="page-blueprint" class="page page-section" data-page="blueprint" hidden>
        <div class="page-header">
          <div>
            <h2>MSME Success Blueprint</h2>
            <p class="subtitle">Actionable growth strategies derived from 12,450 anonymized top-performing MSMEs.</p>
          </div>
        </div>
        
        <div class="widget-grid" style="margin-bottom: 24px;">
          
          <article class="card card--metric">
            <header class="card__header"><h3>Cohort Analyzed</h3></header>
            <p class="metric-value">12,450</p>
            <p class="metric-caption">Similar textile & manufacturing MSMEs</p>
          </article>

          <article class="card card--metric" style="background: linear-gradient(135deg, rgba(31, 174, 110, 0.1), rgba(31, 174, 110, 0.05)); border-color: rgba(31, 174, 110, 0.2);">
            <header class="card__header"><h3 style="color: var(--text-primary);">Top Success Driver</h3></header>
            <p class="metric-value">Supplier Switch</p>
            <p class="metric-caption" style="color: var(--text-primary);">Led to a <strong style="color: #1FAE6E;">+34% margin</strong> increase on average.</p>
          </article>
          
          <article class="card card--metric">
            <header class="card__header"><h3>Optimal Team Size</h3></header>
            <p class="metric-value">+2 Hires</p>
            <p class="metric-caption">Top peers hired 2 extra QA staff.</p>
          </article>

        </div>

        <div class="widget-grid">
          
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Proven Success Strategies</h3>
            </header>
            <ul class="summary-list">
              <li style="align-items:flex-start;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>Changing Suppliers (Supply Chain)</strong><br>
                  <span class="meta">Businesses like yours saw a 15% margin increase immediately after diversifying local suppliers to cut freight costs.</span>
                </div>
                <span class="badge badge--green">High Impact</span>
              </li>
              <li style="align-items:flex-start;">
                <span class="dot dot--blue"></span>
                <div style="flex:1;">
                  <strong>Increasing Digital Marketing (Sales)</strong><br>
                  <span class="meta">Top performers increased digital ad spend by 20% exactly 6 weeks before festive seasons, resulting in 2.4x ROI.</span>
                </div>
                <span class="badge badge--blue">Growth</span>
              </li>
              <li style="align-items:flex-start;">
                <span class="dot dot--amber"></span>
                <div style="flex:1;">
                  <strong>Reducing Inventory (Operations)</strong><br>
                  <span class="meta">Reducing raw material holding time from 45 to 30 days prevented severe cash flow crunches in 88% of analyzed peers.</span>
                </div>
                <span class="badge badge--amber">Efficiency</span>
              </li>
              <li style="align-items:flex-start;">
                <span class="dot dot--blue"></span>
                <div style="flex:1;">
                  <strong>Hiring Specialized Staff (HR)</strong><br>
                  <span class="meta">Hiring two dedicated Quality Assurance employees reduced product return rates by an average of 40%.</span>
                </div>
                <span class="badge badge--blue">Quality</span>
              </li>
            </ul>
          </article>

          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Your Implementation Roadmap</h3>
            </header>
            <ul class="summary-list">
              <li style="align-items:center;">
                <span class="dot dot--blue"></span>
                <div style="flex:1;">
                  <strong>Step 1:</strong> Compare local suppliers in the Procurement AI tab to cut freight costs by 15%.
                </div>
                <button class="btn btn--primary" style="padding: 4px 12px; font-size: 0.8rem;">Do It</button>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--blue"></span>
                <div style="flex:1;">
                  <strong>Step 2:</strong> Allocate ₹20,000 to targeted Facebook Ads for the upcoming festive season.
                </div>
                <button class="btn" style="padding: 4px 12px; font-size: 0.8rem; background: var(--bg-surface-2); border: 1px solid var(--border-subtle); color: var(--text-primary);">Plan</button>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--blue"></span>
                <div style="flex:1;">
                  <strong>Step 3:</strong> Post two job listings for Quality Assurance Inspectors on local job boards.
                </div>
                <button class="btn" style="padding: 4px 12px; font-size: 0.8rem; background: var(--bg-surface-2); border: 1px solid var(--border-subtle); color: var(--text-primary);">Plan</button>
              </li>
            </ul>
          </article>

        </div>
      </section>
"""

html = html.replace('</main>', new_page + '\n    </main>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
