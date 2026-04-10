from cProfile import label

import pandas as pd
import matplotlib.pyplot as plt

region_sales = { "region": ["North", "South", "West", "East", "North", "South", "West", "East"],
                 "sales": [120, 150, 150, 200, 500, 100, 300, 250],
                 "date": [ "01-01-26",
                           "01-02-26",
                           "01-03-26",
                           "01-04-26",
                           "01-05-26",
                           "01-06-26",
                           "01-07-26",
                           "01-08-26",
                 ],


}

df = pd.DataFrame(region_sales)
df["date"] = pd.to_datetime(df["date"])
print(df.head())





grouped_region_sales = df.groupby("region")["sales"].aggregate(["sum", "mean", "min", "max"])
grouped_region_sales.columns = ["total_sales", "avg_sales", "min_sales", "max_sales"]



print(grouped_region_sales.head())


sorted_table = grouped_region_sales.sort_values("total_sales", ascending=False)

best_region_sales = sorted_table.iloc[0]
worst_region_sales = sorted_table.iloc[-1]
best_region_name = best_region_sales.name
worst_region_name = worst_region_sales.name
print("Best region:", best_region_name)
print("Worst region:", worst_region_name)
print(f"Best region: {best_region_name} with total sales of {best_region_sales['total_sales']}")
print(f"Worst region name: {worst_region_name} with total sales of {worst_region_sales['total_sales']}")


for region in df["region"].unique():
    region_df = df[df["region"] == region]
    plt.plot(region_df["date"], region_df["sales"], label=region, marker="o")

plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales by Region")
plt.grid()
plt.legend()

plt.show()