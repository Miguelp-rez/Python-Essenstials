# The pyramid is stacked according to one simple principle:
# each lower layer contains one block more than the layer above

blocks = int(input("Enter the number of blocks: "))
height = 0

# While there is a valid number of blocks
while blocks >= 0:
    # Try to build one more layer
    height += 1
    blocks -= height
else:
    height -= 1 # It was not possible to build one more layer

print("The height of the pyramid:", height)
