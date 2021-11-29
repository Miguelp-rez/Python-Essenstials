anything = input("Enter a number: ")
# Convertion of string to float (Be careful with this one)
edge = float(anything)
# Convertion of float to integer (Some data may be lost here)
edge = int(edge)
#Convertion of float to string (Completely safe)
print("You have created a rectangle of " + str(edge) + "x" + str(edge*2))

print("+" + edge*2 * "- " + "+")
print(("|" + "  " * edge*2 + "|\n") * edge, end="")
print("+" + edge*2 * "- " + "+")

