# Section 3
# If a function does not have an explicit return statement,
# it returns None

def is_even(number):
    """
    Even numbers are: 0,2,4,6,8,...,etc
    """
    if number % 2 == 0:
        return True


result = is_even(9)
print(result)

# How to pass a list to a function
def sort(lst):
    lst.sort()


even_numbers = [2,4,6,8,0,10]
sort(even_numbers)
print(even_numbers)


# A function can return a list
def reverse(lst):
    new_list = lst[:]
    new_list.reverse()
    return new_list


print(reverse(even_numbers))
print(even_numbers) # Original list still intact

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_year_leap(1952))

def days_in_month(year, month):
    months_lengths = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year < 1582:
        return
    if month > 12 or month < 1:
        return
    if month == 2:
        if is_year_leap(year):
            return months_lengths[month - 1] + 1
    return months_lengths[month - 1]


print(days_in_month(1997, 2))

def day_of_year(year, month, day):
    days_past = 0
    for i in range(1, month):
        days_past += days_in_month(year, i)
    return days_past + day


print(day_of_year(2000, 12, 31))

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")

def liters_100km_to_miles_gallon(liters):
    liters_per_mile = liters / 100 * 1.609344
    mpg = 3.785411784 / liters_per_mile
    return mpg


def miles_gallon_to_liters_100km(miles):
    kilometers_per_liter = miles / 3.785411784 * 1.609344
    liters_100km = 100 / kilometers_per_liter
    return liters_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
