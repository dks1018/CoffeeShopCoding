
# define variables
num1 = input("Input your first number: ")
num2 = input("Input your second number: ")

options = "Pick an operation:\
\n1 for add\
\n2 for subtract\
\n3 for multiply\
\n4 for divide\
\n5 for Modulous"

# define math funcitons
sum1 = int(num1) + int(num2)
sub1 = int(num1) - int(num2)
mult1 = int(num1) * int(num2)
div1 = int(num1) / int(num2)
mod1 = int(num1) % int(num2)

#print statement
print(options)
choice = input()

#if statment
if(choice == '1'):
    print(sum1)
elif(choice == '2'):
    print(sub1)
elif(choice == '3'):
    print(mult1)
elif(choice == '4'):
    print(div1)
else:
    print(mod1)