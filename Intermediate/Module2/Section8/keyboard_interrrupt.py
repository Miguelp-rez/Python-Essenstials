# Section 7: useful exceptions

# KeyboardInterrupt
# This exception is raised when the user enters the program termination shortcut

x = 0
while True:
    try:
        print(x)
        x += 1
    except KeyboardInterrupt:
        print('You escaped from the loop')
        exit(0)

# Lookup error
# This exception cannot be raised, but it includes all other exceptions caused
# by invalid references to multiple collections
