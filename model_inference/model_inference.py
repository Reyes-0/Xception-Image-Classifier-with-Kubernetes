# need to import the trained_model from model_train.py
# need to import the processed image/images from the data_processing.py
# need to somehow create a image with the prdicted label for the webpage to display.

# Imports go here doing that later
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.xception import preprocess_input
import matplotlib.pyplot as plt

# Test data directory
test_dir = 'path_to_test_data'

# Load the trained model
model = load_model("xception_model.h5")

# Test data generator (assuming no augmentation is needed for test data)
test_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

# Create a test data generator
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(299, 299),  # Xception input size
    batch_size=32,
    class_mode='categorical',
    shuffle=False  # Important for consistent predictions
)

class_names = {0: 'airplane', 1: 'automobile', 2: 'ship', 3: 'truck'}

# Iterate over a few test images
num_images_to_test = 5
for _ in range(num_images_to_test):
    img, label = next(test_generator)
    predictions = model.predict(img)
    output = np.argmax(predictions[0])  # Get the prediction for the first image in the batch
    predicted_label = class_names[output]
    actual_label = list(test_generator.class_indices.keys())\
                    [list(test_generator.class_indices.values()).index(np.argmax(label[0]))]
    print('Actual label:', actual_label)
    print('Predicted label:', predicted_label)