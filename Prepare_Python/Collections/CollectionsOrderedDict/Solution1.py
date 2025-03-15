# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from collections import OrderedDict

input_list = sys.stdin.read().splitlines()

ordered_dictionary = OrderedDict()

for idx in range(1, (int(input_list[0])+1)):
    item, price = input_list[idx].rsplit(" ", 1)
    # print(item)
    # print(price)
    ordered_dictionary[item] = 0
    
for idx in range(1, (int(input_list[0])+1)):
    item, price = input_list[idx].rsplit(" ", 1)
    # print(item)
    # print(price)
    ordered_dictionary[item] += int(price)
    
# print(ordered_dictionary)

for key, value in ordered_dictionary.items():
    print(key, value)