# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys, re


def validCreditCardCheck(cardDetail: str) -> None:
    pattern = r"^[456](?:\d{15}|\d{3}(?:-\d{4}){3})$"
    if not (re.match(pattern, cardDetail)):
        print("Invalid")
        return
    newCard = cardDetail.replace("-", "")
    pattern1 = r"(\d)\1{3}"
    if not (re.search(pattern1, newCard)):
        print("Valid")
    else:
        print("Invalid")


noOfCards = int(sys.stdin.readline())
for _ in range(noOfCards):
    validCreditCardCheck(sys.stdin.readline().strip())
