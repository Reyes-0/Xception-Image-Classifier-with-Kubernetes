from flask import Flask, render_template, request, send_file
from PIL import Image, ImageOps
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        image = Image.open(file)

        # Data preparation step
        prepared_image = prepare_image(image)

        # Model inference step (Placeholder)
        output_image = model_inference(prepared_image)

        # Save the processed image to display
        img_io = io.BytesIO()
        output_image.save(img_io, 'PNG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png')

def prepare_image(image):
    # Example data preparation: convert to grayscale and resize
    image = ImageOps.grayscale(image)
    image = image.resize((224, 224))
    return image

def model_inference(image):
    # Placeholder for actual model inference
    # This example just inverts the image colors as a dummy "inference"
    return ImageOps.invert(image)

if __name__ == '__main__':
    app.run(debug=True)
