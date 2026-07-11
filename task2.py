import pandas as pd

# Load Dataset
df = pd.read_csv("Dataset .csv")   # உங்க file பெயருக்கு ஏற்ப

# -------------------------------
# Basic Statistics
# -------------------------------

print("===== BASIC STATISTICS =====")
print(df.describe())

# Mean
print("\nMean:")
print(df.mean(numeric_only=True))

# Median
print("\nMedian:")
print(df.median(numeric_only=True))

# Standard Deviation
print("\nStandard Deviation:")
print(df.std(numeric_only=True))

# -------------------------------
# Top Cities
# -------------------------------

print("\n===== TOP 10 CITIES =====")
print(df["City"].value_counts().head(10))

# -------------------------------
# Top Cuisines
# -------------------------------

print("\n===== TOP 10 CUISINES =====")
print(df["Cuisines"].value_counts().head(10))