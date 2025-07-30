# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


def allChecks(integers: list) -> bool:
    checks = all([1 if i > 0 else 0 for i in integers])
    if checks:
        expectedList = [11, 22, 33, 44, 55, 66, 77, 88, 99]
        return any(
            i if ((i > 0 and i < 10) or (i in expectedList)) else 0 for i in integers
        )
    else:
        return "False"


if __name__ == "__main__":
    _ = sys.stdin.readline()
    integers = list(map(int, sys.stdin.read().split()))
    print(allChecks(integers))
