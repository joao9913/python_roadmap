"""
10_abstract_classes.py
Topic: Abstract Classes
Goal: Understand what abstract classes and methods are, how to enforce interfaces and why they are useful in Python
"""

# ------------------
# What is an Abstract Class
# ------------------

# An abstract class is a class that cannot be instantiated directly.
# It is meant to define a common interface for its subclasses

# Abstract classes can have:
# - Concrete methods (with implementation)
# - Abstract methods (without implementation, must be implemented by subclasses)

# Abstract classes enforce that certain methods must exist in subclasses, which is useful for API design and consistent behavior


# ------------------
# Creating an Abstract Class
# ------------------

# Python provides the "abc" module to define abstract classes and methods

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Trying to create an instance of Shape will raise an error
# shape = Shape()   # TypeError: Can't instatiate abstract class


# ------------------
# Subclass Must Implement Abstract Methods
# ------------------

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Now we can create a Square
square = Square(3)
print(square.area())    # Output: 9

# If a subclass does not implement all abstract methods, it cannot be instantiated


# ------------------
# Abstract Methods Can Have Default Implementation
# ------------------

class Animal(ABC):
    @abstractmethod
    def speak(self):
        print("Some generic animal sound")  # a optional default behavior

class Dog(Animal):
    def speak(self):
        super().speak() # can call defaulkt behavior
        print("Woof")

dog = Dog()
dog.speak()


# ------------------
# Why Use Abstract Classes
# ------------------

# 1. Enforce a consistent interface
#   - All subclasses must implement the abstract methods
# 2. Encourage polymorphism
#   - Different subclasses can be treated the same if they implement the interface
# 3. Useful in frameworks and API design
#   - Guarantees that certain methods exist without specifying implementation details


# ------------------
# Summary
# ------------------

# Key points:
# - Abstract classes cannot be instantiated directly
# - Abstract methods must be implemented by subclasses
# - Use 'abc' module with ABC and @abstractmethod
# - Can include concrete methods alongside abstract methods
# - Ensures consistent interfaces for subclasses
