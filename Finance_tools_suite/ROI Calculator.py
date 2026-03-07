print("Hello, welcome to the Return On Investment Calculator")

#Formula used to calculate ROI

# ROI = (Net return - Investment Cost) / (Investment Cost) * 100
# Profit = Net Return - Investment Cost

Investment_cost = float(input("Whats the cost of the Investment (£)? "))

Net_return = float(input("What is the Net return (£) ? "))


Return_on_Investment = Net_return - Investment_cost

ROI_percentage = Return_on_Investment / Investment_cost * 100

if ROI_percentage < 0:
    print("You have made a loss")
elif ROI_percentage == 0:
    print("You broke even")
else:
    print("You have made a profit")

print(f"Return on Investment: £{Return_on_Investment:.2f}")
print(f"ROI percentage: {ROI_percentage:.2f} %")




