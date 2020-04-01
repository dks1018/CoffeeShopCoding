# # write a program to print out capitols in the quote
# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
# capitolString = ""

# for capitol in quote:
#     if capitol.isupper():
#         capitolString += capitol
# print(capitolString)

# #Alternate solution
# alt_capitol_String = ""

# for cap in quote:
#     if cap in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#         alt_capitol_String += cap
# print(alt_capitol_String)

# # Write a program to print number 0-9
# for num in range(0, 10):
#     print(num)
    
# right a loop that stops when it is exactly divisiable by 11 using break
# for num in range(0,100, 7):
#     if(num > 0 and num % 11 == 0):
#         print(num)
#         break

#print out all number from 0 to 20 that are not divisible by 3 to 5 using continue

list1 = ""
list2 = ""

#using continue
for num1 in range(0,20):
    if num1 % 3 == 0 or num1 % 5 == 0:
        continue
    else:
        list1 += (":" + str(num1))

#without using continue
for num2 in range(0,20):
    if num2 % 3 != 0 and num2 % 5 != 0:
        list2 += (":" + str(num2))
              
print(list1, list2, sep="\n")
#boolean compare
print(list1==list2)


    