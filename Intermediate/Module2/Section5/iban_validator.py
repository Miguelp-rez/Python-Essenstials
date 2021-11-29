# International Bank Account Numbers (IBAN) validator

# Check one: the total IBAN lenght is correct.

# Move the first four characters to the end of the string,
# replace each letter with its two-digit number representation
# A = 10, B = 11, C = 12, ..., Z = 35
# convert the string to an decimal integer

# Check two: Compute the remainder of the previous number on division by 97;
# if the remainder is 97, the check is passed.


iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

        


