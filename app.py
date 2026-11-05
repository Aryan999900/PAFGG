import streamlit as st
import pandas as pd
import joblib
import json

st.title('Employee Attrition Prediction App')
st.write('Predict whether an employee is likely to leave the company.')

# Load model and columns
model = joblib.load('rf_model.pkl')
with open('feature_columns.json', 'r') as f:
    cols = json.load(f)

st.write('Model and features loaded successfully!')
