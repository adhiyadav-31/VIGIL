import json
import time
from deep_translator import GoogleTranslator

def translate_dict(en_dict, target_lang):
    translator = GoogleTranslator(source='en', target=target_lang)
    translated_dict = {}
    
    keys = list(en_dict.keys())
    values = list(en_dict.values())
    
    for i in range(len(keys)):
        k = keys[i]
        v = values[i]
        try:
            res = translator.translate(v)
            translated_dict[k] = res if res else v
        except Exception as e:
            print(f"Error translating {k}: {e}")
            translated_dict[k] = f"[{target_lang.upper()}] {v}"
            
        if i % 50 == 0:
            print(f"[{target_lang}] Translated {i}/{len(keys)}")
            time.sleep(1) # Prevent rate limiting
            
    return translated_dict

def main():
    with open('locales/en/translation.json', 'r', encoding='utf-8') as f:
        en_dict = json.load(f)
        
    print("Translating to Hindi...")
    hi_dict = translate_dict(en_dict, 'hi')
    with open('locales/hi/translation.json', 'w', encoding='utf-8') as f:
        json.dump(hi_dict, f, indent=2, ensure_ascii=False)
        
    print("Translating to Telugu...")
    te_dict = translate_dict(en_dict, 'te')
    with open('locales/te/translation.json', 'w', encoding='utf-8') as f:
        json.dump(te_dict, f, indent=2, ensure_ascii=False)
        
    print("Translation complete!")

if __name__ == '__main__':
    main()
