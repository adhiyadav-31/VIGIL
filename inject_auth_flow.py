import os
import re

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make app shell hidden by default
html = html.replace('<div class="app-shell" id="app-shell">', '<div class="app-shell" id="app-shell" style="display:none;">')

# Create the new pages HTML
new_pages = '''
<!-- ===================== AUTH & LANDING PAGES ===================== -->
<style>
  .fullscreen-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background-color: var(--bg-base);
    color: var(--text-primary);
    text-align: center;
    padding: 20px;
  }
  
  .hero-title {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 20px;
    background: linear-gradient(135deg, var(--brand-primary), var(--accent-blue));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  
  .hero-subtitle {
    font-size: 1.25rem;
    color: var(--text-secondary);
    max-width: 600px;
    margin-bottom: 40px;
    line-height: 1.6;
  }
  
  .auth-card {
    background-color: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 16px;
    padding: 40px;
    width: 100%;
    max-width: 400px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    text-align: left;
  }
  
  .auth-card h2 {
    font-size: 1.5rem;
    margin-bottom: 24px;
    text-align: center;
  }
  
  .brand-logo-large {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin-bottom: 20px;
    font-size: 2rem;
    font-weight: 700;
    color: var(--text-primary);
  }
  
  .brand-logo-large svg {
    color: var(--brand-primary);
  }
</style>

<!-- Landing Page -->
<div id="landing-page" class="fullscreen-page">
  <div class="brand-logo-large">
    <svg viewBox="0 0 32 32" width="48" height="48">
      <polyline points="2,17 9,17 12,7 18,25 21,17 30,17" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    Vigil<em>AI</em>
  </div>
  <h1 class="hero-title">Early-warning intelligence for MSMEs.</h1>
  <p class="hero-subtitle">Predict financial distress, track growth opportunities, and generate AI-driven recovery plans before crises hit.</p>
  <button id="btn-get-started" class="btn btn--primary" style="font-size: 1.1rem; padding: 12px 32px;">Get Started</button>
</div>

<!-- Login Page -->
<div id="login-page" class="fullscreen-page" style="display:none;">
  <div class="auth-card">
    <div class="brand-logo-large" style="margin-bottom:32px;">
      <svg viewBox="0 0 32 32" width="36" height="36">
        <polyline points="2,17 9,17 12,7 18,25 21,17 30,17" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      Vigil<em>AI</em>
    </div>
    <h2>Sign In</h2>
    <form id="login-form">
      <div class="form-field">
        <label for="login-email">Email Address</label>
        <input type="email" id="login-email" required placeholder="Enter your email" value="rhea@meridiantextiles.in" />
      </div>
      <div class="form-field">
        <label for="login-password">Password</label>
        <input type="password" id="login-password" required placeholder="Enter your password" value="password123" />
      </div>
      <button type="submit" class="btn btn--primary btn--full" style="margin-top: 16px;">Sign In to Dashboard</button>
    </form>
    <p style="text-align:center; margin-top:20px; color:var(--text-secondary); font-size:0.9rem;">
      Don't have an account? <a href="#" style="color:var(--brand-primary); text-decoration:none;">Sign Up</a>
    </p>
  </div>
</div>

<div class="app-shell" id="app-shell" style="display:none;">
'''

# Inject right before the app-shell
html = html.replace('<div class="app-shell" id="app-shell" style="display:none;">', new_pages)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
