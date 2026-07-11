import pandas as pd
import os

print(os.listdir())

# Load dataset
df = pd.read_csv("Dataset .csv")

# Dataset shape
print("Rows and Columns:", df.shape)

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Aggregate Rating Summary
print("\nAggregate Rating Summary:")
print(df["Aggregate rating"].describe())

# Rating Distribution
print("\nRating Distribution:")
print(df["Aggregate rating"].value_counts())