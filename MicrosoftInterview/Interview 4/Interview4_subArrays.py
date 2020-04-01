# recursive functions
def recursive_subarray_func(array_length):
    if(array_length <= 0):
        return 0
    else:
        total = array_length + recursive_subarray_func(array_length-1)
        return total


# looping subarray counter    
def SubArray_func1(array_length):
    total = array_length
    while array_length > 0:
        total = total + (array_length - 1)
        array_length = array_length -  1
    return total


# sum largest sub array
def subarray_sum(array):
    sum = 0
    for arrayCounter in array:
        sum += arrayCounter 
    return sum


# print sub arrays
def print_subarrays(array):
    n = 0
    for i in array[n:]:
        print(array[n:])
        n += 1
    return "SUCCESS!"
    
# variables
user_array = []
total_nums = int(input("Enter how many value you want to enter into the array: "))


for i in range(total_nums):
    array_nums = int(input("Enter the number to go into the array: "))
    user_array.append(array_nums)

# print created array
# print(user_array)
    
# amount of subarrays function call
recursive_subarray_func_call = recursive_subarray_func(len(user_array))
# subarray_func1_call = SubArray_func1(len(user_array))


# subarray sum function call
sum_subarray_func_call = subarray_sum(user_array)

# print subarray function call
print_subarray_func_call = print_subarrays(user_array)

# print func_call
print(recursive_subarray_func_call)
# print(subarray_func1_call)
print(sum_subarray_func_call)
print(print_subarray_func_call)