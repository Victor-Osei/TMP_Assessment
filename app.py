import streamlit as st
import pandas as pd
import numpy as np
import joblib
from utils import preprocess_data, predict_from_file
import seaborn as sns
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load('best_rf_model.pkl')

# Define the app layout
def main():
    st.title('Customer Subscription Prediction')

    menu = ["Upload File", "Make Prediction", "Dashboard"]
    choice = st.sidebar.selectbox("Select Page", menu)

    if choice == "Upload File":
        upload_file_page()
 
    elif choice == "Make Prediction":
        prediction_page()

    elif choice == "Dashboard":
        dashboard_page() 

# File Upload Page
def upload_file_page():
    st.header('Upload Customer Data CSV File')
    uploaded_file = st.file_uploader("Choose a file", type="csv")
    
    if uploaded_file is not None:
        # Save the uploaded file to session_state
        df = pd.read_csv(uploaded_file)
        st.write("Preview of the uploaded file:")
        st.write(df.head())
        
        # Store the dataframe in session_state to persist it across pages
        st.session_state.df = df

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

def dashboard_page():
    st.subheader('Dashboard')

    # Check if the file is uploaded and available in session state
    if 'df' in st.session_state:
        df = st.session_state.df  # Retrieve the dataframe from session state
        st.write('Data for Dashboard:', df.head())
        
        create_dashboard(df)
    else:
        st.write("Please upload a CSV file first to view the dashboard.")

# Dashboard function
def create_dashboard(df):
    st.title('Customer Subscription Analysis Dashboard')

    # Ensure 'y' column exists for subscription status
    if 'y' not in df.columns:
        st.error("DataFrame must contain a 'y' column for subscription status")
        return

    # # Subscription Rate by Job
    # st.header('1. Subscription Rate by Job')
    # job_subscription = df.groupby('job')['y'].apply(lambda x: (x == 'yes').mean() * 100).sort_values(ascending=False)
    # st.bar_chart(job_subscription)

    # 1. Subscription Rate by Job
    st.header('1. Subscription Rate by Job')
    job_subscription = df.groupby('job')['y'].apply(lambda x: (x == 'yes').mean() * 100).sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    job_subscription.plot(kind='bar')
    plt.title('Subscription Rate by Job Category')
    plt.xlabel('Job Category')
    plt.ylabel('Subscription Rate (%)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()  # Clear the figure to avoid overlapping in multiple plots
    
    # 2. Age Distribution
    st.header('2. Age Distribution by Subscription Status')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='y', y='age', data=df)
    plt.title('Age Distribution by Subscription Status')
    plt.xlabel('Subscription Status')
    plt.ylabel('Age')
    st.pyplot(plt)
    plt.clf()
    
    # 3. Balance vs. Subscription
    st.header('3. Balance vs. Subscription')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='y', y='balance', data=df)
    plt.title('Account Balance by Subscription Status')
    plt.xlabel('Subscription Status')
    plt.ylabel('Account Balance')
    st.pyplot(plt)
    plt.clf()
    
    # 4. Duration and Subscription Relationship
    st.header('4. Contact Duration and Subscription')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='y', y='duration', data=df)
    plt.title('Contact Duration by Subscription Status')
    plt.xlabel('Subscription Status')
    plt.ylabel('Contact Duration (seconds)')
    st.pyplot(plt)
    plt.clf()
    
    # Additional Insights
    st.header('Additional Insights')
    
    # Overall Subscription Rate
    total_subscription_rate = (df['y'] == 'yes').mean() * 100
    st.metric('Overall Subscription Rate', f'{total_subscription_rate:.2f}%')
    
    # Subscription by Categorical Features
    categorical_features = ['job', 'marital', 'education', 'contact']
    
    for feature in categorical_features:
        st.subheader(f'Subscription Rate by {feature.capitalize()}')
        feature_subscription = df.groupby(feature)['y'].apply(lambda x: (x == 'yes').mean() * 100).sort_values(ascending=False)
        
        plt.figure(figsize=(10, 6))
        feature_subscription.plot(kind='bar')
        plt.title(f'Subscription Rate by {feature.capitalize()}')
        plt.xlabel(feature.capitalize())
        plt.ylabel('Subscription Rate (%)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(plt)
        plt.clf()

def dashboard_page():
    st.title('Customer Subscription Dashboard')
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)
        
        # Check if required columns exist
        required_columns = ['y', 'job', 'age', 'balance', 'duration']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            st.error(f"Missing required columns: {', '.join(missing_columns)}")
        else:
            st.write("File uploaded successfully!")  # Debugging step to show that the file is uploaded
            create_dashboard(df)
    else:
        st.write("Please upload a CSV file to proceed.")  # Debugging step to show the upload prompt



# Run the app
if __name__ == "__main__":
    main()

