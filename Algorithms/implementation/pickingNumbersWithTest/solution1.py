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


def pickingNumbers(a):
    # Write your code here
    a.sort()
    distinctValues = list(set(a))
    counts = Counter(a)
    listOfCount = []
    for i in range(len(distinctValues) - 1):
        if abs(distinctValues[i] - distinctValues[i + 1]) == 1:
            listOfCount.append([distinctValues[i], distinctValues[i + 1]])
    if not listOfCount:
        return max(counts.values())
    countList = []
    for x, y in listOfCount:
        countList.append(counts[x] + counts[y])
    return (
        max(countList)
        if max(countList) > max(counts.values())
        else max(counts.values())
    )


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + "\n")

    fptr.close()
