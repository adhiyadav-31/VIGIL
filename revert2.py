import re
import os

js_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\script.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Revert the toggles trigger
js = js.replace('''    const newProd = $('#sim-newproduct');
    const newBranch = $('#sim-newbranch');
    if (newProd) newProd.addEventListener('change', triggerSimulation);
    if (newBranch) newBranch.addEventListener('change', triggerSimulation);

    // --- Pill selectors (Hire Employees, Price Adjustment) ---''', '''    // --- Pill selectors (Hire Employees, Price Adjustment) ---''')

# Revert the pill trigger
js = js.replace('''          }
          if (typeof triggerSimulation === 'function') triggerSimulation();
        });''', '''          }
        });''')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

css_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Revert user-select
css = css.replace('  font-family: var(--font-mono, monospace);\n  user-select: none;\n}', '  font-family: var(--font-mono, monospace);\n}')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Reverted latest changes successfully.")
