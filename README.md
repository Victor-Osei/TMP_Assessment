# Term Deposit Subscription Prediction  

## Overview  

This project focuses on building a predictive model to determine the likelihood of clients subscribing to a term deposit. The analysis follows the CRISP-DM (Cross Industry Standard Process for Data Mining) methodology to systematically approach the problem and achieve the desired business objectives.  

---

## CRISP-DM Process  

## 1. Business Understanding  

The objective of this project is to assist the marketing team in identifying clients likely to subscribe to a term deposit, allowing for targeted marketing campaigns that maximize efficiency and return on investment.  


## 2. Data Understanding  

The dataset contains demographic, socio-economic, and historical interaction details of clients with the bank. Key features include:  
- **Client attributes:** age, job, marital status, education, etc.  
- **Campaign attributes:** number of contacts, previous outcomes, and communication types.  
- **Economic context:** indicators like employment variation rate, consumer price index, and interest rate.  

### Attribute information:

   #### Input variables:
   #### Bank client data:
   
   *  age (numeric)
   *  job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student",
                                       "blue-collar","self-employed","retired","technician","services") 
   *  marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)
   *  education (categorical: "unknown","secondary","primary","tertiary")
   *  default: has credit in default? (binary: "yes","no")
   *  balance: average yearly balance, in euros (numeric) 
   *  housing: has housing loan? (binary: "yes","no")
   *  loan: has personal loan? (binary: "yes","no")

   #### Related with the last contact of the current campaign:
   *  contact: contact communication type (categorical: "unknown","telephone","cellular") 
   *  day: last contact day of the month (numeric)
   *  month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")
   *  duration: last contact duration, in seconds (numeric)

   #### Other attributes:
  *  campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
  *  pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)
  *  previous: number of contacts performed before this campaign and for this client (numeric)
  *  poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

  #### Output variable (desired target):
  * y - has the client subscribed a term deposit? (binary: "yes","no")


### Key Observations from Exploratory Data Analysis (EDA):  
1. **Subscription Trends:** Most clients did not subscribe ("no").  
2. **Impactful Features:**  
   - **Campaign-related features** (e.g., number of contacts, previous campaign outcome) significantly influence subscription likelihood.  
   - Economic indicators also correlate with subscription tendencies.  
3. **Client Characteristics:** Clients who subscribed were often contacted fewer times, had positive outcomes in previous campaigns, and belonged to specific professional categories (e.g., "admin," "management").  

---

### 3. Data Preparation  

**Data Cleaning and Preprocessing:**  
- No missing values and Duplicates and ensured data completeness.  
- Encoded categorical variables (e.g., job, marital status, and education) using one-hot encoding.  
- Scaled numerical features to standardize the data.  
- Split data into training and testing sets for model evaluation.  

---

### 4. Modeling  

Built predictive model using Random Forest(RF).
Evaluated using metrics like accuracy, precision, recall, and F1-score.


The RF model was developed to predict the target variable (`y`) indicating whether a client will subscribe to a term deposit.  

**Model Performance Metrics:**  
- **Accuracy:** 1.00 (100%)  
- **Classification Report:**  
  - **Precision:** 1.00 for both classes (subscribed and not subscribed).  
  - **Recall:** 1.00 for both classes.  
  - **F1-Score:** 1.00 for both classes.  
- **Confusion Matrix:**  
  ```
  [[7985    0]
   [   0 1058]]
  ```  

True Negatives (TN): 7985 — The model correctly predicted 7985 clients would not subscribe.
True Positives (TP): 1058 — The model correctly predicted 1058 clients would subscribe.
There are no false positives or false negatives, confirming perfect performance on both classes.

The model demonstrated excellent performance, with no misclassifications on the test data.  

---

### 5. Evaluation  

**Findings and Insights:**  

  - **Feature Importance:**
    - The Random Forest model provides an implicit feature importance ranking, allowing the marketing team to identify which features (e.g., age, job, marital status) most influence the likelihood of a client subscribing to the service.

     - Client Segments Likely to Subscribe: The perfect performance of the model indicates that it has learned the key characteristics that distinguish clients likely to subscribe. Clients who meet certain demographic or behavioral patterns are more likely to be correctly predicted as subscribers.

- **Key Influential Features:**  

    - Key Predictors: Call duration, contact type, and prior campaign outcomes.
    - Successful Client Profiles: Middle-aged individuals with moderate balances and successful prior contacts.

  - Fewer contacts and positive outcomes from previous campaigns strongly correlate with subscription.  
  - Clients in specific jobs, such as administrative roles and management, are more likely to subscribe.  
  - Economic indicators like employment variation rate and consumer price index also play a significant role.  

- **Actionable Recommendations:** 

  - Based on the model's findings, the marketing team can:

     - Target specific client segments:  Use the feature importance insights to focus marketing efforts on demographics or behaviors that are strongly associated with subscription likelihood. With this the team can focus marketing campaigns on clients with a positive history of prior interactions.  
    - Refine marketing strategies: Develop tailored campaigns for clients with characteristics that predict a higher likelihood of subscribing, potentially leading to improved conversion rates. This helps to reduce excessive contacts, as fewer attempts yield better subscription rates.  
    - Design targeted campaigns for specific professional groups likely to subscribe. 
 

---

### 6. Deployment  

The model has been successfully deployed using Streamlit, providing an interactive and user-friendly decision-support tool for the marketing team. This tool allows the team to upload client data, make predictions on subscription likelihood, and visualize key insights directly. By leveraging this app, the marketing team can optimize resource allocation and tailor campaigns effectively.

You can access the deployed application at: https://victor-osei-tmp-assessment-app-q1vels.streamlit.app/ 

**Prediction Output:**  
Predictions have been converted to readable labels ("yes" or "no") for ease of understanding and implementation.  

---

## Conclusion  

The project successfully identified key drivers of term deposit subscriptions and provided actionable insights to improve marketing strategies. The highly accurate predictive model can help the business achieve its objectives efficiently.  

---
