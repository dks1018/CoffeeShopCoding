import random


# variables
rand_num1 = random.randint(1,1000)
random_numbers_Arr = []
counter = 0

# Create randomized array
while counter < rand_num1:
    rand_num2 = random.randint(1,20)
    random_numbers_Arr.append(rand_num2)
    counter += 1
print(random_numbers_Arr)
    
# count repeated numbers in the array and store in new array
counter = 1
solution_arr = []
for i in random_numbers_Arr[1:]:
    if(i == random_numbers_Arr[-1]):
        counter += 1
    else:
        solution_arr.append("{Set")
        solution_arr.append(counter)
        solution_arr.append(i)
        solution_arr.append("}")
        counter = 1

newString = str(solution_arr).replace("'","")
newString2 = newString.replace(",","")

print(newString2)
#print("\n",str(solution_arr).strip('[]'))