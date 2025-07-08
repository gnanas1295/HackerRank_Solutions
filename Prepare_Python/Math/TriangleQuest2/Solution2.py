# # Enter your code here. Read input from STDIN. Print output to STDOUT
# palindromeTrainagleInput = int(input())

# for iteration in range(1, (1+palindromeTrainagleInput)):
#     temp = []
#     for internalItreation in range(1, (1+iteration)):
#         temp.append(internalItreation)
#         if internalItreation == iteration:
#             for internalIteration1 in range(iteration-1 ,0, -1):
#                 temp.append(internalIteration1)
#     print(*temp, sep="")

for i in range(1, int(input()) + 1): print(int('1' * i) ** 2)