import pandas as pd

def read_excel(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        print(f"File: {file_path} loaded successfully!")
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return None