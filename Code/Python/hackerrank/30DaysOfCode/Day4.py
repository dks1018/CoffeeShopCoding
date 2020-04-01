class Person:
    def __init__(self,initialAge):
        if(initialAge < 0):
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
        
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if(age < 13):
            print("You are young.")
        elif(13 <= age < 18):
            print("You are a teenager.")
        elif age >= 18:
            print("You are old.")
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        global age
        age += 1
        # Increment the age of the person in here

t = int(input())