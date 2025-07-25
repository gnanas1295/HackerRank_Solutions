#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    maxValue = sum(arr) - sorted(arr)[0]
    minValue = sum(arr) - sorted(arr, reverse=True)[0]
    print(minValue, maxValue)


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
