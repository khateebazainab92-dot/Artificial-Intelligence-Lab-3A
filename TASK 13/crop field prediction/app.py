# streamlit run app.py

import streamlit as st
import pandas as pd
import pickle
import os

# =========================
# Load files safely
# =========================
base_path = os.path.dirname(__file__)

model_path = os.path.join(base_path, "crop_yield_model.pkl")
columns_path = os.path.join(base_path, "feature_columns.pkl")

model = pickle.load(open(model_path, "rb"))
expected_columns = pickle.load(open(columns_path, "rb"))

# =========================
# UI
# =========================
st.title("🌾 Crop Yield Prediction")

st.write("Enter input values:")

# Example inputs (YOU MUST MATCH YOUR DATASET)
fertilizer = st.number_input("Fertilizer Used (kg)", value=50.0)
pesticides = st.number_input("Pesticides Used (kg)", value=10.0)
humidity = st.number_input("Humidity (%)", value=60.0)
density = st.number_input("Planting Density", value=100.0)
region = st.text_input("Region", value="Punjab")

# =========================
# Create input dataframe
# =========================
input_data = {
    "Fertilizer_Used_kg": fertilizer,
    "Pesticides_Used_kg": pesticides,
    "Humidity_pct": humidity,
    "Planting_Density": density,
    "Region": region
}

input_df = pd.DataFrame([input_data])

# =========================
# Fix column mismatch
# =========================
input_df = input_df.reindex(columns=expected_columns, fill_value=0)

# =========================
# Prediction
# =========================
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Crop Yield: {prediction[0]}")