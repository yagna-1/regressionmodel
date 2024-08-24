# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OW3YkfkY8-qVvS4ndEp061ctCHkz0QuP
"""

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import ipywidgets as widgets
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the visual style
sns.set(style="whitegrid")

# Load the California housing dataset
data = fetch_california_housing()

# Convert to a DataFrame for easier manipulation and exploration
df = pd.DataFrame(data.data, columns=data.feature_names)
df['MedHouseValue'] = data.target

# Display the first few rows of the dataset
print("First few rows of the dataset:")
display(df.head())

# Display basic statistics of the dataset
print("\nBasic statistics of the dataset:")
display(df.describe())

# Display correlation matrix to understand feature relationships
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix of Features')
plt.show()

# Split the data into features and target
X, y = df.drop('MedHouseValue', axis=1), df['MedHouseValue']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the training and testing sets
print(f"Training set shape: X_train={X_train.shape}, y_train={y_train.shape}")
print(f"Testing set shape: X_test={X_test.shape}, y_test={y_test.shape}")

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Display a few rows of the standardized features
print("Standardized feature sample:")
print(X_train[:5])

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate and print the Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Since we're using Linear Regression, we can look at the coefficients as a measure of feature importance
coefficients = pd.Series(model.coef_, index=data.feature_names)

# Display the coefficients
print("Feature Importance (Coefficients):")
display(coefficients.sort_values(ascending=False))

# Plot the feature importance
plt.figure(figsize=(10, 6))
coefficients.sort_values().plot(kind='barh')
plt.title('Feature Importance based on Linear Regression Coefficients')
plt.show()

# Function to predict house price
def predict_price(change):
    input_values = {
        'MedInc': med_inc.value,
        'HouseAge': house_age.value,
        'AveRooms': ave_rooms.value,
        'AveBedrms': ave_bedrooms.value,
        'Population': population.value,
        'AveOccup': ave_occupancy.value,
        'Latitude': latitude.value,
        'Longitude': longitude.value
    }

    # Convert the input to a DataFrame to ensure it has feature names
    input_df = pd.DataFrame([input_values])

    # Standardize the input values
    input_values_scaled = scaler.transform(input_df)

    # Predict the house price
    prediction = model.predict(input_values_scaled)[0]

    # Display the prediction
    print(f"Predicted House Price: ${prediction*100000:.2f}")

# Button to trigger the prediction
predict_button = widgets.Button(description="Predict")
predict_button.on_click(predict_price)

# Display the form
display(med_inc, house_age, ave_rooms, ave_bedrooms, population, ave_occupancy, latitude, longitude, predict_button)

# Plot Actual vs Predicted Prices
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Housing Prices')
plt.show()

# Calculate residuals
residuals = y_test - y_pred

# Plot Residuals
plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True, bins=30)
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Distribution of Residuals')
plt.show()

# prompt: Try the same with polynomial regression with complete code like above

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import ipywidgets as widgets
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the visual style
sns.set(style="whitegrid")

# Load the California housing dataset
data = fetch_california_housing()

# Convert to a DataFrame for easier manipulation and exploration
df = pd.DataFrame(data.data, columns=data.feature_names)
df['MedHouseValue'] = data.target

# Split the data into features and target
X, y = df.drop('MedHouseValue', axis=1), df['MedHouseValue']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Apply Polynomial Features (degree 2 for demonstration)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train the Polynomial Regression model
model_poly = LinearRegression()
model_poly.fit(X_train_poly, y_train)

# Predict on the test set
y_pred_poly = model_poly.predict(X_test_poly)

# Calculate and print the Mean Squared Error for Polynomial Regression
mse_poly = mean_squared_error(y_test, y_pred_poly)
print(f"Mean Squared Error (Polynomial Regression): {mse_poly}")

# Function to predict house price with Polynomial Regression
def predict_price_poly(change):
    input_values = {
        'MedInc': med_inc.value,
        'HouseAge': house_age.value,
        'AveRooms': ave_rooms.value,
        'AveBedrms': ave_bedrooms.value,
        'Population': population.value,
        'AveOccup': ave_occupancy.value,
        'Latitude': latitude.value,
        'Longitude': longitude.value
    }

    # Convert the input to a DataFrame to ensure it has feature names
    input_df = pd.DataFrame([input_values])

    # Standardize the input values
    input_values_scaled = scaler.transform(input_df)

    # Apply Polynomial Features to the input
    input_values_poly = poly.transform(input_values_scaled)

    # Predict the house price using the Polynomial Regression model
    prediction = model_poly.predict(input_values_poly)[0]

    # Display the prediction
    print(f"Predicted House Price (Polynomial Regression): ${prediction*100000:.2f}")

# Button to trigger the prediction for Polynomial Regression
predict_button_poly = widgets.Button(description="Predict (Polynomial)")
predict_button_poly.on_click(predict_price_poly)

# Display the form
display(med_inc, house_age, ave_rooms, ave_bedrooms, population, ave_occupancy, latitude, longitude, predict_button_poly)

# Plot Actual vs Predicted Prices (Polynomial Regression)
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_poly, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices (Polynomial)')
plt.title('Actual vs Predicted Housing Prices (Polynomial Regression)')
plt.show()

# Calculate residuals for Polynomial Regression
residuals_poly = y_test - y_pred_poly

# Plot Residuals for Polynomial Regression
plt.figure(figsize=(10, 6))
sns.histplot(residuals_poly, kde=True, bins=30)
plt.xlabel('Residuals (Polynomial)')
plt.ylabel('Frequency')
plt.title('Distribution of Residuals (Polynomial Regression)')
plt.show()

# Train Linear Regression model
model_linear = LinearRegression()
model_linear.fit(X_train, y_train)

# Predict and evaluate
y_pred_linear = model_linear.predict(X_test)

# Compute metrics
mse_linear = mean_squared_error(y_test, y_pred_linear)
mae_linear = mean_absolute_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

print(f"Mean Squared Error (Linear Regression): {mse_linear}")
print(f"Mean Absolute Error (Linear Regression): {mae_linear}")
print(f"R² Score (Linear Regression): {r2_linear}")

# Apply Polynomial Features (degree 2 for demonstration)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train Polynomial Regression model
model_poly = LinearRegression()
model_poly.fit(X_train_poly, y_train)

# Predict and evaluate
y_pred_poly = model_poly.predict(X_test_poly)

# Compute metrics
mse_poly = mean_squared_error(y_test, y_pred_poly)
mae_poly = mean_absolute_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print(f"Mean Squared Error (Polynomial Regression): {mse_poly}")
print(f"Mean Absolute Error (Polynomial Regression): {mae_poly}")
print(f"R² Score (Polynomial Regression): {r2_poly}")

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Assuming y_test, y_pred_linear, y_pred_poly are defined
# For Linear Regression
mse_linear = mean_squared_error(y_test, y_pred_linear)
mae_linear = mean_absolute_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

# For Polynomial Regression
mse_poly = mean_squared_error(y_test, y_pred_poly)
mae_poly = mean_absolute_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

# Print metrics for comparison
print("Comparison of Regression Models:")
print(f"Linear Regression:")
print(f"  Mean Squared Error: {mse_linear}")
print(f"  Mean Absolute Error: {mae_linear}")
print(f"  R² Score: {r2_linear}\n")

print(f"Polynomial Regression:")
print(f"  Mean Squared Error: {mse_poly}")
print(f"  Mean Absolute Error: {mae_poly}")
print(f"  R² Score: {r2_poly}\n")

# Determine which model is better
print("Model Comparison:")
if mse_poly < mse_linear:
    print("Polynomial Regression has a lower Mean Squared Error.")
else:
    print("Linear Regression has a lower Mean Squared Error.")

if mae_poly < mae_linear:
    print("Polynomial Regression has a lower Mean Absolute Error.")
else:
    print("Linear Regression has a lower Mean Absolute Error.")

if r2_poly > r2_linear:
    print("Polynomial Regression has a higher R² Score.")
else:
    print("Linear Regression has a higher R² Score.")