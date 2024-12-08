# Step 1: Import necessary libraries
import pandas as pd
import numpy as np

# Step 2: Load the dataset
file_path = 'path_to_your_dataset.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Step 3: View the dataset
# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Display the summary of the dataset
print("\nSummary of the dataset:")
print(df.info())

# Display basic statistics of the dataset
print("\nBasic statistics of the dataset:")
print(df.describe())
