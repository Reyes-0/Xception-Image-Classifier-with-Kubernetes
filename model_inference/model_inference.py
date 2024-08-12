# need to import the trained_model from model_train.py
# need to import the processed image/images from the data_processing.py
# need to somehow create a image with the prdicted label for the webpage to display.

# # Import the necessary libraries
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.xception import preprocess_input
# from parameters.py import test_img, model_x

# # Load the trained model
# model = load_model(f"{model_x}/xception_model.h5")

# class_names = {0: 'airplane', 1: 'automobile', 2: 'ship', 3: 'truck'}

# # Function to load and preprocess an image
# def load_image(img_path):
#     img = image.load_img(img_path, target_size=(299, 299))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array = preprocess_input(img_array)
#     return img_array

# # Load and preprocess the image
# img_array = load_image(test_img)

# # Make predictions
# predictions = model.predict(img_array)
# output = np.argmax(predictions[0])
# predicted_label = class_names[output]

# print('Predicted label:', predicted_label)

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from parameters import test_img, model_x

class ImageClassifier:
    def __init__(self, model_path, class_names):
        # Load the trained model and store the class names
        self.model = load_model(model_path)
        self.class_names = class_names

    def predict(self, preprocessed_img_array):
        """Predict the class of the preprocessed image using the trained model."""
        predictions = self.model.predict(test_img)
        output = np.argmax(predictions[0])
        predicted_label = self.class_names[output]
        return predicted_label

    def classify_preprocessed_image(self, preprocessed_img_array):
        """Classify a preprocessed image."""
        return self.predict(preprocessed_img_array)

if __name__ == '__main__':
    # Define class names and model path
    class_names = {0: 'airplane', 1: 'automobile', 2: 'ship', 3: 'truck'}
    model_path = f"{model_x}xception_model.h5"

    # Example of a dummy preprocessed image (replace this with the actual preprocessed image)
    preprocessed_img_array = np.load("preprocessed_image.npy")  # Example loading from a file

    # Instantiate the ImageClassifier
    classifier = ImageClassifier(model_path, class_names)

    # Classify the preprocessed image
    predicted_label = classifier.classify_preprocessed_image(preprocessed_img_array)
    print('Predicted label:', predicted_label)