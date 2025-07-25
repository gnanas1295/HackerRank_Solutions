# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

inputArray = sys.stdin.read().splitlines()

inputASet = set(inputArray[1].split())

# print(inputASet)
# print(int(inputArray[2]))

i = 0
for _ in range(int(inputArray[2])):
    mutationType, _ = inputArray[3 + i].split()
    # print(inputArray[3 + i + 1])
    mutationValue = set(inputArray[3 + i + 1].split())
    # print(f"mutationValue: {mutationValue}")

    if mutationType == "intersection_update":
        inputASet.intersection_update(mutationValue)
    if mutationType == "update":
        inputASet.update(mutationValue)
    if mutationType == "difference_update":
        inputASet.difference_update(mutationValue)
    if mutationType == "symmetric_difference_update":
        inputASet.symmetric_difference_update(mutationValue)

    i += 2

    # print(inputASet)

inputASetNumbers = map(int, inputASet)
# print(*inputASet)
# print(*inputASetNumbers)

print(sum(inputASetNumbers))
