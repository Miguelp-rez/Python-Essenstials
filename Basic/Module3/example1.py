# Python implicitly converts the integer value to float
print("2 == 2.", 2 == 2.) # True

# The equality and inequality operators have low priority
print("Priority level 5 4 == 2", 4 == 2, sep="\t")
print("Priority level 5 4 != 2", 4 != 2, sep="\t")

# The following operators have higher priorities than == and !=
print("Priority level 6 2 > 0", 2 > 0, sep="\t") #Non-strict 
print("Priority level 6 2 >= 0",2 >= 0, sep="\t") #Strict
print("Priority level 6 2 < 0",2 < 0, sep="\t") #Non-strict
print("Priority level 6 2 <= 0",2 <= 0, sep="\t") #Strict

#Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Choose the largest number
largest_number = number1

if number2 > largest_number: largest_number = number2

if number3 > largest_number: largest_number = number3

print("The largest number is:", largest_number)

