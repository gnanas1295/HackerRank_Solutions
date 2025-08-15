import numpy
import sys


def find_max_of_row_mins():
    """
    Reads a 2D array, finds the minimum of each row,
    and then finds the maximum of those minimums.
    """
    try:
        n, m = map(int, sys.stdin.readline().split())
    except (ValueError, IndexError):
        return

    # Read the input into a Python list of lists
    my_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # Convert to a NumPy array first
    my_array = numpy.array(my_list)

    # Chain the methods directly on the NumPy object for a concise solution.
    # 1. my_array.min(axis=1) -> finds the minimum of each row
    # 2. .max() -> finds the maximum of that resulting 1-D array
    result = my_array.min(axis=1).max()

    print(result)


if __name__ == "__main__":
    find_max_of_row_mins()
