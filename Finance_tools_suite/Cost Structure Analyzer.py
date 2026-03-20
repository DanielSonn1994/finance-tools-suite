def cost_structure_analyzer():
    print("Cost Structure Analyzer")

    fixed_costs = float(input("Please enter the fixed costs: "))

    variable_costs = float(input("Please enter the variable costs: "))

    total_costs = fixed_costs + variable_costs

    if total_costs == 0:
        print("The total cost cannot be zero")
        return

    fixed_percentage = (fixed_costs / total_costs) * 100
    variable_percentage = (variable_costs / total_costs) * 100

    print(f"Fixed cost: £{fixed_costs:.2f}")
    print(f"Variable cost: £{variable_costs:.2f}")
    print(f"Total cost: £{total_costs:.2f}")
    print(f"Fixed cost percentage: {fixed_percentage:.2f}%")
    print(f"Variable cost percentage: {variable_percentage:.2f}%")

    if fixed_percentage > variable_percentage:
        print("The business has higher fixed costs")
    elif fixed_percentage < variable_percentage:
        print("The business has higher variable costs")
    else:
        print("The cost structure is balanced")

    print("\nCost structure analysis complete.")






cost_structure_analyzer()