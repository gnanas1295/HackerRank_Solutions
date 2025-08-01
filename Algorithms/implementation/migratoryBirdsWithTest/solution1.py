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
    count = Counter(arr).most_common()
    if len(count) > 1:
        if count[0][1] == count[1][1]:
            return count[0][0] if count[0][0] < count[1][0] else count[1][0]
        else:
            return count[0][0]
    else:
        return count[0][0] if count else None


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
