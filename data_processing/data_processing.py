import numpy as np
import keras
import matplotlib.pyplot as plt
# import PTL.Image as Image 
import os
import cv2
from keras.preprocessing.image import ImageDataGenerator
from parameters import *

class DataProcessing:
    def __init__(self):
        pass
    
    def process_image(self):
        # raw_train_path = raw_train_path
        # image = cv2.imread(self.path)
        # define the data augmentation parameters
        train_datagen = self.ImageDataGenerator(rescale = rescale,
                                   rotation_range = rotation_range,
                                   width_shift_range = width_shift_range,
                                   height_shift_range = height_shift_range,
                                   shear_range = shear_range)

        train_generator = train_datagen.flow_from_directory(raw_train_path,
                                                    class_mode='categorical',
                                                    target_size = target_size,
                                                    shuffle = shuffle,
                                                    batch_size = batch_size)
        
        test_datagen = ImageDataGenerator(rescale = rescale)   
        # raw_test_path = raw_test_path
        validation_generator = test_datagen.flow_from_directory(
                raw_test_path,
                class_mode='categorical',
                target_size = target_size,
                batch_size = batch_size,
                shuffle = shuffle)
        return train_generator, validation_generator
        
    def inference_process_image(self):
        # uploaded_image_path = uploaded_image_path
        test_datagen = self.ImageDataGenerator(rescale = rescale)
        inference_generator = test_datagen.flow_from_directory(
                uploaded_image_path,
                class_mode='categorical')
        
        return inference_generator
    
if __name__ == '__main__':
    
    DP = DataProcessing()
    train_data, validate_data = DP.process_image()
    processed_uploaded_image = DP.inference_process_image()
    dp.process_image()