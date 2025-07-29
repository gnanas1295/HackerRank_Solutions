import os


def getTotalX(a, b):
    """
    Determines the number of integers that are 'between' two arrays.
    """
    count = 0

    # Iterate through every number in the valid logical range.
    # A number 'x' must be >= max(a) and <= min(b).
    iterations = (i for i in range(max(a), min(b) + 1) if (i % max(a)) == 0)

    for x in iterations:

        # Condition 1: Check if x is a multiple of all elements in 'a'.
        # all() is a clean way to check if a condition is true for every item.
        is_multiple_of_a = all(x % num == 0 for num in a)

        # If the first condition passes, check the second one.
        if is_multiple_of_a:
            # Condition 2: Check if x is a factor of all elements in 'b'.
            is_factor_of_b = all(num % x == 0 for num in b)

            if is_factor_of_b:
                # If both conditions pass, we've found a valid number.
                count += 1

    return count


if __name__ == "__main__":

    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + "\n")

    fptr.close()
