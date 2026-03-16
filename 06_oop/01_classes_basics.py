"""
# 01_classes_basics.py
# Topic: Classes Basics
# Goal: Understand what classes and objects are, how they are created, and how they organize data and behaviour in Python
"""

# ------------------
# What Is A Class
# ------------------

# A class is a blueprint used to create objects
# It defines the structure and behaviour that the objects created from it, will have

# Classes allow us to group:
# - Data (attributes)
# - Behaviours (Methods)

# Think of a class like a template
# The template defines what an object should contain


# ------------------
# Creating a class
# ------------------

# The simples class possible:

class Person:
    pass

# "pass" means the class is emtpy for now


# ------------------
# Creating Objects (Instances)
# ------------------

# Objects are created from classes

person1 = Person()
person2 = Person()

print(type(person1))
print(type(person2))

# Each object is called an "instance" of the class

print("\n----------------------------------------------------------------------\n")


# ------------------
# Why Classes Are Useful
# ------------------

# Classes help organize code by grouping related data and behaviour

# Example without classes:

name = "Alice"
age = 30

# With classes, we can model this information as an object


# ------------------
# Adding Attributes and __init__
# ------------------

# The __init__ method is used to initialize objects when they are create
# It runs automatically when a new instance is created

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)

print(person1.name)
print(person1.age)

# self refers to the specific object being created

print("\n-----------------------------------------------------------------------\n")


# ------------------
# Understanding self
# ------------------

# "self" represents the current instance of the class
# It allows the object to store and access its own data

class Person:
    def __init__(self, name):
        self.name = name

person1 = Person("Bob")
person2 = Person("Charlie")

print(person1.name)
print(person2.name)

# Each object stores its own data independently

print("\n---------------------------------------------------------------------\n")


# ------------------
# Adding Methods
# ------------------

# Methods are functions defined inside classes
# They represent behaviours of the object

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"

person1 = Person("Alice")
print(person1.greet())

# Methods can access attributes using self.

print("\n----------------------------------------------------------------------\n")


# ------------------
# Objects Have State
# ------------------

# The attributes stored inside an object represent its "state"

# Example:

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

counter = Counter()

print(counter.value)
counter.increment()
print(counter.value)

# The object's internal state changed

print("\n--------------------------------------------------------------\n")


# ------------------
# Multiple Instances
# ------------------

# Each instance maintains its own state

class Counter:
    def __init__(self):
        self.value

    def increment(self):
        self.value += 1

counter1 = Counter()
counter2 = Counter()

counter1.increment()

print(counter1.value)
print(counter2.value)

# The objects are independent

print("\n----------------------------------------------------------------\n")


# ------------------
# Summary
# ------------------

# Classes allow us to:
# - Define blueprints for objects
# - Group related data and behaviour
# - Create multiple independent instances
# - Model real-world concepts

# Core ideas introduced:
# - Classes
# - Objects (instances)
# - Attributes
# - Methods
# - __init__
# - self
# - Object state
