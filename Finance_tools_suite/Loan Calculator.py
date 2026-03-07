
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
#2f rounds to 2 decimal places
print(f"Monthly payment: £{monthly_payments:.2f}")
print(f"Total repayment: £{total_repayments:.2f}")
print(f"Total interest paid: £{total_interest:.2f}")