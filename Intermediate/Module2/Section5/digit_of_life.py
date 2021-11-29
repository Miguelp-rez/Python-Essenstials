# The digit of life
# It's the sum of all the digits of somebody's birthday
# If the result contains more than one digit, you have to repeat the addition

def digit_of_life(birthday):
    total = 0
    for digit in birthday:
        total += int(digit) 
    if total > 9:
        return digit_of_life(str(total))
    else:
        return total

birthday = input("Enter your birthday (DDMMYYYY): ")
print(digit_of_life(birthday))

