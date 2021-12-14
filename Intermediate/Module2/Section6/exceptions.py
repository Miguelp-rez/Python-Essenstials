# Section 7: error handling (exceptions)
# In python an exception is raised whenever an error occurs

# ZeroDivisionError
# ValueError
# IndexError

# Some instructions may not be executed if an error occurs
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")


# This new version of the code can handle multiple exceptions
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print('You must enter an integer vlaue')
except ZeroDivisionError:
    print('You cannot divide by zero, sorry')
except:
    print("Oh dear, something went wrong...")
print("THE END.")


# The unnamed except branch is not mandatory
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")
# If another exception occurs, it will be unhandled and
# the program will terminate abruptly

print("THE END.")
