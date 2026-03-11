import anthropic
import os
import json

# Load the API data we fetched in Script 1
with open("data/raw_api_resopnse.json", "r") as f:
    api_data = json.load(f)
    
# Convert it into a string for the AI to process
api_data_str = json.dumps(api_data, indent=2)

# Set up the Anthropic client with your API key
# It automatically reads your ANTHROPIC_API_KEY from the environment variables
client = anthropic.Anthropic()

# Build the prompt for the AI
prompt = f"""
You are a technical writer. I have an API response below. Please do three things:
1. Write a one-sentence description of what this endpoint does.
2. List each field and explian what it contains in plain English.
3. Give one example use case for this API endpoint.

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
os.makedirs("data", exist_ok=True)
with open("data/ai_summary.txt", "w") as f:
    f.write(summary)
    
print("\nSummary saved to data/ai_summary.txt")     