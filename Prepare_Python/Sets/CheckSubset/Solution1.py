# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

inputList = sys.stdin.read().splitlines()

testCases = int(inputList[0])

if not testCases:
    print(False)
else:
    currentIndex = 0
    for _ in range(testCases):
        currentIndex += 1
        setACount = int(inputList[currentIndex])
        currentIndex += 1
        setAElements = set(map(int, inputList[currentIndex].split()))
        currentIndex += 1
        setBcount = int(inputList[currentIndex])
        currentIndex += 1
        setBElements = set(map(int, inputList[currentIndex].split()))
        # print(f"setAcount: {setACount}, setAElements: {setAElements}, setBcount: {setBcount}, setBElements: {setBElements}")

        if setACount > setBcount:
            # print("Coming Here")
            print(False)
            continue
        # print(setAElements.isdisjoint(setBElements))
        subSet = setAElements.intersection(setBElements)
        if len(subSet) == setACount:
            print(True)
        else:
            print(False)
