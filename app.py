import os
import json
import pdfplumber
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import requests # type: ignore



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/submit_form')
# def submit_form():
#     state = request.form['state']
#     city = request.form['city']
   
#     prompt = request.form['prompt']
#     report = request.files['report']


        def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text += page.extract_text()
    return text

    
# Example usage
api_key = "TP1CcABATnjNxFHZaXoPifGyou33iQDc"  # Replace with your actual API key
  # Replace with the location key
location_key = get_location_key(city, "IN")
print(location_key," <-- location")

weather_data = get_accuweather_data(api_key, location_key)

if weather_data:
  print(weather_data)

   @app.route('/submit_form', methods=['POST'])
def submit_form():
      state = request.form['state']
    city = request.form['city']
   
    prompt = request.form['prompt']
    report = request.files['report']
    if 'report' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['report']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract text from PDF
        extracted_text = extract_text_from_pdf(file_path)

        
        # Simulate converting extracted text to JSON format
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
     # Print the converted JSON for debugging purposes
        print("Converted Report JSON:", json.dumps(report_json, indent=4))
        
        # Return the JSON response
        return jsonify(report_json)

    return jsonify({"error": "Invalid file format"}), 400
def get_location_key(city, country_code):
  api_key = "TP1CcABATnjNxFHZaXoPifGyou33iQDc"
  url = f"https://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city}&countrycode={country_code}"
  response = requests.get(url)
  if response.status_code == 200:
    data = json.loads(response.text)
    if data:
      return data[0]['Key']
  else:
    print("Error fetching location key")
    return None

# Example usage

def get_accuweather_data(api_key, location_key):
  """Fetches weather data from AccuWeather API.

  Args:
    api_key: Your AccuWeather API key.
    location_key: The location key for the desired location.

  Returns:
    A JSON response containing the weather data.
  """

  base_url = "http://dataservice.accuweather.com"
  endpoint = f"/currentconditions/v1/{location_key}?apikey={api_key}&details=true"
  url = base_url + endpoint

  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error fetching data: {response.text}")
    return None


if __name__ == '__main__':
    app.run(debug=True)



 

