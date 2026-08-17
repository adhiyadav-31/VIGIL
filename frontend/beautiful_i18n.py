import json

en_to_hi = {
    "Dashboard": "डैशबोर्ड",
    "Business Health": "व्यवसाय स्वास्थ्य",
    "Daily Check-in": "दैनिक चेक-इन",
    "AI Decision Board": "AI निर्णय बोर्ड",
    "Growth Opportunities": "विकास के अवसर",
    "What-if Simulator": "सिमुलेटर",
    "Grant & Subsidy Hunter": "अनुदान और सब्सिडी",
    "Reports": "रिपोर्ट्स",
    "Benchmark Intelligence": "बेंचमार्क इंटेलिजेंस",
    "Disaster Planner": "आपदा योजनाकार",
    "Expansion Scanner": "विस्तार स्कैनर",
    "Secure Vault": "सुरक्षित वॉल्ट",
    "Review Intelligence": "समीक्षा इंटेलिजेंस",
    "Procurement AI": "खरीद AI",
    "Knowledge Base": "ज्ञान का आधार",
    "Shared Asset Network": "साझा संपत्ति नेटवर्क",
    "Settings": "सेटिंग्स",
    "Search reports, agents, documents…": "रिपोर्ट, एजेंट, दस्तावेज़ खोजें...",
    "Meridian Textiles Pvt. Ltd.": "मेरिडियन टेक्सटाइल्स प्रा. लिमिटेड",
    "Good morning": "सुप्रभात",
    "Run Analysis": "विश्लेषण चलाएं",
    "Financial Distress Risk": "वित्तीय संकट जोखिम",
    "Business Pulse Score": "व्यवसाय पल्स स्कोर",
    "Revenue Trend": "राजस्व प्रवृत्ति",
    "Cash Flow Trend": "नकदी प्रवाह प्रवृत्ति",
    "Customer Satisfaction": "ग्राहक संतुष्टि",
    "Inventory Health": "इन्वेंटरी स्वास्थ्य",
    "Supplier Reliability": "आपूर्तिकर्ता विश्वसनीयता",
    "Employee Stability": "कर्मचारी स्थिरता",
    "Market Opportunity Score": "बाजार अवसर स्कोर",
    "Compliance Status": "अनुपालन स्थिति",
    "Recommendation Summary": "सिफारिश सारांश",
    "View all": "सभी देखें",
    "Moderate": "मध्यम",
    "Stable": "स्थिर",
    "Healthy": "स्वस्थ",
    "Watch": "ध्यान दें",
    "New": "नया",
    "Action Needed": "कार्रवाई की आवश्यकता है",
    "Working Capital Ratio": "कार्यशील पूंजी अनुपात",
    "Expense Volatility": "व्यय अस्थिरता",
    "Prioritized actions generated from your latest analysis.": "आपके नवीनतम विश्लेषण से उत्पन्न प्राथमिकता वाली कार्रवाइयां।",
    "Root cause": "मूल कारण",
    "Action": "कार्रवाई",
    "Receivables aging past 45 days": "45 दिनों से अधिक के प्राप्य",
    "Inventory concentration risk": "इन्वेंटरी एकाग्रता जोखिम",
    "Rising customer acquisition cost": "बढ़ती ग्राहक अधिग्रहण लागत",
    "Thin cash buffer": "कम नकद बफर",
    "Manual attendance tracking": "मैनुअल उपस्थिति ट्रैकिंग",
    "Underused loyalty program": "कम उपयोग किया गया वफादारी कार्यक्रम",
    "Executive Analysis Summary": "कार्यकारी विश्लेषण सारांश",
    "Active Analysis": "सक्रिय विश्लेषण",
    "Run AI Simulation": "AI सिमुलेशन चलाएं",
    "Run AI Analysis": "AI विश्लेषण चलाएं",
    "Details": "विवरण",
    "Lease Now": "अभी पट्टे पर लें",
    "Download Agreement PDF": "समझौता पीडीएफ डाउनलोड करें",
    "Search Network": "नेटवर्क खोजें",
    "Heavy Machinery": "भारी मशीनरी",
    "Robotics": "रोबोटिक्स",
    "Logistics": "रसद",
    "Packaging": "पैकेजिंग",
    "Available Assets": "उपलब्ध संपत्तियां",
    "Active Leases": "सक्रिय पट्टे",
    "Live": "लाइव",
    "Cost Leader": "लागत नेता",
    "Speed Leader": "गति नेता",
    "Quality Leader": "गुणवत्ता नेता",
    "Opportunity": "अवसर",
    "Immediate Action:": "तत्काल कार्रवाई:",
    "Logistics Shift:": "रसद बदलाव:",
    "Contract Renewal:": "अनुबंध नवीनीकरण:",
    "Do It": "इसे करें",
    "Plan": "योजना",
    "High Impact": "उच्च प्रभाव",
    "Growth": "विकास",
    "Efficiency": "दक्षता",
    "Quality": "गुणवत्ता",
    "Account settings": "खाता सेटिंग्स",
    "My reports": "मेरी रिपोर्ट",
    "Log out": "लॉग आउट",
    "Notifications": "सूचनाएं",
    "Mark all read": "सभी को पढ़ा हुआ चिह्नित करें",
    "Today's health score is 78 out of 100": "आज का स्वास्थ्य स्कोर 100 में से 78 है",
    "Health Score": "स्वास्थ्य स्कोर"
}

en_to_te = {
    "Dashboard": "డాష్‌బోర్డ్",
    "Business Health": "వ్యాపార ఆరోగ్యం",
    "Daily Check-in": "రోజువారీ చెక్-ఇన్",
    "AI Decision Board": "AI నిర్ణయ బోర్డు",
    "Growth Opportunities": "వృద్ధి అవకాశాలు",
    "What-if Simulator": "సిమ్యులేటర్",
    "Grant & Subsidy Hunter": "గ్రాంట్ & సబ్సిడీ",
    "Reports": "నివేదికలు",
    "Benchmark Intelligence": "బెంచ్‌మార్క్ ఇంటెలిజెన్స్",
    "Disaster Planner": "విపత్తు ప్రణాళిక",
    "Expansion Scanner": "విస్తరణ స్కానర్",
    "Secure Vault": "సురక్షిత వాల్ట్",
    "Review Intelligence": "సమీక్ష ఇంటెలిజెన్స్",
    "Procurement AI": "సేకరణ AI",
    "Knowledge Base": "జ్ఞాన ఆధారం",
    "Shared Asset Network": "భాగస్వామ్య ఆస్తి నెట్‌వర్క్",
    "Settings": "సెట్టింగ్‌లు",
    "Search reports, agents, documents…": "నివేదికలు, ఏజెంట్లు, పత్రాలను శోధించండి...",
    "Meridian Textiles Pvt. Ltd.": "మెరిడియన్ టెక్స్‌టైల్స్ ప్రైవేట్ లిమిటెడ్",
    "Good morning": "శుభోదయం",
    "Run Analysis": "విశ్లేషణను అమలు చేయండి",
    "Financial Distress Risk": "ఆర్థిక ఇబ్బందుల ప్రమాదం",
    "Business Pulse Score": "వ్యాపార పల్స్ స్కోర్",
    "Revenue Trend": "రాబడి ధోరణి",
    "Cash Flow Trend": "నగదు ప్రవాహ ధోరణి",
    "Customer Satisfaction": "కస్టమర్ సంతృప్తి",
    "Inventory Health": "ఇన్వెంటరీ ఆరోగ్యం",
    "Supplier Reliability": "సరఫరాదారు విశ్వసనీయత",
    "Employee Stability": "ఉద్యోగి స్థిరత్వం",
    "Market Opportunity Score": "మార్కెట్ అవకాశ స్కోర్",
    "Compliance Status": "కట్టుబడి ఉన్న స్థితి",
    "Recommendation Summary": "సిఫార్సు సారాంశం",
    "View all": "అన్నీ చూడండి",
    "Moderate": "మితమైన",
    "Stable": "స్థిరమైన",
    "Healthy": "ఆరోగ్యకరమైన",
    "Watch": "గమనించండి",
    "New": "కొత్తది",
    "Action Needed": "చర్య అవసరం",
    "Working Capital Ratio": "వర్కింగ్ క్యాపిటల్ నిష్పత్తి",
    "Expense Volatility": "ఖర్చు అస్థిరత",
    "Prioritized actions generated from your latest analysis.": "మీ తాజా విశ్లేషణ నుండి రూపొందించబడిన ప్రాధాన్యత చర్యలు.",
    "Root cause": "మూల కారణం",
    "Action": "చర్య",
    "Receivables aging past 45 days": "45 రోజులు దాటిన స్వీకరించదగినవి",
    "Inventory concentration risk": "ఇన్వెంటరీ ఏకాగ్రత ప్రమాదం",
    "Rising customer acquisition cost": "పెరుగుతున్న కస్టమర్ సముపార్జన వ్యయం",
    "Thin cash buffer": "తక్కువ నగదు బఫర్",
    "Manual attendance tracking": "మాన్యువల్ హాజరు ట్రాకింగ్",
    "Underused loyalty program": "తక్కువగా ఉపయోగించబడిన లాయల్టీ ప్రోగ్రామ్",
    "Executive Analysis Summary": "ఎగ్జిక్యూటివ్ విశ్లేషణ సారాంశం",
    "Active Analysis": "క్రియాశీల విశ్లేషణ",
    "Run AI Simulation": "AI సిమ్యులేషన్ రన్ చేయండి",
    "Run AI Analysis": "AI విశ్లేషణను రన్ చేయండి",
    "Details": "వివరాలు",
    "Lease Now": "ఇప్పుడే లీజుకు తీసుకోండి",
    "Download Agreement PDF": "అగ్రిమెంట్ PDF డౌన్‌లోడ్",
    "Search Network": "నెట్‌వర్క్‌ను శోధించండి",
    "Heavy Machinery": "భారీ యంత్రాలు",
    "Robotics": "రోబోటిక్స్",
    "Logistics": "లాజిస్టిక్స్",
    "Packaging": "ప్యాకేజింగ్",
    "Available Assets": "అందుబాటులో ఉన్న ఆస్తులు",
    "Active Leases": "యాక్టివ్ లీజులు",
    "Live": "లైవ్",
    "Cost Leader": "ఖర్చు లీడర్",
    "Speed Leader": "స్పీడ్ లీడర్",
    "Quality Leader": "నాణ్యత లీడర్",
    "Opportunity": "అవకాశం",
    "Immediate Action:": "తక్షణ చర్య:",
    "Logistics Shift:": "లాజిస్టిక్స్ మార్పు:",
    "Contract Renewal:": "ఒప్పందం పునరుద్ధరణ:",
    "Do It": "చేయండి",
    "Plan": "ప్రణాళిక",
    "High Impact": "అధిక ప్రభావం",
    "Growth": "వృద్ధి",
    "Efficiency": "సమర్థత",
    "Quality": "నాణ్యత",
    "Account settings": "ఖాతా సెట్టింగ్‌లు",
    "My reports": "నా నివేదికలు",
    "Log out": "లాగ్ అవుట్",
    "Notifications": "నోటిఫికేషన్‌లు",
    "Mark all read": "అన్నీ చదివినట్లుగా గుర్తించండి",
    "Today's health score is 78 out of 100": "నేటి ఆరోగ్య స్కోరు 100కి 78",
    "Health Score": "ఆరోగ్య స్కోర్"
}

def translate_str(text, mapping):
    # If the exact text is in mapping, return it
    if text in mapping:
        return mapping[text]
    
    # Try lowercase match
    for k, v in mapping.items():
        if k.lower() == text.lower():
            # Match case roughly
            if text.isupper():
                return v.upper()
            return v
            
    # For a clean look, if we can't translate it beautifully, leave it in English
    # This prevents the ugly transliteration of long unmapped sentences.
    return text

def main():
    with open('locales/en/translation.json', 'r', encoding='utf-8') as f:
        en_dict = json.load(f)
        
    hi_dict = {}
    te_dict = {}
    
    # Update dicts with the hardcoded mappings directly
    for k, v in en_dict.items():
        # The key 'k' in translation.json is the hash or string, 'v' is the English text
        hi_dict[k] = translate_str(v, en_to_hi)
        te_dict[k] = translate_str(v, en_to_te)
        
    # Overwrite the translation files
    with open('locales/hi/translation.json', 'w', encoding='utf-8') as f:
        json.dump(hi_dict, f, indent=2, ensure_ascii=False)
        
    with open('locales/te/translation.json', 'w', encoding='utf-8') as f:
        json.dump(te_dict, f, indent=2, ensure_ascii=False)
        
    print("Beautiful localization complete!")

if __name__ == '__main__':
    main()
