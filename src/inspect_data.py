
import pandas as pd
from pathlib import Path

# Locate dataset
file_path = Path("data/raw/marketing_campaigns.csv")

# Load dataset
df = pd.read_csv(file_path)

print("\n========== DATASET OVERVIEW ==========")

print("\nFirst 5 records:")
print(df.head())

print("\nDataset dimensions:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate records:")
print(df.duplicated().sum())

print("\nStatistical summary:")
print(df.describe(include="all").T)

print("\n========== INSPECTION COMPLETE ==========")
