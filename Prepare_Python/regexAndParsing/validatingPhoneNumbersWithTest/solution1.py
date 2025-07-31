# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys, re


def validPhoneNumber(phoneNumber: str) -> str:
    pattern = r"[789][\d]{9}"
    if re.fullmatch(pattern, phoneNumber):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    inputCount = int(sys.stdin.readline())
    for _ in range(inputCount):
        phoneNumber = sys.stdin.readline().strip()
        print(validPhoneNumber(phoneNumber))
