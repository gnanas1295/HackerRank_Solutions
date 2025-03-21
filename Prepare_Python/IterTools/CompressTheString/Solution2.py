import sys
from itertools import groupby

input_data = sys.stdin.read().strip()
uniqueKeys = 0
groups = 0
finalList = []

for k, g in groupby(input_data):
    # print(f"{*a}:{*b}")
    # print(k)
    finalList.append(f"({len(list(g))}, {k})")

print(" ".join(finalList))