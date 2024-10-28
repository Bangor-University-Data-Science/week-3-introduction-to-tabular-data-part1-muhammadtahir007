# titanic_analysis/feature_type_dict.py
import pandas as pd
def create_feature_type_dict(df: pd.DataFrame) -> dict:
    """Classifies features into numerical and categorical."""
    feature_types = {'numerical': [], 'categorical': []}
    
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            feature_types['numerical'].append(column)
        else:
            feature_types['categorical'].append(column)
    
    return feature_types
