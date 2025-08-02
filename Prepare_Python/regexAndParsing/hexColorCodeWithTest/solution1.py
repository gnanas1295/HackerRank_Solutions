# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys, re


def regexPatternSearch(inputStr: str) -> None | list:
    pattern = re.compile(r"(?<=[ :\(,])#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
    matchedResults = pattern.findall(inputStr)
    if matchedResults:
        for items in matchedResults:
            print(items)
    return matchedResults


if __name__ == "__main__":
    numOfInputs = int(sys.stdin.readline())

    for _ in range(numOfInputs):
        inputStr = sys.stdin.readline().strip()
        searchOutput = regexPatternSearch(inputStr)
