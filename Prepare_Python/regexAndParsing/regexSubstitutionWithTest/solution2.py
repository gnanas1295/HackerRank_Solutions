import sys
import re


def replacer_func(match):
    """Returns the correct replacement based on the matched operator."""
    if match.group(0) == "&&":
        return "and"
    else:  # It must be '||'
        return "or"


def replace_operators_single_pass(line):
    # This single pattern finds EITHER '&&' OR '||' surrounded by spaces.
    pattern = r"(?<=\s)(?:&&|\|\|)(?=\s)"
    # re.sub calls our function for each match it finds.
    return re.sub(pattern, replacer_func, line)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for _ in range(n):
        print(replace_operators_single_pass(sys.stdin.readline().rstrip()))
