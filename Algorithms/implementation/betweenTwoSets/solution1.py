#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b) -> int:

    iterationsToCheck = []

    iterationsToCheck = (i for i in range(max(a), min(b) + 1) if (i % max(a)) == 0)
    # print(iterationsToCheck)
    finalList = []
    for i in iterationsToCheck:
        # print(i)
        valid = False
        for j in a:
            if (i % j) == 0:
                valid = True
            else:
                valid = False
                break
        if valid:
            for k in b:
                if (k % i) == 0:
                    valid = True
                else:
                    valid = False
                    break
        if valid:
            finalList.append(i)

    # print(finalList)
    return len(finalList)


if __name__ == "__main__":

    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + "\n")

    fptr.close()
