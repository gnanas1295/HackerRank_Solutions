# This solution is for Python 2, as intended by the challenge.

# Read x and k from the first line.
# raw_input() is used in Python 2 for reading a line as a string.
x, k = map(int, raw_input().split())

# The input() function in Python 2 will read the next line (the polynomial)
# and automatically evaluate it as Python code. Since 'x' is already
# defined in the local scope, it will be used in the expression.
result = input()

# Print True or False based on the comparison.
print result == k