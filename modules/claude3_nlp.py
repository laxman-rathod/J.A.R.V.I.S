import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY_CLAUDE3')

def ask_to_claude3(prompt):
    client = anthropic.Anthropic(api_key=API_KEY)

    try:
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=200,
            temperature=0.5,
            messages=[{"role": "user", "content": prompt}]
        )
        
        if not message.error:
            return message.content
        else:
            return f"Error: {message.error}"

    except Exception as e:
        return f"Error: {str(e)}"  