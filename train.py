from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

import pandas as pd
import joblib

print("loading datasets")

# Load California housing dataset
data = fetch_california_housing()

# Create input features
x = pd.DataFrame(data.data, columns=data.feature_names)

# Target = house price
y = data.target

print(f"total records: {x.shape[0]}")

# Split data into training and testing
xtrain, xtest, ytrain, ytest = train_test_split(
    x, y,
    test_size=0.2,
    random_state=42
)

# Create regression model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(xtrain, ytrain)

# Make predictions
ypredict = model.predict(xtest)

# Calculate errors
mae = mean_absolute_error(ytest, ypredict)
r2 = r2_score(ytest, ypredict)

print(f"average error: ${mae * 10000:,.0f}")
print(f"R2 score: {r2:.2f}")

# Save model
joblib.dump(model, "house_model.joblib")

# Save feature names
joblib.dump(list(x.columns), "house_features.joblib")

print("Model saved successfully!")
print(x)