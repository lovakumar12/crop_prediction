
from sklearn.preprocessing import LabelEncoder, StandardScaler

from src.init import data

# Encode categorical variables


label_encoders = {}
for column in ['Crop_Type', 'Irrigation_Type', 'Soil_Type', 'Season']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Scale numerical features
scaler = StandardScaler()
numerical_features = ['Farm_Area(acres)', 'Fertilizer_Used(tons)', 'Pesticide_Used(kg)', 'Water_Usage(cubic meters)']
data[numerical_features] = scaler.fit_transform(data[numerical_features])