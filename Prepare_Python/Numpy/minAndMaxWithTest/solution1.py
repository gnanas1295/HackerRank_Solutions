import numpy
import sys


def minAndMaxNumPY(arrayList: list) -> int:

    return max(numpy.min(arrayList, axis=1))


if __name__ == "__main__":

    n, _ = map(int, sys.stdin.readline().split())

    arrayList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    print(minAndMaxNumPY(arrayList))
