from math import ceil, floor, trunc

x = 1.4
y = 2.6

# floor(x), returns the lowest integer less than or equal to x
print(floor(x), floor(y))#1,2
print(floor(-x), floor(-y))#-2,-3

# ceil(x), returns the lowest integer greater than or equal to x
print(ceil(x), ceil(y))#2,3
print(ceil(-x), ceil(-y))#-1,-2

# trunc(x), returns only the integer part of x
print(trunc(x), trunc(y))#1,2
print(trunc(-x), trunc(-y))#-1,-2
