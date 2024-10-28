# titanic_analysis/categorical_unique_values.py
import pandas as pd
def display_unique_values(df: pd.DataFrame, categorical_features: list) -> dict:
    """Displays unique values for each categorical column."""
    unique_values = {}
    for feature in categorical_features:
        unique_values[feature] = df[feature].unique().tolist()
    return unique_values
