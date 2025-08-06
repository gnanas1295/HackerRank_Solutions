# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys, re


def vowelFind(inputStr: str) -> list | int:
    # print(inputStr)
    # pattern = r"(?<=\w)([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])"
    vowels = "aeiouAEIOU"
    consonants = "QWRTYPSDFGHJKLZXCVBNM"
    pattern = rf"(?<=[{consonants.lower()}{consonants}])([{vowels}]{{2,}})(?=[{consonants.lower()}{consonants}])"
    matching = re.findall(pattern, inputStr)
    return matching if matching else -1


if __name__ == "__main__":
    finds = vowelFind(sys.stdin.readline().rstrip())
    print("\n".join(finds) if finds != -1 else "-1")
