#!/bin/python3

import os
from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    """
    Calculates the total number of matching pairs of socks.
    """
    # 1. Count the occurrences of each sock color.
    color_counts = Counter(ar)

    # 2. For each color's total count, calculate the number of pairs
    #    using integer division by 2.
    # 3. Sum up the number of pairs for all colors.
    total_pairs = sum(count // 2 for count in color_counts.values())

    return total_pairs


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
