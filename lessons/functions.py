# fucntions - a block of code - either perform a task or return a value. 
# Repeatability

# def greet(name): # parameters that takes in arguments
#     print(f"hi {name}")

# greet("chris")

# def greet_1(first_name, second_name, age):
#     print(f"{first_name} {second_name} is {age}")

# greet_1("chris", "reeves", 30)

# # print and input limit functionality
# # beter to store output in variable or file

# # return

# def greeter(name):
#     return f"hello {name}"

# x = greeter("chris")

# print(x)

# default values 

# def greet_3(name, age=10): # defaults to come at end of line. 
#     return f"{name} is {age}"

# print(greet_3("chris")) 
# print(greet_3("chris", 30)) 

# *args
# used for when we do not know how many args will be passed through
# Reveives a tuple of args

# def fruit_list(*fruits):
#     print("the fruits are:")
#     for fruit in fruits:
#         print(fruit)

# fruit_list("orange", "apple", "pear")


# def numbers_list(*numbers):
#     for i in numbers:
#         print(i)

# numbers_list(1, 2, 3, 4, 5, 6, 7, 8)


#def make_pizza(size, *toppings):
#    print(f"order for {size}-inch pizza with the following toppings:")
#    for topping in toppings:
#        print(topping)

#make_pizza(12, "mushrooms", "green peppers")

# kwargs - keyword arguments
# send args as key:value pairs
# therefore order does not matter

# def fruit_list(fruit1, fruit2, fruit3):
#     print(f"fav is {fruit1}")
#     print(f"2nd fav is {fruit2}")
#     print(f"3rd fav is {fruit3}")

# fruit_list(fruit3="apple", fruit2="orange", fruit1="pear")

# **kwargs
# if we dont know how many Kwargs there will be

# def fav_food(**food):
#     print("fav food is", food['dessert'], "not", food["dairy"])

# fav_food(dessert="ice-cream", fruit="apple", dairy="milk")

# combined *args and **kwrags

# def combine(*args, **kwargs):
#     print("args: ", args)
#     print("kargs:", kwargs)

# combine(1, 2, 3, a=5, b=4)

# # / *
# # / - a marker dividing postional-only params from the rest
# # before / the params have to be in order
# # * everything after the star is keyword args
# # introduced 3.8

# def example(a, b, /, c, d):
#     print(f"a = {a}, b= {b}, c= {c}, d= {d}")

# example(1, 2, d=4, c=3)

# def math_operations(a, b, /, operation="add", *, decimal_place=2):
#     if operation == "add":
#         result = a + b
#     elif operation == "subtract":
#         result = a - b
#     else:
#         raise ValueError("Invalid operation")
#     return round(result, decimal_place)

# print(math_operations(10, 5))
# print(math_operations(10, 5, operation="subtract"))
# print(math_operations(10, 5, operation="add", decimal_place=4))


# passing a list to a function

# def my_function(food):
#     for x in food:
#         print(x)

# list1 = ["apple", "pear", "orange"]
# my_function(list1)

# Others

# type annotations
# allows you to specifiy the expected data types for vars, params and outputs.
# introduced 3.5.
# Not checked at run time.

# def greet(name: str) -> str:
#      return f"hello {name}"

# def add(x: int, y: int) -> int:
#     return x + y

# print(add("a", "b"))
# print(greet(10))

# higher functions

# def apply_fucntion(func, value):
#     return func(value)

# def square(x):
#     return x * x

# print(apply_fucntion(square, 5))

# recursion

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))

# lambda functions
# argument: expression (iterable)
# short, unamed fucntions, calculate a single expression, good for passing to other functions
# and lightweight.

# def add(x, y):
#     return x + y

# add_lambda = lambda x, y: x + y

# print(add(2, 3))
# print(add_lambda(2, 3))

# numbers = [1, 2, 3, 4]
# squared = map(lambda x: x**2, numbers)
# print(list(squared))

# format

# name = "chris"
# age = 30
# height = 1.7

# #print("my name is {}, age is {}, height is {}".format(name, age, height))

# x = "my name is {}, age is {}, height is {}"

# print(x.format(name, age, height))


# TODO list
# finish previous labs
# labs 5 and 6
# rock, paper scissor app using a function
# extra functions challenges. 























































