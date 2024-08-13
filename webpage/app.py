from flask import Flask, render_template, request, send_file
from PIL import Image, ImageOps
import io

app = Flask(__name__)

# Home route to display the webpage
@app.route('/')
def home():
    return render_template('index.html')

# Handle image upload, process it, and return the result
@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['file']
    if file:
        image = Image.open(file)
        processed_image = model_inference(image)
        return send_image(processed_image)
    return "No file uploaded", 400

# Process the image (dummy model inference)
def model_inference(image):
    processed_image = ImageOps.invert(image)  # Example processing
    return processed_image

# Display the processed image
def send_image(image):
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
