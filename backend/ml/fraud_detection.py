import random
from typing import Dict, Any

class FraudDetectionEngine:
    """
    Detects anomalies and generates a fraud score with reasoning.
    """
    def __init__(self):
        pass

    def detect(self, applicant_data: Dict[str, Any]) -> Dict[str, Any]:
        # Dummy logic for demonstration
        score = random.randint(10, 90)
        reasons = []
        if score > 50:
            reasons.append("High variance in monthly revenue reported vs bank statements.")
            if applicant_data.get("age_of_business", 0) < 2:
                reasons.append("New business with unusually high credit requests.")
                
        return {
            "fraud_score": score,
            "risk_level": "High" if score > 70 else "Medium" if score > 40 else "Low",
            "reasons": reasons,
            "recommendation": "Manual Review Required" if score > 50 else "Proceed"
        }
