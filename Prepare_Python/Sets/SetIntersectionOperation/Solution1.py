# Enter your code here. Read input from STDIN. Print output to STDOUT

engNewsCount = input()
engNewsList = set(input().split())
frenchNewsCount = input()
frenchNewsList = set(input().split())

# print(engNewsList)
# print(frenchNewsList)

print(len(list(engNewsList.intersection(frenchNewsList))))
