import re
import sys


def find_first_repeated_char(s: str):
    """
    Finds the first occurrence of a consecutively repeated alphanumeric character.
    Uses re.search() for efficiency as it stops after the first find.
    """
    # This pattern looks for:
    # ([a-zA-Z0-9]) -> Group 1: any single alphanumeric character.
    # \1             -> a backreference to whatever was matched in Group 1.
    match = re.search(r"([a-zA-Z0-9])\1", s)

    # If a match object exists, return the content of the first captured group.
    # The character we want is in group 1.
    # Otherwise, return -1.
    return match.group(1) if match else -1


if __name__ == "__main__":
    # Read the input string and strip whitespace
    input_str = sys.stdin.readline().strip()
    # Call the function and print the result
    print(find_first_repeated_char(input_str))
