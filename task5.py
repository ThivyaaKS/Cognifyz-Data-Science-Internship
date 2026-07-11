import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Dataset .csv")

# Most common price range
print("===== MOST COMMON PRICE RANGE =====")
print(df["Price range"].value_counts())

# Average rating for each price range
avg_rating = df.groupby("Price range")["Aggregate rating"].mean()

print("\n===== AVERAGE RATING =====")
print(avg_rating)

# Rating Color for each Price Range
rating_color = df.groupby("Price range")["Rating color"].agg(lambda x: x.mode()[0])

print("\n===== RATING COLOR =====")
print(rating_color)

# Bar Chart
plt.figure(figsize=(8,5))
avg_rating.plot(kind="bar")

plt.title("Average Rating by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Average Rating")

plt.tight_layout()
plt.show()