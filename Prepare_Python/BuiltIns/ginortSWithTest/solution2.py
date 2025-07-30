def get_sort_key(char):
    """
    Returns a tuple that defines the sorting priority for a character.
    Python sorts tuples element-by-element, so (0, 'a') comes before (1, 'A').
    Priority: lowercase < uppercase < odd digits < even digits
    """
    if char.islower():
        return (0, char)
    if char.isupper():
        return (1, char)
    if char.isdigit():
        if int(char) % 2 != 0:  # Odd digit
            return (2, char)
        else:  # Even digit
            return (3, char)


# --- Main execution ---
input_string = input()

# Use sorted() with the custom key function and join the result.
sortedString = "".join(sorted(input_string, key=get_sort_key))

print(sortedString)
