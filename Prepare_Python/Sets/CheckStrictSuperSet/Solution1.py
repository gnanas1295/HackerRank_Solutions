# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

setAElements = set(map(int, sys.stdin.readline().split()))

noOFTestCase = int(sys.stdin.readline())

notFalse = False

for _ in range(noOFTestCase):
    setBElements = set(map(int, sys.stdin.readline().split()))
    # print(f"setA: {setAElements}, setb: {setBElements}")
    check = setAElements.issuperset(setBElements)
    # print(check)
    if not check:
        print(False)
        notFalse = True
        break
if not notFalse:
    print(True)
