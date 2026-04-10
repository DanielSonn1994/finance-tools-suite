import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("multi_metric_sales.csv")
df.columns = df.columns.str.strip()

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Metrics
df["Revenue"] = df["Units Sold"] * df["Unit Price"]
df["Revenue MA"] = df["Revenue"].rolling(window=3).mean()
df["Cumulative Revenue"] = df["Revenue"].cumsum()

# Create dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 8))

# 1. Revenue
axes[0, 0].plot(df["Date"], df["Revenue"], marker="o")
axes[0, 0].set_title("Revenue Trend")
axes[0, 0].set_ylabel("Revenue")
axes[0, 0].grid(True)

# 2. Units Sold
axes[0, 1].bar(df["Date"], df["Units Sold"])
axes[0, 1].set_title("Units Sold")
axes[0, 1].set_ylabel("Units")
axes[0, 1].grid(True)

# 3. Cumulative Revenue (NEW)
axes[1, 0].plot(df["Date"], df["Cumulative Revenue"], marker="o")
axes[1, 0].set_title("Cumulative Revenue")
axes[1, 0].set_ylabel("Total Revenue")
axes[1, 0].grid(True)

# 4. Revenue + Moving Average
axes[1, 1].plot(df["Date"], df["Revenue"], marker="o", label="Revenue")
axes[1, 1].plot(df["Date"], df["Revenue MA"], marker="o", label="3-Day Avg")
axes[1, 1].set_title("Revenue Trend (Smoothed)")
axes[1, 1].legend()
axes[1, 1].grid(True)

# Rotate dates
for ax in axes.flat:
    ax.tick_params(axis="x", rotation=45)

# Title
fig.suptitle("Sales Dashboard (Multi-Metric)", fontsize=16)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()