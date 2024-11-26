# TMP_Assessment
Data Analytics Pathway Assessment

Project: Client Subscription Prediction Model
1. Introduction
This report summarizes the analysis and model developed to predict client subscription using various client features. The model aims to assist the marketing team in identifying key customer segments likely to subscribe to the service.

2. Objective
The goal was to predict client subscription likelihood for a term deposit based on operational data, enabling the marketing team to optimize campaigns effectively.

3. Data Overview
The dataset consists of client information, including demographic details, previous contact history, and other features such as age, job, marital status, education, and more. The target variable is whether the client subscribed to a service.


4. Methods

* Data Cleaning & Preprocessing:

No missing values or duplicates.
Encoded categorical variables and standardized numerical features.

* Exploratory Data Analysis:

Analyzed age, balance, and campaign features for patterns.
Identified correlations between subscription rates and various socio-economic factors.

* Model Development:

Built predictive models using Random Forest.
Evaluated using metrics like accuracy, precision, recall, and F1-score.

* Insights

Key Predictors: Call duration, contact type, and prior campaign outcomes.

Successful Client Profiles: Middle-aged individuals with moderate balances and successful prior contacts.

* Performance Metrics

Accuracy: X% (replace with value from the notebook).
Precision: Y% (replace with value from the notebook).
Recall: Z% (replace with value from the notebook).

* Recommendations

Optimize outreach strategies by focusing on impactful client demographics and effective communication channels.
Reduce redundant contacts for better campaign perception and success.





3. Methodology
We used a Random Forest (RF) model for classification to predict whether a client will subscribe. Random Forest is an ensemble method known for its effectiveness in handling both categorical and continuous variables, as well as its ability to reduce overfitting.

4. Model Performance
Accuracy: The model achieved an accuracy of 100%, meaning it correctly predicted the subscription status of every client in the dataset. This high level of accuracy suggests the model performs very well in distinguishing between the two classes (subscribed vs. not subscribed).

Classification Report:

Precision (for class 1, subscribed): 1.00 — Every time the model predicted a client would subscribe, it was correct.
Recall (for class 1, subscribed): 1.00 — The model correctly identified all clients who subscribed, with no false negatives.
F1-Score: 1.00 — The model achieved a perfect balance between precision and recall for both classes, indicating it accurately predicted both subscribed and non-subscribed clients.

Confusion Matrix:

True Negatives (TN): 7985 — The model correctly predicted 7985 clients would not subscribe.
True Positives (TP): 1058 — The model correctly predicted 1058 clients would subscribe.
There are no false positives or false negatives, confirming perfect performance on both classes.

               Predicted No (0)	    Predicted Yes (1)
Actual No (0)	   7985	                   0
Actual Yes (1)	     0	                  1058

5. Insights and Findings
Feature Importance: The Random Forest model provides an implicit feature importance ranking, allowing the marketing team to identify which features (e.g., age, job, marital status) most influence the likelihood of a client subscribing to the service.

Client Segments Likely to Subscribe: The perfect performance of the model indicates that it has learned the key characteristics that distinguish clients likely to subscribe. Clients who meet certain demographic or behavioral patterns are more likely to be correctly predicted as subscribers.

6. Recommendations
Based on the model's findings, the marketing team can:

* Target specific client segments: Use the feature importance insights to focus marketing efforts on demographics or behaviors that are strongly associated with subscription likelihood.
* Refine marketing strategies: Develop tailored campaigns for clients with characteristics that predict a higher likelihood of subscribing, potentially leading to improved conversion rates.
* Monitor model performance: Given the current perfect performance, it's important to ensure the model continues to generalize well by testing on new data or monitoring it over time.

7. Conclusion
The Random Forest model demonstrates excellent predictive accuracy for identifying clients who are likely to subscribe to the service. With an accuracy of 100%, along with perfect precision, recall, and F1-score, the model offers a high-confidence tool for marketing decision-making. The key features driving predictions can help refine targeting strategies and improve overall campaign effectiveness.



# Term Deposit Subscription Prediction  

## Overview  

This project focuses on building a predictive model to determine the likelihood of clients subscribing to a term deposit. The analysis follows the CRISP-DM (Cross Industry Standard Process for Data Mining) methodology to systematically approach the problem and achieve the desired business objectives.  

---

## CRISP-DM Process  

### 1. Business Understanding  

The objective of this project is to assist the marketing team in identifying clients likely to subscribe to a term deposit, allowing for targeted marketing campaigns that maximize efficiency and return on investment.  

**Key Questions Addressed:**  
- What are the key features influencing a client's decision to subscribe?  
- What actionable recommendations can be provided to improve marketing strategies?  
- Can a predictive model be used to estimate the likelihood of subscription accurately?  

---

### 2. Data Understanding  

The dataset contains demographic, socio-economic, and historical interaction details of clients with the bank. Key features include:  
- **Client attributes:** age, job, marital status, education, etc.  
- **Campaign attributes:** number of contacts, previous outcomes, and communication types.  
- **Economic context:** indicators like employment variation rate, consumer price index, and interest rate.  

### Key Observations from Exploratory Data Analysis (EDA):  
1. **Subscription Trends:** Most clients did not subscribe ("no").  
2. **Impactful Features:**  
   - **Campaign-related features** (e.g., number of contacts, previous campaign outcome) significantly influence subscription likelihood.  
   - Economic indicators also correlate with subscription tendencies.  
3. **Client Characteristics:** Clients who subscribed were often contacted fewer times, had positive outcomes in previous campaigns, and belonged to specific professional categories (e.g., "admin," "management").  

---

### 3. Data Preparation  

**Steps Taken:**  
- Handled missing values and ensured data completeness.  
- Encoded categorical variables (e.g., job, marital status, and education) using one-hot encoding.  
- Scaled numerical features to standardize the data.  
- Split data into training and testing sets for model evaluation.  

---

### 4. Modeling  

A classification model was developed to predict the target variable (`y`) indicating whether a client will subscribe to a term deposit.  

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

The model demonstrated excellent performance, with no misclassifications on the test data.  

---

### 5. Evaluation  

**Findings and Insights:**  
- **Key Influential Features:**  
  - Fewer contacts and positive outcomes from previous campaigns strongly correlate with subscription.  
  - Clients in specific jobs, such as administrative roles and management, are more likely to subscribe.  
  - Economic indicators like employment variation rate and consumer price index also play a significant role.  
- **Actionable Recommendations:**  
  - Focus marketing campaigns on clients with a positive history of prior interactions.  
  - Reduce excessive contacts, as fewer attempts yield better subscription rates.  
  - Design targeted campaigns for specific professional groups likely to subscribe.  

---

### 6. Deployment  

The model's predictions can be integrated into a decision-support tool for the marketing team. For example, a dashboard can provide insights on potential clients and help optimize resource allocation for campaigns.  

**Example Prediction Output:**  
Predictions have been converted to readable labels ("yes" or "no") for ease of understanding and implementation.  

---

## Conclusion  

The project successfully identified key drivers of term deposit subscriptions and provided actionable insights to improve marketing strategies. The highly accurate predictive model can help the business achieve its objectives efficiently.  

---
