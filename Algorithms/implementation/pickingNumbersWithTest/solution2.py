#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

from collections import Counter


def pickingNumbers(a):
    """
    Finds the length of the longest subarray where the absolute difference
    between any two elements is less than or equal to 1.
    """
    # 1. Get the frequency of each number in a single pass.
    counts = Counter(a)
    max_length = 0
    print(counts)

    # 2. Iterate through the unique numbers found in the array.
    for num in counts:
        print(num)
        current_length = counts[num] + counts.get(num + 1, 0)

        # 4. Keep track of the maximum length found so far.
        if current_length > max_length:
            max_length = current_length

    return max_length


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + "\n")

    fptr.close()
