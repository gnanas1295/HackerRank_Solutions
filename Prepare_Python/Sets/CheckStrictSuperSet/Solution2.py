# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

setAElements = set(map(int, sys.stdin.readline().split()))

numOfTestCases = int(sys.stdin.readline())

result = all(
    setAElements.issuperset(set(map(int, sys.stdin.readline().split())))
    for _ in range(numOfTestCases)
)

print(result)
