#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # Write your code here
    thresholdScore = scores[0]
    highestScores = []
    lowestScores = []

    for i in scores:
        if i > thresholdScore:
            if i not in highestScores:
                if highestScores:
                    if i > max(highestScores):
                        highestScores.append(i)
                else:
                    highestScores.append(i)
        elif i < thresholdScore:
            if i not in lowestScores:
                if lowestScores:
                    if i < min(lowestScores):
                        lowestScores.append(i)
                else:
                    lowestScores.append(i)

    # return f"{len(highestScores)}{len(lowestScores)}"
    return [len(highestScores), len(lowestScores)]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
