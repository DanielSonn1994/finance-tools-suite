def revenue_growth_simulator():
    print("Revenue Growth Simulator")

    starting_value = float(input("What is your starting value? "))
    growth_rate = float(input("What is your growth rate? "))
    periods = int(input("How many periods would you like? "))

    revenue = starting_value
    revenues = []

    for i in range(periods):
        revenue = revenue * (1 + growth_rate / 100)
        print(f"Period {i+1}: £{revenue:.2f}")
        revenues.append(revenue)

    print("\nAll projected revenues:")
    print(revenues)

    total_growth = ((revenue - starting_value) / starting_value) * 100
    print(f"\nTotal growth: {total_growth:.2f}%")

revenue_growth_simulator()