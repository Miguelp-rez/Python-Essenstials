# Palindromes

text = input('Enter some text: ')

# Remove all spaces
text = text.lower()
text = text.replace(' ', '')
backward_text = text[-1::-1]    # Easy way to reverse a string

if text == '':
    print("It's not a palindrome")
elif text == backward_text:
    print("It's a palindrome")
else:
    print("It's not a palindrome")


