def calculate_score(analysis):
    score = 100

    if analysis["SPF"] == "fail":
        score -= 40
    if analysis["DKIM"] == "missing":
        score -= 30
    if analysis["DMARC"] == "fail":
        score -= 30

    return max(score, 0)
