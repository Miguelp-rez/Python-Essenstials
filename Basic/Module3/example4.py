numbers = [10, 5, 7, 2, 1]
print("List content:", numbers)  # Printing original list content.

# Any expression can be the index
numbers[True] = 0
print("New contents:", numbers)


# del is an instruction, not a function
del numbers[0]
print("New contents:", numbers)
print("List's length:", len(numbers))


numbers.append(10)
print("New contents:", numbers)
print("List's length:", len(numbers))

# Effective way to swap values
numbers[0], numbers[4] = numbers[4], numbers[0]
numbers[1], numbers[3] = numbers[3], numbers[1]

print(numbers)

length = len(numbers)

# Flipping the list
for i in range(length // 2):
    numbers[i], numbers[-i - 1] = numbers[-i -1], numbers[i]
print(numbers)

# Delete the whole list
del numbers
