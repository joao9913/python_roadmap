"""
02_instance_vs_class_vars.py
Topic: Instance vs Class Variables
Goal: Understand the difference between variables that belong to an object
(instance variables) and variables that belong to the class itself (class variables)
"""



# ------------------
# Instance Variables
# ------------------

# Instance variables belong to a specific object.
# Each object has its own copy of these variables

class Person:
    def __init__(self, name):
        self.name = name    # instance variable

person1 = Person("Alice")
person2 = Person("Bob")

print(person1.name)
print(person2.name)

# Each object stores its own value

print("\n---------------------------------------------------------------------\n")


# ------------------
# Class Variables
# ------------------

# Class variables belong to the class itself
# All instances share the same value

class Dog:

    species = "Canis Familiaris"    # class variable

    def __init__(self, name):
        self.name = name

dog1 = Dog("Max")
dog2 = Dog("Charlie")

print(dog1.species)
print(dog2.species)

# Both objects access the same shared variable

print("\n----------------------------------------------------------------------\n")


# ------------------
# Accessing Class Variables
# ------------------

# Class variables can be acessed in two ways:

print(Dog.species)  # through the class
print(dog1.species) # through an instance

print("\n----------------------------------------------------------------------\n")


# ------------------
# Instance Variables vs Class Variables
# ------------------

# Instance variables:
# - Defined inside __init__
# - Belong to individual objects
# - Each object can have different values

# Class variables:
# - Defined directly inside the class
# - Shared across all instances
# - Represent data common to all objects

print("\n---------------------------------------------------------------------\n")


# ------------------
# Modifying Class Variables
# ------------------

# Changing a class variable affects all instances
# (if modified through the class)

class Game:
    difficulty = "Normal"   # class variable

game1 = Game()
game2 = Game()

Game.difficulty = "Hard"

print(game1.difficulty)
print(game2.difficulty)

# Both objects reflect the change.

print("\n------------------------------------------------------------------------\n")


# ------------------
# Shadowing a Class Variable
# ------------------

# If an instance modifies a class variable through itself,
# it creates a new instance variable instead of modifying the class variable

class Example:
    value = 10  # class variable

obj1 = Example()
obj2 = Example()

obj1.value = 50 # creates an instance variable

print(obj1.value)
print(obj2.value)
print(Example.value)

# obj1 now has its own variable that hides the class variable

print("\n--------------------------------------------------------------------\n")


# ------------------
# When To Use Class Variables
# ------------------

# Use class variables when:
# - The value should be shared by all instances
# - The data represents a common property
# - The value conceptually belongs to the class itself

# Examples:
# - species of an animal
# - default configuration
# - global counters
# - constants

print("\n-------------------------------------------------------------------\n")


# ------------------
# Summary
# ------------------

# Instance variables:
# - Belong to each object
# - Defined in __init__
# - Stored separately for every instance

# Class variables:
# - Belong to the class itself
# - Shared across all instances
# - Defined directly inside the class
