def loan_calculator():
    # Loan calculator
    # 1. Calculates monthly payments
    # 2. Shows total repayment and interest
    # 3. Handles zero-interest loans

    loan_amount = float(input("Enter loan amount:"))
    annual_interest_rate = float(input("Enter the interest rate:"))
    loan_term_in_years = int(input("How many years is the loan for?"))

    monthly_interest_rate = annual_interest_rate / 100 / 12
    number_of_payments = loan_term_in_years * 12

    # Formula for Monthly payment is:

    # M = P * r(1+r)/(1+r)^n -1
    # M = monthly payment
    # P = loan amount
    # r = monthly interest
    # n = total number of payments
    if monthly_interest_rate == 0:
        monthly_payments = loan_amount / number_of_payments
    else:
        monthly_payments = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / (
                (1 + monthly_interest_rate) ** number_of_payments - 1)

    # This works out total repayment amount by using the monthly payment * total amount of payments
    total_repayments = monthly_payments * number_of_payments

    total_interest = total_repayments - loan_amount

    # f inserts a variable into a string
    # 2f rounds to 2 decimal places
    print(f"Monthly payment: £{monthly_payments:.2f}")
    print(f"Total repayment: £{total_repayments:.2f}")
    print(f"Total interest paid: £{total_interest:.2f}")


def roi_calculator():

    print("Hello, welcome to the Return On Investment Calculator")

    # Formula used to calculate ROI

    # ROI = (Net return - Investment Cost) / (Investment Cost) * 100
    # Profit = Net Return - Investment Cost

    investment_cost = float(input("Whats the cost of the Investment (£)? "))

    net_return = float(input("What is the Net return (£) ? "))

    return_on_Investment = net_return - investment_cost

    roi_percentage = return_on_Investment / investment_cost * 100

    if roi_percentage < 0:
        print("You have made a loss")
    elif roi_percentage == 0:
        print("You broke even")
    else:
        print("You have made a profit")

    print(f"Return on Investment: £{return_on_Investment:.2f}")
    print(f"ROI percentage: {roi_percentage:.2f} %")


def cash_flow_projection():
    # Cash Flow Projection Tool

    starting_balance = float(input("What is your starting balance? (£) "))

    monthly_income = float(input("What is your monthly income? (£) "))

    monthly_expense = float(input("What is your monthly expense? (£) "))

    number_of_months_to_project = int(input("How many months would you like to project? "))

    cash_change = monthly_income - monthly_expense

    balance = starting_balance

    for month in range(number_of_months_to_project):
        balance = balance + monthly_income - monthly_expense
        print(f"Month {month + 1}: Change £{cash_change:.2f} | Balance £{balance:.2f}")



print("Welcome to Finance Tools Suite")
print("1. Loan Calculator")
print("2. ROI Calculator")
print("3. Cash Flow Projection Tool")

choice = input("Choose an option: ")

if choice == "1":
    loan_calculator()
elif choice == "2":
    roi_calculator()
elif choice == "3":
    cash_flow_projection()
else:
    print("Invalid option")




