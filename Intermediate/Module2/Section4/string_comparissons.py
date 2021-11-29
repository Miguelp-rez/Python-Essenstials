# String comparissons are based on its ASCII/UNICODE codepoints

# Two strings are equal if they consist of the same characters in the same order
print('ab' == 'ba') # 65 == 66 ?
print('a' != 'A')   # 97 != 65 ?

# Left-most characters are more important
print('z' > 'aaaaaaaaaaaaaaaaa')    # 122 > 97 ?
print('9' > '10')       # 57 > 49
print('Smith' < '1000') # 83 < 49 

# When the beginning of two strings are identical
# the longer is considered greater
print('az' >= 'azy')

# Upper-case letters are taken as leser than lowe-case
print('A' < 'a')    # 65 < 97 ?
print(' ' <= 'a')   # 32 <= 97 ?

# Do not compare strings and numbers (Bad idea)
print('10' == 10) # Always false
print('10' != 10) # Always True
# print('10' > 9) # TypeError exception

# sorted() function
alphabet = ['a', 'c', 'b', 'e', 'd']
new_alphabet = sorted(alphabet)
print(new_alphabet)

# sort() method
alphabet.sort()
print(alphabet)

# Number to string conversion
ten = 10
almost_ten = 9.9
text = str(ten) + str(almost_ten)
print(text)

# String to number conversion
ten = '10'
almost_ten = '9.9'
number = int(ten) + float(almost_ten)
print(number)

invalid_number = '10.0'
# print(int(invalid_number)) #ValueError exception

