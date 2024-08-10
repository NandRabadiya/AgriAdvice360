import os
import json
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import ollama

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Pull the model when the application starts
def pull_model_if_needed(model_name):
    try:
        ollama.pull_model(model_name)
    except ollama._types.ResponseError as e:
        print(f"Error pulling model: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    state = request.form['state']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    prompt = request.form['prompt']
    report = request.files['report']

    # Convert the PDF report to JSON format (simulating conversion)
    report_json = {
        "soil_ph": 6.5,
        "soil_type": "loamy",
        "water_quality": "good",
        "nutrients": {
            "nitrogen": "medium",
            "phosphorus": "low",
            "potassium": "high"
        }
    }

    # Ensure the model is pulled
    model_name = 'mistral'
    pull_model_if_needed(model_name)

    # Use Ollama's chat API
    response = ollama.chat(
        model=model_name,
        messages=[
            {
                'role': 'user',
                'content': f"Based on the following soil and water report, suggest the best crops to grow:\n\n{json.dumps(report_json)}"
            }
        ]
    )

    suggested_crops = response['message']['content'].strip()

    # Render the suggested crops and ask for user selection
    return render_template('crop_selection.html', crops=suggested_crops)

@app.route('/select_crop', methods=['POST'])
def select_crop():
    selected_crop = request.form['selected_crop']

    # Based on the selected crop, suggest fertilizers
    fertilizers = {
        "crop_name": selected_crop,
        "organic": ["Compost", "Vermicompost", "Green manure"],
        "inorganic": ["Urea", "Superphosphate", "Muriate of Potash"]
    }

    # Ensure the model is pulled
    model_name = 'mistral'
    pull_model_if_needed(model_name)

    # Use Ollama's chat API for cost and profit estimation
    response = ollama.chat(
        model=model_name,
        messages=[
            {
                'role': 'user',
                'content': f"Estimate the cost and profit for growing {selected_crop} in the given conditions:\n\n{json.dumps(fertilizers)}"
            }
        ]
    )

    cost_profit_estimation = response['message']['content'].strip()

    return render_template('fertilizer_suggestion.html', fertilizers=fertilizers, cost_profit=cost_profit_estimation)

if __name__ == '__main__':
    app.run(debug=True)
