import re

# Regex for URL detection
URL_REGEX = r"(https?://[^\s]+)"
# Common phishing keywords
PHISHING_KEYWORDS = [
    "verify", "reset", "urgent", "password",
    "account", "security alert", "click here"
]
# Obfuscation characters
OBFUSCATION_CHARS = ["¥", "$", "§", "¡", "¿", "0", "1"]

def extract_urls(text):
    return re.findall(URL_REGEX, text)

def phishing_keywords(text):
    text_lower = text.lower()
    return [kw for kw in PHISHING_KEYWORDS if kw in text_lower]

def detect_obfuscation(text):
    return any(char in text for char in OBFUSCATION_CHARS)
# For future extra helper functions
pass
