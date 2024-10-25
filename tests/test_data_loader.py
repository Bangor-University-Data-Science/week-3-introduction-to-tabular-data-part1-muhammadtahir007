import pandas as pd
from titanic_analysis.data_loader import load_titanic_data

def test_load_titanic_data():
    # Load data from a sample CSV path
    df = load_titanic_data("../../data/titanic.csv")
    
    # Check if the returned object is a DataFrame
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    
    # Check if the DataFrame is not empty
    assert not df.empty, "The DataFrame should not be empty"
