import sys
from collections import deque

input_data = sys.stdin.read().splitlines()

final_deque = deque()

actions_without_argument= {
    "pop" : final_deque.pop,
    "popleft" : final_deque.popleft
}

action_with_argument= {
    "append" : final_deque.append,
    "appendleft" : final_deque.appendleft
}

for lines in input_data[1:]:
    
    parts = lines.split()
    if parts[0] in action_with_argument:
        action_with_argument[parts[0]](parts[1])
    elif parts[0] in actions_without_argument:
        actions_without_argument[parts[0]]()
        
print(*final_deque)
