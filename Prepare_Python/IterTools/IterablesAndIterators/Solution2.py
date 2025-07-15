from itertools import combinations


numberOfChar = int(input())
inputString = input().split()
threshold = int(input())

# print(numberOfChar, inputString, threshold)

indexsWithA = {i for i, char in enumerate(inputString) if char == "a"}

totalCombinations = list(combinations(range(numberOfChar), int(threshold)))
totalCountCombinations = len(totalCombinations)

# print(indexsWithA)
# print(totalCombinations)

counter = 0
for tupleToCheck in totalCombinations:
    if not indexsWithA.isdisjoint(tupleToCheck):
        counter += 1

print(f"{counter/totalCountCombinations:.4f}")
