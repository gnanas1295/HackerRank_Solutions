import sys
import datetime

temp = list(sys.stdin.read().splitlines())

timedetails = []
i = 1

for a in range(int(temp[0])):
    time1 = temp[i]
    time2 = temp[i + 1]
    gmtTime1 = datetime.datetime.strptime(time1, '%a %d %b %Y %H:%M:%S %z')
    gmtTime2 = datetime.datetime.strptime(time2, '%a %d %b %Y %H:%M:%S %z')
    print(abs(int((gmtTime1 - gmtTime2).total_seconds())))
    i += 2