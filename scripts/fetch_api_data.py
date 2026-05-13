import requests
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "../config/api_config.json")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)
    
def fetch_api(api):
    url = api["url"]
    name = api["name"]
    limit = api.get("limit", 10)
    
    response = requests.get(url)
    data = response.json()
    
    trimmed = data[:limit]
    
    output_path = os.path.join(BASE_DIR, f"../data/{name}_raw.json")
    with open(output_path, "w") as f:
        json.dump(trimmed, f, indent=2)
        
    print(f"Saved: {output_path}")
    
def main():            
    config = load_config()
    for api in config["apis"]:
        fetch_api(api)
        
if __name__ == "__main__":
    main()        