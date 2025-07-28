#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


def kangaroo(x1, v1, x2, v2):
    # Write your code here

    differenceInFactor = abs(v1 - v2)
    differenceInStartPoint = abs(x1 - x2)

    if differenceInFactor == 0:
        return f"{"YES" if x1==x2 else "NO"}"

    firstKangarooDistance = (v1 * (differenceInStartPoint // differenceInFactor)) + x1
    rightKangarooDistance = (v2 * (differenceInStartPoint // differenceInFactor)) + x2

    return f"{"YES" if firstKangarooDistance == rightKangarooDistance else "NO"}"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + "\n")

    fptr.close()
