#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    """
    Calculates the number of valleys a hiker traverses.
    A valley is counted at the moment the hiker steps down from sea level.
    """
    altitude = 0
    valleys_entered = 0

    for step in path:
        # A valley starts ONLY when stepping down from sea level (altitude 0).
        if altitude == 0 and step == "D":
            valleys_entered += 1

        # # Update the altitude for the current step.
        # if step == 'U':
        #     altitude += 1
        # else:
        #     altitude -= 1
        altitude = altitude + 1 if step == "U" else altitude - 1

    return valleys_entered


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + "\n")

    fptr.close()
