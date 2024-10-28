# titanic_analysis/summary_table.py
import pandas as pd
def create_summary_table(df: pd.DataFrame) -> pd.DataFrame:
    """Creates a summary table with feature names, data types, unique value count, and missing values."""
    summary_data = {
        "Feature Name": df.columns,
        "Data Type": df.dtypes,
        "Number of Unique Values": [df[col].nunique() for col in df.columns],
        "Has Missing Values?": [df[col].isnull().any() for col in df.columns]
    }
    return pd.DataFrame(summary_data)
