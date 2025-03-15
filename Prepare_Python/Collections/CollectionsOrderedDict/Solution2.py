import sys
from collections import OrderedDict

input_list = sys.stdin.read().splitlines()
itemDetails = OrderedDict()

for line in input_list[1:]:
    # print(line.split())
    itemName, value = line.rsplit(" ", 1)
    itemDetails[itemName] = itemDetails.get(itemName, 0) + int(value)
    # print(itemDetails)
    
for item, value in itemDetails.items():
    print(item, value)