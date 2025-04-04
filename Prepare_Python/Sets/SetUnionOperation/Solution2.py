#!/bin/python3

import sys

# Read the input lines
input_data = sys.stdin.read().splitlines()

# Create sets for English and French newspaper subscribers
english_subscribers = set(input_data[1].split())
french_subscribers = set(input_data[3].split())

# Use the union operator '|' to combine both sets and print the count of unique subscribers
print(len(english_subscribers | french_subscribers))

