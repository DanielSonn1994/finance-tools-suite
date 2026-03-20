# Project 14: Monthly Business KPI Tracker
# Tracks revenue, expenses, and profit over multiple months

def monthly_kpi_tracker():
    print("Monthly Business KPI Tracker")

    months = int(input("Enter the number of months: "))

    revenues = []
    expenses = []
    profits = []

    for i in range(months):
        print(f"\nMonth {i+1}")

        revenue_value = float(input("What is the revenue? "))
        expenses_value = float(input("What are the expenses? "))

        profit = revenue_value - expenses_value

        revenues.append(revenue_value)
        expenses.append(expenses_value)
        profits.append(profit)

    total_revenue = sum(revenues)
    total_expenses = sum(expenses)
    total_profit = sum(profits)

    average_revenue = total_revenue / months
    average_expenses = total_expenses / months
    average_profit = total_profit / months

    best_profit = max(profits)
    worst_profit = min(profits)

    best_month = profits.index(best_profit) + 1
    worst_month = profits.index(worst_profit) + 1

    print("\n--- Summary ---")
    print(f"Total revenue: £{total_revenue:.2f}")
    print(f"Total expenses: £{total_expenses:.2f}")
    print(f"Total profit: £{total_profit:.2f}")

    print(f"\nAverage revenue: £{average_revenue:.2f}")
    print(f"Average expenses: £{average_expenses:.2f}")
    print(f"Average profit: £{average_profit:.2f}")

    print(f"\nBest month: Month {best_month} with profit of £{best_profit:.2f}")
    print(f"Worst month: Month {worst_month} with profit of £{worst_profit:.2f}")

    print("\nKPI tracking complete.")

monthly_kpi_tracker()