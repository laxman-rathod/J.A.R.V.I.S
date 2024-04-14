from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()
API_KEY = os.getenv("API_KEY_OPENROUTER")
base_url = "https://openrouter.ai/api/v1"

def interact_with_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    data = json.dumps({
        "model": "openai/gpt-4-turbo-preview",  # Optional
        "messages": [
            {"role": "user", "content": prompt}
        ]
    })
    response = requests.post(
        url=f"{base_url}/chat/completions",
        headers=headers,
        data=data,
    )
    response_json = json.loads(response.text)
    openrouter_response = response_json["choices"][0]["message"]["content"]
    return openrouter_response