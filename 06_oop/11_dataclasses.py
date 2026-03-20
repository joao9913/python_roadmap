"""
11_dataclasses.py
Topic: Dataclasses
Goal: Learn how to use dataclasses to simplify data-centric classes, automatically generate common methods,
and maintain immutability, ordering and defaults
"""

# ------------------
# What is a Dataclass
# ------------------

# A dataclass is a decorator (@dataclass) that automatically adds special methods
# like __init__, __repr__, __eq__, and others to classes that are primarily used
# to store data

# Benefits of dataclasses:
# - Reduces boilerplate code
# - Provides clear syntax for data containers
# - Supports defaults, immutability, ordering and type hints


# ------------------
# Creating A Basic Dataclass
# ------------------

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

# __init__ and __repr__ are automatically generated
book = Book("1984", "George Orwell")
print(book)     # Book(title = "1984", author = "George Orwell")


# ------------------
# Default Values
# ------------------

@dataclass
class Book:
    title: str
    author: str
    pages: int = 100    # default value

book1 = Book("1984", "George Orwell")
book2 = Book("Animal Farm", "George Orwell", 112)

print(book1.pages)  # 100
print(book2.pages)  # 112


# ------------------
# Immutability with frozen = True
# ------------------

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
# p.x = 5   # This would raise an error because the instance is immutable


# ------------------
# Comparison with order = True
# ------------------

@dataclass(order=True)
class Player:
    score: int
    name: str

p1 = Player(100, "Alice")
p2 = Player(200, "Bob")

print(p1 < p2)  # True, compares by score first


# ------------------
# Custom Methods in Dataclasses
# ------------------

@dataclass
class Circle:
    radius: float

    def area(self):
        from math import pi
        return pi * self.radius ** 2

c = Circle(3)
print(c.area())


# ------------------
# Post-Init Processing
# ------------------

@dataclass
class Rectangle:
    width: int
    height: int
    area: int = 0

    def __post_init__(self):
        self.area = self.width * self.height

r = Rectangle(3, 4)
print(r.area)


# ------------------
# Field Customization With default_factory
# ------------------

from dataclasses import field

@dataclass
class Inventory:
    items: list = field(default_factory=list)

inv1 = Inventory()
inv2 = Inventory()
inv1.items.append("apple")

print(inv1.items)
print(inv2.items)


# ------------------
# Summary
# ------------------

# Key points:
# - Use @dataclass to simplify data container classes
# - Supports default values and default factories for mutable types
# - Can be made immutable with frozen = True
# - Can auto-generate comparison operators with order = True
# - Allows custom methods and post-init calculations
