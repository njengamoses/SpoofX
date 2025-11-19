def analyze_headers(headers):
    results = {}

    # SPF
    spf = headers.get("Received-SPF", "missing")
    results["SPF"] = "valid" if "pass" in spf.lower() else "fail"

    # DKIM
    dkim = headers.get("DKIM-Signature", None)
    results["DKIM"] = "present" if dkim else "missing"

    # DMARC
    dmarc = headers.get("Authentication-Results", "")
    results["DMARC"] = "pass" if "dmarc=pass" in dmarc.lower() else "fail"

    return results
