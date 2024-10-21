def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    pass  # Implement the logic here








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

