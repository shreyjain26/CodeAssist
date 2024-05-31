from flask import Flask, render_template, request
from gemini import (
    generate_documentation,
    suggest_improvements,
    generate_code_snippet,
    improve_code_structure_and_naming,
    suggest_better_libraries,
    complete_function
)
from utils import markdown_to_html
import logging
import os

app = Flask(__name__)

# Configure logging
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(filename='logs/ai_code_assistant.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    code = request.form['code']
    task = request.form['task']
    instruction = request.form.get('instruction', '')

    logging.info(f"Received request - Task: {task}, Instruction: {instruction}")

    try:
        if task == 'generate_documentation':
            result = generate_documentation(code)
        elif task == 'suggest_improvements':
            result = suggest_improvements(code)
        elif task == 'generate_code_snippet':
            result = generate_code_snippet(instruction)
        elif task == 'improve_code_structure_and_naming':
            result = improve_code_structure_and_naming(code)
        elif task == 'suggest_better_libraries':
            result = suggest_better_libraries(code)
        elif task == 'complete_function':
            result = complete_function(code, instruction)
        else:
            result = 'Invalid task selected.'
            logging.error(f"Invalid task selected: {task}")

        logging.info(f"Task completed successfully - Task: {task}")
        
        result = markdown_to_html(result)
        logging.info(f"Task completed successfully - Task: {task}")

    except Exception as e:
        result = f"An error occurred: {str(e)}"
        logging.error(f"Error processing task: {str(e)}")


    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
