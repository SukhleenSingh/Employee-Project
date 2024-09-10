# Employee-Project
This is a Python project that allows you to filter and sort employee data based on various criteria like salary, age, name, and more. The data can be easily filtered for numeric values (e.g., salary greater than 10000) or searched and sorted for string values (e.g., employees with the surname "Verma").

Note: If you want to use a CSV file for the dataset, you can load it using the pandas library. Add the following code to your existing code:
import pandas as pd
def load_data(file_path):
    return pd.read_csv(file_path)
