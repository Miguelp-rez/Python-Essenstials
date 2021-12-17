# Section 7: the hierarchy of exceptions
# 63 built-in exceptions
# Tree-shaped structure, with its root at the top
# It goes from general to particular, from top to bottom.


# Any of the following exceptions will match the ZeroDivisionError.
# ^ BaseException
# | Exception
# | ArithmeticError
# | ZeroDivisionError

# Don't put more general exceptions before more concrete ones;
try:
    y = 1 / 0
    print(y)
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!") # This branch is now unreachable

print("THE END.")

# You can handle two or more exceptions in the same branch
try:
    x = int(input("Enter an integer number: "))
except (ValueError, TypeError):
    print("That's not an integer number")

print("THE END.")

# An exception can cross function and module boundaries
def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")
