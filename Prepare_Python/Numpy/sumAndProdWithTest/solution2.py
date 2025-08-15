import numpy
import sys


def sumAndProdNumPY(arrayList: list) -> int:
    numpyArraySum = numpy.sum(numpy.array(arrayList), axis=0)
    return numpy.prod(numpyArraySum, axis=None)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    arrayList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    print(sumAndProdNumPY(arrayList))
