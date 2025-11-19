def score_email(analysis):
    """
    Calculate a risk score (0-100) based on analysis.
    """
    score = 100

    # Header penalties
    if not analysis.get("SPF Pass", False):
        score -= 30
    if not analysis.get("DKIM Present", False):
        score -= 25
    if analysis.get("From-ReturnPath Mismatch", False):
        score -= 20

    # Body penalties
    score -= min(analysis.get("Phishing Keywords Detected", 0) * 5, 25)
    score -= min(analysis.get("Suspicious URLs Detected", 0) * 5, 25)
    if analysis.get("Obfuscation Detected", False):
        score -= 15

    score = max(score, 0)
    
    # Determine risk category
    if score >= 70:
        category = "Low"
    elif score >= 40:
        category = "Medium"
    else:
        category = "High"

    return score, category
