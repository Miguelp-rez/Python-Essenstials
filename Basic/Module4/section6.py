# Section 6
# A tuple is an immutable sequence type
# it can only be assigned once, and you can't change its value later
tuple_1 = (1, 2, 3, 4)
tuple_2 = 1.0, 5.0, 0.25, 0.125

print(tuple_1)
print(tuple_2)

# A sequence is data which can be scanned by the for loop
for element in tuple_1:
    print(element)

# Parenthesis are required to create an empty tuple
empty_tuple = ()
print(type(empty_tuple))

# One-element tuple
lonely_tuple_1 = 1,
lonely_tuple_2 = (1.0,)
print(lonely_tuple_1)
print(lonely_tuple_2)

# Tuples can be indexed
my_tuple = (1, 10, 100, 1000)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2]) # 100 and 1000 are not included

# Joining tuples
combined_tuple = tuple_1 + tuple_2 # Addition
triple_tuple = tuple_1 * 3 # Multiplication
print(combined_tuple, "lenght:", len(combined_tuple))
print(triple_tuple, "lenght:", len(triple_tuple))

# Searching tuples
print("Is 4 in tuple_1?", 4 in tuple_1)

# A dictionary is not a sequence type and it is mutable.
# It is a set of key-value pairs
dictionary = {"cat": "chat",
              "dog": "chien",
              "horse": "cheval"
              }

# Getting a dictionary's value
print(dictionary["cat"])
print(dictionary.get("cat"))

# Accessing a non-existant key will cause a KeyError
# print(dictionary["chat"])

# Searching through dictionaries' keys
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

print("\nLooping through a dictionary using a for loop")
for item in dictionary:
    print(item)
      
# Adapting any dictionary to the for loop requirements
print("\nUsing keys() in for loop")
for key in dictionary.keys():
    print(key, "->", dictionary[key])

print("\nUsing items() in for loop")
for english, french in dictionary.items():
    print(english, "->", french)

print("\nUsing values() and sorted() in for loop")
for french in sorted(dictionary.values()):
    print(french)

# Modifying the dictionary's values
dictionary["cat"] = "minou"
print(dictionary)

# Adding a new key to the dictionary
dictionary["swan"] = "cygne"
print(dictionary)
dictionary.update({"duck": "canard"})
print(dictionary)

# Removing a key from the dictionary
del dictionary["cat"]
print(dictionary) # Its corresponding value it's also removed

# Removing a non-existant key will cause a KeyError
# del dictionary["cat"]

# Removing the last item from the dictionary
dictionary.popitem()
print(dictionary)

# Copying a dictionary
new_dictionary = dictionary.copy()
print("new_dictionary")
print(new_dictionary)

# Removing all items from a dictionary
dictionary.clear()
print("Removing all items in dictionary... Length:", len(dictionary))

# Converting a list to a tuple
a_list = [1,2,3]
x = tuple(a_list)
print(a_list, "->", x, type(x))

# Converting a tuple to a list
a_tuple = (1,2,3)
y = list(a_tuple)
print(a_tuple, "->", y, type(y))

# Counting duplicate elements in a tuple
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print("duplicates", duplicates)

# Merging two dictionaries
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

# Convert tuple of tuples to a dictionary
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)

print(colors_dictionary)
