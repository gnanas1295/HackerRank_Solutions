# No 'import sys' needed for this approach if just using input()
a = int(input())
b = int(input())

print(a // b)
print(a % b)
print(divmod(a, b))