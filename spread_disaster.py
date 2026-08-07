import os

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make Risk Radar card span 2
old_card1 = '''<!-- Risk Radar Card -->
          <article class="card card--list">'''
new_card1 = '''<!-- Risk Radar Card -->
          <article class="card card--list card--span2">'''
html = html.replace(old_card1, new_card1)

# Make Continuity Assets card span 2
old_card2 = '''<!-- Continuity Assets Card -->
          <article class="card card--list">'''
new_card2 = '''<!-- Continuity Assets Card -->
          <article class="card card--list card--span2">'''
html = html.replace(old_card2, new_card2)

# Make Checklist card span full width
old_card3 = '''<!-- Checklist & Recovery Plan -->
          <article class="card card--agent card--span2">'''
new_card3 = '''<!-- Checklist & Recovery Plan -->
          <article class="card card--agent" style="grid-column: 1 / -1;">'''
html = html.replace(old_card3, new_card3)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
