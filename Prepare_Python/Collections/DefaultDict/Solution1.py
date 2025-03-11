# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from collections import defaultdict

temp_Input = sys.stdin.read().split()

groupA = int(temp_Input[0])
groupB = int(temp_Input[1])

list_groupA = []
list_groupB = []

defaultListA = defaultdict(list)

for i in range(2, (2 + groupA)):
    list_groupA.append(temp_Input[i])

unique_char_groupA = set(list_groupA)
# print(unique_char_groupA)

for i in unique_char_groupA:
    for j in range(0, len(list_groupA)):
        if i == list_groupA[j]:
            defaultListA[i].append(j + 1)

# print(defaultListA)

for i in range(2 + groupA, (2 + groupA + groupB)):
    list_groupB.append(temp_Input[i])
    
# print(list_groupA)
# print(list_groupB)

for i in list_groupB:
    if i in defaultListA:
        temp = map(str, defaultListA[i])
        # print(temp)
        print(*temp)
    else:
        print("-1")