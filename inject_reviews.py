import os

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add to navigation
old_nav = '<li><a href="#" class="nav-item" data-page="knowledge"><span class="nav-icon" aria-hidden="true">▥</span><span class="nav-label">Knowledge Base</span></a></li>'
new_nav = '''<li><a href="#" class="nav-item" data-page="reviews"><span class="nav-icon" aria-hidden="true">🛒</span><span class="nav-label">Review Intelligence</span></a></li>
        <li><a href="#" class="nav-item" data-page="knowledge"><span class="nav-icon" aria-hidden="true">▥</span><span class="nav-label">Knowledge Base</span></a></li>'''
html = html.replace(old_nav, new_nav)

# Add page section
new_page = """
      <!-- ============ PAGE: CUSTOMER REVIEW INTELLIGENCE ============ -->
      <section id="page-reviews" class="page page-section" data-page="reviews" hidden>
        <div class="page-header">
          <div>
            <h2>Customer Review Intelligence</h2>
            <p class="subtitle">Upload Amazon, Flipkart, and Google reviews for AI-powered competitor analysis and feature requests.</p>
          </div>
        </div>
        
        <!-- Upload State -->
        <div id="review-upload" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 60px 20px; text-align: center; border: 2px dashed var(--border-subtle); border-radius: 16px; margin-bottom: 24px; background: var(--bg-surface);">
          <div style="font-size: 3rem; margin-bottom: 20px;">📁</div>
          <h3 style="margin-bottom: 12px;">Upload Review Data</h3>
          <p class="meta" style="margin-bottom: 32px; max-width: 400px;">Supported formats: CSV, Excel (.xlsx), PDF, Word (.docx).</p>
          
          <div style="width: 100%; max-width: 400px; text-align: left;">
            <input type="file" id="review-file" class="form-field" accept=".csv, .xlsx, .pdf, .docx" style="margin-bottom: 16px; width: 100%;" />
            <button id="btn-analyze-reviews" class="btn btn--primary btn--full">Run AI Analysis</button>
          </div>
        </div>

        <!-- Analyzing State -->
        <div id="review-analyzing" style="display: none; flex-direction: column; align-items: center; justify-content: center; padding: 60px 20px; text-align: center;">
          <div class="loading-spinner" style="margin-bottom: 20px;"></div>
          <h3>AI is reading reviews...</h3>
          <p class="meta">Detecting complaints, feature requests, and benchmarking against competitors.</p>
        </div>

        <!-- Results Dashboard -->
        <div id="review-results" style="display: none;">
          <div class="widget-grid" style="margin-bottom: 24px;">
            
            <article class="card card--metric" style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.05)); border-color: rgba(239, 68, 68, 0.2);">
              <h3 style="color: var(--text-primary);">Critical Finding</h3>
              <div class="metric-val" style="font-size: 1.5rem; margin-top: 12px;">Delayed Delivery</div>
              <p class="meta" style="color: var(--text-primary);">Customers mention delayed delivery <strong style="color: #ef4444;">43% more</strong> than top competitors.</p>
            </article>

            <article class="card card--metric">
              <h3>Overall Sentiment</h3>
              <div class="metric-val">68 / 100</div>
              <p class="meta meta--positive">↑ 5% from last month</p>
            </article>
            
            <article class="card card--metric">
              <h3>Total Reviews Analyzed</h3>
              <div class="metric-val">1,248</div>
              <p class="meta">Amazon, Flipkart, Google</p>
            </article>

          </div>

          <div class="widget-grid">
            
            <article class="card card--list card--span2">
              <header class="card__header">
                <h3>Top Detected Complaints</h3>
              </header>
              <ul class="summary-list">
                <li style="align-items:flex-start;">
                  <span class="dot dot--red"></span>
                  <div style="flex:1;">
                    <strong>Packaging Damage during Transit</strong><br>
                    <span class="meta">Mentioned in 18% of 1-star and 2-star reviews. Primarily Flipkart orders.</span>
                  </div>
                  <span class="badge badge--red">High Priority</span>
                </li>
                <li style="align-items:flex-start;">
                  <span class="dot dot--red"></span>
                  <div style="flex:1;">
                    <strong>Sizing Inconsistency</strong><br>
                    <span class="meta">"Runs small" mentioned 124 times. Competitor 'BrandX' has fewer sizing complaints.</span>
                  </div>
                  <span class="badge badge--amber">Medium</span>
                </li>
              </ul>
            </article>
            
            <article class="card card--list card--span2">
              <header class="card__header">
                <h3>Frequently Requested Features</h3>
              </header>
              <ul class="summary-list">
                <li style="align-items:flex-start;">
                  <span class="dot dot--green"></span>
                  <div style="flex:1;">
                    <strong>More Color Variations</strong><br>
                    <span class="meta">Customers frequently ask for 'Navy Blue' and 'Olive Green'. High demand indicator.</span>
                  </div>
                  <span class="badge badge--green">Opportunity</span>
                </li>
                <li style="align-items:flex-start;">
                  <span class="dot dot--green"></span>
                  <div style="flex:1;">
                    <strong>Eco-Friendly Packaging</strong><br>
                    <span class="meta">Mentioned by 45 users. Aligning with this trend could boost brand perception.</span>
                  </div>
                </li>
              </ul>
            </article>

            <article class="card card--list" style="grid-column: 1 / -1;">
              <header class="card__header">
                <h3>AI Improvement Suggestions</h3>
              </header>
              <ul class="summary-list">
                <li style="align-items:center;">
                  <span class="dot dot--blue"></span>
                  <div style="flex:1;">
                    <strong>Supply Chain:</strong> Switch to double-corrugated boxes for Flipkart fulfillments to reduce transit damage by estimated 60%.
                  </div>
                </li>
                <li style="align-items:center;">
                  <span class="dot dot--blue"></span>
                  <div style="flex:1;">
                    <strong>Logistics:</strong> Renegotiate SLA with current logistics partner or switch to 'Delhivery' for Tier-2 cities to address the 43% delayed delivery gap.
                  </div>
                </li>
                <li style="align-items:center;">
                  <span class="dot dot--blue"></span>
                  <div style="flex:1;">
                    <strong>Product:</strong> Add a detailed sizing chart with exact measurements in cm/inches to all Amazon listings immediately.
                  </div>
                </li>
              </ul>
            </article>

          </div>
        </div>
      </section>
"""

html = html.replace('</main>', new_page + '\n    </main>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
