# Section one: imports

# Inside a certain namespace, each name must remain unique.
# Existing names may disappear when other entity of the same name
# enters the namespace. 
pi = 3.14159

# All the names defined here become known, but they don't enter my namespace
import math

print(pi) # My local pi
print(math.pi) # math's pi (you're entering math's namespace)




