#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    # print(arr)
    leftValue = 0
    rightValue = 0
    noOfelements = len(arr)
    for i in range(noOfelements):
        j = arr[i]
        leftValue += j[i]
        rightValue += j[noOfelements - 1 - i]
        print(leftValue, rightValue)
    return abs(leftValue - rightValue)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
