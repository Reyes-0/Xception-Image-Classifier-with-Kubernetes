# need to import the trained_model from model_train.py
# need to import the processed image/images from the data_processing.py
# need to somehow create a image with the prdicted label for the webpage to display.

# Import the necessary libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input

# Load the trained model
model = load_model("xception_model.h5")

class_names = {0: 'airplane', 1: 'automobile', 2: 'ship', 3: 'truck'}

# Function to load and preprocess an image
def load_image(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

# Get the image path from the webpage (e.g., using a file input field)
img_path = 'path_to_input_image.jpg'

# Load and preprocess the image
img_array = load_image(img_path)

# Make predictions
predictions = model.predict(img_array)
output = np.argmax(predictions[0])
predicted_label = class_names[output]

print('Predicted label:', predicted_label)