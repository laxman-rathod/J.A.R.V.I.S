import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY_Gemini_PRO')

def ask_to_geminipro(prompt):
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        if not hasattr(response, 'error'):
            return response.text
        else:
            return f"Error: {response.error.message}"

    except Exception as e:
        return f"Error: {str(e)}"

'''prompt = "what is the meaning of life? describe in 2 lines."
To live, to love, to learn, to grow,
To make a difference, before we go. '''