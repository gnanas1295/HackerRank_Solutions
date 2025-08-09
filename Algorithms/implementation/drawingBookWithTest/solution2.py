#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n: int, p: int) -> int:
    totalTurns = n // 2
    totalTurnsFromFront = p // 2
    totalTurnsFromBack = totalTurns - totalTurnsFromFront

    return min(totalTurnsFromFront, totalTurnsFromBack)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + "\n")

    fptr.close()
