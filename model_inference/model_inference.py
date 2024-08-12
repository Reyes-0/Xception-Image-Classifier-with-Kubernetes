# need to import the trained_model from model_train.py
# need to import the processed image/images from the data_processing.py
# need to somehow create a image with the prdicted label for the webpage to display.

# # Import the necessary libraries
import os
import numpy as np
from tensorflow.keras.models import load_model
import cv2
from parameters import model_save_dir

class ModelInference:
    def __init__(self, model_path, class_names):
        self.model = load_model(model_path)
        self.class_names = class_names

    def predict(self, image_path):
        # Load the resized image
        resized_img = np.load(image_path)

        # Make predictions
        predictions = self.model.predict(resized_img.reshape((1, 71, 71, 3)))

        # Get the predicted class index
        predicted_class_index = np.argmax(predictions)

        # Get the predicted class name
        predicted_class_name = self.class_names[predicted_class_index]

        return predicted_class_name

# Example usage:
model_path = os.path.join(model_save_dir, "xception_model.h5")
class_names = {0: 'airplane', 1: 'automobile', 2: 'ship', 3: 'truck'}
image_path = os.path.join('data/processed_uploaded_image', 'resized__uploaded_image.npy')

inference = ModelInference(model_path, class_names)
predicted_class_name = inference.predict(image_path)
print(f"Predicted class: {predicted_class_name}")