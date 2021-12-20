# Section 8: useful exceptions

# ArithmeticError
# This exception cannot be raised, but it includes all exceptions caused by
# arithmetic operations

# AssertionError
# This exceptions is raised by the assert instruction when its arguments
# evaluate to False

from math import tan, radians

angle = int(input('Enter an angle in degrees: '))

# We must be sure that the angle is not 90, 270, 450, etc...
assert angle % 180 != 90
print(tan(radians(angle)))
