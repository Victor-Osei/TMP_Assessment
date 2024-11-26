# # import streamlit as st
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt

# # def create_dashboard(df):
# #     """
# #     Create a comprehensive dashboard for subscription analysis
    
# #     Parameters:
# #     df (pandas.DataFrame): Input dataframe with customer data
# #     """
# #     st.title('Customer Subscription Analysis Dashboard')
    
# #     # Ensure 'y' column exists for subscription status
# #     if 'y' not in df.columns:
# #         st.error("DataFrame must contain a 'y' column for subscription status")
# #         return
    
# #     # 1. Subscription Rate by Job
# #     st.header('1. Subscription Rate by Job')
# #     job_subscription = df.groupby('job')['y'].apply(lambda x: (x == 'yes').mean() * 100).sort_values(ascending=False)
    
# #     plt.figure(figsize=(10, 6))
# #     job_subscription.plot(kind='bar')
# #     plt.title('Subscription Rate by Job Category')
# #     plt.xlabel('Job Category')
# #     plt.ylabel('Subscription Rate (%)')
# #     plt.xticks(rotation=45, ha='right')
# #     plt.tight_layout()
# #     st.pyplot(plt)
# #     plt.close()
    
# #     # 2. Age Distribution
# #     st.header('2. Age Distribution by Subscription Status')
# #     plt.figure(figsize=(10, 6))
# #     sns.boxplot(x='y', y='age', data=df)
# #     plt.title('Age Distribution by Subscription Status')
# #     plt.xlabel('Subscription Status')
# #     plt.ylabel('Age')
# #     st.pyplot(plt)
# #     plt.close()
    
# #     # 3. Balance vs. Subscription
# #     st.header('3. Balance vs. Subscription')
# #     plt.figure(figsize=(10, 6))
# #     sns.boxplot(x='y', y='balance', data=df)
# #     plt.title('Account Balance by Subscription Status')
# #     plt.xlabel('Subscription Status')
# #     plt.ylabel('Account Balance')
# #     st.pyplot(plt)
# #     plt.close()
    
# #     # 4. Duration and Subscription Relationship
# #     st.header('4. Contact Duration and Subscription')
# #     plt.figure(figsize=(10, 6))
# #     sns.boxplot(x='y', y='duration', data=df)
# #     plt.title('Contact Duration by Subscription Status')
# #     plt.xlabel('Subscription Status')
# #     plt.ylabel('Contact Duration (seconds)')
# #     st.pyplot(plt)
# #     plt.close()
    
# #     # Additional Insights
# #     st.header('Additional Insights')
    
# #     # Overall Subscription Rate
# #     total_subscription_rate = (df['y'] == 'yes').mean() * 100
# #     st.metric('Overall Subscription Rate', f'{total_subscription_rate:.2f}%')
    
# #     # Subscription by Categorical Features
# #     categorical_features = ['job', 'marital', 'education', 'contact']
    
# #     for feature in categorical_features:
# #         st.subheader(f'Subscription Rate by {feature.capitalize()}')
# #         feature_subscription = df.groupby(feature)['y'].apply(lambda x: (x == 'yes').mean() * 100).sort_values(ascending=False)
        
# #         plt.figure(figsize=(10, 6))
# #         feature_subscription.plot(kind='bar')
# #         plt.title(f'Subscription Rate by {feature.capitalize()}')
# #         plt.xlabel(feature.capitalize())
# #         plt.ylabel('Subscription Rate (%)')
# #         plt.xticks(rotation=45, ha='right')
# #         plt.tight_layout()
# #         st.pyplot(plt)
# #         plt.close()

# # def dashboard_page():
# #     st.title('Customer Subscription Dashboard')
    
# #     uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
# #     if uploaded_file is not None:
# #         # Read the uploaded CSV file
# #         df = pd.read_csv(uploaded_file)
        
# #         # Check if required columns exist
# #         required_columns = ['y', 'job', 'age', 'balance', 'duration']
# #         missing_columns = [col for col in required_columns if col not in df.columns]
        
# #         if missing_columns:
# #             st.error(f"Missing required columns: {', '.join(missing_columns)}")
# #         else:
# #             create_dashboard(df)



import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_dashboard(df):
    """
    Create a comprehensive dashboard for subscription analysis
    
    Parameters:
    df (pandas.DataFrame): Input dataframe with customer data
    """
    st.title('Term Deposit Subscription Analysis Dashboard')
    
    # Ensure 'y' column exists for subscription status
    if 'y' not in df.columns:
        st.error("DataFrame must contain a 'y' column for subscription status")
        return
    
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

