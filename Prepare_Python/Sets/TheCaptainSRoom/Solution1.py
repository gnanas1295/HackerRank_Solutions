# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

sizeOfGroup = int(input())
roomNumbers = list(map(int, input().split()))

# print(Counter(roomNumbers))

for key, value in Counter(roomNumbers).items():
    if value == 1:
        print(key)
