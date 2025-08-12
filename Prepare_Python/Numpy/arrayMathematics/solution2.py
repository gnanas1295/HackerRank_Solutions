import numpy
import sys


def perform_array_operations():
    """
    Reads two NxM arrays and prints the results of 6 arithmetic operations.
    """
    try:
        n, m = map(int, sys.stdin.readline().split())
    except (ValueError, IndexError):
        # Handle case with no input
        return

    # Use a more concise list comprehension to read the array data
    list_a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    list_b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # Convert the Python lists to NumPy arrays
    a = numpy.array(list_a)
    b = numpy.array(list_b)

    # Use the overloaded arithmetic operators for better readability
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a**b)


if __name__ == "__main__":
    perform_array_operations()
