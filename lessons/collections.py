# collections are our complex data types.
# different ways of storing data.

# lists - ordered, mutable, collection of values - [a(index position 0), b(index position 1), c ....]
# dictionaries - unordered, mutable, collection of key:pair values. 
# - {value: "key", value2: "key", ....}
# tuples - ordered, immutable, collection of values - (a, b, c) or no brackets at all x = a, b, c.
# sets - unordered, mutable, collection of unique values - {a, b, c, ....}


# lists are stored with [].

#colours = ["blue", "green", "red", "yellow"]

#print(colours)

# referencing elements in a list by index location
# starts at 0 end at -1

#print(colours[0])
#print(colours[3])
#print(colours[-4])

# slicing - create a sub-list up to but not including the second number.

#print(colours[0:2])
#print(colours[1: ]) # no second number slices till the end. 


# Altering lists - using index postion, need a value, delete with del.

#food = ["bread", "apple", "pizza", "pasta"]

#print(food)
#food[0] = "rice"
#print(food)

#del food[1]
#print(food)

# check if an item is in a list

#print("pizza" in food)
#print("orange" in food)

# nested lists

#numbers = [1, 2, 3, 4]
#letters = ["a", "b", "c", "d"]

#combined = [numbers, letters]

#print(combined[0][1], combined[1][1])

# combined data types
#a = ["red", 5, ["list", 5.404], 10.65, True]

# list methods

# append

#my_fruits = ["apple", "orange", "pear"]

#my_fruits.append("kiwi")
#print(my_fruits)

# remove

#my_fruits.remove("apple")
#print(my_fruits)

# insert

#my_fruits.insert(0, "mango")
#my_fruits.insert(0, "grapes")

#print(my_fruits)

# extend

#my_fruits.extend(["melon", "pomegranete"]) # must be an iterable
#print(my_fruits)

# reverse

#my_fruits.reverse()
#print(my_fruits)

# sort

#my_fruits.sort()
#print(my_fruits)

#my_fruits.sort(key=len)
#print(my_fruits)

# join 

#x = ", ".join(my_fruits)
#print(x)
#print(type(x))

# dictionaries
# {} - key:value pairs
# similar to lists but no indexing
# keys have to be unique, values dont. 


#drinks = {"fizzy": "sprite", "still": "water", "juice": "orange", "alcoholic": "wine"}

#print(drinks)

# direct access

#print(drinks["still"])

# add key pair value

#drinks["non-alcoholic"] = "water"
#print(drinks)

# overwrite

#drinks["non-alcoholic"] = "squash"
#print(drinks)

# returning values with methods

#print(drinks.values())
#print(drinks.keys())
#print(drinks.items())

#print("water" in drinks.values())

# get method

#print(drinks.get("still"))
#print(drinks.get("stilleel"))
#print(drinks.get("stilllelele", "not-found"))

# update method

#drinks.update({"sugery": "cola"})
#print(drinks)

# pop method

#print(drinks.pop("non-alcoholic"))
#print(drinks)
# 
# # make a dictionary of books, with 3 authors and multiple books per author.
# use an input to ask for an author name.
# print a STRING of books by that author (not a list)
# optionally have a bit of error handling for incorrect author name. 

#books = {"author1": ["book1", "book2"], "author2": ["book3", "book4"]}

# 1st solution:

#y = input("enter author name: ")

#print(", ".join(books[y]))

# 2nd solution

#y = input("enter author name: ")

#books_query = books.get(y, [])

#print(", ".join(books_query) or "author not found")

# tuples
# similar to a list but immutable. 
# indicate that we dont to change the data. 
# less memory - very slight. 
# more speed - very slight. 

#rectangle = 10, 5 # nothing at all or () - to set a tuple. 

#rectangle[0] = 15

# tuple methods - just count and index
# inbuilt functions: max, sum, len, min etc ...

# sets 
# no indexing, unique values - {}. 

#set1 = {1, 2, 3, 4, 5}
#set2 = {4, 5, 6, 7, 8}

#  union - combnine sets removing duplicates

#print(set1.union(set2))

# intersection 

#print(set1.intersection(set2))

# difference

#print(set1.symmetric_difference(set2))

# tuples - we cant update but otherwise is the same as a list
# indicates that we dont want to change the data.
# less memory - very slight
# more spped - very slight


#rectangle = (10, 5) # regular () or nothing at all.
#rectangle[0] = 15

# available tuple methods - count, index etc....
# inbuilt python functions like max(), min(), sum() etc .... 


# sets no indexing, unique values - uses {a, b, c}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union - combines but removes duplicates. 

print(set1.union(set2))

# intersection

print(set1.intersection(set2))

# difference

print(set1.difference(set2))












