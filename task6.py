import pandas as pd

# Load Dataset
df = pd.read_csv("Dataset .csv")

# ---------------------------------
# Restaurant Name Length
# ---------------------------------

df["Restaurant_Name_Length"] = df["Restaurant Name"].str.len()

# Address Length
df["Address_Length"] = df["Address"].str.len()

# ---------------------------------
# Encode Table Booking
# ---------------------------------

df["Table_Booking"] = df["Has Table booking"].map({
    "Yes": 1,
    "No": 0
})

# ---------------------------------
# Encode Online Delivery
# ---------------------------------

df["Online_Delivery"] = df["Has Online delivery"].map({
    "Yes": 1,
    "No": 0
})

print("===== NEW FEATURES =====")
print(df[[
    "Restaurant_Name_Length",
    "Address_Length",
    "Table_Booking",
    "Online_Delivery"
]].head())

# Save New Dataset
df.to_csv("Feature_Engineered_Dataset.csv", index=False)

print("\nFeature Engineered Dataset Saved Successfully!")