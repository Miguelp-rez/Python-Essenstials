# Section 7: useful exceptions

# MemoryError
# This exception is raised when an operation cannot be completed due to
# lack of memory

# Warning: executing this code may affect your OS.
# Don't run it in production environments!

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')

# It did not work on windows 10
