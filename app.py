import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")
model = joblib.load("best_model.pkl")
st.title("Student Performance Predictor")
study_hours = st.slider("Study Hours per day", 0.0, 12.0, 2.0)
attendance = st.slider("Attendance Percentage", 0.0, 100.0, 80.0)
mental_health = st.slider("Mental Health Score (1-10)", 1, 10, 7)
sleep_hours = st.slider("Sleep Hours per day", 0.0, 12.0, 6.0)
part_time_job = st.selectbox("Part-time Job", ["Yes", "No"])

ptj_encoded = 1 if part_time_job == "Yes" else 0

if st.button("Predict Exam Score"):
    features = np.array([[study_hours, attendance, mental_health, sleep_hours, ptj_encoded]])
    prediction = model.predict(features)[0]
    prediction = max(0, min(100, prediction))  # Ensure score is between 0 and 100
    st.success(f"Predicted Exam Score: {prediction:.2f}")
