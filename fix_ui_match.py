import re

html_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace vault-locked
old_vault_locked = """        <!-- Locked State -->
        <div id="vault-locked" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 60px 20px; text-align: center;">
          <div style="font-size: 3rem; margin-bottom: 20px;">🔒</div>
          <h3 style="margin-bottom: 12px;">Vault is Locked</h3>
          <p class="meta" style="margin-bottom: 32px; max-width: 400px;">This area contains highly sensitive financial and tax documents. Please enter your Owner Master Password to decrypt.</p>
          
          <div class="card" style="width: 100%; max-width: 400px; text-align: left;">
            <div class="form-field">
              <label for="vault-password">Master Password</label>
              <input type="password" id="vault-password" placeholder="Enter password to decrypt" />
            </div>
            <button id="btn-unlock-vault" class="btn btn--primary btn--full" style="margin-top: 16px;">Decrypt & Unlock Vault</button>
          </div>
        </div>"""

new_vault_locked = """        <!-- Locked State -->
        <div id="vault-locked" class="card" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 60px 20px; text-align: center; max-width: 500px; margin: 40px auto;">
          <div style="font-size: 3rem; margin-bottom: 20px;">🔒</div>
          <h3 style="margin-bottom: 12px;">Vault is Locked</h3>
          <p class="meta" style="margin-bottom: 32px; max-width: 400px; margin-left: auto; margin-right: auto;">This area contains highly sensitive financial and tax documents. Please enter your Owner Master Password to decrypt.</p>
          
          <div style="width: 100%; max-width: 350px; text-align: left; margin: 0 auto;">
            <div class="form-field">
              <label for="vault-password">Master Password</label>
              <input type="password" id="vault-password" placeholder="Enter password to decrypt" />
            </div>
            <button id="btn-unlock-vault" class="btn btn--primary btn--full" style="margin-top: 16px;">Decrypt & Unlock Vault</button>
          </div>
        </div>"""

html = html.replace(old_vault_locked, new_vault_locked)

# Replace review-upload
old_review_upload = """        <!-- Upload State -->
        <div id="review-upload" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 60px 20px; text-align: center; border: 2px dashed var(--border-subtle); border-radius: 16px; margin-bottom: 24px; background: var(--bg-surface);">
          <div style="font-size: 3rem; margin-bottom: 20px;">📁</div>
          <h3 style="margin-bottom: 12px;">Upload Review Data</h3>
          <p class="meta" style="margin-bottom: 32px; max-width: 400px;">Supported formats: CSV, Excel (.xlsx), PDF, Word (.docx).</p>
          
          <div style="width: 100%; max-width: 400px; text-align: left;">
            <input type="file" id="review-file" class="form-field" accept=".csv, .xlsx, .pdf, .docx" style="margin-bottom: 16px; width: 100%;" />
            <button id="btn-analyze-reviews" class="btn btn--primary btn--full">Run AI Analysis</button>
          </div>
        </div>"""

new_review_upload = """        <!-- Upload State -->
        <div id="review-upload" class="card" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 60px 20px; text-align: center; border: 2px dashed var(--border-subtle); max-width: 600px; margin: 40px auto;">
          <div style="font-size: 3rem; margin-bottom: 20px;">📁</div>
          <h3 style="margin-bottom: 12px;">Upload Review Data</h3>
          <p class="meta" style="margin-bottom: 32px; max-width: 400px; margin-left: auto; margin-right: auto;">Supported formats: CSV, Excel (.xlsx), PDF, Word (.docx).</p>
          
          <div style="width: 100%; max-width: 350px; text-align: left; margin: 0 auto;">
            <input type="file" id="review-file" class="form-field" accept=".csv, .xlsx, .pdf, .docx" style="margin-bottom: 16px; width: 100%;" />
            <button id="btn-analyze-reviews" class="btn btn--primary btn--full">Run AI Analysis</button>
          </div>
        </div>"""

html = html.replace(old_review_upload, new_review_upload)

# Replace review-analyzing
old_review_analyzing = """        <!-- Analyzing State -->
        <div id="review-analyzing" style="display: none; flex-direction: column; align-items: center; justify-content: center; padding: 60px 20px; text-align: center;">
          <div class="loading-spinner" style="margin-bottom: 20px;"></div>
          <h3>AI is reading reviews...</h3>
          <p class="meta">Detecting complaints, feature requests, and benchmarking against competitors.</p>
        </div>"""

new_review_analyzing = """        <!-- Analyzing State -->
        <div id="review-analyzing" class="card" style="display: none; flex-direction: column; align-items: center; justify-content: center; padding: 60px 20px; text-align: center; max-width: 600px; margin: 40px auto;">
          <div class="loading-spinner" style="margin-bottom: 20px;"></div>
          <h3>AI is reading reviews...</h3>
          <p class="meta">Detecting complaints, feature requests, and benchmarking against competitors.</p>
        </div>"""

html = html.replace(old_review_analyzing, new_review_analyzing)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
