# Project 15: Customer Lifetime Value Calculator

def customer_lifetime_value_calculator():
    print("\nCustomer Lifetime Value Calculator")

    average_purchase_value = float(input("Please enter the average purchase value: "))
    purchase_frequency = float(input("Please enter the purchase frequency (per year): "))
    customer_lifespan = float(input("Please enter the customer lifespan (years): "))

    clv = average_purchase_value * purchase_frequency * customer_lifespan

    print(f"\nAverage purchase value: £{average_purchase_value:.2f}")
    print(f"Purchase frequency: {purchase_frequency}")
    print(f"Customer lifespan: {customer_lifespan:.2f} years")
    print(f"Customer Lifetime Value (CLV): £{clv:.2f}")

    if clv > 1000:
        print("High-value customer")
    elif clv > 500:
        print("Moderate-value customer")
    else:
        print("Low-value customer")

customer_lifetime_value_calculator()