import json
import os
from datetime import date

CONFIG_PATH = os.path.join(BASE_DIR, "../config/api_config.json")
def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def export_docs(api):
    api_name = api["name"]
    url = api["url"]

    with open(os.path.join(BASE_DIR, f"../data/{api_name}_raw.json"), "r") as f:
        api_data = json.load(f)

    with open(os.path.join(BASE_DIR, f"../data/{api_name}_summary.json"), "r") as f:
        ai_summary = json.load(f)

    today = date.today().strftime("%B %d, %Y")

    markdown_content = f"""# API Documentation - {api_name}

**Generated:** {today}
**Endpoint:** GET {url}
**Tool:** ai-api-doc-toolkit

---

## AI Analysis
{ai_summary["endpoint_summary"]}

---
## Sample API Response
```json
{json.dumps(api_data, indent=2)}
```
"""

    docs_dir = os.path.join(BASE_DIR, "../docs")
    os.makedirs(docs_dir, exist_ok=True)
    output_path = os.path.join(docs_dir, f"{api_name}_summary.md")

    with open(output_path, "w") as f:
        f.write(markdown_content)

    print(f"Documentation exported to {output_path}")

def main():
    config = load_config()
    for api in config["apis"]:
        export_docs(api)

if __name__ == "__main__":
    main()