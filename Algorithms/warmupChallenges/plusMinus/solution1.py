#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    zeroCount = 0
    postiveCount = 0
    negativeCount = 0
    lenArray = len(arr)
    for i in range(lenArray):
        if not arr[i]:
            zeroCount += 1
        elif arr[i] > 0:
            postiveCount += 1
        else:
            negativeCount += 1

    postivefactor = "{:.6f}".format(postiveCount / lenArray)
    negativefactor = "{:.6f}".format(negativeCount / lenArray)
    zerofactor = "{:.6f}".format(zeroCount / lenArray)

    print(postivefactor)
    print(negativefactor)
    print(zerofactor)


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
