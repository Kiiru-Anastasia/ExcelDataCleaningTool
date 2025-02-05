from readFile import *
from cleaningFunctions import *

# Cleaning Pipeline

def cleaning_pipeline(file_path):

    df = read_excel(file_path)

    if df is not None:
        df = normalize_text(df)
        df = remove_duplicates(df)
        df = handle_missing_values(df, method="drop", fill_value=0)
        df = handle_outliers(df)

        return df
    else:
        print("Failed to clean data due to loading error.")
        
        return None