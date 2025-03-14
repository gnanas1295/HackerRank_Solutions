import sys
import re

# Read all input lines
input_list = sys.stdin.read().splitlines()
t = int(input_list[0])

# Iterate over each test case (skipping the first line)
for pattern in input_list[1:]:
    try:
        re.compile(pattern)
        print("True")
    except re.error:
        print("False")
