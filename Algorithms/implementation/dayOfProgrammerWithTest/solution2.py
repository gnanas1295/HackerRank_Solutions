#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#


def is_gregorian_leap(year):
    """Checks for a leap year using the Gregorian calendar rules."""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def is_julian_leap(year):
    """Checks for a leap year using the Julian calendar rules."""
    return year % 4 == 0


def dayOfProgrammer(year):
    """
    Calculates the 256th day of the year in Russia, accounting for
    the Julian/Gregorian calendar change.
    """
    if year == 1918:
        # In 1918, Russia skipped 13 days, so the 256th day is shifted.
        return "26.09.1918"

    # Determine if it's a leap year based on the calendar in use.
    is_leap = is_julian_leap(year) if year < 1918 else is_gregorian_leap(year)

    day = "12" if is_leap else "13"

    return f"{day}.09.{year}"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + "\n")

    fptr.close()
