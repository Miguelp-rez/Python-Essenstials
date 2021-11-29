# Section 2
# A backslash is not included in the string's length
i_am = "I\'m"
print(len(i_am))

# Multiline strings
long_string = """Line #1
Line #2"""
print(len(long_string)) # 7 + 7 + 1 (\n)

# String concatenation
print("a" + "b" + "c")

# String replication
print("a" * 3)

the_string = "d"
print(the_string) # Original string
the_string += "d"
print(the_string) # String concatenation
the_string *= 3
print(the_string) # String replication

# How many letters are in the_string?
print(len(the_string))

# Show a character's codepoint
print(ord('ñ')) # Use one-char strings only
# print(ord('aa')) # TypeError exception

# Take a codepoint and return its character
print(chr(241))
# print(chr(-10)) # ValueError exception
# print(chr('1')) # TypeError exception

# Indexing strings.
the_string = 'silly walks'
for ix in range(-1, -1 - len(the_string), -1):
    print(the_string[ix], end=' ')
print()

# Iterating through strings
the_string = 'silly walks'
for character in the_string:
    print(character, end=' ')
print()

# Slices
# [start:end:step] end is not included
alpha = "abdefg"
print(alpha[1:3])   #bd
print(alpha[3:])    #efg
print(alpha[:3])    #abd
print(alpha[3:-2])  #e
print(alpha[-3:4])  #e
print(alpha[::2])   #adf
print(alpha[1::2])  #beg
