# String operators
alphabet = 'abcdefghijklmnopqrstuvwxyz'

print('f' in alphabet)
print('' in alphabet) # The empty string is always contained in any string
print('ñ' not in alphabet)
print('8' not in alphabet)


## Exceptions

# You can delete a string as a whole, but not parts of it
# del alphabet[0] # TypeError exception

# Strings do not have an append method
# alphabet.append("A") # AttributeError exception

# Strings do not have an insert method
# alphabet.insert(0, "A") # AttributeError exception

## Useful functions
# min() finds the minimum element of a sequence using ascii codepoints
print(min("aAbBcCdD"), ord('a'), ord('A'))

# max() finds the maximum element of a sequence using ascii codepoints
print(max("aAbBcCdD"), ord('d'), ord('D'))

# list() creates a new list with one character per element
alphabet_list = list(alphabet)
print(alphabet_list)

# Useful methods
# index() finds the first ocurrence of the argument
print(alphabet.index('a'))
print(alphabet.index('n'))
print(alphabet.index('z'))

# count() counts all ocurrences of the argument
print(alphabet.count('a'))

