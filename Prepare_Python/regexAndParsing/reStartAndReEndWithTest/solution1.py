# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys, re


def findIndices(strToCheck: str, strToComp: str) -> list:
    pattern = rf"(?=({strToComp}))"
    retnList = []
    matches = re.finditer(pattern, strToCheck)
    flag = False

    for item in matches:
        flag = True
        # print(f"({item.start(1)}, {item.end(1)-1})")
        retnList.append(f"({item.start(1)}, {item.end(1)-1})")

    if not flag:
        retnList.append("(-1, -1)")

    return retnList


if __name__ == "__main__":
    strToCheck, strToComp = sys.stdin.read().split()
    finalMatch = findIndices(strToCheck, strToComp)
    print("\n".join(match for match in finalMatch))
