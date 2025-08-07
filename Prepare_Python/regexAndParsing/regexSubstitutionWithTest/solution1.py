# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys, re


def reSubFunc(inputStr: str) -> str:
    # print(f"inputStr Here: {inputStr}")
    patternAnd = r"(?<=[ ])[&]{2,2}(?=[ ])"
    patternOr = r"(?<=[ ])[|]{2,2}(?=[ ])"
    listTosend = inputStr
    if re.search(patternAnd, inputStr):
        # print("Coming TO and")
        listTosend = re.sub(patternAnd, "and", listTosend)

    if re.search(patternOr, inputStr):
        # print("Coming TO Or")
        listTosend = re.sub(patternOr, "or", listTosend)

    return listTosend


if __name__ == "__main__":
    noOfLines = int(sys.stdin.readline())
    for itr in range(noOfLines):
        print(reSubFunc(sys.stdin.readline().rstrip()))
