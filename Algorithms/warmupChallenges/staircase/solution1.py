#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(n+1):
        if i == 0:
            continue
        elif i == n:
            print('#' * n)
        else:
            print(f"{' ' * (n-i)}{'#' * i}")
        
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
