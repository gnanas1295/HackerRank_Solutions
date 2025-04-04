import sys
from itertools import combinations_with_replacement

input_string, seperator_value = sys.stdin.read().split()

input_list = sorted(input_string)

final_list = combinations_with_replacement(input_list, int(seperator_value))

for lines in final_list:
    print(''.join(list(lines)))