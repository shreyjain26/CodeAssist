import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get Gemini API key from environment variables
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
# GEMINI_API_URL = 'https://api.gemini.com/v1'


genai.configure(api_key=GEMINI_API_KEY)
     
model = genai.GenerativeModel('gemini-1.5-flash')


def call_gemini_api(prompt, max_tokens=100, temperature=0.5):
    response = model.generate_content(
        contents=prompt,
        # stream=True,
        generation_config=genai.types.GenerationConfig(
        max_output_tokens=max_tokens,
        temperature=temperature,
        )
    )
    return response.text

def generate_documentation(code):
    """Generate documentation for the given code."""
    prompt = f"Generate documentation for the following code:\n\n{code}"
    return call_gemini_api(prompt, 200)

def suggest_improvements(code):
    """Suggest improvements for the given code."""
    prompt = f"Suggest improvements for the following code:\n\n{code}"
    return call_gemini_api(prompt, temperature=0.30)

def generate_code_snippet(instruction):
    """Generate a code snippet based on the given instruction."""
    prompt = f"Generate a code snippet for the following instruction:\n\n{instruction}"
    return call_gemini_api(prompt, temperature=0)

def improve_code_structure_and_naming(code):
    """Improve code structure and naming for the given code."""
    prompt = f"Improve the code structure and naming for the following code:\n\n{code}"
    return call_gemini_api(prompt, temperature=0.2)

def suggest_better_libraries(code):
    """Suggest better libraries/alternatives for the given code."""
    prompt = f"Suggest better libraries/alternatives for the following code:\n\n{code}"
    return call_gemini_api(prompt, 150, 0.4)

def complete_function(code, instruction):
    """Complete the function based on the given instruction."""
    prompt = f"Complete the following function based on the instruction:\n\nCode:\n{code}\n\nInstruction:\n{instruction}"
    return call_gemini_api(prompt, 200, 0)
