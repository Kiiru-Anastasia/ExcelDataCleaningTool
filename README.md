# ExcelDataCleaningTool
A program that takes in any excel data as input and outputs a cleaned dataset.

### Progress Update
The prototype for the backend scripts has been finalized.

The tool allows batch cleaning of excel files (.xlsx) in a local folder.

To test the functionality thus far:
1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) the project to your local repository.
2. [Create](https://python.land/virtual-environments/virtualenv) a virtual environment and activate it.
3. Install project dependencies to your virtual environment using: ```pip install -r requirements.txt```
4. Navigate to Scripts folder, 'main.py' file and provide:
* 'folder_path' - The file path to the local folder with the uncleaned excel files.
* 'output_path' - The file path to a folder where the cleaned excel files will be saved 
5. Run the 'main.py' file: ```python main.py```

*NOTE: All cleaned files are prefixed with the name 'cleaned_'*

### Cleaning Functionalities Included
**Normalization of Text Columns** 

Changing data in all text columns to Title case.

**Duplicates Removal**

Removal of exact duplicates.

**Handling missing values**

Missing values are handled in one of three main methods:
* 'drop' - removes missing values from the dataset.
* 'fill' - replaces missing values with a provided 'fill_value'.
* 'impute' - replaces missing values for numerical columns with either the 'median' or 'mean' provided as the 'impute_method'

**Handling Outliers**

Outliers in numerical columns are resolved using the inter quartile range (IQR) method.


### Next Steps
Adding a prototype frontend for a user-friendly interface.