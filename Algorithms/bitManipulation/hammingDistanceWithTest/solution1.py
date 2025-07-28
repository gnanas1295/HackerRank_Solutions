# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Note: We are not packing and unpacking the lists everytime as its unnecessary and whenever we needed we are packing for printing purpose alone
# This solution is okay, however it doesn't run all the test cases as the time optimization isn't enough in this as we are using normal list slicing for the operation, for all the test cases to pass we need to use graph, deque or other algothirms concept which I will comeback later, this solution is with the knowledge that I currently possess


def change(stringList: list, startValue: int, endValue: int, replacementStr: str):

    rangeDiff = 1 if startValue == endValue else (endValue - startValue) + 1
    replacementList = list(replacementStr * rangeDiff)

    stringList[startValue : endValue + 1] = replacementList


def swap(
    stringList: list,
    firstStartValue: int,
    firstEndValue: int,
    secondStartValue: int,
    secondEndValue: int,
) -> list:
    firstPart = []
    secondPart = []
    thirdPart = []
    remainingPart = []
    middlePart = []
    # print(stringList)
    firstPart = stringList[0:firstStartValue]
    secondPart = stringList[firstStartValue : firstEndValue + 1]
    thirdPart = stringList[secondStartValue : secondEndValue + 1]

    if firstEndValue + 1 != secondStartValue:
        middlePart = stringList[firstEndValue + 1 : secondStartValue]
    if (len(stringList) - 1) > secondEndValue:
        remainingPart = stringList[secondEndValue + 1 : len(stringList)]

    # returningString = ''.join(firstPart) + ''.join(thirdPart) +''.join(middlePart)+ ''.join(secondPart) + ''.join(remainingPart)
    stringList = firstPart + thirdPart + middlePart + secondPart + remainingPart
    return stringList


def reversing(stringList: list, firstValue: int, endValue: int):
    reversePart = []
    reversePart = stringList[firstValue : endValue + 1]
    reversePart.reverse()
    stringList[firstValue : endValue + 1] = reversePart

    # return stringList


def outPutting(stringList: list, startValue: int, endValue: int) -> None:
    print(f"{''.join(stringList[startValue:endValue])}")
    # print(stringList[startValue:endValue])


def hamming(stringList: list, firstValue: int, endValue: int, length: int) -> None:
    firstPart = []
    secondPart = []

    startEndlength = (
        firstValue + length
        if firstValue + length < len(stringList)
        else len(stringList)
    )
    endEndlength = (
        endValue + length if endValue + length < len(stringList) else len(stringList)
    )

    count = 0

    firstPart = stringList[firstValue:startEndlength]
    secondPart = stringList[endValue:endEndlength]

    for i, j in zip(firstPart, secondPart):
        count += 1 if i != j else 0

    print(count)


if __name__ == "__main__":
    _ = sys.stdin.readline()

    stringTobeWorked = list(sys.stdin.readline().strip())
    noOfTestCases = int(sys.stdin.readline().strip())
    # print(stringTobeWorked)

    for _ in range(noOfTestCases):
        query = sys.stdin.readline().strip()
        if "C" in query:
            query = query.split()
            change(stringTobeWorked, int(query[1]) - 1, int(query[2]) - 1, query[3])
            # stringTobeWorked = change(stringTobeWorked, int(query[1])-1,int(query[2])-1, query[3])

        elif "S" in query:
            query = query.split()
            # swap(stringTobeWorked, int(query[1])-1, int(query[2])-1, int(query[3])-1, int(query[4])-1)
            stringTobeWorked = swap(
                stringTobeWorked,
                int(query[1]) - 1,
                int(query[2]) - 1,
                int(query[3]) - 1,
                int(query[4]) - 1,
            )

        elif "R" in query:
            query = query.split()
            reversing(stringTobeWorked, int(query[1]) - 1, int(query[2]) - 1)
            # stringTobeWorked = reversing(stringTobeWorked, int(query[1])-1, int(query[2])-1)

        elif "W" in query:
            query = query.split()
            outPutting(stringTobeWorked, int(query[1]) - 1, int(query[2]))

        elif "H" in query:
            query = query.split()
            hamming(
                stringTobeWorked, int(query[1]) - 1, int(query[2]) - 1, int(query[3])
            )
