# if, elif, else
# allows different pathways for our code to take. 

#my_bool = True

#if my_bool:
#    print("my_bool is true")
#else:
#    print("my_bool is false")

# is_admin = False
# is_verified = True
# on_holiday = False

# if is_admin or is_verified and not on_holiday:
#     print("access granted")
# else:
#     print("access denied")

# if some condition:
#     if some condition:
#         some code
#     else:
#         some code
#else: some code

# conditional operators:

# equals to: == 
# not equals to: !=
# more than and more than or equals to: > >=
# less than and less than or equals to: < <=

#money = 10

#if money >= 11:
#    print("i have some money")
#else:
#    print("i dont have much money")

# temp = 11

# if temp >= 30:
#     print("its very hot")
# elif temp > 25:
#     print("pretty hot")
# elif temp > 20:
#     print("its ok")
# elif temp > 10:
#     print("chilly")
# else:
#     print("generally bad")


# exercise: user to input a grade/mark
# if the mark is above 85 print distinction
# between 65 and 85 print pass
# anything else is fail.
# use if elif else. 

#x = int(input("enter a grade: "))
#if x > 85:
#    print("distinction")
#elif x >= 65:
#    print("pass")
#else:
#    print("fail")

# multiple comparators

#deposit = 50
#password = "password1"

#if 0 < deposit < 100 or password == "password":
#    print(f"thankyou for deposit of {deposit}")
#else:
#    print("deposit failed")

# not

#if not 0 < deposit < 100 or password != "password":
#    print("deposit failed")
#else:
#    print(f"thankyou for deposit of {deposit}")

# in and not in  

#name = "root123"

#if name in ("root", "admin", "user"):
#    print("invalid username")
#else:
#    print("accepted")

#if name not in ("root", "admin", "user"):
#    print("accepted")
#else:
#    print("invalid username")

# weight converter app
# user to input weight (float)
# user to select either Kgs or Lbs
# if statement to check for unit enetered
# logic to convert from Kgs to Lbs and Lbs to Kgs
# print out the converted value
# error handling for upper/lower case
# optional - input validation. 

# 1st solution 

# weight = float(input("enter weight: "))
# unit = input("enter K (Kgs) or L (lbs): ")

# if unit.upper() == "K":
#     converted = weight / 0.45
#     print(f"converted is {converted}")
# elif unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"converted is {converted}")
# else:
#     print("invalid unit enter K or L")

#  2nd solution    
# import sys

# try:
#     weight = float(input("enter weight: "))
# # except ValueError:
#     print("invalid input. Please enter a numeric value")
#     sys.exit()

# while True:
#     unit = input("enter K (Kgs) or L (lbs): ").upper()
#     if unit == "K":
#         converted = weight / 0.45
#         print(f"converted is {converted}")
#         break
#     elif unit == "L":
#         converted = weight * 0.45
#         print(f"converted is {converted}")
#         break
#     else:
#         print("invalid unit enter K or L")

# getting highest number 

# num = 10
# num1 = 20

# if num > num1:
#     print(num)
# else: 
#     print(num1)

# rewrite without using if statements are any in built functions (no max!!)



#num = 10
#num1 = 20

#largest = num * (num > num1) + num1 * (num1 > num)

#print(F"largest is {largest}")

