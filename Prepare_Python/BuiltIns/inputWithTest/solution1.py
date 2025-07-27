# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys


def functionExection(func: str, k: int) -> None:

    return f"{True if eval(func) == k else False}"


if __name__ == "__main__":
    x, k = map(int, sys.stdin.readline().split())

    polyFunc = sys.stdin.readline()

    updatedPolyFunc = polyFunc.replace("x", str(x))

    print(functionExection(updatedPolyFunc, k))
