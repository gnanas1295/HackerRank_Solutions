# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = input()
engNewsList = set(input().split())
_ = input()
frnchNewsList = set(input().split())


print(len(engNewsList.difference(frnchNewsList)))
