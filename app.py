from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    state = request.form['state']
    postalcode = request.form['postalcode']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    prompt = request.form['prompt']
    report = request.files['report']

    if report and report.filename.endswith('.pdf'):
        report_path = os.path.join(app.config['UPLOAD_FOLDER'], report.filename)
        report.save(report_path)

        # Prepare the data for API
        data = {
            "state": state,
            "postalcode": postalcode,
            "latitude": latitude,
            "longitude": longitude,
            "prompt": prompt,
            "report_path": report_path
        }

        # Example of sending the data to an API (replace with your actual API call)
        # response = requests.post('http://yourapi.com/endpoint', json=data)
        
        # For now, we'll just return the data as JSON to verify
        return jsonify(data)

    return jsonify({"error": "Invalid file type"}), 400

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
