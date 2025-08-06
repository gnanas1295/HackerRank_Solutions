import re
import sys


def find_all_indices(main_string: str, sub_string: str) -> list[tuple[int, int]]:
    """
    Finds all overlapping occurrences of a substring.
    Returns a list of (start, end) tuples.
    """
    # Use re.escape() for safety, in case the substring has special regex chars.
    pattern = re.compile(rf"(?=({re.escape(sub_string)}))")

    # A list comprehension is a very Pythonic way to build the list.
    # It directly returns the list of tuples, which is cleaner.
    return [
        (match.start(1), match.end(1) - 1) for match in pattern.finditer(main_string)
    ]


if __name__ == "__main__":
    s, k = sys.stdin.read().strip().split()

    # 1. Get the list of results from the function.
    matches = find_all_indices(s, k)

    # 2. The main block handles all the printing logic.
    if not matches:
        print("(-1, -1)")
    else:
        for match_tuple in matches:
            print(match_tuple)
