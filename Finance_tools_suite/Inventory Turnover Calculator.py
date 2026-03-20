# Project 18: Inventory Turnover Calculator

def inventory_turnover_calculator():
    print("\nInventory Turnover Calculator")

    cost_of_goods_sold = float(input("Enter cost of goods sold: "))
    average_inventory = float(input("Enter average inventory: "))

    if average_inventory == 0:
        print("Average inventory cannot be 0")
        return

    inventory_turnover = cost_of_goods_sold / average_inventory

    print(f"Cost of goods sold: £{cost_of_goods_sold:.2f}")
    print(f"Average inventory: £{average_inventory:.2f}")
    print(f"Inventory turnover: {inventory_turnover:.2f}")

    if inventory_turnover > 5:
        print("High inventory turnover (efficient)")
    elif inventory_turnover > 1:
        print("Moderate inventory turnover")
    else:
        print("Low inventory turnover (inefficient)")

inventory_turnover_calculator()