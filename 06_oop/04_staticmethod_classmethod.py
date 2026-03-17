"""
04_staticmethod_classmthod.py
Topic: Static Methods and Class Methods
Goal: Understand the difference between instance methods, class methods and static methods and when each should be used
"""


# ------------------
# Types of Methods
# ------------------

# In python classes there are three main types of methods:

# 1. Instance Methods
# - Receive "self"
# - Operate on a specific object

# 2. Class Methods
# - Receive "cls"
# - Operate on the class itself

# 3. Static Methods
# - Receive no automatic argument
# - Behave like regular functions but belong to the class


# ------------------
# Instance Method
# ------------------

# Instance methods work with object data

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"

p = Person("Alice")
print(p.greet())


print("\n-------------------------------------------------------------\n")


# ------------------
# Class Methods
# ------------------

# Class methods receive the class as the first argument (cls)
# They are defined using the @classmethod decorator

class User:
    user_count = 0

    def __init__(self, name):
        self.name = name
        User.user_count += 1

    @classmethod
    def get_user_count(cls):
        return cls.user_count

u1 = User("Alice")
u2 = User("Bob")

print(User.get_user_count())

print("\n-------------------------------------------------------------\n")


# ------------------
# Why use cls instead of Class Name
# ------------------

# Using "cls" makes the method flexible
# It allows the method to work correctly with subclasses

class Example:
    value = 10

    @classmethod
    def show_value(cls):
        return cls.value

print(Example.show_value())

print("\n-------------------------------------------------------------\n")


# ------------------
# Static Methods
# ------------------

# Static methods do not receive self or cls
# They behave like regular functions but are logically related to the class

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 4))

print("\n-------------------------------------------------------------\n")


# ------------------
# Static Methods Inside Objects
# ------------------

# Static methods can also be called through instances,
# although they do not interact with the object.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 1.8 + 32

print(TemperatureConverter.celsius_to_fahrenheit(0))

temp = TemperatureConverter()
print(temp.celsius_to_fahrenheit(0))

print("\n-------------------------------------------------------------\n")


# ------------------
# Comparing Method Types
# ------------------

# Instance Method
# - Receives: self
# - Works with object state

# Class Method
# - Receives: cls
# - Works with class state

# Static Method
# - Receives: nothing automatically
# - Utility functions related to the class


# ------------------
# Summary
# ------------------

# Instance Methods:
# - Work with object data
# - Use "self"

# Class Methods:
# - Work with class-level data
# - Use "cls"
# - Declared with @classmethod

# Static Methods:
# - Do not access instance or class data
# - Declared with @staticmethod
# - Used for helper functions related to the class
