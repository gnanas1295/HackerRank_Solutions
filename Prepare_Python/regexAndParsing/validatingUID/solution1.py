import sys, re

noOfTestCases = int(sys.stdin.readline())

# print(noOfTestCases)
for i in range(noOfTestCases):
    valueTobeChecked = sys.stdin.readline().strip()
    if len(set(valueTobeChecked)) != 10:
        print("Invalid")
        continue
    elif not valueTobeChecked.isalnum():
        print("Invalid")
        continue
    upperCaseCounter = 0
    digitsCounter = 0
    for i in valueTobeChecked:
        if i.isupper():
            upperCaseCounter += 1
        if i.isdigit():
            digitsCounter += 1
        if upperCaseCounter >= 2 and digitsCounter >= 3:
            break
    if not (upperCaseCounter >= 2 and digitsCounter >= 3):
        print("Invalid")
    else:
        print("Valid")
