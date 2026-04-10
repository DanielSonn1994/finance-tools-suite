import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": [
        "2024-01-01",
        "2024-01-02",
        "2024-01-03",
        "2024-01-04",
        "2024-01-05",
        "2024-01-06",
        "2024-01-07",
    ],
    "Sales": [120, 135, 150, 160, 170, 165, 180]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
max_sales = df["Sales"].max()
min_sales = df["Sales"].min()

best_index = df["Sales"].idxmax()
worst_index = df["Sales"].idxmin()

best_day = df.loc[best_index, "Date"]
worst_day = df.loc[worst_index, "Date"]


print(f"Total sales: £{total_sales:.2f}")
print(f"Average sales: £{average_sales:.2f}")
print(f"Max sales: £{max_sales:.2f}")
print(f"Min sales: £{min_sales:.2f}")
print(f"Best day: {best_day}")
print(f"Worst day: {worst_day}")

print(f"Best day: {best_day.date()} (£{max_sales:.2f})")
print(f"Worst day: {worst_day.date()} (£{min_sales:.2f})")


plt.plot(df["Date"], df["Sales"], marker='o')

plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Trend Over Time")

plt.grid()

plt.scatter(best_day, max_sales)
plt.scatter(worst_day, min_sales)

plt.plot(df["Date"], df["Sales"], marker='o')

plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Trend Over Time")

plt.grid()

plt.scatter(best_day, max_sales)
plt.scatter(worst_day, min_sales)

plt.text(best_day, max_sales, f"Max: {max_sales}")
plt.text(worst_day, min_sales, f"Min: {min_sales}")

plt.show()

plt.show()






