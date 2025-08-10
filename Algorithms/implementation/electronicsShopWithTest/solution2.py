#!/bin/python3

import os
import sys


#
# Complete the getMoneySpent function below.
#
# def getMoneySpent(keyboards, drives, b):
#     kPtr = 0
#     dPtr = 0
#     maxValue = -1
#     keyboards.sort()
#     drives.sort(reverse=True)

#     while kPtr < len(keyboards) and dPtr < len(drives):
#         tempSum = keyboards[kPtr] + drives[dPtr]

#         if tempSum <= b:
#             if tempSum > maxValue:
#                 maxValue = tempSum

#             kPtr += 1
#         else:
#             dPtr += 1
#     return maxValue

from itertools import product


def getMoneySpent(keyboards, drives, b):
    """
    Finds the most expensive combination of a keyboard and drive
    that is within the budget 'b'.
    """
    # Create a generator of all valid sums (under or equal to the budget).
    # A generator doesn't store all values in memory at once.
    valid_sums = (k + d for k in keyboards for d in drives if k + d <= b)

    # Find the maximum value from the generator.
    # The `default=-1` for max() gracefully handles the case where
    # the generator is empty (no valid pairs found).
    return max(valid_sums, default=-1)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + "\n")

    fptr.close()
