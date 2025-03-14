# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

input_list = sys.stdin.read().splitlines()
# print(input_list)

try:
    for i in range(1, (int(input_list[0])+ 1)):
        try: 
            # print(input_list[i])
            input1, input2 = map(int, input_list[i].split(" "))
            # input1, input2 = input_list[i].split(" ")
            print(input1//input2)
        except Exception as E:
            print("Error Code:", E)
except Exception as E:
    print("Error Code:", E)
