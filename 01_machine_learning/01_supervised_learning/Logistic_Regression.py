import numpy as np
from sklearn.linear_model import LogisticRegression

class My_LogisticRegression:
    """
    A custom logistic regression class that trains a model and provides prediction and probability functionality.
    """

    def __init__(self, X, y):
        """
        Initializes the class with training data.

        Args:
          X (np.ndarray): A 2D array representing the feature matrix (multiple features).
          y (np.ndarray): A 1D array representing the binary target vector (0 or 1).
        """
        self.X = np.array(X, dtype=float)
        self.y = np.array(y, dtype=float)

        # Ensure the data has the correct format
        if self.X.ndim != 2:
            raise ValueError("X must be a 2D array representing multiple features.")
        if self.y.ndim != 1:
            raise ValueError("y must be a 1D array representing the binary target variable.")
        if self.X.shape[0] != self.y.shape[0]:
            raise ValueError("The number of samples in X and y must match.")
        if not np.all(np.isin(self.y, [0, 1])):
            raise ValueError("y must contain only binary values (0 or 1).")

        # Create the Logistic Regression model
        self.reg = LogisticRegression()

    def create_and_train(self):
        """
        Trains the logistic regression model using the stored data.

        Returns:
          tuple: A tuple containing the learned coefficients and intercept.
          - Coefficients: Array of values for each feature.
          - Intercept: Bias term (theta_0).
        """
        self.reg.fit(self.X, self.y)
        return self.reg.coef_, self.reg.intercept_

    def predict_sample(self, sample):
        """
        Predicts the class (0 or 1) for a new sample.

        Args:
          sample (np.ndarray or list): A 1D array or list representing the new sample (feature values).

        Returns:
          int: The predicted class (0 or 1) for the given sample.
        """
        sample = np.array(sample, dtype=float)

        # Validate the sample
        if sample.ndim != 1:
            raise ValueError("Sample must be a 1D array or list.")
        if sample.shape[0] != self.X.shape[1]:
            raise ValueError("Sample size must match the number of features in X.")

        return int(self.reg.predict(sample.reshape(1, -1))[0])

    def predict_probability(self, sample):
        """
        Predicts the probability of each class (0 or 1) for a new sample.

        Args:
          sample (np.ndarray or list): A 1D array or list representing the new sample (feature values).

        Returns:
          np.ndarray: An array of probabilities for each class.
        """
        sample = np.array(sample, dtype=float)

        # Validate the sample
        if sample.ndim != 1:
            raise ValueError("Sample must be a 1D array or list.")
        if sample.shape[0] != self.X.shape[1]:
            raise ValueError("Sample size must match the number of features in X.")

        return self.reg.predict_proba(sample.reshape(1, -1))[0]

    def get_model_summary(self):
        """
        Provides a summary of the trained model, including coefficients and intercept.

        Returns:
          str: A summary string with the model details.
        """
        if not hasattr(self.reg, 'coef_'):
            raise ValueError("The model has not been trained yet. Call create_and_train first.")
        
        summary = "Logistic Regression Model Summary:\n"
        summary += f"Intercept (theta_0): {self.reg.intercept_}\n"
        summary += f"Coefficients (theta_1, theta_2, ...): {self.reg.coef_}\n"
        return summary


# Logistic Regression is a machine learning method that predicts the probability 
# that an event belongs to one of two classes (e.g. yes/no, 1/0) and then classifies 
# the result based on a threshold (usually 0.5).

# How it works:
# 1. Analyzes features (e.g. age, income) to calculate a probability between 0 and 1.
# 2. Uses a threshold (usually 0.5) to classify the event into one of two classes.

# Example: Predicting if a customer will churn (leave) a subscription service.
# Features: Age, Income, Subscription Length.
# Target: Churn (0 or 1).

# Complete code from Logistic_Regression lesson.

# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import log_loss
# import matplotlib.pyplot as plt

# # Load the dataset
# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/ChurnData.csv"
# churn_df = pd.read_csv(url)

# # Add the 'callcard' feature
# churn_df['callcard'] = churn_df['tenure'] * churn_df['age']

# # Function to calculate log loss
# def calculate_log_loss(features):
#     X = np.asarray(churn_df[features])
#     y = np.asarray(churn_df['churn'])
#     X_norm = StandardScaler().fit(X).transform(X)
#     X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2, random_state=4)
#     LR = LogisticRegression().fit(X_train, y_train)
#     yhat_prob = LR.predict_proba(X_test)
#     return log_loss(y_test, yhat_prob)

# # a. Add the 'callcard' feature
# features_a = ['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip', 'callcard']
# log_loss_a = calculate_log_loss(features_a)
# print(f"Log loss with 'callcard': {log_loss_a}")

# # b. Add the 'wireless' feature
# churn_df['wireless'] = np.random.randint(0, 2, churn_df.shape[0])  # Add a dummy 'wireless' column
# features_b = ['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip', 'wireless']
# log_loss_b = calculate_log_loss(features_b)
# print(f"Log loss with 'wireless': {log_loss_b}")

# # c. Add both 'callcard' and 'wireless' features
# features_c = ['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip', 'callcard', 'wireless']
# log_loss_c = calculate_log_loss(features_c)
# print(f"Log loss with 'callcard' and 'wireless': {log_loss_c}")

# # d. Remove the 'equip' feature
# features_d = ['tenure', 'age', 'address', 'income', 'ed', 'employ']
# log_loss_d = calculate_log_loss(features_d)
# print(f"Log loss without 'equip': {log_loss_d}")

# # e. Remove the 'income' and 'employ' features
# features_e = ['tenure', 'age', 'address', 'ed', 'equip']
# log_loss_e = calculate_log_loss(features_e)
# print(f"Log loss without 'income' and 'employ': {log_loss_e}")


# Logistic Regression is great for problems that require a binary solution (e.g. yes/no, 1/0). Here's a simple summary:

# 1. Use features:

# Analyze independent variables (e.g. age, income) to calculate a probability.

# 2. Predict probability:

# Calculate how likely it is that the event is in Class 1 (e.g. churn, disease, etc.).

# 3. Classify:

# Use a threshold (e.g. 0.5) to decide:
# Above threshold → Class 1.
# Below threshold → Class 0.

# 4. Calculate Log Loss:

# Measure how much and when the model was wrong in its predictions.
# Heavily penalizes confident but incorrect predictions (e.g. predicting something that doesn't happen with 90% confidence).

# When we talk about classes in Logistic Regression, we are referring to binary solutions, that is, two possible outcomes:

# Class 0: An event does not happen (e.g. the user does not leave the service).
# Class 1: An event happens (e.g. the user leaves the service).