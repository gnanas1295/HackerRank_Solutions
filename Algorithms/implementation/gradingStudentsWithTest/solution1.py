#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades: list) -> list:
    # Write your code here

    finalGrades = []

    for grade in grades:
        if grade < 38:
            finalGrades.append(grade)
        else:
            finalGrade = (round(grade / 5) * 5) if (grade % 5) >= 3 else grade

            finalGrades.append(finalGrade)

    # print(finalGrades)
    return finalGrades


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
