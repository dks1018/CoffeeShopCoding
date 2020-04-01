import math
import os
import random
import re
import sys

# Complete the factorial function below.

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
    # if(n < 0):
    #     result = (n * (n - 1))
    # else:
    #     return result
    # return factorial(n-1)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
