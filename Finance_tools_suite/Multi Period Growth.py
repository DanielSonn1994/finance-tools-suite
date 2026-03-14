def multi_period_growth():
    print("Multi Period Growth Analysis")

    values = [100, 120, 150, 170, 210]



    first_sale = values[0]
    last_sale = values[-1]
    total_change = last_sale - first_sale
    average_change = total_change / (len(values)-1)

    print(f"The first sale value is: {first_sale}")
    print(f"The last sale value is: {last_sale}")
    print(f"The total change is: {total_change}")
    print(f"The average change is: {average_change:.2f}")

    if total_change >0:
        print("Trend: upwards")
    elif total_change < 0:
        print("Trend: downwards")
    else:
        print("Trend: no change")

    print("\nPeriod-by-period growth changes:")
    for i in range(1, len(values)):
        previous = values[i - 1]
        current = values[i]

        growth_rate = (current - previous) / previous * 100

        print(f"Period {i} to {i + 1}: {growth_rate:.2f}%")


multi_period_growth()