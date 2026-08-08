import json

extra_hi = {
    'High': 'उच्च',
    'Medium': 'मध्यम',
    'Low': 'निम्न',
    'Root Cause:': 'मूल कारण:',
    'Action:': 'कार्रवाई:',
    'Impact:': 'प्रभाव:',
    'Working Capital Ratio': 'कार्यशील पूंजी अनुपात',
    'Expense Volatility': 'व्यय अस्थिरता',
    'Action needed': 'कार्रवाई की आवश्यकता है',
    'Watch': 'ध्यान दें',
    'Healthy': 'स्वस्थ'
}

extra_te = {
    'High': 'అధికం',
    'Medium': 'మితమైనది',
    'Low': 'తక్కువ',
    'Root Cause:': 'మూల కారణం:',
    'Action:': 'చర్య:',
    'Impact:': 'ప్రభావం:',
    'Working Capital Ratio': 'వర్కింగ్ క్యాపిటల్ నిష్పత్తి',
    'Expense Volatility': 'ఖర్చు అస్థిరత',
    'Action needed': 'చర్య అవసరం',
    'Watch': 'గమనించండి',
    'Healthy': 'ఆరోగ్యకరమైన'
}

def main():
    with open('locales/hi/translation.json', 'r', encoding='utf-8') as f:
        hi_dict = json.load(f)
        
    with open('locales/te/translation.json', 'r', encoding='utf-8') as f:
        te_dict = json.load(f)
        
    hi_dict.update(extra_hi)
    te_dict.update(extra_te)
    
    with open('locales/hi/translation.json', 'w', encoding='utf-8') as f:
        json.dump(hi_dict, f, indent=2, ensure_ascii=False)
        
    with open('locales/te/translation.json', 'w', encoding='utf-8') as f:
        json.dump(te_dict, f, indent=2, ensure_ascii=False)
        
    print("Extra translations added!")

if __name__ == '__main__':
    main()
