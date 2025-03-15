import sys

data = sys.stdin.read().splitlines()

no_of_people, idx = int(data[0]), data[1].split().index("MARKS")

s = 0

for line in data[2:]:
    temp_line = line.split()
    s += int(temp_line[idx])

print(f"{(s / no_of_people):.2f}")