# Project 16: Unit Economics Calculator
# Tracks revenue per unit, cost per unit, and profit per unit

def unit_economics_calculator():
    print("\nUnit Economics Calculator")

    revenue_per_unit = float(input("\nEnter revenue per unit: "))
    cost_per_unit = float(input("\nEnter cost per unit: "))

    if revenue_per_unit == 0:
        print("Revenue per unit cannot be zero.")
        return

    profit_per_unit = revenue_per_unit - cost_per_unit
    profit_margin = (profit_per_unit / revenue_per_unit) * 100

    print(f"Revenue per unit: £{revenue_per_unit:.2f}")
    print(f"Cost per unit: £{cost_per_unit:.2f}")
    print(f"Profit per unit: £{profit_per_unit:.2f}")
    print(f"Profit margin: {profit_margin:.2f}%")

    if profit_per_unit > 0:
        print("Profitable")
    elif profit_per_unit < 0:
        print("Loss per unit")
    else:
        print("Break-even")

unit_economics_calculator()