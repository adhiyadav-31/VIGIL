import os

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_disaster_html = '''        <div class="widget-grid" style="margin-bottom: 24px;">
          <!-- Risk Radar Card -->
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Predicted Risks Radar</h3>
            </header>
            <ul class="summary-list">
              <li style="justify-content:space-between; align-items:center;">
                <div><strong>Floods (Monsoon upcoming)</strong></div><span class="badge badge--red">High Risk</span>
              </li>
              <li style="justify-content:space-between; align-items:center;">
                <div><strong>Supply Chain Disruption</strong></div><span class="badge badge--red">High Risk</span>
              </li>
              <li style="justify-content:space-between; align-items:center;">
                <div><strong>Fire Hazard</strong></div><span class="badge badge--amber">Medium Risk</span>
              </li>
              <li style="justify-content:space-between; align-items:center;">
                <div><strong>Power Failures</strong></div><span class="badge badge--amber">Medium Risk</span>
              </li>
              <li style="justify-content:space-between; align-items:center;">
                <div><strong>Cyber Attack (Phishing)</strong></div><span class="badge badge--amber">Medium Risk</span>
              </li>
              <li style="justify-content:space-between; align-items:center;">
                <div><strong>Heat Waves</strong></div><span class="badge badge--green">Low Risk</span>
              </li>
              <li style="justify-content:space-between; align-items:center;">
                <div><strong>Pandemic</strong></div><span class="badge badge--green">Low Risk</span>
              </li>
            </ul>
          </article>
          
          <!-- Continuity Assets Card -->
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Continuity Recommendations</h3>
            </header>
            <ul class="summary-list">
              <li>
                <div>
                  <strong>Emergency Fund</strong>
                  <span class="meta">Target: ₹4,50,000 (3 months OPEX). Current gap: ₹1,20,000.</span>
                </div>
              </li>
              <li>
                <div>
                  <strong>Backup Supplier List</strong>
                  <span class="meta">Vendor B (Chennai) pre-approved for raw materials. Lead time: +2 days.</span>
                </div>
              </li>
              <li>
                <div>
                  <strong>Insurance Suggestions</strong>
                  <span class="meta">Upgrade current MSME package to cover "Business Interruption" (+₹3K/mo).</span>
                </div>
              </li>
            </ul>
          </article>

          <!-- Checklist & Recovery Plan -->
          <article class="card card--agent" style="grid-column: 1 / -1;">
            <header class="card__header">
              <div>
                <h3>Disaster Checklist & Recovery Plan</h3>
                <p class="card__subtitle">AI-generated step-by-step action plan</p>
              </div>
              <span class="badge badge--green">Active</span>
            </header>
            <div class="agent-body" style="margin-top: 16px;">
              <h4 style="margin-bottom:12px;">Immediate Checklist (Next 48 Hours)</h4>
              <ul class="insight-list" style="margin-bottom:24px;">
                <li>Back up all local accounting software data to cloud storage.</li>
                <li>Test emergency generator and purchase extra diesel reserves.</li>
                <li>Distribute emergency contact tree to all 18 employees.</li>
                <li>Move inventory stored on the ground floor to elevated racks (Flood risk).</li>
              </ul>
              <h4 style="margin-bottom:12px;">Long-Term Recovery Protocol</h4>
              <ul class="insight-list">
                <li>
                  <div><strong>Activate Alternate Vendor:</strong> <span class="meta">If primary supplier defaults due to disruption, trigger PO to Vendor B immediately.</span></div>
                </li>
                <li>
                  <div><strong>Liquidity Buffer:</strong> <span class="meta">In case of revenue halt, draw down from pre-approved MSME working capital overdraft.</span></div>
                </li>
                <li>
                  <div><strong>Remote Operations:</strong> <span class="meta">Shift sales team to fully remote work; reroute customer support lines to mobile.</span></div>
                </li>
              </ul>
            </div>
          </article>
        </div>'''

new_disaster_html = '''        <div class="widget-grid" style="margin-bottom: 24px;">
          <!-- Risk Radar Card -->
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Predicted Risks Radar</h3>
            </header>
            <ul class="summary-list">
              <li style="align-items:center;">
                <span class="dot dot--red"></span><div style="flex:1;"><strong>Floods (Monsoon upcoming)</strong></div><span class="badge badge--red">High Risk</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--red"></span><div style="flex:1;"><strong>Supply Chain Disruption</strong></div><span class="badge badge--red">High Risk</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--amber"></span><div style="flex:1;"><strong>Fire Hazard</strong></div><span class="badge badge--amber">Medium Risk</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--amber"></span><div style="flex:1;"><strong>Power Failures</strong></div><span class="badge badge--amber">Medium Risk</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--amber"></span><div style="flex:1;"><strong>Cyber Attack (Phishing)</strong></div><span class="badge badge--amber">Medium Risk</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--green"></span><div style="flex:1;"><strong>Heat Waves</strong></div><span class="badge badge--green">Low Risk</span>
              </li>
              <li style="align-items:center;">
                <span class="dot dot--green"></span><div style="flex:1;"><strong>Pandemic</strong></div><span class="badge badge--green">Low Risk</span>
              </li>
            </ul>
          </article>
          
          <!-- Continuity Assets Card -->
          <article class="card card--list card--span2">
            <header class="card__header">
              <h3>Continuity Recommendations</h3>
            </header>
            <ul class="summary-list">
              <li>
                <span class="dot dot--amber"></span>
                <div>
                  <strong>Emergency Fund</strong><br>
                  <span class="meta">Target: ₹4,50,000 (3 months OPEX). Current gap: ₹1,20,000.</span>
                </div>
              </li>
              <li>
                <span class="dot dot--green"></span>
                <div>
                  <strong>Backup Supplier List</strong><br>
                  <span class="meta">Vendor B (Chennai) pre-approved for raw materials. Lead time: +2 days.</span>
                </div>
              </li>
              <li>
                <span class="dot dot--amber"></span>
                <div>
                  <strong>Insurance Suggestions</strong><br>
                  <span class="meta">Upgrade current MSME package to cover "Business Interruption" (+₹3K/mo).</span>
                </div>
              </li>
            </ul>
          </article>

          <!-- Checklist & Recovery Plan -->
          <article class="card card--agent" style="grid-column: 1 / -1;">
            <header class="card__header">
              <div>
                <h3>Disaster Checklist & Recovery Plan</h3>
                <p class="card__subtitle">AI-generated step-by-step action plan</p>
              </div>
              <span class="badge badge--green">Active</span>
            </header>
            <div class="agent-body" style="margin-top: 16px;">
              <h4 style="margin-bottom:12px;">Immediate Checklist (Next 48 Hours)</h4>
              <ul class="summary-list" style="margin-bottom:24px;">
                <li><span class="dot dot--red"></span><div>Back up all local accounting software data to cloud storage.</div></li>
                <li><span class="dot dot--amber"></span><div>Test emergency generator and purchase extra diesel reserves.</div></li>
                <li><span class="dot dot--amber"></span><div>Distribute emergency contact tree to all 18 employees.</div></li>
                <li><span class="dot dot--amber"></span><div>Move inventory stored on the ground floor to elevated racks (Flood risk).</div></li>
              </ul>
              <h4 style="margin-bottom:12px;">Long-Term Recovery Protocol</h4>
              <ul class="summary-list">
                <li>
                  <span class="dot dot--amber"></span>
                  <div><strong>Activate Alternate Vendor:</strong><br> <span class="meta">If primary supplier defaults due to disruption, trigger PO to Vendor B immediately.</span></div>
                </li>
                <li>
                  <span class="dot dot--amber"></span>
                  <div><strong>Liquidity Buffer:</strong><br> <span class="meta">In case of revenue halt, draw down from pre-approved MSME working capital overdraft.</span></div>
                </li>
                <li>
                  <span class="dot dot--green"></span>
                  <div><strong>Remote Operations:</strong><br> <span class="meta">Shift sales team to fully remote work; reroute customer support lines to mobile.</span></div>
                </li>
              </ul>
            </div>
          </article>
        </div>'''

html = html.replace(old_disaster_html, new_disaster_html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
