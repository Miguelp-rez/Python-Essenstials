# Section 8: useful exceptions

# KeyError
# This exception is raised when you try to access a collection's non-existent
# element

numbers = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three'}

for i in range(5):
    try:
        print(numbers[i])
    except KeyError:
        print('Wrong key name: ', i)
