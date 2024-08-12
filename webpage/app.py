from flask import Flask, render_template, request, send_file, jsonify
from PIL import Image, ImageOps
import io
import time  # Simulate processing time

app = Flask(__name__)

# Global state to control the flow
app_state = {
    "data_prep_done": False,
    "model_training_done": False,
    "inference_done": False
}

@app.route('/')
def home():
    trigger_data_prep()
    return render_template('index.html')

# Simulate data preparation
def trigger_data_prep():
    global app_state
    time.sleep(2)  # Simulate a delay for data preparation
    app_state["data_prep_done"] = True
    trigger_model_training()

# Step 2: Trigger model training
def trigger_model_training():
    global app_state
    time.sleep(2)  # Simulate model training
    app_state["model_training_done"] = True

# Step 3: Handle image upload and trigger data processing
@app.route('/upload', methods=['POST'])
def upload_image():
    if app_state["model_training_done"]:
        file = request.files['file']
        if file:
            image = Image.open(file)
            prepared_image = prepare_image(image)
            output_image = model_inference(prepared_image)
            return send_image(output_image)
    return "Model training not completed", 400

# Step 4: Display the result after inference
def send_image(image):
    global app_state
    app_state["inference_done"] = True
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

# Data preparation function
def prepare_image(image):
    image = ImageOps.grayscale(image)
    image = image.resize((224, 224))
    return image

# Model inference function (dummy)
def model_inference(image):
    time.sleep(2)  # Simulate inference time
    return ImageOps.invert(image)

# API to check the state of the app
@app.route('/status')
def check_status():
    return jsonify(app_state)

if __name__ == '__main__':
    app.run(debug=True)
