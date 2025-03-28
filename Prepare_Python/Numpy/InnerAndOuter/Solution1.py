# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import numpy

input_data = sys.stdin.read().splitlines()

firstArray = numpy.array(list(map(int, list(input_data[0].split()))))
secondArray = numpy.array(list(map(int, list(input_data[1].split()))))

print(numpy.inner(firstArray, secondArray))
print(numpy.outer(firstArray, secondArray))