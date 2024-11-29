from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import streamlit as st
import joblib

from src.init import data
from src.encoding import *


# Split data
X = data.drop(['Farm_ID', 'Yield(tons)'], axis=1)
y = data['Yield(tons)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Define models
models = {
    'Linear Regression': LinearRegression(),
    'Random Forest': RandomForestRegressor(),
    'Gradient Boosting': GradientBoostingRegressor()
}

# Evaluate models
best_model = None
best_score = float('inf')
for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print(f"{model_name} - MAE: {mae}, RMSE: {rmse}")
    
    # Select best model based on RMSE
    if rmse < best_score:
        best_score = rmse
        best_model = model

print(f"Selected Model: {best_model}")



# Save the model and preprocessing objects
joblib.dump(best_model, 'yield_prediction_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')
