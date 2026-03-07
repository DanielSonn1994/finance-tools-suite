#Cash Flow Projection Tool

starting_balance = float(input("What is your starting balance? (£) "))

monthly_income = float(input("What is your monthly income? (£) "))

monthly_expense = float(input("What is your monthly expense? (£) "))

number_of_months_to_project = int(input("How many months would you like to project? "))

cash_change = monthly_income - monthly_expense

balance = starting_balance

for month in range(number_of_months_to_project):
    balance = balance + monthly_income - monthly_expense
    print(f"Month {month + 1} balance: £{balance:.2f}")

