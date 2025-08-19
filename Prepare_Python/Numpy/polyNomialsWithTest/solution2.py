import numpy
import sys

if __name__ == "__main__":
    # Read the coefficients as a list of floats from a single line
    coeffs = list(map(float, sys.stdin.readline().split()))

    # Read the integer value of x
    x_val = int(sys.stdin.readline())

    # Directly call numpy.polyval and print the result
    result = numpy.polyval(coeffs, x_val)

    print(result)
