# Python allows underscores to improve readability of numbers
a = -11_111_111
print(a, "is", type(a))

# Octal numbers
print("Octal 123 is decimal", 0o123)

# Hexadecimal numbers
print("Hexadecimal 123 is decimal", 0x123)

#Binary numbers
print("Binary 111 is decimal", 0b111)

# You can omit zero when it is the only digit before or after the decimal point
print("4. is", type(4.))
print(".4 is", type(.4))

# You can use scientific notation
print("3e8 is", type(3e8)) # Three times ten to the power of 8

# Python may present a float literal using scientific notation
print("0.0000000000000000000001 =", 0.0000000000000000000001)

# All integers except 0 are True
print("-1 =", bool(-1))

# True = 1 and False = 0
print("True > False =", True > False) # True
print("True < False =", True < False) # False
