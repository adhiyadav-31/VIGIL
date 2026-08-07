import os

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add to navigation
old_nav = '<li><a href="#" class="nav-item" data-page="disaster"><span class="nav-icon" aria-hidden="true">⚠</span><span class="nav-label">Disaster Planner</span></a></li>'
new_nav = '''<li><a href="#" class="nav-item" data-page="disaster"><span class="nav-icon" aria-hidden="true">⚠</span><span class="nav-label">Disaster Planner</span></a></li>
        <li><a href="#" class="nav-item" data-page="expansion"><span class="nav-icon" aria-hidden="true">⌖</span><span class="nav-label">Expansion Scanner</span></a></li>
        <li><a href="#" class="nav-item" data-page="land"><span class="nav-icon" aria-hidden="true">⛶</span><span class="nav-label">Land Advisor</span></a></li>'''
html = html.replace(old_nav, new_nav)

# Add page sections
new_pages = """
      <!-- ============ PAGE: EXPANSION SCANNER ============ -->
      <section id="page-expansion" class="page page-section" data-page="expansion" hidden>
        <div class="page-header">
          <div>
            <h2>Business Expansion Opportunity Scanner</h2>
            <p class="subtitle">AI-identified new cities, demand hotspots, and export markets based on your product profile.</p>
          </div>
        </div>
        <div class="widget-grid" style="margin-bottom: 24px;">
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Domestic Hotspots & Districts</h3>
            </header>
            <ul class="summary-list">
              <li style="align-items:center;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>Coimbatore, Tamil Nadu</strong><br>
                  <span class="meta">Surging demand for textile machinery components. Competitor saturation: Low.</span>
                </div>
                <span class="badge badge--green">92% Match</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>Pune, Maharashtra (Chakan Hub)</strong><br>
                  <span class="meta">High density of tier-2 auto OEMs seeking localized suppliers.</span>
                </div>
                <span class="badge badge--green">85% Match</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--amber"></span>
                <div style="flex:1;">
                  <strong>Bhubaneswar, Odisha</strong><br>
                  <span class="meta">Emerging market. Requires specialized logistics setup.</span>
                </div>
                <span class="badge badge--amber">68% Match</span>
              </li>
            </ul>
          </article>
          
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Untapped Export Markets</h3>
            </header>
            <ul class="summary-list">
              <li style="align-items:center;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>Vietnam (Ho Chi Minh City)</strong><br>
                  <span class="meta">Free Trade Agreement benefits active. 21% deficit in local raw materials.</span>
                </div>
                <span class="badge badge--green">Highly Viable</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--amber"></span>
                <div style="flex:1;">
                  <strong>UAE (Jebel Ali Free Zone)</strong><br>
                  <span class="meta">Gateway to MENA. High initial setup costs but fast clearance.</span>
                </div>
                <span class="badge badge--amber">Medium Effort</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--red"></span>
                <div style="flex:1;">
                  <strong>Germany (Bavaria)</strong><br>
                  <span class="meta">High demand, but strict ESG and CE certification barriers present.</span>
                </div>
                <span class="badge badge--red">Long-Term</span>
              </li>
            </ul>
          </article>

          <article class="card card--agent" style="grid-column: 1 / -1;">
            <header class="card__header">
              <div>
                <h3>AI Expansion Probability Summary</h3>
                <p class="card__subtitle">Predicted likelihood of success within 18 months</p>
              </div>
              <span class="badge badge--green">Active</span>
            </header>
            <div class="agent-body" style="margin-top: 16px;">
              <h4 style="margin-bottom:12px;">Recommendation: Prioritize Coimbatore Hub</h4>
              <ul class="summary-list">
                <li>
                  <span class="dot dot--green"></span>
                  <div><strong>Success Probability: 89%</strong><br> <span class="meta">Based on current capital liquidity, existing supply chain proximity, and low competitor presence in the target district.</span></div>
                </li>
                <li>
                  <span class="dot dot--amber"></span>
                  <div><strong>Key Risk Factor:</strong><br> <span class="meta">Talent acquisition for specialized mid-level management in a new cultural/linguistic zone. AI suggests hiring a local recruitment agency 3 months prior to launch.</span></div>
                </li>
              </ul>
            </div>
          </article>
        </div>
      </section>

      <!-- ============ PAGE: LAND ADVISOR ============ -->
      <section id="page-land" class="page page-section" data-page="land" hidden>
        <div class="page-header">
          <div>
            <h2>AI Industrial Land & Expansion Advisor</h2>
            <p class="subtitle">Data-driven evaluation of industrial parks, infrastructure, and ROI for your new facility.</p>
          </div>
        </div>
        <div class="widget-grid" style="margin-bottom: 24px;">
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Industrial Park Comparisons (Budget: ₹2.5Cr)</h3>
            </header>
            <ul class="summary-list">
              <li style="align-items:center;">
                <span class="dot dot--green"></span>
                <div style="flex:1;">
                  <strong>Sri City SEZ, Andhra Pradesh</strong><br>
                  <span class="meta">Plot Size: 2 Acres. Cost: ₹2.1Cr. Excellent ecosystem.</span>
                </div>
                <span class="badge badge--green">Top Pick</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--amber"></span>
                <div style="flex:1;">
                  <strong>Sanand GIDC, Gujarat</strong><br>
                  <span class="meta">Plot Size: 1.5 Acres. Cost: ₹2.4Cr. Auto-hub premium pricing.</span>
                </div>
                <span class="badge badge--amber">Runner Up</span>
              </li>
            </ul>
          </article>
          
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Sri City SEZ: Infrastructure & Ecosystem</h3>
            </header>
            <ul class="summary-list">
              <li>
                <span class="dot dot--green"></span>
                <div>
                  <strong>Connectivity & Logistics</strong><br>
                  <span class="meta">NH-16 adjacent (2km). Nearest Port: Krishnapatnam (70km). Rail depot inside SEZ.</span>
                </div>
              </li>
              <li>
                <span class="dot dot--green"></span>
                <div>
                  <strong>Utilities & Labour</strong><br>
                  <span class="meta">33kV dedicated substation. 2MGD water allocation. Semi-skilled labour readily available from nearby districts.</span>
                </div>
              </li>
              <li>
                <span class="dot dot--green"></span>
                <div>
                  <strong>B2B Proximity</strong><br>
                  <span class="meta">4 major raw material suppliers within 50km radius. 12 potential enterprise customers within 100km.</span>
                </div>
              </li>
            </ul>
          </article>

          <article class="card card--agent" style="grid-column: 1 / -1;">
            <header class="card__header">
              <div>
                <h3>Government Incentives & Expansion ROI</h3>
                <p class="card__subtitle">Financial projections and subsidy utilization</p>
              </div>
              <span class="badge badge--green">Active</span>
            </header>
            <div class="agent-body" style="margin-top: 16px;">
              <h4 style="margin-bottom:12px;">Financial Modeling (3-Year Horizon)</h4>
              <ul class="summary-list">
                <li>
                  <span class="dot dot--green"></span>
                  <div><strong>State Incentives (AP Industrial Policy 2023-27):</strong><br> <span class="meta">Eligible for 100% stamp duty reimbursement, ₹1/unit power subsidy for 5 years, and 15% investment subsidy on fixed capital.</span></div>
                </li>
                <li>
                  <span class="dot dot--green"></span>
                  <div><strong>Predicted ROI:</strong><br> <span class="meta">22.4% Annualized ROI. Break-even projected at month 28 of operations, assuming 60% capacity utilization in year 1.</span></div>
                </li>
              </ul>
            </div>
          </article>
        </div>
      </section>
"""

html = html.replace('</main>', new_pages + '\n    </main>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
