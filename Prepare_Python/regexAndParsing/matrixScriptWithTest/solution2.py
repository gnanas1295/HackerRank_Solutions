import re
import sys


def solve_matrix_script():
    """
    Reads a matrix, transposes it, and cleans the resulting string
    according to the problem's rules.
    """
    try:
        n, m = map(int, sys.stdin.readline().split())
        # Read all matrix rows, stripping any OS-specific line endings
        matrix = [sys.stdin.readline().rstrip("\r\n") for _ in range(n)]
    except (ValueError, IndexError):
        # Handle empty input case
        print("")
        return

    # 1. Transpose the matrix efficiently and join into a single string
    decoded_script = "".join("".join(col) for col in zip(*matrix))

    # 2. Use a robust regex to replace non-alphanumeric chunks
    #    that are between two alphanumeric characters.
    cleaned_script = re.sub(
        r"(?<=[a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])", " ", decoded_script
    )

    # 3. CRITICAL STEP: Remove any trailing whitespace that results from
    #    the matrix's padding columns.
    final_result = cleaned_script.rstrip()

    print(final_result)


if __name__ == "__main__":
    solve_matrix_script()
