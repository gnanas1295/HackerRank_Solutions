import numpy
import sys


def calculate_stats(arr):
    """
    Calculates the mean (axis=1), var (axis=0), and std (axis=None)
    of a NumPy array.
    """
    # The problem requires specific print options for formatting.
    # While not included in your code, it's often needed for these challenges.
    # numpy.set_printoptions(legacy='1.13')

    # It's slightly cleaner to return the list directly.
    return [numpy.mean(arr, axis=1), numpy.var(arr, axis=0), numpy.std(arr, axis=None)]


if __name__ == "__main__":
    try:
        n, m = map(int, sys.stdin.readline().split())

        # Read input directly into a NumPy array for efficiency
        my_array = numpy.array([sys.stdin.readline().split() for _ in range(n)], int)

        results = calculate_stats(my_array)

        # Print each result on a new line
        for res in results:
            print(res)

    except (ValueError, IndexError):
        # Handle empty input
        pass
