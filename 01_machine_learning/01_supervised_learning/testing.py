from Simple_Linear_Regression import My_LinearRegression
import numpy as np

# Test 1: Base test with a simple dataset
def test_simple_linear_regression():
    X = [[50], [60], [70], [80]]  # Square meters
    y = [100000, 120000, 140000, 160000]  # Prices
    model = My_LinearRegression(X, y)
    coefficients, intercept = model.create_and_train()
    
    assert np.isclose(coefficients[0], 2000), "Coefficient test failed"
    assert np.isclose(intercept, 0), "Intercept test failed"
    
    prediction = model.predict_sample([75])
    expected_price = 2000 * 75
    assert np.isclose(prediction, expected_price), "Prediction test failed"
    print("Test 1 passed!")

# Test 2: Test with multiple features (e.g., square meters, number of rooms)
def test_multiple_features():
    X = [[50, 2], [60, 3], [70, 4], [80, 5]]  # Square meters and rooms
    y = [100000, 130000, 160000, 190000]  # Prices
    model = My_LinearRegression(X, y)
    coefficients, intercept = model.create_and_train()
    
    prediction = model.predict_sample([75, 4])
    expected_price = coefficients[0] * 75 + coefficients[1] * 4 + intercept
    assert np.isclose(prediction, expected_price), "Prediction with multiple features failed"
    print("Test 2 passed!")

# Test 3: Edge case - Single data point
def test_single_data_point():
    X = [[60]]  # Square meters
    y = [120000]  # Prices
    try:
        model = My_LinearRegression(X, y)
        coefficients, intercept = model.create_and_train()
    except Exception as e:
        assert str(e) == "The number of samples in X and y must match.", "Edge case single data point failed"
    print("Test 3 passed!")

# Test 4: Handling missing or invalid data
def test_invalid_data():
    X = [[50], [60], None, [80]]  # Contains invalid data
    y = [100000, 120000, 140000, None]  # Contains invalid data
    try:
        model = My_LinearRegression(X, y)
    except Exception as e:
        assert "setting an array element with a sequence" in str(e), "Invalid data handling failed"
    print("Test 4 passed!")

# Test 5: Large dataset with random noise
def test_large_dataset():
    np.random.seed(42)
    X = np.random.randint(50, 200, size=(1000, 1))  # Square meters
    y = 200 * X.flatten() + np.random.normal(0, 5000, size=1000)  # Add noise to prices
    model = My_LinearRegression(X, y)
    coefficients, intercept = model.create_and_train()
    
    prediction = model.predict_sample([100])
    expected_price = coefficients[0] * 100 + intercept
    assert np.isclose(prediction, expected_price, atol=5000), "Large dataset test failed"
    print("Test 5 passed!")

# Test 6: Test with no variance in y (constant target)
def test_no_variance_in_target():
    X = [[50], [60], [70], [80]]  # Square meters
    y = [100000, 100000, 100000, 100000]  # Constant prices
    model = My_LinearRegression(X, y)
    coefficients, intercept = model.create_and_train()
    
    assert np.allclose(coefficients, 0), "Coefficient should be 0 for no variance"
    assert np.isclose(intercept, 100000), "Intercept should be equal to the constant target"
    print("Test 6 passed!")

# Run all tests
test_simple_linear_regression()
test_multiple_features()
test_single_data_point()
test_invalid_data()
test_large_dataset()
test_no_variance_in_target()
