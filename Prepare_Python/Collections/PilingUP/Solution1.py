# Enter your code here. Read input from STDIN. Print output to STDOUT'

import sys

input_data = sys.stdin.read().splitlines()

# print(input_data)

numberOfTestCases = int(input_data[0])

for idx in range(numberOfTestCases):
    numberOfCubes = int(input_data[((idx*2) + 1)])
    SidelengthOfCubes = list(map(int, list(input_data[((idx*2) + 2)].split())))
    # print(numberOfCubes)
    # print(SidelengthOfCubes)
    
    latest_value = 0
    left_most = 0
    right_most = 0
    for idx in range(numberOfCubes):
        left_most = SidelengthOfCubes[0]
        right_most = SidelengthOfCubes[-1]
        # print(left_most, right_most)
        if idx == 0:
            if left_most >= right_most:
                latest_value = left_most
                SidelengthOfCubes.pop(0)
            else:
                latest_value = right_most
                SidelengthOfCubes.pop(-1)
        else:
            if left_most >= right_most:
                # print(left_most)
                if latest_value >= left_most:
                    latest_value = left_most
                    SidelengthOfCubes.pop(0)
                else:
                    print("No")
                    break
            else:
                # print(right_most)
                if latest_value >= right_most:
                    latest_value = right_most
                    SidelengthOfCubes.pop(-1)
                else:
                    print("No")
                    break
    if len(SidelengthOfCubes) == 0:
        print("Yes")
