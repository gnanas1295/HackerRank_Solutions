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
    # for i in range(1, n + 1):
    #     spaces = ' ' * (n - i)
    #     hashes = '#' * i
    #     print(spaces + hashes)
    for i in range(1, n + 1):
        # Create the string of hashes and right-justify it in a space of width n
        print(('#' * i).rjust(n))
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
