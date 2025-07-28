import math
import os


def gradingStudents(grades):
    """
    Rounds student grades based on HackerLand University's policy.
    """
    final_grades = []
    for grade in grades:
        # 1. If the grade is less than 38, no rounding occurs.
        if grade < 38:
            final_grades.append(grade)
            continue

        # 2. Find the next multiple of 5
        # A simple way is to use integer division and multiplication.
        next_multiple_of_5 = (grade // 5 + 1) * 5

        # 3. If the difference is less than 3, round up.
        if next_multiple_of_5 - grade < 3:
            final_grades.append(next_multiple_of_5)
        else:
            final_grades.append(grade)

    return final_grades


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
