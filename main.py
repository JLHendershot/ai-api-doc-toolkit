import json
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config/api_config.json")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def run_pipeline(api_name):
    subprocess.run(["python3", "scripts/fetch_api_data.py"], check=True)
    subprocess.run(["python3", "scripts/summarize_response_ai.py"], check=True)
    subprocess.run(["python3", "scripts/export_docs.py"], check=True)


def main():
    config = load_config()