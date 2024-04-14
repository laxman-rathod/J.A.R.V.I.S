from llamaapi import LlamaAPI 
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY_LLAMA2')

def ask_to_llama2(prompt):
    try:
        llama = LlamaAPI(API_KEY)
        api_request_json = {
            "messages": [{"role": "user", "content": prompt}],
            "parameters": {
                "max_length": 100,
                "temperature": 0.1,
                "top_p": 1.0,
                "frequency_penalty": 1.0,
            }
        }

        response = llama.run(api_request_json).json()

        if 'choices' in response and len(response['choices']) > 0:
            return response['choices'][0]['message']['content']
        else:
            return "Unable to generating response."

    except Exception as e:
        return f"Error: {str(e)}"