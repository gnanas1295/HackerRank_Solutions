import sys
import numpy as np

# Read all input lines
input_data = sys.stdin.read().splitlines()

# Convert the input strings to NumPy arrays using fromstring for efficiency
# firstArray = np.fromstring(input_data[0], sep=' ', dtype=int)
# secondArray = np.fromstring(input_data[1], sep=' ', dtype=int)

firstArray = np.array(input_data[0].split(), int)
secondArray = np.array(input_data[1].split(), int)

# Compute inner and outer products
print(np.inner(firstArray, secondArray))
print(np.outer(firstArray, secondArray))