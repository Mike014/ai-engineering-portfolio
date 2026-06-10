# Import the necessary libraries
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Create a sample dataset
data = {
    'Price_High': [1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    'Price_Medium': [0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    'Price_Low': [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    'Maint_High': [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    'Maint_Medium': [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    'Maint_Low': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Seats_Two': [1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    'Seats_More': [0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    'Decision': [0, 1, 0, 2, 1, 2, 0, 3, 1, 3]  # Output classes
}

# Create a DataFrame
df = pd.DataFrame(data)

# Separate features and target
X = df.drop(columns=['Decision'])
y = df['Decision']

# Convert the target to one-hot encoding
y = to_categorical(y, num_classes=4)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create the sequential model
model = Sequential()

# Add two hidden layers with ReLU activation
model.add(Dense(5, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(5, activation='relu'))

# Output layer with softmax activation (4 classes)
model.add(Dense(4, activation='softmax'))

# Compile the model with categorical crossentropy loss
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Print the model summary
model.summary()

# Train the model
model.fit(X_train, y_train, epochs=20, batch_size=5, validation_data=(X_test, y_test))

# Make predictions on the test set
predictions = model.predict(X_test)

# Print the prediction results
predicted_classes = np.argmax(predictions, axis=1)
actual_classes = np.argmax(y_test, axis=1)

results_df = pd.DataFrame({'Actual': actual_classes, 'Predicted': predicted_classes})
print(results_df)




## Extras
# normalize inputs from 0-255 to 0-1
# X_train = X_train / 255
# X_test = X_test / 255