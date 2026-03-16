# Welcome to the Break-Even Calculator

def break_even_calculator():
    print("Break-Even Calculator")

    fixed_costs = float(input("Please enter your fixed costs: "))
    price_per_unit = float(input("Please enter your price per unit: "))
    cost_per_unit = float(input("Please enter your cost per unit: "))

    if price_per_unit == cost_per_unit:
        print("Price per unit must be greater than cost per unit.")
        return

    break_even_units = fixed_costs / (price_per_unit - cost_per_unit)

    print(f"Fixed costs: £{fixed_costs:.2f}")
    print(f"Price per unit: £{price_per_unit:.2f}")
    print(f"Cost per unit: £{cost_per_unit:.2f}")
    print(f"Break-even units: {break_even_units:.2f}")

    print(f"You must sell {break_even_units:.2f} units to break even.")

break_even_calculator()