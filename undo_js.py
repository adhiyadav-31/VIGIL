import os

script_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\script.js'
with open(script_path, 'r', encoding='utf-8') as f:
    script = f.read()

# Revert initLogout
old_logout = """  function initLogout() {
    ['#logoutBtn', '#logoutBtn2'].forEach(sel => {
      $(sel)?.addEventListener('click', (e) => {
        e.preventDefault();
        $('#app-shell').style.display = 'none';
        $('#login-page').style.display = 'flex';
      });
    });
  }"""
new_logout = """  function initLogout() {
    ['#logoutBtn', '#logoutBtn2'].forEach(sel => {
      $(sel)?.addEventListener('click', (e) => {
        e.preventDefault();
        showToast('Logged out — redirecting to sign in…');
      });
    });
  }"""
script = script.replace(old_logout, new_logout)

# Revert injected Auth flow
auth_logic = """// --- Auth Flow Logic ---
document.addEventListener('DOMContentLoaded', () => {
  const btnGetStarted = document.getElementById('btn-get-started');
  const loginForm = document.getElementById('login-form');
  const landingPage = document.getElementById('landing-page');
  const loginPage = document.getElementById('login-page');
  const appShell = document.getElementById('app-shell');

  if (btnGetStarted) {
    btnGetStarted.addEventListener('click', () => {
      landingPage.style.display = 'none';
      loginPage.style.display = 'flex';
    });
  }

  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      loginPage.style.display = 'none';
      appShell.style.display = 'block';
      // Trigger resize for charts to render properly
      window.dispatchEvent(new Event('resize'));
    });
  }
});
"""
script = script.replace(auth_logic, "")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(script)
