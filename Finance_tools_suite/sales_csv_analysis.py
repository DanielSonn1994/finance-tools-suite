import statistics

sales = []

with open("sales_data.csv", "r", encoding="utf-8-sig") as file:
    next(file)  # skip header

    for line in file:
        day, sale = line.strip().replace('"', '').split(",")
        sales.append(int(sale))

print("Welcome to the sales CSV analysis")
print("Sales data:", sales)

total_sales = sum(sales)
print("Total sales:", total_sales)

mean_sales = total_sales / len(sales)
print(f"Average sales: £{mean_sales:.2f}")

minimum_sale = min(sales)
print(f"Minimum sale: £{minimum_sale}")

maximum_sale = max(sales)
print(f"Maximum sale: £{maximum_sale}")

median_sale = statistics.median(sales)
print(f"Median sale: £{median_sale}")

std_dev = statistics.stdev(sales)
print(f"Standard deviation: {std_dev:.2f}")