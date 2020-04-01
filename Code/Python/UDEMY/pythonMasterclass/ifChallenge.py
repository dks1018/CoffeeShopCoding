userName = str(input("What is your name: "))
userAge = int(input("What is your age: "))


if(17 < userAge < 30):
    print("Welcome to the Holiday!")
elif(userAge > 30):
    print("It looks like you might be a little to old.")
else:
    print("Sorry it seems like you are not old enough.")