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
    """
    Determines if two kangaroos will meet at the same location at the same time.
    This logic works regardless of which kangaroo starts ahead.
    """
    # If k2 has a different speed than k1
    if v1 != v2:
        # Calculate the number of jumps 'j' needed: j = (x1 - x2) / (v2 - v1)
        # Check two conditions:
        # 1. The number of jumps must be a whole number (remainder is 0).
        # 2. The number of jumps must be positive or zero (they meet in the future).
        if (x1 - x2) % (v2 - v1) == 0 and (x1 - x2) / (v2 - v1) >= 0:
            return "YES"

    # If they have the same speed, they only meet if they start at the same place.
    # The problem constraints usually mean x1 != x2, but this covers it.
    elif x1 == x2:
        return "YES"

    # In all other cases, it's impossible.
    return "NO"


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
