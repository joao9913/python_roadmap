"""
06_dunder_methods.py
Topic: Dunder (Magic) Methods
Goal: Understand how special methods control object behavior and integrate custom classes with Python built-in operations
"""


# ------------------
# What Are Dunder Methods
# ------------------

# "Dunder" stands for "double underscore"
# These are special methods like __init__, __str__, __len__

# They allow Python to interact with your objects in built-in ways

# Example:
# - print(obj) -> calls __str__
# - len(obj) -> calls __len__
# - obj1 + obj2 -> __add__

# You usually don't call them directly
# Python calls them automatically


# ------------------
# Basic Example
# ------------------

class Example:
    def __init__(self, value):
        self.value = value

obj = Example(10)

print("\n----------------------------------------------------------------\n")


# ------------------
# String Representation (__str__)
# ------------------

# __str__ defines how the object is displayed to users
# It is called when using print()

class Product:
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #       return ...

product = Product("Laptop")
print(product)  # a default output is not very useful

print("\n----------------------------------------------------------------\n")


# ------------------
# Debug Representation (__repr__)
# ------------------

# __repr__ is used for debugging
# It should be more detailed than __str__

class User:
    def __init__(self, username):
        self.username = username

    # def __repr__(self):
    #       return ...

print("\n----------------------------------------------------------------\n")


# ------------------
# Length Behavior (__len__)
# ------------------

# __len__ allows objects to work with len()

class Collection:
    def __init__(self, items):
        self.items = items

    # def __len__(self):
    #       return ...

collection = Collection([1, 2, 3])
# print(len(collection))

print("\n----------------------------------------------------------------\n")


# ------------------
# Comparison (__eq__)
# ------------------

# __eq__ allows objects to be compared using ==

class Item:
    def __init__(self, value):
        self.value = value

    # def __eq__(self, other):
    #       return ...

item1 = Item(10)
item2 = Item(10)

# print(item1 == item2)

print("\n----------------------------------------------------------------\n")


# ------------------
# Arithmetic (__add__)
# ------------------

# __add__ allows using the + operator

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __add__(self, other):
    #       return ...

v1 = Vector(1, 2)
v2 = Vector(3, 4)

# v3 = v1 + v2

print("\n----------------------------------------------------------------\n")


# ------------------
# Boolean Value (__bool__)
# ------------------

# __bool__ defines truthiness of an object

class Account:
    def __init__(self, balance):
        self.balance = balance

    # def __bool__(self):
    #       return ...

account = Account(100)

# if account:
#       print("Account has funds")

print("\n----------------------------------------------------------------\n")


# ------------------
# Index Access (__getitem__)
# ------------------

# __getitem__ allows object[key] access

class DataStore:
    def __init__(self, data):
        self.data = data

    # def __getitem__(self, key):
    #       return ...

store = DataStore({"a": 1, "b": 2})

# print(store["a"])

print("\n----------------------------------------------------------------\n")


# ------------------
# Setting Values (__setitem__)
# ------------------

# __setitem__ allows object[key] = value

class Config:
    def __init__(self):
        self.settings = {}

    # def __setitem__(self, key, value):
    #       pass

config = Config()

# config["theme"] = "dark"

print("\n----------------------------------------------------------------\n")


# ------------------
# Callable Objects (__call__)
# ------------------

# __call__ allows objects to behave like functions

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    # def __call__(self, value):
    #       return ...

mul = Multiplier(2)

# print(mul(5))

print("\n----------------------------------------------------------------\n")


# ------------------
# Summary
# ------------------

# Dunder methods allow you to:
# - Customize object behavior
# - Integrate with Python built-in functions
# - Make objects behave like built-in types

# Core methods introduced:
# - __str__ -> user-friendly display
# - __repr__ -> debug display
# - __len__ -> len()
# - __eq__ -> ==
# - __add__ -> +
# - __bool__ -> truth value
# - __getitem__ -> obj[key]
# - __setitem__ -> obj[key] = value
# - __call__ -> obj()

# These are fundamental for:
# - Clean API design
# - Advanced OOP
# - Technical Interviews
