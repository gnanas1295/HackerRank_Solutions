# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

input_data = sys.stdin.read().splitlines()

count_ele, list_ele, count_comm = int(input_data[0]) , input_data[1].split(), int(input_data[2])

list_ele_set = set(sorted(list(map(int, list_ele))))
# print(list_ele_set)


for lines in input_data[3:]:
    # print(list_ele_set)
    # print(lines)
    if lines.count("pop"):
        # print("coming here")
        # list_ele_set.pop()
        list_ele_set.remove(min(list_ele_set))
    else:
        temp1, temp2 = lines.split(" ")
        # print(temp1, temp2)
        # list_ele_set.temp1(int(temp2))
        if temp1.count("remove"):
            try:
                list_ele_set.remove(int(temp2))
            except Exception as e:
                # print(e)
                continue
        else:
            list_ele_set.discard(int(temp2))

print(sum(list(list_ele_set)))