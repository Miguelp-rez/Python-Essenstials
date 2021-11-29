# Section 2
# Positional parameters
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

# Positional arguments  
introduction("Miguel", "Quiroz")

# Keyword arguments
introduction(last_name="Quiroz", first_name="Miguel")

# TypeError exception invalid keyword argument
#introduction(surname="Skywalker", first_name="Luke")

# If you mix positional and keyword arguments,
# you have to put positional arguments first
# otherwise you get SyntaxError
# introduction(last_name="Quiroz", "Miguel")

# You cannot pass more than one value to one argument
# introduction("Miguel", first_name="Angel")

# Default parameters
# They have to be defined last
# otherwise you get SyntaxError
# If c is ommited, its value will be zero
def adding(a, b, c=0):
    print(a, "+", b, "+", c, "=", a+b+c)

adding(1,2,3)
adding(1,2)
adding(a=1,b=2)
