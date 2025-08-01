# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils, sys, re


def emailValidation(emailDetails: str) -> str:
    emailDetailsSplitted = emailDetails.split()
    print(emailDetailsSplitted)
    pattern = re.compile(r"^<[a-z][a-zA-Z0-9_.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}+>$")
    if pattern.match(emailDetailsSplitted[-1]):
        parsedEmail = email.utils.parseaddr(emailDetails)
        return email.utils.formataddr(parsedEmail)


if __name__ == "__main__":
    emailCount = int(sys.stdin.readline())

    for _ in range(emailCount):
        emailDetails = sys.stdin.readline()
        value = emailValidation(emailDetails)
        if value:
            print(value)
        else:
            continue
