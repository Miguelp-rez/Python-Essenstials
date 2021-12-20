# Section 7: useful exceptions

# OverFlowError
# This exception is raised when an operation produces a number too big to be
# successfully stored

from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')
