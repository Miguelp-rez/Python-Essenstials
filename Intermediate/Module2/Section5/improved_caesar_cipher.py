# Section 5

# Caesar Cipher
def decrypt():
    cipher = input('Enter your ciphertext: ')
    try:
        shift = int(input('Enter a shift value between 1 and 25 (inclusive): '))
        if shift < 1 or shift > 25:
            raise Exception()
    except:
        shift = 1
        print('That is not a valid shift number. Using default shift of 1')
    text = ''
    for char in cipher:
        if not char.isalpha():
            text += char
        if char.isupper():
            code = (ord(char) - ord('A') - shift) % 26 + ord('A')
            text += chr(code)
        if char.islower():
            code = (ord(char) - ord('a') - shift) % 26 + ord('a')
            text += chr(code)

    print(text)


def encrypt():
    text = input("Enter your message: ")
    try:
        shift = int(input('Enter a shift value between 1 and 25 (inclusive): '))
        if shift < 1 or shift > 25:
            raise Exception()
    except:
        shift = 1
        print('That is not a valid shift number. Using default shift of 1')
    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char
        if char.isupper():
            code = (ord(char) - ord('A') + shift) % 26 + ord('A')
            cipher += chr(code)
        if char.islower():
            code = (ord(char) - ord('a') + shift) % 26 + ord('a')
            cipher += chr(code)

    print(cipher)

encrypt()
decrypt()
