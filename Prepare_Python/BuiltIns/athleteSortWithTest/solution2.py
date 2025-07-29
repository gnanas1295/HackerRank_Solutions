#!/bin/python3

import sys


def sort_and_print_table(table, k):
    """
    Sorts a 2D table based on the k-th column and prints the result.

    Args:
        table (list): A list of lists representing the table.
        k (int): The zero-indexed column to sort by.
    """
    # Python's sorted() is a stable sort, which preserves the original
    # order of elements that have equal keys.
    # A lambda function provides the key for sorting.
    sorted_table = sorted(table, key=lambda row: row[k])

    for row in sorted_table:
        # The splat (*) operator unpacks the row list into individual arguments
        # for print(), which separates them with spaces by default.
        print(*row)


if __name__ == "__main__":
    # Read n (rows) and m (columns)
    n, m = map(int, sys.stdin.readline().split())

    # Read the table into a list of lists
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # Read the sort key index
    k = int(sys.stdin.readline())

    sort_and_print_table(table, k)
