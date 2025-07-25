#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    # print(s)
    pattern = r"(\d{2}):(\d{2}):(\d{2})(\w{2})"
    matching = re.findall(pattern, s)
    if matching[0][3] == "PM":
        if matching[0][0] == "12":
            return f"{int(matching[0][0])}:{matching[0][1]}:{matching[0][2]}"
        return f"{int(matching[0][0]) + 12}:{matching[0][1]}:{matching[0][2]}"
    else:
        if matching[0][0] == "12":
            return f"00:{matching[0][1]}:{matching[0][2]}"
        return f"{matching[0][0]}:{matching[0][1]}:{matching[0][2]}"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
