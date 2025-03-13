import sys
import datetime

# Read all lines from input and split them
data = sys.stdin.read().splitlines()
n = int(data[0])

# Iterate over each test case (each test case has 2 lines)
for i in range(1, 2 * n, 2):
    timestamp1 = data[i]
    timestamp2 = data[i + 1]
    
    dt1 = datetime.datetime.strptime(timestamp1, '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.datetime.strptime(timestamp2, '%a %d %b %Y %H:%M:%S %z')
    
    # Calculate and print the absolute difference in seconds
    print(int(abs((dt1 - dt2).total_seconds())))
