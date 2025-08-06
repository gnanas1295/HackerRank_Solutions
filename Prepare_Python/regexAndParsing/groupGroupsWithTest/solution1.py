# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys, re


def repetitiveValueCheck(inputStr: str) -> str | int:
    # print(inputStr)
    pattern = r"([a-zA-Z0-9])\1"
    matching = re.findall(pattern, inputStr)
    return matching[0] if matching else -1


if __name__ == "__main__":
    print(repetitiveValueCheck(sys.stdin.readline().rstrip()))
