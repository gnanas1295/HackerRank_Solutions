# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

input_intergers_list = list(map(int, sys.stdin.read().split()))

print(input_intergers_list[0] ** input_intergers_list[1])
print(pow(input_intergers_list[0], input_intergers_list[1], input_intergers_list[2]))
