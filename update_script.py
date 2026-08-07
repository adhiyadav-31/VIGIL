import os

script_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\script.js'
with open(script_path, 'r', encoding='utf-8') as f:
    script = f.read()

script = script.replace("$('#schemesGrid').innerHTML = SAMPLE.schemes.map(recoCardHtml).join('');", "// $('#schemesGrid').innerHTML = SAMPLE.schemes.map(recoCardHtml).join('');")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(script)
