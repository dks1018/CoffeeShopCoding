import sys
import os
import math

phoneBook = {
    # 'Darius': 24,
    # 'Katia' : 22,
    # 'Sydney': 17,
    # 'Darrell': 50,
    # 'Michele': 50,
}


n = int(input())
for v in range(n):
    # j = str(input())
    # a = int(input())
    # phoneBook[j] = a
    x = input().split()
    phoneBook[x[0]] = x[1]
    v+=1 
#print(phoneBook)

for i in range(n):
    k = input()
    if(k in phoneBook):
        print("{}={}".format(k, phoneBook[k]))
        i += 1
    else:
        print("Not Found")
        i += 1
        
# for n in enumerate(phoneBook.items()):
#     print(n)
# for n in phoneBook:
#     print(n,"=", phoneBook[n])
# for n in phoneBook:
#     print("{0}={1}".format(n, phoneBook[n]))
# for n in phoneBook:
#     print(str(n)+'='+str(phoneBook[n]))
# for n in phoneBook:
#     print(str(n),'=',str(phoneBook[n]))


