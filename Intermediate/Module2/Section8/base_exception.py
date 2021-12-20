# Section 8: useful exceptions

# Base exception
# This exception cannot be raised, but it includes all other exceptions

try:
    x = int(input('Enter a number: '))
except BaseException: # All exceptions will be handled by this block
    print('Ooops an error ocurred')
