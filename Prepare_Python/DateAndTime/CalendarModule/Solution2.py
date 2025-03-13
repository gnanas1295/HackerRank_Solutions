# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import calendar

day, month, year = map(int, sys.stdin.read().split()) # read the input
day_number = calendar.weekday(year, month, day) # get the day number
print(calendar.day_name[day_number].upper()) # print the day name in uppercase