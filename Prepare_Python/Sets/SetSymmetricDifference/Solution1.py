# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = input()
engNewsList = set(input().split())
_ = input()
frenchNewsList = set(input().split())

print(len(frenchNewsList.symmetric_difference(engNewsList)))
