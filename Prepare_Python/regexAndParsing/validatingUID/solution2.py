# import sys


# def validate_uid(uid):
#     """
#     Checks if a UID is valid based on 5 specific rules.
#     Returns 'Valid' or 'Invalid'.
#     """
#     # Combine length and uniqueness check
#     rule_unique_and_length = len(set(uid)) == 10

#     # Check for alphanumeric characters
#     rule_alnum = uid.isalnum()

#     # Here, having even two for loops doesn't small up the process because we know the input is max of 10 char
#     # Use sum() with generator expressions for concise counting
#     rule_uppercase = sum(1 for char in uid if char.isupper()) >= 2
#     rule_digits = sum(1 for char in uid if char.isdigit()) >= 3

#     # A UID is valid if ALL rules are true
#     if all([rule_unique_and_length, rule_alnum, rule_uppercase, rule_digits]):
#         return "Valid"
#     else:
#         return "Invalid"


# # Main execution block
# num_test_cases = int(sys.stdin.readline())
# for _ in range(num_test_cases):
#     uid_input = sys.stdin.readline().strip()
#     print(validate_uid(uid_input))

import sys, re


def validate_uid(uid) -> str:

    if len(set(uid)) != 10:
        return "Invalid"

    pattern = r"^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$"

    if re.match(pattern, uid):
        return "Valid"
    else:
        return "Invalid"


num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    uid_input = sys.stdin.readline().strip()
    print(validate_uid(uid_input))
