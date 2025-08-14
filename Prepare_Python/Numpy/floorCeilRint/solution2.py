import numpy
import sys


def print_rounding_operations():
    """
    Reads a 1-D array and prints its floor, ceil, and rint values.
    """
    # Read the line of space-separated floats
    input_list = list(map(float, sys.stdin.readline().split()))

    # Set the print option required by the challenge for backward compatibility
    numpy.set_printoptions(legacy="1.13")

    # Convert the list to a NumPy array
    my_array = numpy.array(input_list)

    print(f"{numpy.floor(my_array)}\n{numpy.ceil(my_array)}\n{numpy.rint(my_array)}")


if __name__ == "__main__":
    print_rounding_operations()
