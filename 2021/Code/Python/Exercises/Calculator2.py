# Variable statements
Number1 = input("Enter your first number: ")
Number2 = input("Enter your second number: ")
NumberAsk = input("Would you like to add a third number? Y or N: ")
if NumberAsk == str("Y"):
    Number3 = input("Please enter your third number: ")
Operation = input("What operation would you like to perform on these numbers? +, -, *, or /? ")

# Operations

Sum = (int(Number1) + int(Number2))
# noinspection PyUnboundLocalVariable
Sum2 = (int(Number1) + int(Number2) + int(Number3))
Difference = (int(Number1) - int(Number2))
Difference2 = (int(Number1) - int(Number2) - int(Number3))
Product = (int(Number1) * int(Number2))
Product2 = (int(Number1) * int(Number2) * int(Number3))
Quotient = (int(Number1) / int(Number2))
Quotient2 = (int(Number1) / int(Number2) / int(Number3))

# Variable operations
Addition = "+"
Subtraction = "-"
Multiplication = "*"
Division = "/"

# Conditionals

if Operation == str("+") and NumberAsk == str("N"):
    print(Sum)
if Operation == str("+") and NumberAsk == str("Y"):
    print(Sum2)

if Operation == str("-") and NumberAsk == str("N"):
    print(Difference)
if Operation == str("-") and NumberAsk == str("Y"):
    print(Difference2)

if Operation == str("*") and NumberAsk == str("N"):
    print(Product)
if Operation == str("*") and NumberAsk == str("Y"):
    print(Product2)

if Operation == str("/") and NumberAsk == str("N"):
    print(Quotient)
if Operation == str("/") and NumberAsk == str("Y"):
    print(Quotient2)
