from utils import load_model, preprocess_inputs
import streamlit as st
import numpy as np

# Load Ridge model and scaler
model = load_model('ridge.pkl')
scaler = load_model('scaler.pkl')

# App title
st.title("Algerian Forest Fire Risk Predictor")

# Description
st.markdown("""
This app uses a trained Ridge Regression model to predict the **Fire Weather Index (FWI)** or **Burned Area** (depending on your training target).
Please enter the relevant feature values below:
""")

# Feature inputs
feature_names = [
    "Temperature",
    "Relative Humidity",
    "Wind Speed",
    "Rainfall",
    "Fine Fuel Moisture Code",
    "Duff Moisture Code",
    "Drought code"
    "Initial Speed Index",
    "Classes",
    "Region"
]

user_inputs = []

# Collect user inputs
for feature in feature_names:
    if feature in ["Classes", "Region"]:
        # For binary categorical features: 0 or 1
        value = st.radio(f"Select {feature}:", [0, 1])
    else:
        value = st.number_input(f"Enter {feature}:", value=0.0, step=0.1)
    user_inputs.append(value)

# Preprocess inputs
input_array = preprocess_inputs(user_inputs, scaler)

# Predict
if st.button("Predict"):
    prediction = model.predict(input_array)
    st.success(f"Predicted value: {prediction[0]:.2f}")
    st.caption("Note: This prediction reflects the estimated Fire Weather Index or Burned Area based on the input features.")
