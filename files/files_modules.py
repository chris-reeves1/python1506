# modules
# modules are just file, that we use to extend functionality.
# many built in, some need to be imported others need to installed. 
# pip is our package manager.

# pypi.org

# import math

# number = 10

# answer = math.sqrt(number) # modulename.method(args)

# print(answer)

# import math
# import random


# def random_pi():
#     return math.ceil(random.randint(1,10) * math.pi)

# for i in range(5):
#     print(random_pi())

# just with desired objects to save memory

# from math import ceil, floor, pi
# from random import randint

# def random_pi():
#     return floor(randint(1,10) * pi)

# for i in range(5):
#     print(random_pi())


# exercise
# Create 2 files, one called dice.py - write a fucntion that will 
# generate a random number between 1 and 6. 
# in the second file import the dice module to simulate throwing 2 dice
# and print its result. 

# files:
# importance:
# logs
# storing and retrieving data
# sharing data
# configuring systems
# running scripts

# read, write, edit files
# most file types are supported, some require importing modules.

# lets on focus on .txt
# read mode ("r"): default mode - used for readign a file.
# write mode ("w"): opens a file for editing, creates a new file if doesnt exist.
# append ("a"): opens for writing, will create a new file, appends to the end. 

# eg:

# file = open("filename.txt", "mode")

# .... 


# file.close() # must remeber to close the file, most recently opened will close first.


# reading from a file
# read() - read an entire file. 
# readline() - read the next line and move on
# readlines() - read all the lines, puts in a list. 
# seek() - go to a line, defualts to line 1.

# writing to a file
# write() - used to write a string to a file
# writelines() - used to  write a list to a file.

# file = open("lines.txt", "r")

# lines = file.readlines()

# print(lines)

# file = open("lines.txt", "w")

# for n in range(1,11):
#     newline = "this is a new line" + " " + str(n) + "\n"
#     file.write(newline)

# file.close()

# file = open("lines.txt", "r")

# outfile = ""

# for line in range(1, 10):
#     if line % 2 == 0:
#         outfile += file.readline()
#     else:
#         file.readline()

# file = open("lines.txt", "w")


# file.write(outfile)
# file.close()

# exercise
# open a new text file (w mode) - called teams.txt. add the names of 5 sports teams.
# read and display the names of the 1st and 4th team (.strip())
# edit the file so that the top line is replaced with "this is a new line"
# print out the edited file line by line. 

























