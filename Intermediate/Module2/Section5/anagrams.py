# Two words are anagrams if they use the same letters the same number of times
# Example: 'rail safety' and 'fairy tales'

from collections import defaultdict 


anagrams = True
text_one = input('Enter one phrase/word: ')
text_two = input('Enter another phrase/word: ')

text_one = text_one.lower()
text_one = text_one.replace(' ', '')

text_two = text_two.lower()
text_two = text_two.replace(' ', '')

counter = defaultdict(int)
for char in text_one:
    counter[char] += 1

for char in text_two:
    counter[char] -= 1

for ocurrences in counter.values():
    if ocurrences != 0:
        anagrams = False

if anagrams:
    print('They are anagrams')
else:
    print('They are not anagrams')
