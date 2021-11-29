#!/usr/bin/env python3

""" module.py - an example of a Python module """

# Convention
# Variable names starting with underscores should not be modified by the user
__counter = 0 


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    # When run directly
    print("I prefer to be a module, but I can do some tests for you.")
    # You can test your functions here
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
else:
    # When imported
    print("I like to be a module.")
