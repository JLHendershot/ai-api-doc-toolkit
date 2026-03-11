import json
import os
from datetime import date

# Load the raw API data
with open("data/raw_api_resopnse.json", "r") as f:
    api_data = json.load(f)
    
# Load the AI summary
with open("data/ai_summary.txt", "r") as f:
    ai_summary = f.read()
    
# Get today's date for the document
today = date.today().strftime("%B %d, %Y")

# Build the Markdown content
markdown_content = f"""# API Documentation - Posts Endpoint

**Generated:** {today}
**Endpoint:** GET https://jsonplaceholder.typicode.com/posts
**Tool:** ai-api-doc-toolkit

---

## Endpoint Summary
{ai_summary}

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