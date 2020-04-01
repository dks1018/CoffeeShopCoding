# n=int(input())
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

# def factorial(n):
#     if(n > 0):
#         fact = (n * (n - 1))
#     else:
#         return result
#     return factorial(n-1)

# if __name__ == "__main__":
#     n=int(input())
#     result = factorial(n)
#     print(result)

n = int(input())
a = (n - 1)
print(a)
for i in range(1,n):
    n = (n * a)
    print(n, a)
    a-=1
print(n)

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    a = (n - 1)
    for i in range(1,n):
        n = (n * a)
        a-=1
    return n

if __name__ == '__main__':
    n = int(input())
    result = factorial(n)
    print(result)

