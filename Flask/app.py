import numpy as np
import os
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input

# Load the trained model
modeln = load_model("VGG16-Tea-Leaves-disease-model.h5")

app = Flask(__name__)

# Home page routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/About')
def teahome():
    return render_template('About.html')

@app.route('/Tryit', methods=["GET", "POST"])
def nres():
    if request.method == "POST":
        f = request.files.get('image')
        if not f:
            return render_template('Tryit.html', error="No file selected.")

        # Save image to static/uploads
        basepath = os.path.dirname(__file__)
        upload_folder = os.path.join(basepath, 'static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        filepath = os.path.join(upload_folder, f.filename)
        f.save(filepath)

        # Load and preprocess image
        img = image.load_img(filepath, target_size=(224, 224))
        x = image.img_to_array(img)
        X = np.expand_dims(x, axis=0)
        img_data = preprocess_input(X)

        # Predict using model
        prediction = np.argmax(modeln.predict(img_data))

        # Class labels
        index = [
            'Anthracnose',
            'Algal Leaf',
            'Bird Eye Spot',
            'Brown Blight',
            'Gray Light',
            'Healthy',
            'Red Leaf Spot',
            'White Spot'
        ]
        nresult = index[prediction] if prediction < len(index) else "Unknown"

        # Fertilizer and prevention data
        disease_info = {
            'Anthracnose': {
                'fertilizer': "Name: Bordeaux Mixture\nContents: Copper Sulfate + Lime\nWhy: Copper acts as a broad-spectrum fungicide\nMethod: Spray 1% Bordeaux mixture on affected plants every 10-15 days.",
                'prevention': 'Prune infected parts, avoid overhead irrigation, and ensure proper air circulation.'
            },
            'Algal Leaf': {
                'fertilizer': "Name: NPK 19:19:19\nContents: 19% Nitrogen, 19% Phosphorus, 19% Potassium\nWhy: Supports balanced growth and strengthens plant immune system\nMethod: Apply as a foliar spray, diluted in water (5g/litre) every 15 days.",
                'prevention': 'Reduce humidity, improve ventilation, and apply copper-based fungicide if needed.'
            },
            'Bird Eye Spot': {
                'fertilizer': "Name: Muriate of Potash (MOP)\nContents: 60% Potassium\nWhy: Enhances disease resistance and water regulation\nMethod: Soil application at root zone, 20-25 kg/acre during active growth.",
                'prevention': 'Apply fungicides like Mancozeb and remove infected leaves to prevent spread.'
            },
            'Brown Blight': {
                'fertilizer': "Name: Compost + Urea\nContents: Organic matter + 46% Nitrogen\nWhy: Improves soil health and promotes leaf recovery\nMethod: Apply compost monthly and urea at 1g/litre water as foliar feed.",
                'prevention': 'Avoid leaf wetness, ensure drainage, and apply protective fungicides like Chlorothalonil.'
            },
            'Gray Light': {
                'fertilizer': "Name: Urea or Ammonium Sulfate\nContents: High Nitrogen (Urea 46%, Ammonium Sulfate 21%)\nWhy: Stimulates new leaf development and recovery\nMethod: Foliar spray every 15 days at 1g/litre dilution.",
                'prevention': 'Increase sunlight exposure, maintain plant hygiene, and apply sulfur dust.'
            },
            'Healthy': {
                'fertilizer': "Name: Balanced Organic Fertilizer\nContents: Vermicompost + NPK\nWhy: Sustains plant health and boosts immunity\nMethod: Apply 2-3 kg per plant every month.",
                'prevention': 'Maintain regular nutrient schedule and monitor for early symptoms.'
            },
            'Red Leaf Spot': {
                'fertilizer': "Name: Zineb or Mancozeb Fungicide Fertilizer\nContents: Zinc-based or Manganese-based contact fungicides\nWhy: Prevents fungal growth and leaf decay\nMethod: Spray every 10 days using 2g/litre dilution.",
                'prevention': 'Remove affected foliage and spray contact fungicides like Zineb every 10 days.'
            },
            'White Spot': {
                'fertilizer': "Name: Sulfur 80% WDG\nContents: 80% elemental sulfur (wettable)\nWhy: Controls fungal spores and improves resistance\nMethod: Spray 2g/litre on foliage, avoid application during peak sunlight.",
                'prevention': 'Avoid overhead watering and apply sulfur-based sprays during early infection stages.'
            }
        }

        details = disease_info.get(nresult, {
            'fertilizer': 'No info available',
            'prevention': 'No info available'
        })

        image_path = f'static/uploads/{f.filename}'

        return render_template(
            'Tryit.html',
            prediction=nresult,
            image_path=image_path,
            fertilizer=details['fertilizer'],
            prevention=details['prevention']
        )

    return render_template('Tryit.html')  # For GET requests

if __name__ == "__main__":
    app.run(debug=True, port=8989)