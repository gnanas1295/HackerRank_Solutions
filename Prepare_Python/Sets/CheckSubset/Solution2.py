import sys

numTestCases = int(sys.stdin.readline())

for _ in range(numTestCases):
    _ = sys.stdin.readline()
    setAElements = set(map(int, sys.stdin.readline().split()))

    _ = sys.stdin.readline()
    setBElements = set(map(int, sys.stdin.readline().split()))

    print(setAElements.issubset(setBElements))
