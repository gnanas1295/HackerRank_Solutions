# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys, re


def vowelFind(inputStr: str) -> list | int:
    # print(inputStr)
    pattern = r"(?<=\w)([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])"
    matching = re.findall(pattern, inputStr)
    return matching if matching else -1


if __name__ == "__main__":
    finds = vowelFind(sys.stdin.readline().rstrip())
    if finds != -1:
        for item in finds:
            print(item)
    else:
        print("-1")
