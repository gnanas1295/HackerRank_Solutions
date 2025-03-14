import sys
import re 

# print(sys.stdin.read())
input_list = sys.stdin.read().splitlines()
# print(input_list)

for idx in range(1, (int(input_list[0])+1)):
    # print(input_list[idx])
    try:
        validation = re.compile(input_list[idx])
        print("True")
    except Exception as e:
        print("False")