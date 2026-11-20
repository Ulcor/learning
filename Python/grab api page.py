# Source - https://stackoverflow.com/a/55596356
# Posted by chitown88, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-16, License - CC BY-SA 4.0

import requests
import pandas as pd

# Fetch the OpenAPI spec (example URL — replace with actual)
url = "https://api.datalens.tech/openapi.json"
resp = requests.get(url)
spec = resp.json()

paths = spec.get("paths", {})

rows = []
for path, methods in paths.items():
    for method, details in methods.items():
        rows.append({
            "link": path,
            "method": method.upper(),
            "summary": details.get("summary", ""),
            "description": details.get("description", ""),
            "parameters": details.get("parameters", []),
            "requestBody": details.get("requestBody", {}),
            "responses": details.get("responses", {})
        })

df = pd.DataFrame(rows)
print(df)

