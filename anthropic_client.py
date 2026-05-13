import anthropic
import os

def get_client():
    return anthropic.Anthropic(
        api_key=os.environ["ANTHROPIC_API_KEY"]
    )