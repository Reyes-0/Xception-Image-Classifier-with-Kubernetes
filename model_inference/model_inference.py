# # Import the necessary libraries
import os
import numpy as np
from tensorflow.keras.models import load_model
import cv2
import PIL.Image as Image
from parameters import model_save_dir, prediction_save_dir, image_directory

# Load the saved model
model_path = os.path.join(model_save_dir, "xception_model.h5")
model = load_model(model_path)

# Load the class names
class_names = {0: 'airplane', 1: 'automobile', 2: 'ship', 3: 'truck'}

# Load the resized image
# image_path = os.path.join('data/processed_uploaded_image', 'resized__uploaded_image.npy')
# img = Image.open('/content/ship.jpg').resize((71,71))
# img_array = np.array(img)/255.0
# img_array = img_array.reshape((1, 71, 71, 3))
# resized_img = np.load(image_path)

uploaded_image_path = os.path.join(image_directory, 'saved_file_path.txt')

with open(uploaded_image_path, 'r') as f:
    image_path_str = f.read()
img = cv2.imread(image_path_str)
resized_img = cv2.resize(img, (71, 71))

img_array = np.array(resized_img) / 255.0
img_array = img_array.reshape((1, 71, 71, 3))

# Make predictions
predictions = model.predict(img_array)

# Get the predicted class index
predicted_class_index = np.argmax(predictions)

# Get the predicted class name
predicted_class_name = class_names[predicted_class_index]

print(f"Predicted class: {predicted_class_name}")

# Create the directory if it doesn't exist
if not os.path.exists(prediction_save_dir):
    os.makedirs(prediction_save_dir)  # Create the directory

# Save the predicted class to a file
# prediction_file_path = os.path.join(prediction_save_dir, "predicted_class.npy")
# with open(prediction_file_path, "w") as f:
#     f.write(predicted_class_name)  # This writes the predicted class name to the file

# Convert the string to a NumPy array
predicted_class_array = np.array([predicted_class_name])

# Save the array to a .npy file
prediction_file_path = os.path.join(prediction_save_dir, "predicted_class.npy")
np.save(prediction_file_path, predicted_class_array)
