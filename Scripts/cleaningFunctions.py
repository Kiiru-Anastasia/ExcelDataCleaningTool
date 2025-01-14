# Removing duplicates
def remove_duplicates(df):

    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print(f"Removed {before - after} duplicate rows.")

    return df

#Handling missing values
def handle_missing_values(df, method="drop", fill_value=None):

    if method == "drop":
        df = df.dropna() #droping rows with missing values
    elif method == "fill":
        df = df.fillna(fill_value) #fill missing values with specified value

    print(f"Handled missing values using method: {method}")

    return df

#Normalizing column names
def normalize_column_names(df):

    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    print(f"Normalized column names.")

    return df