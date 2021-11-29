# String methods

# capitalize() method
print('bOoK'.capitalize())
print('1bOoK'.capitalize())
print('σ'.capitalize())
print()

# center() method
print('hello'.center(80)) # Adds some spaces before and after the string
print('world'.center(80, '*')) # Adds some asteriscs instead
print()

# endswith() method
print('television'.endswith('sion'))
print('television'.endswith('n'))
print('television'.endswith('sio'))
print()

# find() method
print('this is a large text'.find('is'))
print('kappa'.find('a', 2)) # Start searching at index 2
print('kappa'.find('a', 2, 4)) # Stop searching at index 4 (not included)
print()

# find() versus index()
print('this is a large text'.find('isa')) # Returns -1 if not found
#print('this is a large text'.index('isa')) # ValueError exception
print()

# isalnum() method
print(''.isalnum())
print('a b c'.isalnum())
print('αβπσ'.isalnum())
print('1q2w3e'.isalnum())
print('$'.isalnum())
print()

# isalpha() method
print('Mooo'.isalpha())
print('Mo oo'.isalpha())
print('Mooo4'.isalpha())
print()

# isdigit() method
print('123'.isdigit())
print('12 3'.isdigit())
print('0x123'.isdigit())
print()

# islower() method
print('Hello'.islower())
print('hello'.islower())
print()

# isspace() method
print(' \n'.isspace())
print('a b'. isspace())
print(' \n \t'.isspace())
print()

# isupper() method
print('Hello'.isupper())
print('HELLO'.isupper())
print()

# join() method
print(' separator '.join(['list', 'of', 'strings']))
print()

# lower() method
print('HelloWorld_Today_is_a_good_day :3'.lower())
print()

