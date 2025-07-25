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
    # n = len(arr)
    # positive_count = 0
    # negative_count = 0
    # zero_count = 0

    # # Iterate directly over the numbers in the array
    # for num in arr:
    #     if num > 0:
    #         positive_count += 1
    #     elif num < 0:
    #         negative_count += 1
    #     else:
    #         zero_count += 1

    # # Use f-strings for modern, readable formatting
    # print(f"{positive_count / n:.6f}")
    # print(f"{negative_count / n:.6f}")
    # print(f"{zero_count / n:.6f}")

    # The below solution is not optimised as it runs three times
    n = len(arr)

    # sum() with a generator expression counts all items matching a condition
    positives = sum(1 for num in arr if num > 0)
    negatives = sum(1 for num in arr if num < 0)
    zeros = sum(1 for num in arr if num == 0)

    print(f"{positives / n:.6f}")
    print(f"{negatives / n:.6f}")
    print(f"{zeros / n:.6f}")


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
