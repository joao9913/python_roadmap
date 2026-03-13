"""
03_object_oriented_programming.py
Topic: Object-Oriented Programming (OOP)
Goal: Understand the fundamentals of OOP in Python, including classes, objects, encapsulation,
attributes and methods.
"""


# ------------------
# What Is OOP
# ------------------

# Object Oriented Programming is a paradigm based on the concepts of "Objects" -
# - self contained units that combine data and behaviour

# Code ideas:
# - Classes: Blueprints for creating objects
# - Objects (Instances): Concrete examples of a class
# - Attributes: Data stored inside objects
# - Methods: Functions defined inside classes
# - Encapsulation: Bundling data and behaviour together
# - State: Objects can store and modify internal data

# OOP is **state-oriented** and models systems as interacting objects


# ------------------
# Classes and Objects
# ------------------

# A class defines a blueprint

class Person:
    pass

# Creating objects (instances) from a class:

person1 = Person()
person2 = Person()

print(type(person1))

print("\n-------------------------------------------------------------\n")


# ------------------
# Adding Attributes
# ------------------

# Attributes store data inside an object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)

print(person1.name)
print(person1.age)

print("\n-------------------------------------------------------------\n")


# ------------------
# Methods (Functions Inside Classes)
# ------------------

# Methods define behaviour of objects

class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def greet(self):
        return f"My name is {self.name} and I am {self.age} years old."

person1 = Person(26, "Bob")
print(person1.greet())

print("\n-------------------------------------------------------------\n")


# ------------------
# Modifying Object State
# ------------------

# Objects can change their internal state.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(10000)

account.deposit(100)
print(account.balance)

account.withdraw(50)
print(account.balance)

print("\n-------------------------------------------------------------\n")


# ------------------
# Encapsulation
# ------------------

# Encapsulation means keeping data and behaviour inside the objet.
# The object controls how its data is accessed or modified

# In Python, we use naming conventions:
# - _variable (protected by convention)
# - __variable (name mangling from stronger encapsulation)

class Example:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"

    def get_private(self):
        return self.__private

obj = Example()

print(obj.public)
print(obj.get_private())

print("\n-------------------------------------------------------------\n")


# ------------------
# When to Use OOP
# ------------------

# - Modeling real-world entities
# - Large applications
# - Systems with complex state
# - GUI applications
# - Game Development
# - Backend architectures


# ------------------
# Summary
# ------------------

# Object-Oriented Programming:
# - Organizes code around objects
# - Uses classes as blueprints
# - Combines data and behaviour
# - Focuses on state and interactions
# - Supports encapsulation and modular design
