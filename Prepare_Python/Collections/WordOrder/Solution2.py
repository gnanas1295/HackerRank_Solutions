import sys

input_data = sys.stdin.read().split()
# Optionally, use a normal dict if you're on Python 3.7+
wordsCountDict = {}

for word in input_data[1:]:
    wordsCountDict[word] = wordsCountDict.get(word, 0) + 1

print(len(wordsCountDict))
print(*wordsCountDict.values())