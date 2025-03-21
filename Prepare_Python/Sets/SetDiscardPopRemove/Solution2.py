import sys

data = sys.stdin.read().splitlines()
n = int(data[0])
s = set(map(int, data[1].split()))
num_commands = int(data[2])
for command in data[3:]:
    parts = command.split()
    if parts[0] == "pop":
        s.remove(min(s))
    elif parts[0] == "remove":
        try:
            s.remove(int(parts[1]))
        except Exception as E:
            continue
    elif parts[0] == "discard":
        s.discard(int(parts[1]))
print(sum(s))