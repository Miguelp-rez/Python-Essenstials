# Section 8: useful exceptions

# IndexError
# This exception is raised when you try to access a non-existent element of
# a sequence.

lenght = 10
numbers = range(lenght)
index = 0
flag = True

while flag:
    try:
        print(numbers[index])
        index += 1
    except IndexError:
        flag = False
