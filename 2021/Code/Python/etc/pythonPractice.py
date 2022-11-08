import sys

password = [0, 1, 2, 3, 4, 5]
password2 = [5, 4, 3, 2, 1, 0]
x = 0
i = 0
print(password2)
while x < len(password):
    print(password[x])
    password2[i] = password[x]
    x+=1
    i+=1

print(password2)