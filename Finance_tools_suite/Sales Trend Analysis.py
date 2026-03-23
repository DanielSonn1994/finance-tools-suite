def sales_trend_analysis():
    sales = [120, 135, 150, 160, 170, 165, 180, 175, 190, 200]

    if len(sales) < 2:
        print("Not enough data to analyse a trend.")
        return

    print("Sales Trend Analysis")
    print("-" * 25)

    first_sale = sales[0]
    last_sale = sales[-1]
    total_change = last_sale - first_sale
    average_change = total_change / (len(sales) - 1)

    print(f"Sales data: {sales}")
    print(f"First sales value: {first_sale}")
    print(f"Last sales value: {last_sale}")
    print(f"Total change: {total_change}")
    print(f"Average change per period: {average_change:.2f}")

    if total_change > 0:
        print("Trend: Upward")
    elif total_change < 0:
        print("Trend: Downward")
    else:
        print("Trend: Stable")

    print("\nPeriod-by-period changes:")
    for i in range(1, len(sales)):
        change = sales[i] - sales[i - 1]
        print(f"Period {i} to {i + 1}: {change}")



sales_trend_analysis()
