# Removing duplicates
def remove_duplicates(df):

    duplicates = df.duplicated()

    if duplicates.any():
        before = len(df)
        df = df.drop_duplicates()
        after = len(df)
        
        print(f"Removed {before - after} duplicate rows.")

    return df

#Handling missing values
def handle_missing_values(df, method="drop", impute_method="median", fill_value=None):

    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if method == "drop":
        df = df.dropna() #droping rows with missing values
    elif method == "fill":
        df = df.fillna(fill_value) #fill missing values with specified value
    elif method == "impute":
        for col in numeric_columns:
            if impute_method == "median":
                df[col].fillna(df[col].median(), inplace=True)
            elif impute_method == "mean":
                df[col].fillna(df[col].mean(), inplace=True)

    print(f"Handled missing values using method: {method}")

    return df

#Handle outliers using IQR
def handle_outliers(df):

    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    for col in numeric_columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)

    print(f"Outliers handled using Inter-Quartile Range(IQR)")

    return df


#Normalizing text columns
def normalize_text(df):

    #df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    text_columns = df.select_dtypes(include=["object"]).columns.tolist()

    for col in text_columns:
        df[col] = df[col].str.strip().str.lower().str.title()

    print(f"Text columns normalized successfully.")

    return df