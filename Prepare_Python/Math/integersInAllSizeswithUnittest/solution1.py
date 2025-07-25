# Enter your code here. Read input from STDIN. Print output to STDOUT

import math, sys


def powerCalculation(a: int, b: int) -> int:
    return pow(a, b)


if __name__ == "__main__":
    inputs = list(map(int, sys.stdin.readlines()))

    firstValue = powerCalculation(inputs[0], inputs[1])
    secondValue = powerCalculation(inputs[2], inputs[3])

    print(firstValue + secondValue)
