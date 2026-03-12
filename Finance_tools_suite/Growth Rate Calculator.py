def growth_rate_calculator():
    print("Welcome to the Growth Rate Calculator")

    starting_value = float(input("What is your starting value?"))
    ending_value = float(input("What is your ending value?"))

    if starting_value == 0:
        print("Starting value cannot be zero.")
        return

    # Growth Rate Formula  = (Final - Initial) / initial * 100

    growth_rate = (ending_value - starting_value) / starting_value * 100

    print(f"Growth rate: {growth_rate:.2f}%")

    if growth_rate >0:
        print("The value has increased")
    elif growth_rate <0:
        print("The value has decreased")

    else:
        print("The value has stayed the same")







growth_rate_calculator()