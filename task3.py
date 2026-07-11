import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Dataset .csv")   # உங்க file பெயருக்கு ஏற்ப

# Top 10 Cities
top_cities = df["City"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_cities.plot(kind="bar")

plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()