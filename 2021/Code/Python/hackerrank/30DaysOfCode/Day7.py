import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    j = arr[::-1]
    print(*j)

    #print(" ".join(map(str, arr[::-1])))
    #print(*arr[::-1])
    #print(' '.join(str(x) for x in arr[::-1]))