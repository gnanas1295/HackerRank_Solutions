# Enter your code here. Read input from STDIN. Print output to STDOUT


sizeOfGroup = int(input())
roomNumbers = input().split()

uniqueRoomNumbers = set(map(int, roomNumbers))

sumUniqueRoomNumbers = sum(uniqueRoomNumbers)

sumRoomNumbers = sum(map(int, roomNumbers))

captainRoomNumber = ((sumUniqueRoomNumbers * sizeOfGroup) - sumRoomNumbers) // (
    sizeOfGroup - 1
)

print(captainRoomNumber)
