# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

input_numbers = list(map(int, sys.stdin.read().splitlines()))

print(input_numbers[0] // input_numbers[1])
print(input_numbers[0]%input_numbers[1])
div = divmod(input_numbers[0],input_numbers[1])
print(div)

# Note: Since for this only there are two inputs, we can directly use the input() function, instead of accessing through read() which is best if there are many inputs