# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from itertools import product

numItr, ModuloValue = map(int, sys.stdin.readline().split())

inputLists = [(list(map(int, sys.stdin.readline().split()))[1:]) for _ in range(numItr)]

combinationLists = product(*inputLists)

maxValue = max((sum(j * j for j in i) % ModuloValue) for i in combinationLists)

print(maxValue)
