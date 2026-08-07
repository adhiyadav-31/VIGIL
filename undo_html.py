import os
import re

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the injected block and hidden app shell with just the app shell
# The injected block starts with <!-- ===================== AUTH & LANDING PAGES ===================== -->
# and ends with <div class="app-shell" id="app-shell" style="display:none;">

pattern = r'<!-- ===================== AUTH & LANDING PAGES ===================== -->.*?<div class="app-shell" id="app-shell" style="display:none;">'
html = re.sub(pattern, '<div class="app-shell" id="app-shell">', html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
