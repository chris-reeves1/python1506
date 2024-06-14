# iteration is another word for loops
# repeating blocks of code over and over
# saves time, avoids haviong to duplicate code. 

# 2 types of loops - while and for. 

# while
# a while loop continuosly executes code whilst a condition is true.
# if a condition is never true the while loop will never start.

#print(1)
#print(2)
#print(3)
#print(4)
#print(5)
#print(6)

#x = 0
#while x < 101:
#    print(x)
#    x +=1

# break

#i = 1
#while i < 6:
   # print(i)
   # if i == 3:
   #     break
   # i += 1

# continue

#j = 0 
#while j < 6:
#    j += 1
#    if j == 3:
#        continue
#    print(j)

#while True:
#    name = input("enter your name: ")
#    if name == "quit":
#        break
#    else:
#        print(f"hello {name}")

# for loops
# a for loop will iterate over a collection - lists/dictionaries/strings etc

# lists

# my_fruits = ["apple", "orange", "kiwi"]
#    #item   # iterable
# for fruit in my_fruits:
#     print(fruit)

# numbers = [1, 2, 3, 5, 6]

# for number in numbers:
#     print(number)

# l = 0

# while l < len(numbers):
#     print(numbers[l])
#     l += 1 

# range

#for a in range(5):
#    print(a)

#for a in range(1,5):
#    print(a)

#for a in range(1, 10, 2):
#    print(a)

# strings

#for letter in "hello":
#    print(letter)


#for word in "hello world".split():
#    print(word)

# list comprehenion
        # expression        # item          # iterable
#result = [x**2           for x in            range(5)] 

#print(result)

#result = []
#for x in range(5):
 #   result.append(x**2)

#print(result)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_number_squared = [number**2 for number in numbers if number % 2 == 0]
# print(even_number_squared)

# dictionaries

# for i in {"drink": "wine"}:
#     print(i)

# for i in {"drink": "wine"}.values():
#     print(i)

# for i in {"drink": "wine"}.items():
#     print(i)

# nested for loop

#for i in range(1,3):
#    for j in range(1,4):
#        print(i, "x", j, "=", i*j)


# challenge 
#write to a loop that takes names and prints name + is great.

# while loop
# for loop
# list comprehension
# list comprehsion 1 line of code only!! 

# counter = 0
# while counter < 5:
#     name = input("enter a name: ")
#     print(name + " is great")
#     counter += 1

# for counter in range(5):
#     name = input("enter a name: ")
#     print(name + " is great")

# names = [input("enter a name") for name in range(5)]
# for name in names:
#     print(f"{name} is great")

#[print(f"{name} is great") for name in [input("enter a name: ") for x in range(5)]]













