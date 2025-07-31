import re
import sys


def is_valid_credit_card(card_number: str) -> bool:
    """
    Validates a credit card number against a set of rules.
    Returns True if valid, False otherwise.
    """
    # Rule 1, 2, 3, 4, 5: Check the overall format.
    # Must start with 4, 5, or 6 and have a valid structure.
    format_pattern = r"^[456](?:\d{15}|\d{3}(?:-\d{4}){3})$"
    if not re.match(format_pattern, card_number):
        return False

    # Rule 6: Check for 4 or more consecutive repeated digits.
    # First, remove hyphens to check digits contiguously.
    card_without_hyphens = card_number.replace("-", "")

    # The pattern (\d)\1{3} finds a digit followed by itself 3 times.
    repeat_pattern = r"(\d)\1{3}"
    if re.search(repeat_pattern, card_without_hyphens):
        return False  # Invalid if the "bad" pattern is found.

    # If all checks pass, the card is valid.
    return True


# Main script execution
if __name__ == "__main__":
    num_cards = int(sys.stdin.readline())
    for _ in range(num_cards):
        card_input = sys.stdin.readline().strip()
        if is_valid_credit_card(card_input):
            print("Valid")
        else:
            print("Invalid")
