import requests
import json
import os

# The API we are calling - no key needed
url = "https://jsonplaceholder.typicode.com/posts"
# Make the GET request to the API
response = requests.get(url)
# Convert the response to Python-readable JSON
data = response.json()
# Only keep the first five results to keep things manageable
sample = data[:5]
# Make sure the data folder exists
os.makedirs("data", exist_ok=True)
# Save the sample data to a JSON file
with open("data/raw_api_resopnse.json", "w") as f:
    json.dump(sample, f, indent=4)
print("Done! API data saved to data/raw_api_resopnse.json")