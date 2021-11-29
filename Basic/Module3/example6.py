import time

# Trying to copy a list, but failing in the process
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# Copying a list
list_1 = [1]
list_2 = list_1.copy()
list_1[0] = 2
print(list_2)

# A new method for copying a list
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Slicing
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:100] # my_list[start:end]
print(new_list)

# Slicing with negative indeces
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# Deleting multiple elements from a list at once
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# Deleting all the elements
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# Deleting the list itself, not its contents
# my_list = [10, 8, 6, 4, 2]
# del my_list
# print(my_list)

my_list = [0, 3, 12, 8, 2]

# Look for a value in the list
print(5 in my_list) # False
print(5 not in my_list) # True
print(12 in my_list) # True

# Deleting the referece to a list, not the list itself
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2 

print(list_3)
