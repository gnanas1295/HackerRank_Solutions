import sys, itertools

data = sys.stdin.read().split()
s, k = data[0], int(data[1])
for i in range(1, k + 1):
    for comb in itertools.combinations(sorted(s), i):
        print(''.join(comb))