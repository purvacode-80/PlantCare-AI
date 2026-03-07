from flask import Flask, render_template, request, redirect, url_for
import os
import numpy as np
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import json

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/images/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MODEL_PATH = 'plant_disease_model.h5'
CLASS_NAMES_PATH = 'class_names.json'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load class names
with open(CLASS_NAMES_PATH, 'r') as f:
    class_names = json.load(f)

# Load model
try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully")
except:
    print("Model not found, building new model (note: needs training)")
    from model.model_builder import build_model
    model = build_model()
    # Note: In a real scenario, you'd load trained weights or train the model

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Preprocess and predict
        img_array = preprocess_image(filepath)
        predictions = model.predict(img_array)
        predicted_class_idx = np.argmax(predictions[0])
        predicted_class = class_names[str(predicted_class_idx)]
        
        # Parse plant and disease
        plant, disease_name = predicted_class.split('___', 1)
        disease_name = disease_name.replace('_', ' ')
        
        # Determine status
        if 'healthy' in disease_name.lower():
            status = 'healthy'
        else:
            status = 'disease'
        
        # For result page
        image_path = f'/static/images/uploads/{filename}'
        
        return render_template('result.html', 
                             image_path=image_path, 
                             status=status, 
                             plant=plant,
                             disease=disease_name)
    
    return redirect('/upload')

if __name__ == '__main__':
    app.run(debug=True)