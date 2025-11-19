# Enhanced SpoofX analyzer
import re
from .utils import extract_urls, phishing_keywords, detect_obfuscation

def analyze_email(email):
    """
    Analyze email headers and body to detect spoofing and phishing.
    Returns a dictionary of analysis results.
    """
    headers = email.get("headers", {})
    body = email.get("body", "")

    analysis = {}

    # Header checks
    analysis["SPF Pass"] = "pass" in headers.get("Received-SPF", "").lower()
    analysis["DKIM Present"] = any("dkim-signature" in h.lower() for h in headers.keys())
    analysis["Return-Path Present"] = "Return-Path" in headers
    from_field = headers.get("From", "")
    return_path = headers.get("Return-Path", "")
    analysis["From-ReturnPath Mismatch"] = (from_field and return_path and from_field not in return_path)

    # Body checks
    urls = extract_urls(body)
    analysis["Suspicious URLs Detected"] = len(urls)

    keyword_hits = phishing_keywords(body)
    analysis["Phishing Keywords Detected"] = len(keyword_hits)

    analysis["Obfuscation Detected"] = detect_obfuscation(body)

    return analysis
