# take user input
user_num = int(input())

# in to binary number
binary_num = bin(user_num)

# counter variables
counter_placeholder = 0
answer_counter = 0

# counter consec 1's
for i in binary_num:
    if(i == '1'): # add one to the counter 
        counter_placeholder += 1
    if(counter_placeholder >= answer_counter): # if counter is greater than answer set answer equal to counter
        answer_counter = counter_placeholder
    if(i == '0'): # reset counter if you come across 0
        counter_placeholder = answer_counter
        counter_placeholder = 0
        
# Print binary number
print(binary_num)

# print(counter)

# print number of consecutive 1's
print(answer_counter)
