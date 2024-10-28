# titanic_analysis/numerical_df.py
import pandas as pd
def get_numerical_df(df: pd.DataFrame, numerical_features: list) -> pd.DataFrame:
    """Returns a DataFrame containing only numerical features."""
    return df[numerical_features].copy()
