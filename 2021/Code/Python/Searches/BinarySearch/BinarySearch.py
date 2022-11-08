
low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:
    print("\tGuessing in the range of {} and {}".format(low, high))
    # Calculate midpoint between low adn high values
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess Higher or Lower?"
                     "Enter h or l or c if my guess was correct "
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher.The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower.The high end of the range becomes one less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h,l, or c")
    guesses += 1
else:
    print("You thought of the number {}".format(low))  
    print("I got it in {} guesses".format(guesses))  
#I am choosing 129
# with 1000 number what I want to do is be able to guess the users number within 10 guesses
# to do this i need to continue to devide in half the high form the low
# then establish a new high and low
#  if the number is 22 and the high is 100 and low is 0 first computer says
# 1 is you number 50? higher or lower
# lower, so high is 100-1 / 2 equals 49.5 rounded down high now equals 49 low now equals 0
# 2 is the number 25 or higher or lower
# lower so high is 49-1 / 2 is 24
# 3 is you number 12,
# it is higher so lower = guess + 1
# lower is 13 high is 24
# 4 is you number 18,
# no high
# 5 lower is 19, is your number 21
# no high lower equals 22 high equals 24
# 6 is your number 23, no lower
# 7 your number is 22