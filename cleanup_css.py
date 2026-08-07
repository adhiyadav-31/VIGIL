import os

css_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

metric_css = '''
/* ==========================================================================
   BENCHMARK INTELLIGENCE
   ========================================================================== */
.metric-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.metric-card h3 {
  font-size: .9rem;
  color: var(--text-secondary);
  font-weight: 600;
}
.metric-card .trend {
  font-size: .85rem;
  color: var(--text-primary);
  line-height: 1.4;
}
.benchmark-ai-panel {
  background: var(--bg-surface-2);
  border: 1px solid var(--blue-600, #2952E3);
  box-shadow: 0 4px 20px rgba(41, 82, 227, 0.08);
}'''

css = css.replace(metric_css, '')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
