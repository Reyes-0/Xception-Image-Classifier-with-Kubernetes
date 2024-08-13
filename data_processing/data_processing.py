import keras
import os
import cv2
import numpy as np
import tensorflow as tf
import PIL.Image as Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from parameters import *

# Create directories if they don't exist
# if not os.path.exists(raw_train_path):
#     os.makedirs(raw_train_path)
# if not os.path.exists(raw_test_path):
#     os.makedirs(raw_test_path)

if not os.path.exists(pv_directory):
    os.makedirs(pv_directory)

train_datagen = ImageDataGenerator(rescale = rescale,
                            rotation_range = rotation_range,
                            width_shift_range = width_shift_range,
                            height_shift_range = height_shift_range,
                            shear_range = shear_range)

train_generator = train_datagen.flow_from_directory(raw_train_path,
                                            class_mode='categorical',
                                            target_size = target_size,
                                            shuffle = shuffle,
                                            batch_size = batch_size,
                                            color_mode = color_mode)

test_datagen = ImageDataGenerator(rescale = rescale)
# raw_test_path = raw_test_path
validation_generator = test_datagen.flow_from_directory(
        raw_test_path,
        class_mode='categorical',
        target_size = target_size,
        batch_size = batch_size,
        shuffle = shuffle,
        color_mode = color_mode)

validation_generator.class_indices

# Save the train generator to the PVC
images_list = []
labels_list = []

for _ in range(train_generator.samples // train_generator.batch_size):
    images, labels = next(train_generator)
    images_list.append(images)
    labels_list.append(labels)

images_array = np.concatenate(images_list, axis=0)
labels_array = np.concatenate(labels_list, axis=0)

# Save the validation generator to the PVC
val_images_list = []
val_labels_list = []

for _ in range(validation_generator.samples // validation_generator.batch_size):
    val_images, val_labels = next(validation_generator)
    val_images_list.append(val_images)
    val_labels_list.append(val_labels)

val_images_array = np.concatenate(val_images_list, axis=0)
val_labels_array = np.concatenate(val_labels_list, axis=0)

if not os.path.exists(processed_train_path):
    os.makedirs(processed_train_path)
if not os.path.exists(processed_test_path):
    os.makedirs(processed_test_path)

np.save(os.path.join(processed_train_path, 'train_images.npy'), images_array)
np.save(os.path.join(processed_train_path, 'train_labels.npy'), labels_array)

np.save(os.path.join(processed_test_path, 'val_images.npy'), val_images_array)
np.save(os.path.join(processed_test_path, 'val_labels.npy'), val_labels_array)

# Load processed data from PV
validation_labels = np.load(os.path.join(processed_test_path, 'val_labels.npy'))
first_value = validation_labels[12]
print("First value:", first_value)


image_path = '/content/download ().jpeg'
# image_path = uploaded_image_path

if not os.path.exists(image_path):
    print(f"Error: Image file '{image_path}' does not exist")
else:
    try:
        img = cv2.imread(image_path)

        if len(img.shape) == 2:  # Grayscale image
            raise ValueError("Image is Grayscale")
        elif len(img.shape) == 3:  # RGB image
            if img.shape[2] == 3:  # Check if it has 3 color channels
                pass
            else:
                raise ValueError("Image has an unknown number of color channels")
        else:
            raise ValueError("Image has an unknown shape")
        
        resized_img = cv2.resize(img, (71, 71))
        pv_directory = 'data/processed_uploaded_image'
        if not os.path.exists(pv_directory):
            os.makedirs(pv_directory)

        filename = 'resized__uploaded_image.npy'
        np.save(os.path.join(pv_directory, filename), resized_img)
        print('Image saved successfully')
    
    except ValueError as e:
        print(f"Error: {e}")