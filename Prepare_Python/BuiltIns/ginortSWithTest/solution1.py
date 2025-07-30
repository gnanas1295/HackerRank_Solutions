# Enter your code here. Read input from STDIN. Print output to STDOUT


def strToSort(tempStr: str) -> str:
    # print(sorted(tempStr))
    lowerCase = []
    upperCase = []
    oddDigits = []
    evenDigits = []
    for i in tempStr:
        if i.islower():
            lowerCase.append(i)
        elif i.isupper():
            upperCase.append(i)
        elif (int(i) % 2) == 0:
            evenDigits.append(i)
        else:
            oddDigits.append(i)
    return f"{''.join(sorted(lowerCase))+ ''.join(sorted(upperCase))+ ''.join(sorted(oddDigits))+ ''.join(sorted(evenDigits))}"


if __name__ == "__main__":
    stringToSort = input()
    print(strToSort(stringToSort))
