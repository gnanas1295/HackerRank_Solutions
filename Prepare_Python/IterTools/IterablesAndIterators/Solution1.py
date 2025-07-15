import sys, itertools


inputCount, inputString, inputlength = sys.stdin.read().splitlines()


newString = inputString.replace(" ", "")

# print(newString)

extractedTuple = itertools.combinations(newString, int(inputlength))


count = 0
length = 0

for i in extractedTuple:
    length += 1
    if "a" in i:
        count += 1

print(count / length)
