import re
import sys


def find_css_hex_colors():
    """
    Reads N lines of CSS into a single block and prints all valid hex color codes
    found within CSS property values.
    """
    try:
        n = int(sys.stdin.readline())
    except (ValueError, IndexError):
        n = 0

    # Read all N lines of CSS into a single string to handle multi-line rules.
    css_code = sys.stdin.read()

    # The robust pattern:
    # (?<=[ :\(,]) -> Positive lookbehind for a character that marks a value.
    # # -> Literal hash.
    # (?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3}) -> 6 or 3 hex characters.
    # \b -> Word boundary to prevent partial matches (e.g., #bad from #badcfe).
    pattern = r"(?<=[ :\(,])#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b"

    # Find all matches in the entire block of CSS code.
    matches = re.findall(pattern, css_code)

    # Print each match on a new line.
    for color in matches:
        print(color)


if __name__ == "__main__":
    find_css_hex_colors()
