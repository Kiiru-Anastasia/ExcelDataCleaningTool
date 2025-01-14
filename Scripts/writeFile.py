# Exporting cleaned dataset
def export_to_excel(df, output_path):

    try:
        df.to_excel(output_path, index=False)

        print(f"Cleaned dataset saved to: {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")