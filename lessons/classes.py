# classes is part of OOP (object orientated programming)
# key concepts
# class - a blueprint - of attributes (vars/args), and methods (functions)
# object - is an instance of a class
# allows us to make multiple objects of the same type. 

# class Dog: # class name
#     energy = "high" # setting a atribute of the class

#     def speak(self):
#         print("bark")


# fido = Dog() # makes an object of the class
# fido.speak()
# print(fido.energy)
# fido.energy = "low"
# print(fido.energy)

# class Student:
#     pass

# student1 = Student()
# student2 = Student()

# student1.first = "john"
# student1.last = "smith"
# student1.age = 10

# print(student1.age, student1.last)

# class Student:
#     def __init__(self, first, last, age): # init method, called a dunder and is a background task. 
#         self.first = first # init method initialises the object with these attributes. 
#         self.last = last #  the self param refers to the object itself.
#         self.age = age # self maps the class data to the the object. 

# student1 = Student("john", "smith", 10)
# student2 = Student("katy", "smith", 12)

# print(student1.age, student2.age)


# class Student:
#     def __init__(self, first, last, age): # init method, called a dunder and is a background task. 
#         self.first = first # init method initialises the object with these attributes. 
#         self.last = last #  the self param refers to the object itself.
#         self.age = age # self maps the class data to the the object.
#         self.full = first + " " + last 

# student1 = Student("john", "smith", 10)
# student2 = Student("katy", "smith", 12)

# print(student1.full, student2.full) 

# class Student:
#     def __init__(self, first, last, age): # init method, called a dunder and is a background task. 
#         self.first = first # init method initialises the object with these attributes. 
#         self.last = last #  the self param refers to the object itself.
#         self.age = age # self maps the class data to the the object. 


#     def fullname(self):
#         return self.first + " " + self.last

# student1 = Student("john", "smith", 10)
# student2 = Student("katy", "smith", 12)

# print(student1.fullname())
# print(Student.fullname(student2))

# change an attribute with a method

# class Student:
#     def __init__(self, first, last, age): # init method, called a dunder and is a background task. 
#         self.first = first # init method initialises the object with these attributes. 
#         self.last = last #  the self param refers to the object itself.
#         self.age = age # self maps the class data to the the object. 


#     def fullname(self):
#         return self.first + " " + self.last

#     def change_age(self):
#         self.age = self.age + 1

# student1 = Student("john", "smith", 10)
# # student2 = Student("katy", "smith", 12)

# # student1.change_age()
# # Student.change_age(student2)

# # print(student1.age, student2.age)

# # self class variable

# class Student:

#     age_increase_amount = 25

#     def __init__(self, first, last, age): # init method, called a dunder and is a background task. 
#         self.first = first # init method initialises the object with these attributes. 
#         self.last = last #  the self param refers to the object itself.
#         self.age = age # self maps the class data to the the object. 


#     def fullname(self):
#         return self.first + " " + self.last

#     def change_age(self):
#         self.age = self.age + self.age_increase_amount

# student1 = Student("john", "smith", 10)
# student2 = Student("katy", "smith", 12)

# print(student1.age)
# student1.change_age()
# print(student1.age)

# print(student1.age_increase_amount)
# print(student2.age_increase_amount)

# # __dict__

# print(student1.__dict__)
# print(Student.__dict__)

# # change to the variable

# student1.age_increase_amount = 10
# print(student1.__dict__)
# print(student2.__dict__)

# student1.change_age()
# student2.change_age()

# print(student1.age, student2.age)


# non self class variable

# class Student:

#     age_increase_amount = 25
#     num_of_students = 0

#     def __init__(self, first, last, age): # init method, called a dunder and is a background task. 
#         self.first = first # init method initialises the object with these attributes. 
#         self.last = last #  the self param refers to the object itself.
#         self.age = age # self maps the class data to the the object. 

#         Student.num_of_students += 1

#     def fullname(self):
#         return self.first + " " + self.last

#     def change_age(self):
#         self.age = self.age + self.age_increase_amount

# print(Student.num_of_students)
# student1 = Student("john", "smith", 10)
# student2 = Student("katy", "smith", 12)
# print(Student.num_of_students)

# parent child classes

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def eat(self):
#         print(f"{self.name} is eating")

# class Cat(Animal):
#     def __init__(self, name, species, breed):
#         super().__init__(name, species)
#         self.breed = breed

#     def meow(self):
#         print("meow")

# my_cat = Cat("w", "x", "y")

# my_cat.eat()
# my_cat.meow()

# print(my_cat)

# with a str method 

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return f"{self.name} - {self.species} - {self.__class__.__name__}"

class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")

    def __str__(self):
        return super().__str__() + f"- {self.breed}"

my_cat = Cat("w", "x", "y")

my_cat.eat()
my_cat.meow()

print(my_cat)