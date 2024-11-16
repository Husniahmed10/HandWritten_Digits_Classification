from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import io
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


try:
    model = load_model("C:/Users/husni/OneDrive/Desktop/My AI/Projects/Digits_Recognizer/Backend/models.h5")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error: {e}")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB limit

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        print("No file part")
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    print(f"Received file: {file.filename}")

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only PNG, JPG, JPEG, GIF are allowed.'}), 400

    try:
        img = Image.open(file).convert('L')
        img = img.resize((28, 28))
        img_array = np.array(img) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        predictions = model.predict(img_array)
        predicted_digit = np.argmax(predictions[0])

        return jsonify({'digit': int(predicted_digit)})
    except Exception as e:
        print(f"Error processing image: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
