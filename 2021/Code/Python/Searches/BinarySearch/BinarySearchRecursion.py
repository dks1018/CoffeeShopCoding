import sys

# Variables
low = 1
high = 1000

# Guessing Statement
print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER when your ready")

# User Number and Answer L, H, or C
user_number = int(input("Enter your number: "))
user_answer = ""

# Binary Search Equation
def Higher():
    print("\nHigher")
    return guess - 1


def Lower():
    print("\nLower")
    return guess + 1


counter = 0 
while True:
    counter += 1
    guess = low + (high - low) // 2
    print("Guessing in between the range of ", low, high, sep=":")
    print("Is your number {0}".format(guess))
    
    user_answer = str(input("Enter H for higher,L for lower, or C for correct: "))
    if user_answer == "H":
        low = Higher()
    elif user_answer == "L":
        high = Lower()
    else:
        print("Your answer is {0}".format(guess))
        print(counter)
        break
    
# def BinarySearch(answer):
#     if answer == "H":
#         print("Higher")
#         return guess + 1
#     if answer == "L":
#         print("Lower")
#         return guess - 1
#  while True:
#     counter += 1
#     guess = low + (high - low) // 2
#     user_answer = str(input("Enter H,L, or C: "))
#     if user_answer == "H":
#         high = BinarySearch(user_answer)
#     if user_answer == "L":
#         low = BinarySearch(user_answer)
#     else:
#         print("Your answer is {0}".format(guess))
#         print(counter)
#         break
#     print(high,low,guess,sep=":")