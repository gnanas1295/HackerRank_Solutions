import sys
import numpy


def numpyTransactions(n, m):

    arrayA = []
    for i in range(n):
        arrayA.append(list(map(int, sys.stdin.readline().split())))

    arrayB = []
    for i in range(n):
        arrayB.append(list(map(int, sys.stdin.readline().split())))

    arrayA = numpy.array(arrayA)
    arrayB = numpy.array(arrayB)

    print(numpy.add(arrayA, arrayB))
    print(numpy.subtract(arrayA, arrayB))
    print(numpy.multiply(arrayA, arrayB))
    print(numpy.floor_divide(arrayA, arrayB))
    print(numpy.mod(arrayA, arrayB))
    print(numpy.power(arrayA, arrayB))


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    numpyTransactions(n, m)
