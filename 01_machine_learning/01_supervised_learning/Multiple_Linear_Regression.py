import numpy as np
from sklearn.linear_model import LinearRegression

class My_Multiple_LinearRegression:
    """
    A custom multiple linear regression class that trains a model and provides prediction functionality.
    """

    def __init__(self, X, y):
        """
        Initializes the class with training data.

        Args:
          X (np.ndarray): A 2D array representing the feature matrix (multiple features).
          y (np.ndarray): A 1D array representing the target vector.
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

        # Create the Linear Regression model
        self.reg = LinearRegression()

    def create_and_train(self):
        """
        Trains the linear regression model using the stored data.

        Returns:
          tuple: A tuple containing the learned coefficients and intercept.
          - Coefficients: Array of values for each feature.
          - Intercept: Bias term (theta_0).
        """
        self.reg.fit(self.X, self.y)
        return self.reg.coef_, self.reg.intercept_

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

    def get_model_summary(self):
        """
        Provides a summary of the trained model, including coefficients and intercept.

        Returns:
          str: A summary string with the model details.
        """
        if not hasattr(self.reg, 'coef_'):
            raise ValueError("The model has not been trained yet. Call create_and_train first.")
        
        summary = "Model Summary:\n"
        summary += f"Intercept (theta_0): {self.reg.intercept_}\n"
        summary += f"Coefficients (theta_1, theta_2, ...): {self.reg.coef_}\n"
        return summary


# This code creates a linear regression model to estimate house prices based on square meters.
# Training: It uses historical data (square meters and prices) to calculate:

# Square Meters = Independent Variable (what you already know, the data you base your guess on).
# House Price = Dependent Variable (what you want to predict, based on square meters).
# Linear Regression: The model learns the relationship between square meters and house prices.
# Coefficient: How much the price increases per additional square meter.
# Intercept: The base price when square meters are 0.
# Prediction: For a new house, the model calculates the estimated price using the formula:
# Price = Coefficient * SquareMeters + Intercept
# Example: If the coefficient is 200 and the intercept is 50,000, for 80 square meters, the price would be:
# Price = 200 * 80 + 50,000 = 66,000