import requests
import cohere
from dotenv import load_dotenv
import os


load_dotenv()


COHERE_API_KEY = os.getenv('COHERE_API_KEY')


cohere_client = cohere.Client("COHERE_API_KEY")


def generate_documentation(code):
    """Generate documentation for the given code."""
    prompt = f"Generate documentation for the following code:\n\n{code}. Give the output in markdown format."
    response = cohere_client.generate(
        model='command-light',  # Specify the model type
        prompt=prompt,
        max_tokens=150,
        temperature=0.3,
    )
    return response.generations[0].text.strip()


def suggest_improvements(code):
    """Suggest improvements for the given code."""
    prompt = f"Suggest improvements for the following code:\n\n{code}. Make sure to make it point by point."
    response = cohere_client.generate(
        model='command-light',  # Specify the model type
        prompt=prompt,
        max_tokens=100,
        temperature=0.2,

    )
    return response.generations[0].text.strip()


def generate_code_snippet(instruction):
    """Generate a code snippet based on the given instruction."""
    prompt = f"Generate a code snippet for the following instruction:\n\n{instruction}"
    response = cohere_client.generate(
        model='command-light',  # Specify the model type
        prompt=prompt,
        max_tokens=100,
        temperature=0
    )
    return response.generations[0].text.strip()


def improve_code_structure_and_naming(code):
    """Improve code structure and naming for the given code."""
    prompt = f"Improve the code structure and naming for the following code:\n\n{code}"
    response = cohere_client.generate(
        model='command-light',  # Specify the model type
        prompt=prompt,
        max_tokens=100,
        temperature=0.3
    )
    return response.generations[0].text.strip()


def suggest_better_libraries(code):
    """Suggest better libraries/alternatives for the given code."""
    prompt = f"Suggest better libraries/alternatives for the following code:\n\n{code}.\n\nWhen suggesting, also show some code snippet to see how to use them."
    response = cohere_client.generate(
        model='command-light',  # Specify the model type
        prompt=prompt,
        max_tokens=150,
        temperature=0.5
    )
    return response.generations[0].text.strip()


def complete_function(code, instruction):
    """Complete the function based on the given instruction."""
    prompt = f"Complete the following function based on the instruction:\n\nCode:\n{code}\n\nInstruction:\n{instruction}\n\nIf the function requires more code than the instruction, please include it and specify so."
    response = cohere_client.generate(
        model='command-light',  # Specify the model type
        prompt=prompt,
        max_tokens=100,
        temperature=0.1
    )
    return response.generations[0].text.strip()