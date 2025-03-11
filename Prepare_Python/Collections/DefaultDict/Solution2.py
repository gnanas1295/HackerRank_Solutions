import sys
from collections import defaultdict

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])

# Using slicing to separate group A and group B words
groupA = data[2:2 + n]
groupB = data[2 + n:2 + n + m]

# Build a mapping from each word in group A to its 1-indexed positions
word_positions = defaultdict(list)
for idx, word in enumerate(groupA, start=1):
    word_positions[word].append(idx)

# For each word in group B, print its positions or -1 if not found
for word in groupB:
    if word in word_positions:
        print(*word_positions[word])
    else:
        print("-1")