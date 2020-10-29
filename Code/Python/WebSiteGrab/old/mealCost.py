meal = float(input("Enter your total meal cost: "))
tip =  int(input("How much do you want to tip: "))
tax = int(input("What is the tax rate: "))

total_bill = round(meal + tip + tax)

print(total_bill)