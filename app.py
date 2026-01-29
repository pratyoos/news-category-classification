import joblib
import streamlit as st

model = joblib.load("./models/news_classifier_model.joblib")

st.title("News Category Predictor")
user_input = st.text_area("Enter news text here:", max_chars=5000)

sample= [[user_input]]

if st.button("Predict Category"):
    prediction = model.predict([item[0] for item in sample])
    st.write(f"The predicted category is: **{prediction[0]}**")