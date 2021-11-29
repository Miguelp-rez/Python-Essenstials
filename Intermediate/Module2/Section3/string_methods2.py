# More string methods

# lstrip() method
print('   hello world   '.lstrip()) # Remove all leading spaces
print('/a./ ./Hello world./'.lstrip('./')) # Remove the specified characters
print("pythoninstitute.org".lstrip(".org")) # The first char is p
print()

# replace() method
print('This is a string with many ths'.replace('th', 'd'))
print('HELLO'.replace('', '.'))
print('ooooooh'.replace('o', '', 3)) # Three replacements at most
print()

# rfind() method
print('tau tau tau'.rfind('au '))
print('tau tau tau'.rfind('au ', 6)) # rfind('', start) start is included
print('tau tau tau'.rfind('au ', 0, 3)) # rfind('', start, end) end not included
print()

# rstrip() method
print('hello world   ?  '.rstrip())
print('hello world.   ?  '.rstrip('? '))
print("cisco.com".rstrip(".com"))
print()

# split() method
print('This is a phrase'.split('a'))
print('This is a phrase'.split()) # reverse operation of join() method
print(' '.join(['This', 'is', 'a', 'phrase']))
print()

# startswith() method
print('Hello world'.startswith('he'))
print('Hello world'.startswith('He'))
print()

# strip method
print('\n \t  hello world    \t'.strip())
print('     hello world    end'.strip(' end'))
print()

# swapcase() method
print('wHOOPS i HAD CAPS ENABLED'.swapcase())
print()

# title() method
print('make me a cooler string'.title())
print()

# upper() method
print('The yelling() method!'.upper())
