# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from collections import OrderedDict

input_data = sys.stdin.read().split()

wordsCountDict = OrderedDict()


for words in input_data[1:]:
    if words in wordsCountDict.keys():
        wordsCountDict[words] += 1
    else:
        wordsCountDict.update({words : 1})

# print(wordsCountDict.keys())
        
print(len(wordsCountDict))
print(*wordsCountDict.values())
