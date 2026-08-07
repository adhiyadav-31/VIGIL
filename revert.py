import re
import os

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="style.css?v=2"', 'href="style.css"')
html = html.replace('src="script.js?v=2"', 'src="script.js"')

aside = """
          <aside class="card checkin-tip">
            <h3>Why this matters</h3>
            <p>Daily check-ins feed the CFO and Risk agents directly, tightening distress predictions by up to 22% compared to monthly-only data.</p>
            <ul class="tip-list">
              <li>Takes under 2 minutes</li>
              <li>Auto-saves as you type</li>
              <li>Streak: <strong>11 days</strong></li>
            </ul>
          </aside>
"""

if 'Why this matters' not in html:
    html = html.replace('</form>\n\n        </div>', '</form>\n' + aside + '        </div>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

css_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('  font-family: var(--font-mono, monospace);\n  user-select: none;\n}', '  font-family: var(--font-mono, monospace);\n}')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

js_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\script.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

js = re.sub(r'<article class="reco-card" style="cursor:pointer;" data-priority="\$\{r\.priority\}" onclick="openModal[^"]+">', r'<article class="reco-card" data-priority="${r.priority}">', js)
js = re.sub(r'<article class="agent-card" style="--agent-color:\$\{a\.color\}; cursor:pointer;" onclick="openModal[^"]+">', r'<article class="agent-card" style="--agent-color:${a.color}">', js)
js = re.sub(r'<li style="cursor:pointer;" onclick="openModal[^"]+"><div><h4>\$\{s\.title\}</h4><p>\$\{s\.body\}</p></div></li>', r'<li><div><h4>${s.title}</h4><p>${s.body}</p></div></li>', js)

js = js.replace('if (newProd) newProd.addEventListener(\'change\', triggerSimulation);\n    if (newBranch) newBranch.addEventListener(\'change\', triggerSimulation);\n', '')
js = js.replace('          if (typeof triggerSimulation === \'function\') triggerSimulation();\n', '')

old_faq = """    faq: [
      { q: 'How often does VigilAI refresh my health score?', a: 'Your Business Health Score recalculates hourly using your latest check-ins, transactions and connected data sources.' },
      { q: 'Can I export data for my accountant?', a: 'Yes — visit Reports and download any report as PDF or Excel.' },
      { q: 'What happens if I miss a daily check-in?', a: 'Nothing breaks — VigilAI simply relies more heavily on connected transaction data until your next check-in.' },
    ],"""

if "Your Business Health Score recalculates in real-time" in js:
    # We replace the new FAQ block with the old one
    js = re.sub(r'faq:\s*\[[\s\S]*?\]\s*,', old_faq, js)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Reverted everything successfully.")
