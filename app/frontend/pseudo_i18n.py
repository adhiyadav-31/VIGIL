import json

hindi_map = {
    'a': 'अ', 'b': 'ब', 'c': 'च', 'd': 'द', 'e': 'ए', 'f': 'फ', 'g': 'ग', 'h': 'ह',
    'i': 'इ', 'j': 'ज', 'k': 'क', 'l': 'ल', 'm': 'म', 'n': 'न', 'o': 'ओ', 'p': 'प',
    'q': 'क', 'r': 'र', 's': 'स', 't': 'त', 'u': 'उ', 'v': 'व', 'w': 'व', 'x': 'क्स',
    'y': 'य', 'z': 'ज़',
    'A': 'अ', 'B': 'ब', 'C': 'च', 'D': 'द', 'E': 'ए', 'F': 'फ', 'G': 'ग', 'H': 'ह',
    'I': 'इ', 'J': 'ज', 'K': 'क', 'L': 'ल', 'M': 'म', 'N': 'न', 'O': 'ओ', 'P': 'प',
    'Q': 'क', 'R': 'र', 'S': 'स', 'T': 'त', 'U': 'उ', 'V': 'व', 'W': 'व', 'X': 'क्स',
    'Y': 'य', 'Z': 'ज़'
}

telugu_map = {
    'a': 'అ', 'b': 'బ', 'c': 'చ', 'd': 'ద', 'e': 'ఎ', 'f': 'ఫ', 'g': 'గ', 'h': 'హ',
    'i': 'ఇ', 'j': 'జ', 'k': 'క', 'l': 'ల', 'm': 'మ', 'n': 'న', 'o': 'ఒ', 'p': 'ప',
    'q': 'క', 'r': 'ర', 's': 'స', 't': 'త', 'u': 'ఉ', 'v': 'వ', 'w': 'వ', 'x': 'క్స',
    'y': 'య', 'z': 'జ',
    'A': 'అ', 'B': 'బ', 'C': 'చ', 'D': 'ద', 'E': 'ఎ', 'F': 'ఫ', 'G': 'గ', 'H': 'హ',
    'I': 'ఇ', 'J': 'జ', 'K': 'క', 'L': 'ల', 'M': 'మ', 'N': 'న', 'O': 'ఒ', 'P': 'ప',
    'Q': 'క', 'R': 'ర', 'S': 'స', 'T': 'త', 'U': 'ఉ', 'V': 'వ', 'W': 'వ', 'X': 'క్స',
    'Y': 'య', 'Z': 'జ'
}

def pseudo_translate(text, lang_map):
    res = ""
    for char in text:
        res += lang_map.get(char, char)
    return res

def main():
    with open('locales/en/translation.json', 'r', encoding='utf-8') as f:
        en_dict = json.load(f)
        
    hi_dict = {}
    te_dict = {}
    
    for k, v in en_dict.items():
        hi_dict[k] = pseudo_translate(v, hindi_map)
        te_dict[k] = pseudo_translate(v, telugu_map)
        
    with open('locales/hi/translation.json', 'w', encoding='utf-8') as f:
        json.dump(hi_dict, f, indent=2, ensure_ascii=False)
        
    with open('locales/te/translation.json', 'w', encoding='utf-8') as f:
        json.dump(te_dict, f, indent=2, ensure_ascii=False)
        
    print("Pseudo-localization complete!")

if __name__ == '__main__':
    main()
