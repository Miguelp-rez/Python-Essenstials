# Section 4
# When a name is refereced outside its scope a NameError is produced
def scope_test():
    x = 123


scope_test()
# print(x)


# A funtion can read foreign variables, but assigning a value forces
# the creation of a new variable
def my_function():
    # var = 1
    print(var)


var = 10
my_function()
print(var)


# The previous behaviour can be altered with the global keyword
def new_function():
    global a # Use global a, not local a
    a += 1


a = 0
new_function()
print(a)


# Modifying a function's parameter can change the argument's value
# when using lists
def duplicate_list(a_list):
    for i in range(len(a_list)):
        a_list.append(a_list[i])


# Example 1
small_numbers = [0,1,2,3]
duplicate_list(small_numbers)
print(small_numbers)

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

# Example 2
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

