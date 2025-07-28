# Import the sys module to read from standard input
import sys

# WARNING: Using eval() on raw user input is a major security vulnerability.
# It allows the user to execute any command on the system.
# This approach is used here ONLY because it is the specific requirement
# of this academic challenge. Do not use this in real-world applications.
eval(sys.stdin.readline().strip())
