import pandas as pd

# Load Dataset
df = pd.read_csv("Dataset .csv")

# ---------------------------------
# Table Booking Percentage
# ---------------------------------

table_booking = (df["Has Table booking"] == "Yes").mean() * 100

print("===== TABLE BOOKING =====")
print(f"Restaurants with Table Booking: {table_booking:.2f}%")

# ---------------------------------
# Online Delivery Percentage
# ---------------------------------

online_delivery = (df["Has Online delivery"] == "Yes").mean() * 100

print("\n===== ONLINE DELIVERY =====")
print(f"Restaurants with Online Delivery: {online_delivery:.2f}%")

# ---------------------------------
# Average Rating
# ---------------------------------

print("\n===== AVERAGE RATING =====")
print(df.groupby("Has Table booking")["Aggregate rating"].mean())

# ---------------------------------
# Price Range vs Online Delivery
# ---------------------------------

print("\n===== PRICE RANGE VS ONLINE DELIVERY =====")
print(pd.crosstab(df["Price range"], df["Has Online delivery"]))