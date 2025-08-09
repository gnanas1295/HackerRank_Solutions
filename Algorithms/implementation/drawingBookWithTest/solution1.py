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
    # Write your code here
    middlePage = n / 2
    print(middlePage)
    if p < middlePage:
        print("Go Front")
        return p // 2
    else:
        print("Go Back")
        if n % 2 == 0:
            print("Even")
            if (n - p) // 2 == 0:
                if p == 1:
                    return 0
                elif n != p:
                    return 1
                else:
                    return 0
            else:
                return (n - p) // 2
        else:
            print("Odd")
            return (n - p) // 2

    # return n


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + "\n")

    fptr.close()
