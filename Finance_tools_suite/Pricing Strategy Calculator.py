def pricing_strategy_calculator():
    print("Pricing Strategy Calculator")

    cost = float(input("Please enter the cost of your purchase: "))
    markup_percentage = float(input("Please enter the markup percentage of your purchase: "))
    markup_amount = cost * markup_percentage/100

    selling_price = cost + markup_amount

    print(f"Cost of your purchase: {cost:.2f}")
    print(f"Markup percentage of your purchase: {markup_percentage:.2f}%")
    print(f"Markup amount of your purchase: £{markup_amount:.2f}")
    print(f"Suggested selling price: £{selling_price:.2f}")

pricing_strategy_calculator()