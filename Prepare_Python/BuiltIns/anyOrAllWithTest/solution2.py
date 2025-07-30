# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = input()
intergers = input().split()
print(all(int(i) > 0 for i in intergers) and any(i == i[::-1] for i in intergers))
