"""
03_methods.py
Topic: Methods in Classes
Goal: Understand instance methods, how they work, how they use object state, and how methods interact with each other
"""

# ------------------
# What Is A Method?
# ------------------

# A method is a function defined inside a class
# It belongs to objects of that class
# It is used to define behavior

class Example:
    def say_hello(self):
        return "Hello"

obj = Example()
print(obj.say_hello())

print("\n------------------------------------------------------------------------\n")


# ------------------
# The Role of "self"
# ------------------

# "self" represents the current instance of the class
# It allows the method to access instance variables

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"

p = Person("Alice")

print(p.introduce())

print("\n------------------------------------------------------------------------\n")


# ------------------
# Methods Accessing Object State
# ------------------

# Methods can read instance variables

class Counter:
    def __init__(self):
        self.value = 0

    def show_value(self):
        return self.value


counter = Counter()

print(counter.show_value())

print("\n-----------------------------------------------------------------------\n")


# ------------------
# Methods Modifying State
# ------------------

# Methods can change the internal state of an object.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(100)

account.deposit(50)

print(account.balance)

print("\n-----------------------------------------------------------------------\n")


# ------------------
# Multiple Methods Working Together
# ------------------

# Methods can call other methods inside the same class

class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, number):
        self.value += number

    def reset(self):
        self.value = 0

    def get_value(self):
        return self.value

calc = Calculator(10)

calc.add(5)
print(calc.get_value())

calc.reset()
print(calc.get_value())

print("\n-----------------------------------------------------------------------\n")


# ------------------
# Methods Returning Values
# ------------------

# Methods can return computed results without modifying state

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(10, 4)

print(rect.area())

print("\n-----------------------------------------------------------------------\n")


# ------------------
# Summary
# ------------------

# Instance methods:
# - Defined inside a class
# - Take "self" as first parameter
# - Can access instance variables
# - Can modify object state
# - Can return values
# - Define behaviour of objects
