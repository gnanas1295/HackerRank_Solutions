# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import itertools

input_data = sys.stdin.read().split()

combinations = []
char = []
for i in input_data[0]:
    char.append(i)
    
# print(char)

for idx in range(1, (int(input_data[1])+1)):
    combinations.append(list(itertools.combinations(sorted(char), idx)))
    
final_list = []
for list_Elements in combinations:
    # print(list_Elements)
    for ele in list_Elements:
        print(''.join(ele))