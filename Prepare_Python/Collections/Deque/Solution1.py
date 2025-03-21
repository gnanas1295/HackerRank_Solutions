# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from collections import deque

input_data = sys.stdin.read().splitlines()

final_deque = deque()

for lines in input_data[1:]:
    # print(lines)
    action, *values = lines.split()
    value = values[0] if values else 0
    if action == "append":
        final_deque.append(int(value))
    elif action == "pop":
        final_deque.pop()
    elif action == "popleft":
        final_deque.popleft()
    else:
        final_deque.appendleft(int(value))

print(*final_deque)