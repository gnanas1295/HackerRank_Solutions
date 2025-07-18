# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

inputLines = sys.stdin.read().splitlines()

aSet = set(map(int, inputLines[1].split()))

numOperations = int(inputLines[2])

operations = {
    "intersection_update": set.intersection_update,
    "update": set.update,
    "symmetric_difference_update": set.symmetric_difference_update,
    "difference_update": set.difference_update,
}

currentIndex = 2
for _ in range(numOperations):
    currentIndex += 1
    methodType, _ = inputLines[currentIndex].split()

    currentIndex += 1
    setValues = set(map(int, inputLines[currentIndex].split()))

    operations[methodType](aSet, setValues)

print(sum(aSet))
