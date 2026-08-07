import os

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the icon in sidebar
html = html.replace('<span class="nav-icon" aria-hidden="true">📈</span>', '<span class="nav-icon" aria-hidden="true">▧</span>')

old_grid = '''        <div class="dashboard-grid" style="grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); margin-bottom: 24px;">
          <div class="metric-card">
            <h3>Revenue Comparison</h3>
            <div class="value" style="color: var(--green-600); font-size: 1.5rem;">+18%</div>
            <p class="trend">Similar businesses earn 18% higher revenue</p>
          </div>
          <div class="metric-card">
            <h3>Inventory Turnover</h3>
            <div class="value" style="color: var(--green-600); font-size: 1.5rem;">+22%</div>
            <p class="trend">Their inventory turnover is 22% better</p>
          </div>
          <div class="metric-card">
            <h3>Procurement Cost</h3>
            <div class="value" style="color: var(--green-600); font-size: 1.5rem;">-11%</div>
            <p class="trend">Top MSMEs in Hyderabad spend 11% less</p>
          </div>
          <div class="metric-card">
            <h3>Team Size Efficiency</h3>
            <div class="value" style="color: var(--green-600); font-size: 1.5rem;">-3</div>
            <p class="trend">Businesses with similar size hire 3 fewer employees</p>
          </div>
        </div>'''

new_grid = '''        <div class="widget-grid" style="margin-bottom: 24px;">
          <article class="card card--metric">
            <header class="card__header"><h3>Revenue Comparison</h3></header>
            <p class="metric-value" style="color: var(--green-500, #1FAE6E);">+18<span>%</span></p>
            <p class="metric-caption">Similar businesses earn 18% higher revenue</p>
          </article>
          <article class="card card--metric">
            <header class="card__header"><h3>Inventory Turnover</h3></header>
            <p class="metric-value" style="color: var(--green-500, #1FAE6E);">+22<span>%</span></p>
            <p class="metric-caption">Their inventory turnover is 22% better</p>
          </article>
          <article class="card card--metric">
            <header class="card__header"><h3>Procurement Cost</h3></header>
            <p class="metric-value" style="color: var(--green-500, #1FAE6E);">-11<span>%</span></p>
            <p class="metric-caption">Top MSMEs in Hyderabad spend 11% less</p>
          </article>
          <article class="card card--metric">
            <header class="card__header"><h3>Team Size Efficiency</h3></header>
            <p class="metric-value" style="color: var(--green-500, #1FAE6E);">-3</p>
            <p class="metric-caption">Businesses with similar size hire 3 fewer employees</p>
          </article>
        </div>'''

html = html.replace(old_grid, new_grid)

# Adjust AI panel style to match other panels
old_panel = '''        <div class="card benchmark-ai-panel">
          <div class="card-header" style="border-bottom: 1px solid var(--border-subtle); padding-bottom: 12px; margin-bottom: 16px;">
            <h3>AI Explanation & Action Plan</h3>
            <p style="color: var(--text-secondary); font-size: .85rem; margin-top: 4px;">How to reach these benchmarks</p>
          </div>
          <div id="benchmarkAiContent" style="font-size: .95rem; line-height: 1.6;">
            <!-- Rendered via JS -->
          </div>
        </div>'''

new_panel = '''        <div class="card card--agent">
          <header class="card__header">
            <div>
              <h3>AI Explanation & Action Plan</h3>
              <p class="card__subtitle" style="margin-top: 4px;">How to reach these benchmarks</p>
            </div>
            <span class="badge badge--green">Active</span>
          </header>
          <div class="agent-body" id="benchmarkAiContent" style="margin-top: 16px; font-size: .95rem; line-height: 1.6;">
            <!-- Rendered via JS -->
          </div>
        </div>'''

html = html.replace(old_panel, new_panel)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
