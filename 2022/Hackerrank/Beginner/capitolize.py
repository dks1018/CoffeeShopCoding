#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name = s.split(" ")
    title = []
    for x in name:
        title.append(x.capitalize())
    
    return " ".join(title)
    
    #l = [x.capitalize() for x in s.split(" ")]
    #return " ".join(l)

if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)
