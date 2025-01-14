import os

from cleaningPipeline import *
from writeFile import *

# Batch processing multiple files
def batch_process(folder_path, output_folder):

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            cleaned_df = cleaning_pipeline(file_path)

            if cleaned_df is not None:
                output_path = os.path.join(output_folder, f"cleaned_{file_name}")
                export_to_excel(cleaned_df, output_path)