"""
08_polymorphism.py
Topic: Polymorphism
Goal: Understand how different objects can share the same interface and behave differently depending on their type
"""


# ------------------
# What Is Polymorphism
# ------------------

# Polymorphism means "many forms"

# In Python, it allows different objects to use the same method name
# but behave differently depending on the object

# This is a core concept in object-oriented programming


# ------------------
# Basic Example
# ------------------

class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

# Same method name, different behavior

print("\n-------------------------------------------------\n")


# ------------------
# Polymorphism with Lists
# ------------------

# Different objects can be stored together and treated the same way

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# We don't care about the exact type, only that the method exists

print("\n-------------------------------------------------\n")


# ------------------
# Duck Typing
# ------------------

# "If it looks like a duck and quacks like a duck, it's a duck"

class Bird:
    def speak(self):
        return "Chirp"

class Person:
    def speak(self):
        return "Hello"

things = [Dog(), Bird(), Person()]

# Do you have a .speak() method? Then call it

for thing in things:
    print(thing.speak())

# No inheritance required, only the method matters

print("\n-------------------------------------------------\n")


# ------------------
# Polymorphism with Inheritance
# ------------------

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())

# Same method defined in parent and overridden in children

print("\n-------------------------------------------------\n")


# ------------------
# Built-In Polymorphism
# ------------------

# Python uses polymorphism everywhere

print(len("Hello"))     # string length
print(len([1, 2, 3]))   # list length
print(len({"a": 1}))    # dict length

# Same function, different behaviour depending on type

print("\n-------------------------------------------------\n")


# ------------------
# Function Polymorphism
# ------------------

# Functions can work with different types

def make_sound(obj):
    return obj.speak()

print(make_sound(Dog()))
print(make_sound(Cat()))

# Function doesn't care about type, only that the object has speak()

print("\n-------------------------------------------------\n")


# ------------------
# Operator Polymorphism
# ------------------

# Operators behave differently depending on type

print(1 + 2)        # 3
print("a" + "b")    # "ab"
print([1] + [2])    # [1, 2]

# Same operator (+), different behavior

print("\n-------------------------------------------------\n")


# ------------------
# Summary
# ------------------

# Polymorphism allows:
# - Same method name, different behavior
# - Writing flexible and reusable code
# - Working with different types uniformly

# Key concepts:
# - Method overriding
# - Duck typing
# - Operator overloading
# - Built-in polymorphism
# - Function polymorphism
