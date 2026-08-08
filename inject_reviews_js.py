import os

js_path = r'c:\Users\GUDA ADHI YADAV\Downloads\TKR_404-main\app\frontend\script.js'
with open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

reviews_js = """
// --- Review Intelligence Logic ---
document.addEventListener('DOMContentLoaded', () => {
  const btnAnalyze = document.getElementById('btn-analyze-reviews');
  const reviewFile = document.getElementById('review-file');
  const reviewUpload = document.getElementById('review-upload');
  const reviewAnalyzing = document.getElementById('review-analyzing');
  const reviewResults = document.getElementById('review-results');

  if (btnAnalyze) {
    btnAnalyze.addEventListener('click', () => {
      if (!reviewFile.files.length) {
        if (typeof showToast === 'function') {
          showToast('Please select a file to upload first.');
        } else {
          alert('Please select a file to upload first.');
        }
        return;
      }
      
      // Transition to Analyzing State
      reviewUpload.style.display = 'none';
      reviewAnalyzing.style.display = 'flex';
      
      if (typeof showToast === 'function') {
        showToast('Uploading and parsing reviews...');
      }
      
      // Simulate AI analysis delay
      setTimeout(() => {
        if (typeof showToast === 'function') {
          showToast('Analysis complete! Displaying insights.');
        }
        reviewAnalyzing.style.display = 'none';
        reviewResults.style.display = 'block';
      }, 3500); // 3.5 seconds delay for dramatic effect
    });
  }
});
"""

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(content + "\n" + reviews_js)
