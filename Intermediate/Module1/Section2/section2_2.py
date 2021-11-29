# Section 2: random
from random import random, seed, randrange, randint, choice, sample

#seed(0) # Setting the seed removes all randomness from the code

for i in range(15):
    print(random())

print(randrange(3)) # Random integers from 0 to 3 (3 is excluded)
print(randrange(1,5)) # Random integers from 1 to 5 (5 is excluded)
print(randrange(0,10,2)) # Random even numbers from 0 to 10 (10 is exluded)
print(randint(0,3)) # Random integer from 0 to 3 (3 IS INCLUDED!)

bingo_cards = [1,2,3,4,5,6,7,8,9,10]
print(choice(bingo_cards)) # Chooses a "random" card

# sample(sequence, X) creates a new list
# with X random elements from the sequence
# X can not be greater than the sequence length
bingo_cards_2 = sample(bingo_cards,5) # Creates a list of 5 "random" cards
print(bingo_cards_2)    

bingo_cards_3 = sample(bingo_cards, 10) # Basically shuffles the cards
print(bingo_cards_3)
