my_list = [6, 10, 2, 4, 8]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

for i in range(len(my_list) - 1): # Worst case scenario: 4 passes are needed
    if not swapped:
        break
    swapped = False  # no swaps so far
    for j in range(len(my_list) - 1 - i): # Each pass does 1 less comparisson
        if my_list[j] > my_list[j + 1]:
            swapped = True  # a swap occurred!
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(my_list)


if "A" > " ":
    print("'A' greater than ' '")
