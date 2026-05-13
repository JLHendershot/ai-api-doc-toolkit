import json
import os
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the raw API data
with open(os.path.join(BASE_DIR, "../data/jsonplaceholder_posts_raw.json"), "r") as f:
    api_data = json.load(f)

# Load the AI summary
with open(os.path.join(BASE_DIR, "../data/jsonplaceholder_posts_summary.json"), "r") as f:
    ai_summary = json.load(f)

# Get today's date for the document
today = date.today().strftime("%B %d, %Y")

# Build the Markdown content
markdown_content = f"""# API Documentation - Posts Endpoint

**Generated:** {today}
**Endpoint:** GET https://jsonplaceholder.typicode.com/posts
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

# Save the Markdown file
os.makedirs("docs", exist_ok=True)
with open("docs/generated_api_summary.md", "w") as f:
    f.write(markdown_content)
    
print("Documentation exported to docs/generated_api_summary.md")  