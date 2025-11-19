def parse_headers(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    headers = {}
    for line in raw.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip()] = value.strip()

    return headers
