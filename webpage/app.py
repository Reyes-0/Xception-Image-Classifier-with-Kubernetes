from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import numpy as np
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/mnt/image_uploads'
app.config['PREDICTED_PATH'] = '/mnt/predictions/predicted_class.npy'
# app.config['UPLOAD_FOLDER'] = 'image_uploads'
# app.config['PREDICTED_PATH'] = 'predictions'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max size

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if not os.path.exists(app.config['PREDICTED_PATH']):
    os.makedirs(app.config['PREDICTED_PATH'])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Extract the file extension and save the file as 'uploaded_raw_image.<extension>'
        file_extension = os.path.splitext(file.filename)[1]
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f'uploaded_raw_image{file_extension}')
        file.save(file_path)
        
        # Save the file path to the PREDICTED_PATH folder
        predicted_class_labels_path = os.path.join(app.config['UPLOAD_FOLDER'], 'saved_file_path.npy')
        np.save(predicted_class_labels_path, file_path)
        
        return redirect(url_for('display_image', extension=file_extension))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/display')
def display_image():
    file_extension = request.args.get('extension', '.jpg')
    filename = f'uploaded_raw_image{file_extension}'
    file_url = url_for('uploaded_file', filename=filename)

    time.sleep(60)
    
    # Load the predicted class label
    predicted_class_labels_path = os.path.join(app.config['PREDICTED_PATH'], 'predicted_class.npy')

    predicted_class_label = np.load(predicted_class_labels_path)
    
    return render_template('display.html', filename='uploaded_raw_image.jpg', file_url=file_url, predicted_class_label=predicted_class_label)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
