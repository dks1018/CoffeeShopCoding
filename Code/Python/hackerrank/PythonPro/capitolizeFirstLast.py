import math
import os
import random
import re
import sys
import string

def capitalize(s):
    for x in s[:].split(" "):
        s = s.replace(x, x.capitalize())
        s="".join(s)
        return s
# Complete the solve function below.
# def solve(i):
#    return

if __name__ == '__main__':
    s = input()
    result = capitalize(s)
    print(result)
    
# s = input()
# for x in s[:].split():
#     s = s.replace(x, x.capitalize())

# print(s)


# print(string.capwords(input(), ' '))

# def solve(i):
#     return i[0].upper() + i[1::]

 # capitolize = ''
    # heck = 0
    # while heck < len(i):
    #     capitolize = i[0].upper() + i[1::]
    #     print(heck)
    #     if heck == " ":
    #         capitolize += i[heck + 1].upper()
    #     heck += 1
    
    # for check in i:
    #     if check == i[0]:
    #         capitolize = i[0].upper() + i[1::]
    #     if check == " ":
    #         capitolize = i[check].upper()
    # return capitolize