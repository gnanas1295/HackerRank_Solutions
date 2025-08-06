import re
import sys

# Compile the pattern once, outside the loop, for better performance.
FLOAT_PATTERN = re.compile(r"[+-]?(\d+\.\d+|\.\d+)")


def is_valid_float_regex(s: str) -> bool:
    """Checks if a string is a valid float using a compiled regex."""
    # re.fullmatch is designed to match the entire string.
    return bool(FLOAT_PATTERN.fullmatch(s))


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for _ in range(n):
        s = sys.stdin.readline().strip()
        print(is_valid_float_regex(s))
