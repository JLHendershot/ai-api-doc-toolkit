import os
import json
import anthropic

# Load the API data we fetched in Script 1
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
API_NAME = "jsonplaceholder_posts"
DATA_FILE = os.path.join(BASE_DIR, f"../data/{API_NAME}_raw.json")

with open(DATA_FILE, "r") as f:
    api_data = json.load(f)
    
# Convert it into a string for the AI to process
api_data_str = json.dumps(api_data, indent=2)

# Set up the Anthropic client with your API key
# It automatically reads your ANTHROPIC_API_KEY from the environment variables
client = anthropic.Anthropic()

# Build the prompt for the AI
prompt = f"""

You are a technical writer.

Return your response in VALID JSON ONLY.

Use this structure:

{{
  "endpoint_summary": "string",
  "field_descriptions": {{
    "field_name": "plain English explanation"
  }},
  "use_cases": ["string"],
  "example": "string"
}}

Do NOT include any extra text outside JSON.

API response:
{api_data_str}
"""
# Send to the AI
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}]
)    
    
# Get the AI's response
summary = message.content[0].text

# Print it so you can see it
print("AI Summary:")
print(summary)

# Save it for Script 3 to use
SUMMARY_FILE = os.path.join(BASE_DIR, f"../data/{API_NAME}_summary.json")

with open(SUMMARY_FILE, "w") as f:
    f.write(summary)
    
print(f"/nSummary saved to {SUMMARY_FILE}")
      
