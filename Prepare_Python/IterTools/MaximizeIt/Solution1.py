# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from itertools import product
from math import sumprod

numItr, ModuloValue = map(int, sys.stdin.readline().split())


availableLists = []
for _ in range(numItr):
    tempList = list(map(int, sys.stdin.readline().split()))
    tempList.pop(0)
    availableLists.append(tempList)

maxValue = 0
allCombinationLists = product(*availableLists)

for i in allCombinationLists:
    tempSum = 0
    # print(i)
    for j in i:
        # print(j)
        tempSum += pow(j, 2)
    tempMaxValue = tempSum % ModuloValue
    if maxValue < tempMaxValue:
        maxValue = tempMaxValue

print(maxValue)
# output: 974
