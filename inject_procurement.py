import os

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add to navigation
old_nav = '<li><a href="#" class="nav-item" data-page="knowledge"><span class="nav-icon" aria-hidden="true">▥</span><span class="nav-label">Knowledge Base</span></a></li>'
new_nav = '''<li><a href="#" class="nav-item" data-page="procurement"><span class="nav-icon" aria-hidden="true">⛟</span><span class="nav-label">Procurement AI</span></a></li>
        <li><a href="#" class="nav-item" data-page="knowledge"><span class="nav-icon" aria-hidden="true">▥</span><span class="nav-label">Knowledge Base</span></a></li>'''
html = html.replace(old_nav, new_nav)

# Add page section
new_page = """
      <!-- ============ PAGE: PROCUREMENT INTELLIGENCE ============ -->
      <section id="page-procurement" class="page page-section" data-page="procurement" hidden>
        <div class="page-header">
          <div>
            <h2>Procurement Intelligence</h2>
            <p class="subtitle">AI-driven supplier recommendations and raw material price predictions.</p>
          </div>
        </div>
        
        <div class="widget-grid" style="margin-bottom: 24px;">
          
          <article class="card card--metric" style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.05)); border-color: rgba(239, 68, 68, 0.2);">
            <header class="card__header"><h3 style="color: var(--text-primary);">Cotton Yarn Prediction</h3></header>
            <p class="metric-value">₹245<span>/kg</span></p>
            <p class="metric-caption" style="color: var(--text-primary);">Predicted to rise <strong style="color: #ef4444;">12%</strong> by next quarter.</p>
          </article>

          <article class="card card--metric">
            <header class="card__header"><h3>Best Seasonal Purchase</h3></header>
            <p class="metric-value">Mid-October</p>
            <p class="metric-caption" style="color: var(--green-500, #1FAE6E);">Historically lowest prices post-harvest.</p>
          </article>
          
          <article class="card card--metric">
            <header class="card__header"><h3>Freight Optimization</h3></header>
            <p class="metric-value">-₹4,200<span>/trip</span></p>
            <p class="metric-caption">By switching to local supplier cluster.</p>
          </article>

        </div>

        <div class="widget-grid">
          
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Supplier Leaderboard</h3>
            </header>
            <ul class="summary-list">
              <li style="align-items:flex-start;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>Cheapest Supplier: Rajesh Textiles</strong><br>
                  <span class="meta">₹420/kg. High volume discount applied.</span>
                </div>
                <span class="badge badge--green">Cost Leader</span>
              </li>
              <li style="align-items:flex-start;">
                <span class="dot dot--amber"></span>
                <div style="flex:1;">
                  <strong>Fastest Supplier: Metro Weavers</strong><br>
                  <span class="meta">2 Days SLA. Local fulfillment center in Hyderabad.</span>
                </div>
                <span class="badge badge--amber">Speed Leader</span>
              </li>
              <li style="align-items:flex-start;">
                <span class="dot dot--blue"></span>
                <div style="flex:1;">
                  <strong>Highest Rated: Global Synthetics</strong><br>
                  <span class="meta">4.8/5 Stars (120 orders). 99.8% quality pass rate.</span>
                </div>
                <span class="badge badge--blue">Quality Leader</span>
              </li>
            </ul>
          </article>

          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>AI Procurement Strategy</h3>
            </header>
            <ul class="summary-list">
              <li style="align-items:center;">
                <span class="dot dot--blue"></span>
                <div style="flex:1;">
                  <strong>Immediate Action:</strong> Stockpile Cotton Yarn now before the predicted 12% price hike next quarter.
                </div>
                <button class="btn btn--primary" style="padding: 4px 12px; font-size: 0.8rem;">Auto-Draft PO</button>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--blue"></span>
                <div style="flex:1;">
                  <strong>Logistics Shift:</strong> Shift 40% of emergency orders to Metro Weavers to cut transit time by 5 days.
                </div>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--blue"></span>
                <div style="flex:1;">
                  <strong>Contract Renewal:</strong> Renegotiate terms with Rajesh Textiles using Global Synthetics' pricing as leverage.
                </div>
              </li>
            </ul>
          </article>

        </div>
      </section>
"""

html = html.replace('</main>', new_page + '\n    </main>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
