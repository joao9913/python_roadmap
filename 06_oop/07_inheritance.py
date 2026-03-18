"""
07_inheritance.py
Topic: Inheritance
Goal: Understand how classes can inherit from other classes, reuse code and extend behavior in a structured way
"""


# ------------------
# What Is Inheritance
# ------------------

# Inheritance allows one class (child, subclass) to reuse and extend another class (parent/superclass)

# It enables:
# - Code reuse
# - Logical hierarchy
# - Extension of behavior
# - Polymorphism

# ------------------
# Basic Inheritance
# ------------------

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    pass

dog = Dog()
print(dog.speak())  # Inherited from Animal

print("\n-------------------------------------------------\n")


# ------------------
# Overriding Methods
# ------------------

# A child class can override methods from the parent

class Cat(Animal):
    def speak(self):
        return "Meow"

cat = Cat()
print(cat.speak())

print("\n-------------------------------------------------\n")


# ------------------
# Using super()
# ------------------

# super() allows access to the parent class implementation

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

car = Car("Toyota", "Corolla")
print(car.brand)
print(car.model)

print("\n-------------------------------------------------\n")


# ------------------
# Extending Instead of Replacing
# ------------------

class Logger:
    def log(self, message):
        return f"[LOG]: {message}"

class FileLogger(Logger):
    def log(self, message):
        base_message = super().log(message)
        return base_message + " (saved to file)"

logger = FileLogger()
print(logger.log("System started"))

print("\n-------------------------------------------------\n")


# ------------------
# isinstance() and issubclass()
# ------------------

print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True

print("\n-------------------------------------------------\n")


# ------------------
# Method Resolution Order (MR0)
# ------------------

# Python looks for methods in this order:
# 1. The class itself
# 2. Parent classes (left to right)
# 3. Their parents
# etc.

print(Dog.mro())

print("\n-------------------------------------------------\n")


# ------------------
# Summary
# ------------------

# Inheritance allows:
# - Reuse of code
# - Overriding behavior
# - Extension via super()
# - Logical class hierarchies
# - Polymorphism

# Key concepts:
# - Parent (Base) class
# - Child (Derived) class
# - Method overriding
# - super()
# - MRO
# - isistance()
# - issubclass()
