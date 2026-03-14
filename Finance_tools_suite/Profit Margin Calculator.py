#Profit Margin Calculator

def profit_margin_calculator():
    print("Profit Margin Calculator")

    revenue = float(input("Enter the revenue: "))
    cost = float(input("Enter the cost: "))
    if revenue ==0:
        print("Revenue must be greater than £1.00")

        return

    profit = revenue - cost


    profit_margin = (profit/revenue)*100

    print(f"Revenue: £{revenue:.2f}")

    print(f"Cost: £{cost:.2f}")

    print(f"Profit: £{profit:.2f}")

    print(f"Profit margin: {profit_margin:.2f}%")

    if profit_margin > 0 :
        print("Profitable")
    elif profit_margin < 0 :
        print("Loss")
    else:
        print("Break-even")


profit_margin_calculator()



