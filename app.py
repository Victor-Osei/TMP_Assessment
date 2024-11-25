import streamlit as st
import pandas as pd
import numpy as np
import joblib
from utils import preprocess_data, predict_from_file


# Load the trained model
model = joblib.load('best_rf_model.pkl')  # Model file name

# Define the app layout
def main():
    st.title('Customer Subscription Prediction')

    menu = ["Upload File", "Make Prediction"]
    choice = st.sidebar.selectbox("Select Page", menu)

    if choice == "Upload File":
        upload_file_page()
    elif choice == "Make Prediction":
        prediction_page()

# File Upload Page
def upload_file_page():
    st.header('Upload Customer Data CSV File')
    uploaded_file = st.file_uploader("Choose a file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of the uploaded file:")
        st.write(df.head())
        
        # Save the uploaded file for prediction
        if st.button("Use this data for prediction"):
            prediction_from_uploaded_file(df)

# Prediction from Uploaded File
def prediction_from_uploaded_file(df):
    predictions = predict_from_file(df, model)
    st.write("Predictions for the uploaded data:")
    df['Prediction'] = predictions
    st.write(df)

# Prediction Page (Manual Input)
def prediction_page():
    st.header('Manual Customer Subscription Prediction')
    
    # User input fields (same as in the earlier prediction page)
    age = st.number_input('Age', min_value=18, max_value=100, value=30)
    job = st.selectbox('Job', ['blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'])
    marital = st.selectbox('Marital Status', ['married', 'single'])
    education = st.selectbox('Education', ['secondary', 'tertiary', 'unknown'])
    default = st.selectbox('Has Default', ['yes', 'no'])
    housing = st.selectbox('Has Housing Loan', ['yes', 'no'])
    loan = st.selectbox('Has Personal Loan', ['yes', 'no'])
    contact = st.selectbox('Contact Communication Type', ['telephone', 'unknown'])
    poutcome = st.selectbox('Outcome of Previous Marketing Campaign', ['failure', 'success', 'unknown'])
    balance = st.number_input('Balance', min_value=-5000, max_value=200000, value=1000)
    duration = st.number_input('Duration of Last Contact', min_value=1, max_value=5000, value=100)
    campaign = st.number_input('Number of Contacts During Campaign', min_value=1, max_value=50, value=2)
    pdays = st.number_input('Days since Last Contact', min_value=-1, max_value=1000, value=100)
    previous = st.number_input('Number of Contacts Before Campaign', min_value=0, max_value=50, value=1)
    month = st.selectbox('Month of Last Contact', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
    
    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'age': [age],
        'job': [job],
        'marital': [marital],
        'education': [education],
        'default': [default],
        'housing': [housing],
        'loan': [loan],
        'contact': [contact],
        'poutcome': [poutcome],
        'balance': [balance],
        'duration': [duration],
        'campaign': [campaign],
        'pdays': [pdays],
        'previous': [previous],
        'month': [month]
    })
    
    # Predict the result based on input
    if st.button('Predict Subscription'):
        prediction = predict_from_file(input_data, model)
        st.write(f"Prediction: The customer is predicted to subscribe: {prediction[0]}")

# Run the app
if __name__ == "__main__":
    main()
