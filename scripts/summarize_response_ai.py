import os
import json
import anthropic

CONFIG_PATH = os.path.join(BASE_DIR, "../config/api_config.json")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

# Load the API data we fetched in Script 1
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
# Convert it into a string for the AI to process
api_data_str = json.dumps(api_data, indent=2)

# Set up the Anthropic client with your API key
# It automatically reads your ANTHROPIC_API_KEY from the environment variables
client = anthropic.Anthropic()

# Build the prompt for the AI
def prompt_template(api_data_str):
  return f"""

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
def summarize_api(api_name):
    data_file = os.path.join(BASE_DIR, f"../data/{api_name}_raw.json")
    with open(data_file, "r") as f:
        api_data = json.load(f)

    api_data_str = json.dumps(api_data, indent=2)

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt_template(api_data_str)}]
    )

    summary = message.content[0].text
    parsed = json.loads(summary)  # validates JSON before saving

    summary_file = os.path.join(BASE_DIR, f"../data/{api_name}_summary.json")
    with open(summary_file, "w") as f:
        json.dump(parsed, f, indent=2)

    print(f"\nSummary saved to {summary_file}")  # typo fixed

def main():
    config = load_config()
    for api in config["apis"]:
        summarize_api(api["name"])

if __name__ == "__main__":
    main()