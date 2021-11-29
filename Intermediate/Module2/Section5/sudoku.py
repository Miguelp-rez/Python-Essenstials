# This a sudoku checker.
# This script will tell you if your solution is valid.
# each row of the board must contain all digits from 0 to 9 
# each column of the board must contain all digits from 0 to 9 
# each of the 3x3 sub-squares must contain all digits from 0 to 9.

from collections import defaultdict


# Clear digit counter
def clear_counter(line):
    for digit in line:
        digit_counter[digit] = 0


# Counting digits
def count_digits(line):
    for digit in line:
        digit_counter[digit] += 1


# Verifying that there are not repeated digits
def check(line):
    repeated_digits = False
    count_digits(line)
    for digit in line:
        if digit_counter[digit] != 1:
            repeated_digits = True
    if repeated_digits:
        clear_counter(line)
        return 0
    else:
        clear_counter(line)
        return 1
            
digit_counter = defaultdict(int)
passed_checks = 0 # This must be 27 if the sudoku is valid
length = 9       
table = []

# Reading sudoku table from standard input
for i in range(length):
    line = input('Enter line {}: '.format(i))
    if not line.isdigit() :
        print('Each line must contain digits only')
    elif len(line) != length:
        print(f'Each line must contain {length} digits')
    else:
        table.append(line)

# Performing row check
for row in table:
    passed_checks += check(row)

# Performing column check
column = ''
for i in range(length):
    for j in range(length):
        column += table[j][i]
    passed_checks += check(column)
    column = ''

# Performing sub-square check
sub_square = ''
for w in range(3):
    for x in range(3):
        for y in range(3):
            row = w * 3 + y
            for z in range(3):
                column = x * 3 + z
                sub_square += table[row][column]
        passed_checks += check(sub_square)
        sub_square = ''
    
if passed_checks == 27:
    print('Yes')
else:
    print('No')
    


