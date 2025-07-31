#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


# Logic: a +b % k ==0 is same as  (a%k + b%k) %k ==0
def divisibleSumPairs(n, k, ar):
    remainderCounts = [0] * k
    pairCount = 0

    for num in ar:
        remainder = num % k
        complement = (k - remainder) % k

        pairCount += remainderCounts[complement]

        remainderCounts[remainder] += 1

    return pairCount


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
