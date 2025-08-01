#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    """
    Finds the most frequent bird type, returning the smallest ID in case of a tie.
    Uses a fixed-size array as a frequency map for O(n) performance.
    """
    # Create a list of size 6 to act as a frequency map for bird types 1-5.
    # Index 0 is unused.
    counts = [0] * 6

    # In a single pass, count the occurrences of each bird type.
    for bird_type in arr:
        counts[bird_type] += 1

    # max(counts) finds the highest frequency.
    # counts.index(...) finds the first index (which is the bird type ID)
    # that has that maximum frequency. This automatically handles the tie-breaking
    # rule because .index() returns the lowest index in case of duplicates.
    return counts.index(max(counts))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
