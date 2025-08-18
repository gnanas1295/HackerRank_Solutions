import numpy
import sys


def meanVarStd(inputArrayList: list) -> list:
    returnList = []

    returnList.append(numpy.mean(inputArrayList, axis=1))
    returnList.append(numpy.var(inputArrayList, axis=0))
    returnList.append(round(numpy.std(inputArrayList), 11))

    return returnList


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    inputArrayList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    print(*(x for x in meanVarStd(inputArrayList)), sep="\n")
