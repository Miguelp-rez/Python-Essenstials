# Floating point division 
print(2 / 2) # The result is always a float

# Integer division
print(-1 // 2) # The result is always rounded down

# Modulo operation
print(9 % 2) # 9 - 9 // 2 * 2

# Multiplication
print(2 * 2)

# Exponitiazion
print(2 ** 2)

# Implicit cast
print(2.0 + 1) # Float
print(2 - 1.0) # Float

# The priorities of operators
# Higher priority operations are calculated first
print("Priority level 1: ", +-5)
print("Priority level 2: ", 3 ** 2)
print("Priority level 3: ", 8 * 3 / 2 // 4 % 2)
print("Priority level 4: ", 1 + 2)

# Operators with equal priority
print(12 / 4 / 2) # Left-sided binding
print(2 ** 2 ** 3) # Right-sided binding

print(-0)
