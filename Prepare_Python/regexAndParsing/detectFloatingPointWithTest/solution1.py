# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import re


def floatingValueCheck(inputVal: str) -> bool:
    pattern = r"^[+-]?(\d+\.\d+|\.\d+)$"
    if re.match(pattern, inputVal):
        return True
    return False


if __name__ == "__main__":
    inputCount = int(sys.stdin.readline())
    for _ in range(inputCount):
        inputVal = sys.stdin.readline().strip()

        print(floatingValueCheck(inputVal))
