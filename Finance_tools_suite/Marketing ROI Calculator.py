# Project 17: Marketing ROI Calculator

def marketing_roi_calculator():
    print("\nMarketing ROI Calculator\n")

    marketing_cost = float(input("Please enter the marketing cost: "))
    revenue = float(input("Please enter the total revenue: "))

    if marketing_cost == 0:
        print("Marketing cost cannot be 0.")
        return

    profit = revenue - marketing_cost
    roi = (profit / marketing_cost) * 100

    print(f"Marketing Cost: £{marketing_cost:.2f}")
    print(f"Revenue: £{revenue:.2f}")
    print(f"Profit: £{profit:.2f}")
    print(f"ROI: {roi:.2f}%")

    if roi > 100:
        print("Very strong ROI")
    elif roi > 0:
        print("Positive ROI")
    else:
        print("Negative ROI (loss)")

    print("\nMarketing performance analysis complete.")

marketing_roi_calculator()