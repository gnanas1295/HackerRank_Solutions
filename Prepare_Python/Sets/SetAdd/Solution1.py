# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

input_data = sys.stdin.read().splitlines()

# print(input_data)

distinct_values = list(set(input_data))
# print(distinct_values)

count = 0
for elements in distinct_values[1:]:
    count += 1
print(count)
