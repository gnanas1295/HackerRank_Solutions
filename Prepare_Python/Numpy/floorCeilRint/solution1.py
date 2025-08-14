import numpy
import sys

inputArray = list(map(float, sys.stdin.readline().split()))
numpy.set_printoptions(legacy="1.13")
myArray = numpy.array(inputArray)

print(numpy.floor(myArray))
print(numpy.ceil(myArray))
print(numpy.rint(myArray))
