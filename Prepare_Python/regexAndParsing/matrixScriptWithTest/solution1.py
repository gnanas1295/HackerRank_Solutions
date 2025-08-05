#!/bin/python3

import math
import os
import random
import re
import sys


def matrixScriptDecoding(matrix: list, n: int, m: int) -> str:
    # print(matrix)

    finalStr = ""

    for itr in range(m):
        for i in range(n):
            finalStr += matrix[i][itr]

    # pattern = r'[0-9A-Za-z][ !A#$%&][0-9A-Za-z]'
    pattern = r"(?<=[0-9A-Za-z])[^a-zA-Z0-9]{1,}(?=[0-9A-Za-z])"
    # print(re.findall(pattern, finalStr))
    return re.sub(pattern, " ", finalStr)


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    print(matrixScriptDecoding(matrix, n, m))
