import json
import time
from googletrans import Translator

def main():
    with open('locales/en/translation.json', 'r', encoding='utf-8') as f:
        en_dict = json.load(f)

    # Load existing to not overwrite beautiful translations that were manually added
    try:
        with open('locales/hi/translation.json', 'r', encoding='utf-8') as f:
            hi_dict = json.load(f)
    except:
        hi_dict = {}

    try:
        with open('locales/te/translation.json', 'r', encoding='utf-8') as f:
            te_dict = json.load(f)
    except:
        te_dict = {}

    translator = Translator()
    keys = list(en_dict.keys())
    
    # Let's batch translate or translate one by one with a small delay
    for i, key in enumerate(keys):
        english_text = en_dict[key]
        
        # Check if it was beautifully translated already, if it is English text it wasn't
        is_hi_untranslated = (key not in hi_dict) or (hi_dict[key] == english_text) or any(c in hi_dict[key] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        is_te_untranslated = (key not in te_dict) or (te_dict[key] == english_text) or any(c in te_dict[key] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        if not is_hi_untranslated and not is_te_untranslated:
            continue
            
        # Add a slight delay to prevent rate limit
        if i % 10 == 0:
            time.sleep(1.0)
            
        try:
            if is_hi_untranslated:
                res = translator.translate(english_text, dest='hi')
                hi_dict[key] = res.text
            if is_te_untranslated:
                res2 = translator.translate(english_text, dest='te')
                te_dict[key] = res2.text
        except Exception as e:
            print(f"Error on {key}: {e}")
            # we will just continue, at least some will be translated
            continue

        if i % 50 == 0:
            print(f"Translated {i}/{len(keys)}")

    with open('locales/hi/translation.json', 'w', encoding='utf-8') as f:
        json.dump(hi_dict, f, indent=2, ensure_ascii=False)

    with open('locales/te/translation.json', 'w', encoding='utf-8') as f:
        json.dump(te_dict, f, indent=2, ensure_ascii=False)

    print("Perfect translation complete!")

if __name__ == '__main__':
    main()
