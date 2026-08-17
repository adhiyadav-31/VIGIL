import json
import os
import re
from bs4 import BeautifulSoup
from googletrans import Translator
import time

def generate_key(text):
    # Create a simple key from text
    clean = re.sub(r'[^a-zA-Z0-9]+', '_', text.strip().lower())
    return clean[:40].strip('_') + '_' + str(hash(text))[-6:]

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    en_dict = {}
    
    # Attributes to translate
    attrs_to_translate = ['placeholder', 'title', 'aria-label']

    for tag in soup.find_all(True):
        if tag.name in ['script', 'style', 'svg', 'path', 'circle', 'kbd', 'code']:
            continue
        
        # Handle attributes
        i18n_attrs = []
        for attr in attrs_to_translate:
            if tag.has_attr(attr) and tag[attr].strip():
                val = tag[attr].strip()
                if not re.search(r'[a-zA-Z]', val): continue # Skip if no letters
                key = generate_key(val)
                en_dict[key] = val
                i18n_attrs.append(f"[{attr}]{key}")
        
        # Handle inner text (only direct children text, not nested tags)
        # Only process if there is substantial text and no child elements
        direct_text = "".join([c for c in tag.contents if isinstance(c, str)]).strip()
        if direct_text and not tag.find_all(True):
            if re.search(r'[a-zA-Z]', direct_text): # Has actual letters
                key = generate_key(direct_text)
                en_dict[key] = direct_text
                i18n_attrs.append(key)
        
        if i18n_attrs:
            existing = tag.get('data-i18n', '')
            if existing:
                tag['data-i18n'] = existing + ';' + ';'.join(i18n_attrs)
            else:
                tag['data-i18n'] = ';'.join(i18n_attrs)

    # Hardcoded additions for dynamic script.js values
    script_keys = {
        'toast_lease_initiated': 'Lease request initiated! Escrow instructions sent to your email.',
        'toast_uploading': 'Uploading and parsing reviews...',
        'toast_analysis_complete': 'Analysis complete! Displaying insights.',
        'js_owner': 'Owner',
        'js_moderate': 'Moderate',
        'js_business_pulse': 'Business Pulse',
        'js_request_sent': '✓ Request Sent'
    }
    en_dict.update(script_keys)

    os.makedirs('locales/en', exist_ok=True)
    os.makedirs('locales/hi', exist_ok=True)
    os.makedirs('locales/te', exist_ok=True)

    with open('locales/en/translation.json', 'w', encoding='utf-8') as f:
        json.dump(en_dict, f, indent=2, ensure_ascii=False)
        
    print(f"Extracted {len(en_dict)} strings. Translating...")

    translator = Translator()
    hi_dict = {}
    te_dict = {}
    
    keys = list(en_dict.keys())
    values = list(en_dict.values())
    
    batch_size = 50
    for i in range(0, len(keys), batch_size):
        batch_vals = values[i:i+batch_size]
        print(f"Translating batch {i//batch_size + 1}/{len(keys)//batch_size + 1}")
        try:
            hi_res = translator.translate(batch_vals, dest='hi', src='en')
            te_res = translator.translate(batch_vals, dest='te', src='en')
            for j, k in enumerate(keys[i:i+batch_size]):
                hi_dict[k] = hi_res[j].text if hasattr(hi_res[j], 'text') else hi_res[j].text
                te_dict[k] = te_res[j].text if hasattr(te_res[j], 'text') else te_res[j].text
        except Exception as e:
            print(f"Error during translation: {e}")
            for j, k in enumerate(keys[i:i+batch_size]):
                hi_dict[k] = batch_vals[j]
                te_dict[k] = batch_vals[j]
        time.sleep(1)

    with open('locales/hi/translation.json', 'w', encoding='utf-8') as f:
        json.dump(hi_dict, f, indent=2, ensure_ascii=False)
        
    with open('locales/te/translation.json', 'w', encoding='utf-8') as f:
        json.dump(te_dict, f, indent=2, ensure_ascii=False)

    with open('index_i18n.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Done! Saved index_i18n.html and translation files.")

if __name__ == '__main__':
    main()
