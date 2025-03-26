# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys


input_data = sys.stdin.read().splitlines()

english_Sub_Students = set(input_data[1].split())

french_Sub_Students = set(input_data[3].split())

# print(english_Sub_Students)
# print(french_Sub_Students)

print(len(english_Sub_Students.union(french_Sub_Students)))