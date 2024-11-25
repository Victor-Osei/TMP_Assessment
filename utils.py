import pandas as pd
import numpy as np

# Preprocess data for prediction
def preprocess_data(input_data, model):
    # Apply one-hot encoding to multi-category categorical variables
    categorical_features = ['job', 'marital', 'education', 'contact', 'poutcome']
    input_data = pd.get_dummies(input_data, columns=categorical_features, drop_first=True)
    
    # Label encode binary variables
    binary_features = ['default', 'housing', 'loan']
    for feature in binary_features:
        input_data[feature] = input_data[feature].apply(lambda x: 1 if x == 'yes' else 0)
    
    # Apply log transformation to 'balance' if necessary
    input_data['balance_log'] = input_data['balance'].apply(lambda x: np.log(x + 1) if x >= 0 else 0)
    
    # Create 'total_contacts' feature
    input_data['total_contacts'] = input_data['campaign'] + input_data['previous']
    
    # Map months to seasons (based on one-hot encoded months)
    month_to_season = {
        'jan': 'winter', 'feb': 'winter', 'mar': 'spring', 'apr': 'spring',
        'may': 'spring', 'jun': 'summer', 'jul': 'summer', 'aug': 'summer',
        'sep': 'fall', 'oct': 'fall', 'nov': 'fall', 'dec': 'winter'
    }
    month_columns = [col for col in input_data.columns if col.startswith('month_')]
    season_features = []
    for month_col in month_columns:
        month = month_col.split('_')[1]  # Get the month name from the column
        season = month_to_season.get(month, 'winter')  # Map to season
        season_feature = f'season_{season}'
        season_features.append(season_feature)
    
    input_data[season_features] = input_data[month_columns].apply(lambda row: pd.Series({
        f'season_{season}': 1 if month_to_season.get(month, 'winter') == season else 0 
        for season in ['winter', 'spring', 'summer', 'fall']
    }, axis=1))

    # Drop month columns after mapping to seasons
    input_data.drop(columns=month_columns, inplace=True)

    # Add missing columns to match model's feature set
    for col in model.feature_names_in_:
        if col not in input_data.columns:
            input_data[col] = 0  # Fill missing columns with 0
    
    # Reorder the columns to match the model's expected feature order
    input_data = input_data[model.feature_names_in_]

    return input_data

# Predict from uploaded file or input data
def predict_from_file(df, model):
    # Preprocess data
    processed_data = preprocess_data(df, model)
    
    # Predict using the model
    predictions = model.predict(processed_data)
    
    # Convert binary prediction (0/1) to 'yes'/'no'
    return ['yes' if pred == 1 else 'no' for pred in predictions]
