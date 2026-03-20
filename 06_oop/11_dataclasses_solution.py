"""
12_dataclasses_exercises.py
Topic: Dataclasses
Goal: Practice creating and using dataclasses, handling defaults, immutability,
      ordering, and post-init processing.
"""

from dataclasses import dataclass

# -------------------------------------------------
# 1. Basic Dataclass
# -------------------------------------------------

# Create a dataclass Book with:
# - title (str)
# - author (str)
# Create an instance and print it

print("\n#1")

@dataclass
class Book:
    title: str
    author: str

book = Book("Title", "Author")
print(book)


# -------------------------------------------------
# 2. Default Values
# -------------------------------------------------

# Create a dataclass Book with:
# - title (str)
# - author (str)
# - pages (int, default=100)
# Create two books, one with default pages and one with custom pages, then print pages

print("\n#2")

@dataclass
class Book:
    title: str
    author: str
    pages: int = 100

book1 = Book("Title1", "Author1")
book2 = Book("Title2", "Author2", 140)

print(book1)
print(book2)


# -------------------------------------------------
# 3. Immutability
# -------------------------------------------------

# Create a dataclass Point with:
# - x (int)
# - y (int)
# Make the dataclass frozen
# Try changing x after instantiation (observe the behavior)

print("\n#3")

@dataclass(frozen=True)
class Point:
    x: int
    y: int

point = Point(3, 4)
print(point)
# point.x = 50


# -------------------------------------------------
# 4. Ordering
# -------------------------------------------------

# Create a dataclass Player with:
# - score (int)
# - name (str)
# Enable ordering
# Create two players and compare them using < and >

print("\n#4")

@dataclass(order=True)
class Player:
    score: int
    name: str

p1 = Player(200, "P1")
p2 = Player(100, "P2")

print(p1 > p2)
print(p2 > p1)


# -------------------------------------------------
# 5. Custom Method
# -------------------------------------------------

# Create a dataclass Circle with:
# - radius (float)
# Add a method area() that calculates the area of the circle
# Create an instance and print the area

print("\n#5")

@dataclass
class Circle:
    radius: float

    def area(self):
        from math import pi
        return pi * self.radius ** 2

circle = Circle(5)
print(circle.area())


# -------------------------------------------------
# 6. Post-Init Processing
# -------------------------------------------------

# Create a dataclass Rectangle with:
# - width (int)
# - height (int)
# - area (int, default 0)
# Use __post_init__ to automatically calculate area after initialization
# Create an instance and print the area

print("\n#6")

@dataclass
class Rectangle:
    width: int
    height: int
    area: int = 0

    def __post_init__(self):
        self.area = self.width * self.height

rect = Rectangle(2, 4)
print(rect.area)


# -------------------------------------------------
# 7. Field with default_factory
# -------------------------------------------------

# Create a dataclass Inventory with:
# - items (list, use default_factory=list)
# Create two instances and add an item to the first
# Print the second instance's items to confirm they are separate lists

print("\n#7")

from dataclasses import field

@dataclass
class Inventory:
    items: list = field(default_factory=list)

inv1 = Inventory()
inv2 = Inventory()

inv1.items.append("item1")
print(inv1)
print(inv2)


# -------------------------------------------------
# 8. Dataclass Comparison
# -------------------------------------------------

# Create a dataclass Product with:
# - price (float)
# - name (str)
# Enable ordering
# Create two products and check which one is greater

print("\n#8")

@dataclass(order=True)
class Product:
    price: float
    name: str

p1 = Product(100, "P1")
p2 = Product(200, "P2")

print(p1 > p2)


# -------------------------------------------------
# 9. Nested Dataclasses
# -------------------------------------------------

# Create a dataclass Engine with:
# - horsepower (int)
# Create a dataclass Car with:
# - model (str)
# - engine (Engine)
# Instantiate a car with an engine and print engine horsepower

print("\n#9")

@dataclass
class Engine:
    horsepower: int

@dataclass
class Car:
    model: str
    engine: Engine

engine = Engine(224)
car = Car("BMW 125i", engine)

print(car.engine.horsepower)


# -------------------------------------------------
# 10. Design Challenge
# -------------------------------------------------

# Create a dataclass Student with:
# - name (str)
# - grades (list of floats, use default_factory)
# Add a method average() that returns the average grade
# Create 3 students, add grades, and print each average

print("\n#10")

from dataclasses import field

@dataclass
class Student:
    name: str
    grades: list = field(default_factory = list)

    def average(self):
        return sum(self.grades) / float(len(self.grades))

s1 = Student("S1", [13, 13, 11])
s2 = Student("S2", [14, 15, 16])
s3 = Student("S3", [10, 9, 4])

print(s1.average())
print(s2.average())
print(s3.average())
