# make a dictionary of books, with 3 authors and multiple books per author.
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












