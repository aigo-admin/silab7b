import streamlit as st
import pickle
import pandas as pd

st.title("Height to Weight Prediction")

# Load trained model
with open("height_weight_model.pkl", "rb") as file:
    model = pickle.load(file)

# Input height
height = st.number_input(
    "Enter Height (inches)",
    min_value=40.0,
    max_value=90.0,
    value=70.0,
    step=0.1
)

# Predict
if st.button("Predict Weight"):
    input_data = pd.DataFrame({
        "Height(Inches)": [height]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Weight: {prediction[0]:.2f} pounds"
    )
