import os

js_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\script.js'
with open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

vault_js = """
// --- Vault Logic ---
document.addEventListener('DOMContentLoaded', () => {
  const btnUnlock = document.getElementById('btn-unlock-vault');
  const vaultLocked = document.getElementById('vault-locked');
  const vaultUnlocked = document.getElementById('vault-unlocked');
  const vaultPassword = document.getElementById('vault-password');

  if (btnUnlock) {
    btnUnlock.addEventListener('click', () => {
      if (vaultPassword.value.trim() === '') {
        if (typeof showToast === 'function') {
          showToast('Please enter your Master Password.');
        } else {
          alert('Please enter your Master Password.');
        }
        return;
      }
      
      if (typeof showToast === 'function') {
        showToast('Decrypting vault...');
      }
      
      // Simulate decryption delay
      setTimeout(() => {
        vaultLocked.style.display = 'none';
        vaultUnlocked.style.display = 'grid';
        vaultPassword.value = '';
      }, 600);
    });
  }
});
"""

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(content + "\n" + vault_js)
