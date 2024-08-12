import os
import numpy as np
import tensorflow as tf
from dotenv import load_dotenv
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.applications import Xception

# Load environment variables from config.env
load_dotenv('config.env')

# Paths to preprocessed data
train_data_path = os.getenv('TRAIN_DATA_PATH', '/data/preprocessed/train_data.npy')
train_labels_path = os.getenv('TRAIN_LABELS_PATH', '/data/preprocessed/train_labels.npy')
validation_data_path = os.getenv('VALIDATION_DATA_PATH', '/data/preprocessed/validation_data.npy')
validation_labels_path = os.getenv('VALIDATION_LABELS_PATH', '/data/preprocessed/validation_labels.npy')
model_save_dir = os.getenv('MODEL_SAVE_DIR', '/data/saved_models')

# Load preprocessed data and labels
train_data = np.load(train_data_path)
train_labels = np.load(train_labels_path)
validation_data = np.load(validation_data_path)
validation_labels = np.load(validation_labels_path)

# Model setup
input_shape = train_data.shape[1:]

base_model = Xception(weights='imagenet',
                      include_top=False,
                      input_shape=input_shape,
                      pooling='avg')

# Freezing the base model layers
for layer in base_model.layers:
    layer.trainable = False

# Adding custom layers on top of the base model
x = Dense(1024, activation="relu")(base_model.output)
x = Dropout(0.5)(x)
x = Dense(512, activation="relu")(x)
x = Dropout(0.2)(x)
preds = Dense(4, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=preds)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    train_data, train_labels,
    epochs=30,
    validation_data=(validation_data, validation_labels)
)

# Save the trained model
save_path = os.path.join(model_save_dir, "xception_model.h5")
model.save(save_path, include_optimizer=True)