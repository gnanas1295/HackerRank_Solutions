import numpy, sys


def polyValue(inputCoefficients, xValue):
    return numpy.polyval(inputCoefficients, xValue)


if __name__ == "__main__":
    inputCoefficients = list(map(float, sys.stdin.readline().split()))
    xValue = int(sys.stdin.readline().strip())
    print(polyValue(inputCoefficients, xValue))
