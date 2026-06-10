# Re-import libraries after execution state reset
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

# Load a simple dataset from scikit-learn (California Housing Prices)
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = data.target  # The target variable (house price)

# Print some rows to check the data
print(df.head())

# Choose the target: "Target" column
y = df['Target']

# Select the predictors (all other numerical columns)
X = df.drop(columns=['Target'])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data with StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create the sequential model
model = Sequential()

# First hidden layer with 64 neurons and ReLU
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))

# Second hidden layer with 32 neurons and ReLU
model.add(Dense(32, activation='relu'))

# Output layer with a single neuron for predicting house prices
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Print the model summary
model.summary()

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=10, validation_data=(X_test, y_test))

# Make predictions on the test set
predictions = model.predict(X_test)

# Display results
results_df = pd.DataFrame({'Actual': y_test[:10].values, 'Predicted': predictions[:10].flatten()})
print(results_df)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(results_df['Actual'], label='Actual')
plt.plot(results_df['Predicted'], label='Predicted')
plt.xlabel('Sample Index')
plt.ylabel('House Price')
plt.title('Actual vs Predicted House Prices')
plt.legend()
plt.show()
