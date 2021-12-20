# Section 8: Reading integers safely

# This function reads integers safely
# It prevents the user from entering strings instead of integers and
# it only allows integers within the specified range
def read_int(min, max):
    flag = True
    while flag:
        try:
            x = int(input(f'Enter an integer value from {min} to {max}: '))
            assert x >= min and x <= max
            flag = False
        except ValueError:
            print('Error: wrong input')
        except AssertionError:
            print(f'Error: the value is not within permitted range ({min}, {max})')
    return x    
            

number = read_int(-10,10)
print("The number is:", number)
