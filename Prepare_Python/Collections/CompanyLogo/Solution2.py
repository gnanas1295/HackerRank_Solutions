#!/bin/python3

import sys
from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    # Count the characters in the string
    counts = Counter(s)
    # Sort by descending frequency and then by alphabetical order
    top_three = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:3]
    # Print the top three most common characters and their counts
    for char, count in top_three:
        print(char, count)