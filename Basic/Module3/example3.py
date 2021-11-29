print("Priority level 1: not")
print("Priority level 7: and")
print("Priority level 8: or")

p = True
q = False

# The negation of a conjuction is the disjunction of the negations
print(not (p and q), not p or not q)

# The negation of a disjunction is the conjuction of the negations
print(not (p or q), not p and not q)

print("bitwise conjuction: &")
print("bitwise disjunction: |")
print("bitwise negation: ~")
# True if one or the other is false, but not both
print("bitwise xor: ^")


x = 6 # 110
y = 4 # 100
# if x is False, its value is returned; otherwise, y returned.
logical = x and y
print(logical)

# if x is True, its value is returned; otherwise, y returned.
logical = x or y
print(logical)
 
bitwise = x and y
print(bitwise) # 100

x &= y

bitwise = x or y
print(bitwise) # 100

flag_register = 0x5678
# Check the status of the third bit
bitmask = 0x0008
if bitmask & flag_register == bitmask:
    # Reset bit
    # x & 1 is always x
    # x & 0 is always 0
    flag_register = flag_register & ~bitmask 
else:
    # Set bit
    # x | 1 is always 1
    # x | 0 is always x
    flag_register = flag_register | bitmask 

# Negate bit
# x ^ 1 is always ~x
# x ^ 0 is always x
flag_register = flag_register ^ bitmask 

if flag_register == 0x5678:
    print("Yes")

# Python uses Two's complement to represent signed integers
x = 4  # 0b0100
x = ~x # 0b1011
# Converting signed binary to integer
print(x) # -8 + 3 = 5
