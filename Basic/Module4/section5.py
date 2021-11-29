# Section 5
# Code to calculate the Body Mass Index in metric and imperial systems
def lb_to_kg(lb):
    return lb * 0.45359237

def ft_and_in_to_meters(feet, inches = 0.0):
    return feet * 0.3048 + inches * 0.0254
    
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print(lb_to_kg(1))
print(ft_and_in_to_meters(6))
print(bmi(weight = lb_to_kg(176), height = ft_and_in_to_meters(5, 7)))


# Code to check if a three sides can build a triangle
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Code to check if a certain triangle is a right-angle triangle
def is_a_right_angle_triangle(a, b, c):
    if is_a_triangle(a, b, c) == False:
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    return a ** 2 == b ** 2 + c ** 2

print(is_a_right_angle_triangle(3, 5, 4))

    
# Evaluating a triangle's area using Heron's formula
def heron(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def area_of_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        return heron(a, b, c)

print(area_of_triangle(3, 4, 5))


# Calculating factorials
def factorial_function(n):
    if n < 0:
        return None
    product = 1
    for i in range(1,n + 1):
        product *= i
    return product

for n in range(0, 6):  # testing
    print(n, factorial_function(n))


# Calculating factorials using recursion
def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return factorial(n - 1) * n

for n in range(0, 6):  # testing
    print(n, factorial(n))

    
# Find the i-th number in the fibonacci series
def fibonacci(n):
    if n < 1:
        return None
    prev_element = 1
    prev_prev_element = 1
    for i in range(3, n + 1):
        new_element = prev_element + prev_prev_element
        prev_prev_element, prev_element = prev_element, new_element
        
    return prev_element

for n in range(1, 10):  # testing
    print(n, "->", fibonacci(n))


# Find the i-th number in the fibonacci series using recursion
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(1, 10):  # testing
    print(n, "->", fib(n))


# Be careful when using recursion, as it might cause an infinite loop
def facto(n):
    return n * facto(n - 1)

# print(facto(4)) # RecursionError: maximum recursion depth exceeded
