#!/bin/python3

import sys

input_data = sys.stdin.read().splitlines()
t = int(input_data[0])
line_index = 1

for _ in range(t):
    n = int(input_data[line_index])
    line_index += 1
    cubes = list(map(int, input_data[line_index].split()))
    line_index += 1

    left, right = 0, n - 1
    current = float('inf')
    possible = True

    while left <= right:
        # Determine which end has the larger cube that is valid
        if cubes[left] >= cubes[right]:
            candidate = cubes[left]
            if candidate <= current:
                current = candidate
                left += 1
            else:
                possible = False
                break
        else:
            candidate = cubes[right]
            if candidate <= current:
                current = candidate
                right -= 1
            else:
                possible = False
                break

    print("Yes" if possible else "No")

