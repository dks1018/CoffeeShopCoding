import random

# function to find if numbers in array equal up to the sum
def sumIntInArray(sum,intArray):
    numSet = set()
    for iterator in intArray:
        calculater = sum - iterator
        if(calculater in numSet):
            return iterator, calculater
        
        numSet.add(iterator)
    return False

# function to generate random numbers for array
def generateRandNums():
    counter = random.randint(1,100)
    intArr = []
    while 0 < counter:
        n = random.randint(1,100)
        intArr.append(n)
        counter -= 1
    return intArr

# set the sum number
userInput = int(input("Enter number between 1 and 100: "))

# generate random numbers for arry
randomIntArray = generateRandNums()

# pass in sum number and random integer array to find if any equal sum number
values = sumIntInArray(userInput,randomIntArray)

# print random array
print(randomIntArray)

# print values from array that equal up to sum
print(values)
