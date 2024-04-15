import google.generativeai as palm
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY_PALM2')
palm.configure(api_key=API_KEY)

def ask_to_palm2(prompt):
    try:
        models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        model = models[0].name

        completion = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=1.0,
            max_output_tokens=100,
        )

        if not hasattr(completion, 'error'):
            return completion.result
        else:
            return f"Error: {completion.error.message}"

    except Exception as e:
        return f"Error: {str(e)}"