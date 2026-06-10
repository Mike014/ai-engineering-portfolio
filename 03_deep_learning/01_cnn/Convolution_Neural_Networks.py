import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Import necessary libraries

# Create the CNN model
model = Sequential()

# First convolutional layer: 16 filters of size 2x2 with ReLU activation and input shape specified
model.add(Conv2D(16, (2, 2), strides=(1, 1), activation='relu', input_shape=(128, 128, 3)))

# Max-Pooling layer to reduce image dimensions
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# Second convolutional layer: 32 filters of size 2x2 with ReLU activation
model.add(Conv2D(32, (2, 2), strides=(1, 1), activation='relu'))

# Max-Pooling layer
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# Flatten layer to connect the convolutional layers to the fully connected layer
model.add(Flatten())

# Fully Connected layer with 100 neurons and ReLU activation
model.add(Dense(100, activation='relu'))

# Output layer with Softmax activation for classification into N classes (e.g., 10 classes for digits 0-9)
model.add(Dense(10, activation='softmax'))

# Compile the model using categorical cross-entropy for classification
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Print the model summary
model.summary()

# How do CNNs work?
# 🔹 Primary Architecture:
# - Convolutional Layer: Applies filters to the image to extract features.
# - ReLU Activation: Filters negative values to improve training.
# - Pooling Layer: Reduces the dimensions of the feature maps to make the model more efficient.
# - Fully Connected Layer: Connects the extracted features to the final neurons for classification.
