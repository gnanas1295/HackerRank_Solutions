#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def formingMagicSquare(s):
    """
    Calculates the minimum cost to convert a 3x3 matrix into a magic square
    using a concise generator expression.
    """
    # All 8 possible 3x3 magic squares
    all_magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    # This single line calculates the cost for all 8 squares and finds the minimum.
    # It iterates through each perfect square 'p',
    # calculates the total cost to transform 's' into 'p',
    # and the outer min() finds the smallest of these 8 total costs.
    min_cost = min(
        sum(abs(s[i][j] - p[i][j]) for i in range(3) for j in range(3))
        for p in all_magic_squares
    )

    return min_cost


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + "\n")

    fptr.close()
