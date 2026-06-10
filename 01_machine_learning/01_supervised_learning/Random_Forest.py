import numpy as np
from sklearn.ensemble import RandomForestRegressor

class My_RandomForestRegression:
    """
    A custom Random Forest regression class that trains a model and provides prediction functionality.
    """

    def __init__(self, X, y, n_estimators=100, random_state=None):
        """
        Initializes the class with training data and model parameters.

        Args:
          X (np.ndarray): A 2D array representing the feature matrix (multiple features).
          y (np.ndarray): A 1D array representing the target vector.
          n_estimators (int): The number of trees in the forest (default: 100).
          random_state (int or None): Random state for reproducibility (default: None).
        """
        self.X = np.array(X, dtype=float)
        self.y = np.array(y, dtype=float)

        # Ensure the data has the correct format
        if self.X.ndim != 2:
            raise ValueError("X must be a 2D array representing multiple features.")
        if self.y.ndim != 1:
            raise ValueError("y must be a 1D array representing the target variable.")
        if self.X.shape[0] != self.y.shape[0]:
            raise ValueError("The number of samples in X and y must match.")

        # Create the Random Forest model
        self.reg = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)

    def create_and_train(self):
        """
        Trains the Random Forest regression model using the stored data.

        Returns:
          None
        """
        self.reg.fit(self.X, self.y)

    def predict_sample(self, sample):
        """
        Predicts the target value for a new sample.

        Args:
          sample (np.ndarray or list): A 1D array or list representing the new sample (feature values).

        Returns:
          float: The predicted target value for the given sample.
        """
        sample = np.array(sample, dtype=float)

        # Validate the sample
        if sample.ndim != 1:
            raise ValueError("Sample must be a 1D array or list.")
        if sample.shape[0] != self.X.shape[1]:
            raise ValueError("Sample size must match the number of features in X.")

        return self.reg.predict(sample.reshape(1, -1))[0]

    def get_feature_importance(self):
        """
        Retrieves the importance of each feature in the Random Forest model.

        Returns:
          np.ndarray: An array of feature importances.
        """
        if not hasattr(self.reg, 'feature_importances_'):
            raise ValueError("The model has not been trained yet. Call create_and_train first.")
        
        return self.reg.feature_importances_

    def get_model_summary(self):
        """
        Provides a summary of the trained model, including the number of trees and feature importances.

        Returns:
          str: A summary string with the model details.
        """
        if not hasattr(self.reg, 'feature_importances_'):
            raise ValueError("The model has not been trained yet. Call create_and_train first.")
        
        summary = "Random Forest Model Summary:\n"
        summary += f"Number of Trees: {self.reg.n_estimators}\n"
        summary += f"Feature Importances: {self.get_feature_importance()}\n"
        return summary

# The Random Forest is a machine learning method that combines multiple decision trees to make more accurate and robust predictions.
# What does it need? 
# - Independent variables (feature): E.g. square meters, number of rooms, age of the house.
# - Target (dependent value): E.g. the price of the house.
# - Number of trees: How many decision trees you want to include in the "forest." More trees = better forecasts (usually).

# Each decision tree makes a prediction based on a portion of the data.
# The final prediction is the average (by regression) or majority vote (by classification) of all trees.

# What is random_state?
# - It is a random seed that controls how the data is randomly chosen to train each tree.
# - It is used to obtain reproducible results:
#   . With the same random_state, the model will always give the same results.
# If you don't set it, the model may produce slightly different results each time.

# How to use it?
# - Create an instance of My_RandomForestRegression.
# - Train the model with create_and_train.
# - Predict the target value for a new sample with predict_sample.
# - Get the feature importances with get_feature_importance.
# - Get a summary of the model with get_model_summary.

# Example:
# # Create the Random Forest model
# rfr = My_RandomForestRegression(X=[[50], [100], [150], [200]], y=[100, 200, 300, 400], n_estimators=100, random_state=42)
# rfr.create_and_train()
# rfr.predict_sample([75])
# rfr.get_feature_importance()
# rfr.get_model_summary()

# Output:
# 140.0
# array([1.])
# Random Forest Model Summary:
# Number of Trees: 100
# Feature Importances: [1.]


# if __name__ == "__main__":
#     # Create the Random Forest model
#     rfr = My_RandomForestRegression(X=[[50], [100], [150], [200]], y=[100, 200, 300, 400], n_estimators=100, random_state=42)
#     rfr.create_and_train()
#     print(rfr.predict_sample([75]))
#     print(rfr.get_feature_importance())
#     print(rfr.get_model_summary())  