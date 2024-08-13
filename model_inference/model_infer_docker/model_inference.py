# need to import the trained_model from model_train.py
# need to import the processed image/images from the data_processing.py
# need to somehow create a image with the prdicted label for the webpage to display.

# # Import the necessary libraries
import os
import numpy as np
from tensorflow.keras.models import load_model
import cv2
from parameters import model_save_dir, prediction_save_dir

# Load the saved model
model_path = os.path.join(model_save_dir, "xception_model.h5")
model = load_model(model_path)

# Load the class names
class_names = {0: 'airplane', 1: 'automobile', 2: 'ship', 3: 'truck'}

# Load the resized image
image_path = os.path.join('data/processed_uploaded_image', 'resized__uploaded_image.npy')
resized_img = np.load(image_path)

# Make predictions
predictions = model.predict(resized_img)

# Get the predicted class index
predicted_class_index = np.argmax(predictions)

# Get the predicted class name
predicted_class_name = class_names[predicted_class_index]

print(f"Predicted class: {predicted_class_name}")

# Save the predicted class to a file
prediction_file_path = os.path.join(prediction_save_dir, "predicted_class.txt")
with open(prediction_file_path, "w") as f:
    f.write(predicted_class_name) # writes the predicted class name in the file