# Find a needle in the haystack
# Search the characters of one word in the some text.
# if the word is 'dog',
# the characters ['d', 'o', 'g'] have to be found in that order
# in the text

word = input('Enter a word: ').lower()
text = input('Enter some text: ').lower()

found = True
possition = 0

for char in word:
    possition = text.find(char, possition)
    if possition == -1:
        found = False

if found:
    print('Yes I found that word')
else:
    print('No I could not find that word')
    
