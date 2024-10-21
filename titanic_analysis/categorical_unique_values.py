





# titanic_analysis/categorical_unique_values.py
import pandas as pd

def display_unique_values(df: pd.DataFrame, categorical_features: list) -> dict:
    """
    This function takes a DataFrame and a list of categorical features,
    and returns a dictionary where the keys are the feature names and
    the values are the unique values for those features.
    """
    unique_values = {}
    for feature in categorical_features:
        unique_values[feature] = df[feature].unique().tolist()
    
    return unique_values

