# Section 7: rasing exceptions

# You might want to raise an exception to test your handling strategy
def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")

# You might want to re-raise the same exception as currently handled
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise # This can only be called inside an except block


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

# You might want to secure your code from producing invalid results
# Use assert <expression>
# It can stop the program before something goes wrong.
# It will raise an AssertionError if the expression is False
# Otherwise, it does nothing

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)
