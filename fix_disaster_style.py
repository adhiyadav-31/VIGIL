import os

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_html = '''        <div class="dashboard-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); margin-bottom: 24px;">
          <!-- Risk Radar Card -->
          <div class="card">
            <header class="card__header">
              <h3>Predicted Risks Radar</h3>
            </header>
            <ul style="list-style:none; padding:0; margin-top:12px; display:flex; flex-direction:column; gap:10px;">
              <li style="display:flex; justify-content:space-between; align-items:center;">
                <span>🌊 Floods (Monsoon upcoming)</span><span class="badge badge--red">High Risk</span>
              </li>
              <li style="display:flex; justify-content:space-between; align-items:center;">
                <span>🔗 Supply Chain Disruption</span><span class="badge badge--red">High Risk</span>
              </li>
              <li style="display:flex; justify-content:space-between; align-items:center;">
                <span>🔥 Fire Hazard</span><span class="badge badge--amber">Medium Risk</span>
              </li>
              <li style="display:flex; justify-content:space-between; align-items:center;">
                <span>⚡ Power Failures</span><span class="badge badge--amber">Medium Risk</span>
              </li>
              <li style="display:flex; justify-content:space-between; align-items:center;">
                <span>💻 Cyber Attack (Phishing)</span><span class="badge badge--amber">Medium Risk</span>
              </li>
              <li style="display:flex; justify-content:space-between; align-items:center;">
                <span>🌡️ Heat Waves</span><span class="badge badge--green">Low Risk</span>
              </li>
              <li style="display:flex; justify-content:space-between; align-items:center;">
                <span>🦠 Pandemic</span><span class="badge badge--green">Low Risk</span>
              </li>
            </ul>
          </div>
          
          <!-- Continuity Assets Card -->
          <div class="card">
            <header class="card__header">
              <h3>Continuity Recommendations</h3>
            </header>
            <div style="margin-top:12px; display:flex; flex-direction:column; gap:18px;">
              <div>
                <h4 style="font-size:.9rem; color:var(--text-primary); margin-bottom:4px;">Emergency Fund</h4>
                <p style="font-size:.85rem; color:var(--text-secondary);">Target: ₹4,50,000 (3 months OPEX). Current gap: ₹1,20,000.</p>
              </div>
              <div>
                <h4 style="font-size:.9rem; color:var(--text-primary); margin-bottom:4px;">Backup Supplier List</h4>
                <p style="font-size:.85rem; color:var(--text-secondary);">Vendor B (Chennai) pre-approved for raw materials. Lead time: +2 days.</p>
              </div>
              <div>
                <h4 style="font-size:.9rem; color:var(--text-primary); margin-bottom:4px;">Insurance Suggestions</h4>
                <p style="font-size:.85rem; color:var(--text-secondary);">Upgrade current MSME package to cover "Business Interruption" (+₹3K/mo).</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Checklist & Recovery Plan -->
        <div class="card card--agent">
          <header class="card__header">
            <div>
              <h3>Disaster Checklist & Recovery Plan</h3>
              <p class="card__subtitle" style="margin-top: 4px;">AI-generated step-by-step action plan</p>
            </div>
            <span class="badge badge--green">Active</span>
          </header>
          <div class="agent-body" style="margin-top: 16px; font-size: .95rem; line-height: 1.6;">
            <h4 style="margin-bottom:8px; color:var(--text-primary);">Immediate Checklist (Next 48 Hours)</h4>
            <ul style="padding-left:20px; margin-bottom:24px; color:var(--text-secondary);">
              <li>Back up all local accounting software data to cloud storage.</li>
              <li>Test emergency generator and purchase extra diesel reserves.</li>
              <li>Distribute emergency contact tree to all 18 employees.</li>
              <li>Move inventory stored on the ground floor to elevated racks (Flood risk).</li>
            </ul>
            <h4 style="margin-bottom:8px; color:var(--text-primary);">Long-Term Recovery Protocol</h4>
            <ol style="padding-left:20px; color:var(--text-secondary);">
              <li style="margin-bottom:8px;"><strong>Activate Alternate Vendor:</strong> If primary supplier defaults due to disruption, trigger PO to Vendor B immediately.</li>
              <li style="margin-bottom:8px;"><strong>Liquidity Buffer:</strong> In case of revenue halt, draw down from pre-approved MSME working capital overdraft.</li>
              <li><strong>Remote Operations:</strong> Shift sales team to fully remote work; reroute customer support lines to mobile.</li>
            </ol>
          </div>
        </div>'''

new_html = '''        <div class="widget-grid" style="margin-bottom: 24px;">
          <!-- Risk Radar Card -->
          <article class="card card--list">
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
          <article class="card card--list">
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
        </div>

        <!-- Checklist & Recovery Plan -->
        <article class="card card--agent">
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
        </article>'''

html = html.replace(old_html, new_html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
