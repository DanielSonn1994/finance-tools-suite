import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data_analysis.csv")

# Create moving average
df["Moving_Average"] = df["Sales"].rolling(window=3).mean()

# Plot both lines
plt.plot(df["Month"], df["Sales"], marker="o", label="Sales")
plt.plot(df["Month"], df["Moving_Average"], marker="o", label="Moving Average")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Trend with Moving Average")
plt.legend()
plt.grid()

df["Moving_Average"] = df["Sales"].rolling(window=3).mean().fillna(0)

max_sales = df["Sales"].max()
max_month = df.loc[df["Sales"].idxmax(), "Month"]

plt.scatter(max_month, max_sales)
plt.text(max_month, max_sales, f"Max: {max_sales}")

plt.show()