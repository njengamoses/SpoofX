def parse_email(file_path):
    """
    Parse an email file and return a dictionary with headers and body.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split headers and body
    if "\n\n" in content:
        headers_raw, body = content.split("\n\n", 1)
    else:
        headers_raw = content
        body = ""

    headers = {}
    for line in headers_raw.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip()] = value.strip()

    return {
        "headers": headers,
        "body": body
    }
