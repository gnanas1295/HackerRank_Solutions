import re
import sys
import email.utils


def validate_and_print_emails():
    """
    Reads N email entries, validates them using regex, and prints the valid ones.
    """
    # This pattern validates the email address part ONLY.
    # \w is a shorthand for [a-zA-Z0-9_].
    email_pattern = re.compile(r"^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$")

    try:
        n = int(sys.stdin.readline())
    except (ValueError, IndexError):
        n = 0

    for _ in range(n):
        # Read the full line, e.g., "DEXTER <dexter@hotmail.com>"
        full_line = sys.stdin.readline().strip()

        # Use parseaddr to robustly separate the name and address
        name, addr = email.utils.parseaddr(full_line)

        # Use the compiled regex to validate the address part
        if email_pattern.fullmatch(addr):
            # If valid, print the original formatted line
            print(full_line)


if __name__ == "__main__":
    validate_and_print_emails()
