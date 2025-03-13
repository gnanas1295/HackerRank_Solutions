# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import calendar

# print(calendar.TextCalendar(firstweekday=5).formatyear(2016))
temp = list(map(int, sys.stdin.read().split()))
# print(temp)
day_number = calendar.weekday(temp[2],temp[0],temp[1])
print(calendar.day_name[day_number].upper())