import os

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

nav_item = '        <li><a href="#" class="nav-item" data-page="benchmark"><span class="nav-icon" aria-hidden="true">📈</span><span class="nav-label">Benchmark Intelligence</span></a></li>\n'
html = html.replace('<li><a href="#" class="nav-item" data-page="knowledge"', nav_item + '        <li><a href="#" class="nav-item" data-page="knowledge"')

benchmark_section = """
      <!-- ============ PAGE: BENCHMARK INTELLIGENCE ============ -->
      <section id="page-benchmark" class="page-section" hidden>
        <div class="page-header">
          <div>
            <h2>Anonymous MSME Benchmark Intelligence</h2>
            <p class="subtitle">See how your business compares to similar top-performing MSMEs in your region.</p>
          </div>
        </div>

        <div class="dashboard-grid" style="grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); margin-bottom: 24px;">
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
        </div>

        <div class="card benchmark-ai-panel">
          <div class="card-header" style="border-bottom: 1px solid var(--border-subtle); padding-bottom: 12px; margin-bottom: 16px;">
            <h3>AI Explanation & Action Plan</h3>
            <p style="color: var(--text-secondary); font-size: .85rem; margin-top: 4px;">How to reach these benchmarks</p>
          </div>
          <div id="benchmarkAiContent" style="font-size: .95rem; line-height: 1.6;">
            <!-- Rendered via JS -->
          </div>
        </div>
      </section>
"""

html = html.replace('</main>', benchmark_section + '\n    </main>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
