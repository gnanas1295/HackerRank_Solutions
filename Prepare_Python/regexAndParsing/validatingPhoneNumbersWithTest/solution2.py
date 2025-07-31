import re
import sys


def validate_mobile_numbers():
    """
    Reads N lines of input and validates if they are 10-digit mobile numbers
    starting with 7, 8, or 9.
    """
    # Compile the regex pattern once for better performance on multiple inputs.
    # ^ asserts position at start of the string.
    # [789] matches the first digit.
    # \d{9} matches the next nine digits.
    # $ asserts position at the end of the string.
    pattern = re.compile(r"^[789]\d{9}$")

    try:
        n = int(sys.stdin.readline())
    except (ValueError, IndexError):
        n = 0

    for _ in range(n):
        number_str = sys.stdin.readline().strip()
        # Use fullmatch to ensure the entire string conforms to the pattern.
        if pattern.fullmatch(number_str):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    validate_mobile_numbers()
